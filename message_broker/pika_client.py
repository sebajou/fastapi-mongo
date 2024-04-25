import json
from config.settings import Settings
from fastapi.encoders import jsonable_encoder
from aio_pika import connect_robust,  Message
from aio_pika.abc import AbstractIncomingMessage, DeliveryMode
import asyncio

settings = Settings()


class PikaClient:

    async def send_message(self, message, queue='student') -> None:
        # Perform connection
        connecting = await connect_robust(
            port=int(settings.RABBITMQ_PORT),
            login=settings.RABBITMQ_USER,
            password=settings.RABBITMQ_PASS,
            host=settings.RABBITMQ_HOST,
            timeout=120000,
        )
        print('Robust connection established to rabbitmq', connecting)
              
        async with connecting:
            # Creating a channel
            channel = await connecting.channel()

            # Declare Queue
            await channel.declare_queue("student", durable=True)
            await channel.declare_queue("spring", durable=True)

            try:
                # Sending the message
                json_to_send = json.dumps(jsonable_encoder(message))
                await channel.default_exchange.publish(
                    Message(body=json_to_send.encode(), delivery_mode=DeliveryMode.PERSISTENT),
                    routing_key=queue,
                )
                print(" [x] Sent %r" % message)
            except Exception as e:
                print(f'Error sending message: {e}')

    async def receive_message(self, queue) -> None:
        # Perform connection
        connecting = await connect_robust(
            port=int(settings.RABBITMQ_PORT),
            login=settings.RABBITMQ_USER,
            password=settings.RABBITMQ_PASS,
            host=settings.RABBITMQ_HOST,
            timeout=120000,
        )
        # connecting = await connect("amqp://user:bitnami@rabbitmq:5672/")
              
        async with connecting:
            # Creating a channel
            channel = await connecting.channel()

            # Declaring queue
            queue = await channel.declare_queue(queue)

            # Start listening the queue with name 'hello'
            await queue.consume(self.on_message, no_ack=True)

            print(" [*] Waiting for messages. To exit press CTRL+C")
            await asyncio.Future()

    async def on_message(message: AbstractIncomingMessage) -> any:
        """
        Log the message
        """
        print(" [x] Received message %r" % message)
        print("Message body is: %r" % message.body)
