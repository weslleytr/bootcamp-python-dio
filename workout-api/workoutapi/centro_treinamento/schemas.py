from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import Field, UUID4

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", examples=["CT King"], max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", examples=["Rua X, 002"], max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento", examples=["Sarah"], max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", examples=["CT King"], max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do Centro de Treinamento")]