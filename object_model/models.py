from pydantic import BaseModel


# 对象映射

class LoginModel(BaseModel):
    username: str = ''
    password: str = ''

