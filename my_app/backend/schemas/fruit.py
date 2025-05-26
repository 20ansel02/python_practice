from pydantic import BaseModel, Field

class FruitIn(BaseModel):
    id: int = Field(..., description="The unique identifier for the fruit")
    name: str = Field(..., description="The name of the fruit")
    color: str = Field(..., description="The color of the fruit")
    weight: float = Field(..., description="The weight of the fruit in grams")
    price_per_kg: float = Field(..., description="The price of the fruit per kilogram")
    #new_column: str = Field(default="", description="A new column for additional information")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Apple",
                "color": "Red",
                "weight": 150.0,
                "price_per_kg": 3.5,
                #"new_column": "Additional info"
            }
        }


class FruitOut(BaseModel):
    id: int = Field(..., description="The unique identifier for the fruit")
    name: str = Field(..., description="The name of the fruit")
    color: str = Field(..., description="The color of the fruit")
    weight: float = Field(..., description="The weight of the fruit in grams")
    price_per_kg: float = Field(..., description="The price of the fruit per kilogram")
    #new_column: str = Field(default="", description="A new column for additional information")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Apple",
                "color": "Red",
                "weight": 150.0,
                "price_per_kg": 3.5,
                #"new_column": "Additional info"
            }
        }