from datetime import date
from typing import List, Optional

from beanie import Document, Link
from pydantic import BaseModel


# class SpringComposition(Document):
#     elementName: str
#     formula: str
#     quantity: str
#     unity: str
#
#
# class SpringPrice(Document):
#     price: int
#     money: str
#     by: str
#     country: str
#
#
class SpringLocalisation(Document):
    longitude: int
    latitude: int


class Spring(Document):
    name: Optional[str]
    composition: Optional[list[dict]]
    description: Optional[str]
    brand: Optional[str]
    price: Optional[list[dict]]
    localisation: Optional[dict]
    startExploitationDate: Optional[date]

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
                    },
                ],
                "description": "to being eternaly youngth",
                "brand": "Youngest",
                "price": [
                    {
                        "price": 5000,
                        "money": "USD",
                        "by": "year",
                        "country": "USA",
                    },
                ],
                "localisation": {
                    "longitude": 10,
                    "latitude": 10,
                },
                "startExploitationDate": "2023-05-05",
            }
        }

    class Settings:
        name = "springs"
