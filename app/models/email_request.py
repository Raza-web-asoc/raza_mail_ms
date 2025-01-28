from pydantic import BaseModel, EmailStr

class EmailRequestMatch(BaseModel):
    to_email: EmailStr
    name1: str
    name2: str
    pet_name1: str
    pet_name2: str

class EmailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str