from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class UserDataSchema(BaseModel):
    id_user: int
    nama: str = Field(..., min_length=2, description="Nama tidak boleh kosong")
    email: EmailStr
    nik: str = Field(..., min_length=16, max_length=16)
    umur: Optional[int] = Field(None, ge=0, le=120)

    @field_validator('nik')
    @classmethod
    def validate_nik_digits(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError("NIK harus berupa 16 digit angka")
        return value