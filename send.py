import asyncio
import sys
from aio_pika import Message, connect


async def main(message = sys.argv[1]) -> None:
    # Perform connection
    connection = await connect("amqp://sebajou:argh@localhost/")

    async with connection:
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue("hello")

        # Sending the message
        message_bytes = bytes(message, encoding= 'utf-8')
        await channel.default_exchange.publish(
            Message(message_bytes),
            routing_key=queue.name,
        )

        print(" [x] Sent 'Hello World!'")


if __name__ == "__main__":
    asyncio.run(main())