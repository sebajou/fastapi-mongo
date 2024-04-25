from fastapi import APIRouter, Body

from database.database import *
from models.spring import Spring
from schemas.spring import Response, UpdateSpringModel
from .pika import send_message

router = APIRouter()


@router.get("/", response_description="Springs retrieved", response_model=Response)
async def get_springs():
    springs = await retrieve_springs()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Springs data retrieved successfully",
        "data": springs,
    }


@router.get("/{id}", response_description="Spring data retrieved", response_model=Response)
async def get_spring_data(id: PydanticObjectId):
    spring = await retrieve_spring(id)
    if spring:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Spring data retrieved successfully",
            "data": spring,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Spring doesn't exist",
    }


@router.post(
    "/",
    response_description="Spring data added into the database",
    response_model=Response,
)
async def add_spring_data(spring: Spring = Body(...)):
    print('send spring', spring)
    new_spring = await add_spring(spring)
    print('new spring', new_spring)
    await send_message(new_spring)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Spring created successfully",
        "data": new_spring,
    }


@router.delete("/{id}", response_description="Spring data deleted from the database")
async def delete_spring_data(id: PydanticObjectId):
    deleted_spring = await delete_spring(id)
    if deleted_spring:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Spring with ID: {} removed".format(id),
            "data": deleted_spring,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Spring with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.put("/{id}", response_model=Response)
async def update_spring(id: PydanticObjectId, req: UpdateSpringModel = Body(...)):
    updated_spring = await update_spring_data(id, req.dict())
    if updated_spring:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Spring with ID: {} updated".format(id),
            "data": updated_spring,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Spring with ID: {} not found".format(id),
        "data": False,
    }
