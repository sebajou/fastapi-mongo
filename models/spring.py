from datetime import date

from beanie import Document
from pydantic import BaseModel


class SpringComposition(Document):
    elementName: str
    formula: str
    quantity: str
    unity: str


class SpringPrice(Document):
    price: int
    money: str
    by: str
    country: str


class SpringLocalisation(Document):
    longitude: int
    lattitude: int


class Spring(Document):
    class Settings:
        name = "springs"

    name: str
    composition: list[SpringComposition]
    description: str
    brand: str
    price: list[SpringPrice]
    localisation: SpringLocalisation
    startExploitationDate: date

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
