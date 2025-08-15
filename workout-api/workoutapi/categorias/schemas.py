from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import UUID4, Field

class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", examples=["Scale"], max_length=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da Categoria")]
