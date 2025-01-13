from pydantic import BaseModel

class ProductValidator(BaseModel):
  name: str
  price: int
