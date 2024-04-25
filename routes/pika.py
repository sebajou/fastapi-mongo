from fastapi import APIRouter

from schemas.message import MessageSchema
from message_broker.pika_client import PikaClient

router = APIRouter(
    tags=['items'],
    responses={404: {"description": "Page not found"}}
)


@router.post('/send_message')
async def send_message(payload, queue):
    pika_client = PikaClient()
    await pika_client.send_message(
        message={"message": payload},
        queue=queue
    )
    return {"status": "ok"}
