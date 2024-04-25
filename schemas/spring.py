from datetime import date
from typing import Optional, Any

from pydantic import BaseModel


class UpdateSpringModel(BaseModel):
    name: Optional[str]
    composition: Optional[list]
    description: Optional[str]
    brand: Optional[str]
    price: Optional[list]
    localisation: Optional[dict]
    startExploitationDate: Optional[date]

    class Collection:
        name = "spring"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Youngest spring source",
                "composition": [
                    {
                        "elementName": "Water",
                        "formula": "H2O",
                        "quantity": "10",
                        "unity": "g",
                    }
                ],
                "description": "to being eternaly youngth",
                "brand": "Youngest",
                "price": [
                    {
                        "price": 5000,
                        "money": "USD",
                        "by": "year",
                        "country": "USA",
                    }
                ],
                "localisation": {
                    "longitude": 10,
                    "latitude": 10,
                },
                "startExploitationDate": "2022-01-01",
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
