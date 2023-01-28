from pydantic import BaseModel, Field

class Task(BaseModel):
    id:int = Field(default=None)
    title:str = Field(default=None)
    content:str = Field(default=None)
    class Config:
        the_schema = {
            "userdemo": {
                "name": "Bek",
                "email": "example@gmail.com",
                "password": "123",
            }
        }
