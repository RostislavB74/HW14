from datetime import date, datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict

from src.database.models import Role

class ContactModel(BaseModel):
    first_name: str = Field(
        default="",
        examples=["Taras", "Ostap"],
        min_length=1,
        max_length=25,
        title="Ім'я",
    )
    last_name: str = Field(
        default="",
        examples=["Shevcheko", "Bulba"],
        min_length=1,
        max_length=25,
        title="Прізвище",
    )
    email: EmailStr
    phone: str | None = Field(
        None,
        examples=["+380 44 123-4567", "+380 (44) 1234567", "+380441234567"],
        max_length=25,
        title="Номер телефону",
    )


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: date
    additional_data: str = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
class UserModel(BaseModel):
    username: str = Field(max_length=12)
    email: EmailStr
    password: str = Field(max_length=12)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    avatar: str
    roles: Role

    class Config:
        from_attributes = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RequestEmail(BaseModel):
    email: EmailStr

class ContactBase(BaseModel):
    id: int
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone: str | None
    birthday: date | None
    comments: str | None
    favorite: bool
    created_at: datetime
    updated_at: datetime
    user: UserResponse

    # class Config:
    #     from_attributes = True

    model_config = ConfigDict(from_attributes=True)