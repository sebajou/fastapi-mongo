from fastapi import APIRouter

from schemas.message import MessageSchema


router = APIRouter(
    tags=['items'],
    responses={404: {"description": "Page not found"}}
)


@router.post('/send_message')
async def send_message(payload: MessageSchema, request):
    request.app.pika_client.send_message(
        {"message": payload}
    )
    return {"status": "ok"}