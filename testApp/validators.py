from pydantic import BaseModel, EmailStr, Field

class ProductValidator(BaseModel):
  # id: str
  name: str
  price: int
  email: EmailStr
  code: str = Field(pattern=r"^[A-Za-z\d]{8}$")

  # @classmethod
  # def code(cls, code):
  #     # Validasi panjang minimal 8 karakter
  #     if len(code) < 8:
  #         raise ValueError("code harus minimal 8 karakter")
      
  #     # Validasi dengan regex untuk huruf kapital, non-kapital, dan angka
  #     if not re.search(r'[A-Z]', code):
  #         raise ValueError("code harus mengandung minimal 1 huruf kapital (A-Z)")
  #     if not re.search(r'[a-z]', code):
  #         raise ValueError("code harus mengandung minimal 1 huruf non-kapital (a-z)")
  #     if not re.search(r'\d', code):
  #         raise ValueError("code harus mengandung minimal 1 angka (0-9)")

  #     return code