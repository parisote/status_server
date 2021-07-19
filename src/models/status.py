from pydantic import BaseModel, Field, validator
from datetime import datetime
from bson import ObjectId
from src.models.object_id import PyObjectId

class StatusModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    server: str = Field(...)
    implementation: str = Field(...)
    value: str = Field(...)
    blame_timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "server": "server",
                "implementation": "test",
                "value": "Mensaje server",
                "blame_timestamp": "2021-07-04 00:00:00",
            }
        }
