import asyncio
from urllib.request import Request
from fastapi import FastAPI, Depends, logger
import uvicorn

from config.settings import Settings
from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from message_broker.pika_client import PikaClient
from routes.admin import router as AdminRouter
from routes.student import router as StudentRouter
from routes.spring import router as SpringRouter
from routes.pika import router as PikaRouter
from schemas.message import MessageSchema

settings = Settings()
app = FastAPI()
# app = FooApp()
pika_client = PikaClient()

token_listener = JWTBearer()


@app.on_event('startup')
async def startup():
    await initiate_database()
    # await pika_client.receive_message(settings.CONSUME_QUEUE)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


@app.post('/send_message')
async def send_message(payload: MessageSchema):
    await pika_client.send_message(
        settings.CONSUME_QUEUE,
        {"message": payload}
    )
    return {"status": "ok"}


def start():
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(StudentRouter, tags=["Students"], prefix="/student", dependencies=[Depends(token_listener)], )
app.include_router(SpringRouter, tags=["Springs"], prefix="/spring", dependencies=[Depends(token_listener)], )
app.include_router(PikaRouter, tags=["Pika"])
