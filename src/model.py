from pydantic import BaseModel,Field,EmailStr


class Postschema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content : str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo":{
                "title":"users",
                "content":"users auth"
            }
        }



class UserSchema(BaseModel):
    fullname:str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema= {
            "user_demo":{
                "name":"Andrew",
                "email":"andrew@yahoo.com",
                "password":"578784"
            }
        }



class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema= {
            "user_demo":{
                "email":"andrew@yahoo.com",
                "password":"578784"
            }
        }




