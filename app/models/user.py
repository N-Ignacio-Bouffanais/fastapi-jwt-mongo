from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    email: str = Field(default= None)
    password: str = Field(default= None)
    class Config:
        the_schema = {
            "userdemo":{
                "email": "example@gmail.com",
                "password": "123",
            }
        }
