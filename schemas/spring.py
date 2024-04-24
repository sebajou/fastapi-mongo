from datetime import date
from typing import Optional

from pydantic import BaseModel


class UpdateSpringModel(BaseModel):
    name: Optional[str]
    composition: Optional[list]
    description: Optional[str]
    brand: Optional[int]
    price: Optional[list]
    localisation: Optional[dict]
    startExploitationDate: Optional[date]

    class Collection:
        name = "spring"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
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
                    "lattitude": 10,
                },
                "startExploitationDate": "2022-01-01",
            }
        }
