from fastapi import FastAPI, Depends
import uvicorn

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.student import router as StudentRouter

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

def start():
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)

app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(StudentRouter,tags=["Students"],prefix="/student",dependencies=[Depends(token_listener)],)
