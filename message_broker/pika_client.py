import json
import uuid
from fastapi import logger
import pika
from config.settings import Settings
from aio_pika import connect_robust,  Message
from aio_pika.abc import AbstractIncomingMessage
from contextlib import asynccontextmanager
import asyncio

settings = Settings()


class PikaClient:
    async def connection(self) -> any:
        # Perform connection
        connecting = await connect_robust(
            port=5672,
            login="sebajou",
            password="argh",
            host="rabbitmq",
        )
        
        #connecting = await connect("amqp://sebajou:argh@localhost/")
        #connecting = await connect("amqp://sebajou:argh@localhost:5672/")
        #connecting = await connect("amqp://sebajou:argh@rabbitmq:5672/")
        #connecting = await connect("amqp://sebajou:argh@127.0.0.1:5672/")
        
        async with connecting:
            # Creating a channel
            channel = await connecting.channel()

    async def send_message(self, queue, message) -> None:
        # Perform connection
        connecting = await connect_robust(
            port=5672,
            login="sebajou",
            password="argh",
            host="rabbitmq",
        )
              
        async with connecting:
            # Creating a channel
            channel = await connecting.channel()

        # Declaring queue
        queue = await channel.declare_queue(queue)

        # Sending the message
        json_to_send = json.dumps(message)
        await channel.default_exchange.publish(
            Message(body=json_to_send.encode()),
            routing_key=queue.name,
        )

    async def receive_message(self, queue) -> None:
        # Perform connection
        connecting = await connect_robust(
            port=5672,
            login="sebajou",
            password="argh",
            host="rabbitmq",
        )
              
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


            
"""
class PikaClient:
    
    @asynccontextmanager
    async def get_connection(self):

        connection = await aio_pika.connect_robust(
            host=settings.RABBITMQ_HOST,
            port=int(settings.RABBITMQ_PORT),
            virtualhost=settings.RABBITMQ_VHOST,
            login=settings.RABBITMQ_USER,
            password=settings.RABBITMQ_PASS
        )
        async with connection:
            channel = await connection.channel()
            try:
                yield channel
            finally:
                pass

    async def send_spring_message(self, message):

        try:
            async with self.get_connection() as channel:
                json_to_send = json.dumps(message)
                await self.send_message(channel, settings.CONSUME_QUEUE, json_to_send)
                logger.info("Sent spring to queue")
                return 200

        except Exception as exception:
            logger.info("Error sending spring to queue: %s", exception)
            return 500

    async def send_message(self, channel, queue, message):
        print(f"Sending message to queue in sender: {message}")
        queue = await channel.declare_queue(queue, durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=queue.name,
        )

    async def receive_message_from_queue(self):
        try:
            async with self.get_connection() as channel:
                json_to_send = await self.read_message(channel, settings.CONSUME_QUEUE)
                logger.info("Received message from queue")
                return json_to_send

        except Exception as exception:
            logger.error("Error receving book from queue", exception)

    async def read_message(self, channel, queue):
        try:
            async with self.get_connection() as channel:
                queue = await channel.declare_queue(queue, durable=True)
                async with queue.iterator() as queue_iter:
                    async for message in queue_iter:
                        async with message.process():
                            received_message = message.body.decode()
                            logger.info("Received message from queue: %s", received_message)
                            return received_message

        except Exception as exception:
            logger.error("Error reading message from queue", exception)
"""


"""
class PikaClient:

    def __init__(self, process_callable):
        settings = Settings()
        
        self.publish_queue_name = settings.NEW_STUDENT_QUEUE
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.RABBIT_HOST)
        )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        self.process_callable = process_callable
        logger.info('Pika connection initialized')

    async def consume(self, loop):
        settings = Settings()
        connection = await connect_robust(host=settings.RABBIT_HOST,
                                        port=5672,
                                        loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(settings.CONSUME_QUEUE)
        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info('Established pika async listener')
        return connection
    
    async def process_incoming_message(self, message):
        message.ack()
        body = message.body
        logger.info('Received message')
        if body:
            self.process_callable(json.loads(body))

    def send_message(self, message: dict):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )
"""
