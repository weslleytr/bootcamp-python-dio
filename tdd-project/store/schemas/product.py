from datetime import datetime
from typing import Optional
from pydantic import UUID4, Field, BaseModel
from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[float] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate):
    ...
