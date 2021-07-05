from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId
from src.models.object_id import PyObjectId

class MessageModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    author: str = Field(...)
    group: str = Field(...)
    value: str = Field(...)
    blame_timestamp: datetime = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "author": "pariz",
                "group": "test",
                "value": "Mensaje",
                "blame_timestamp": "2021-07-04 00:00:00",
            }
        }
