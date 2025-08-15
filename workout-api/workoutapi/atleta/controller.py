from atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate, AtletaResumo
from contrib.dependencies import DatabaseDependency
from fastapi import APIRouter, status, Body, HTTPException
from atleta.models import AtletaModel
from uuid import uuid4
from datetime import datetime
from sqlalchemy.future import select
from categorias.models import CategoriaModel
from centro_treinamento.models import CentroTreinamentoModel
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
import re
from fastapi_pagination import paginate, Page


router = APIRouter()

@router.post('/', summary="Create a new athlete", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    categoria_name = atleta_in.categoria.nome
    centro_treinamento_name = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_name))).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'A categoria {categoria_name} não foi encontrada.')

    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_name))).scalars().first()

    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'O Centro de Treinamento {centro_treinamento_name} não foi encontrada.')

    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude=('categoria', 'centro_treinamento')))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        db_session.add(atleta_model)
        await db_session.commit()
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}"
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao inserir os dados no banco de dados."
        )

    return atleta_out

@router.get('/', summary="Consult all athletes", status_code=status.HTTP_200_OK, response_model=list[AtletaOut],)
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scalars().all()

    return [AtletaOut.model_validate(atleta) for atleta in atletas]

# @router.get('/{id}', summary="Consult athlete for id", status_code=status.HTTP_200_OK, response_model=AtletaOut,)
# async def query(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
#     atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

#     if not atleta:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no id: {id}')

#     return atleta

@router.get('/{id}', summary="Consult athlete by id, cpf or nome", status_code=status.HTTP_200_OK, response_model=AtletaResumo)
async def query(id: str, db_session: DatabaseDependency) -> AtletaResumo:
    query = select(AtletaModel).options(
        selectinload(AtletaModel.categoria),
        selectinload(AtletaModel.centro_treinamento)
    )

    try:
        uuid_val = UUID4(id)
        query = query.filter(AtletaModel.id == uuid_val)
    except ValueError:
        if re.fullmatch(r"\d{11}", id):
            query = query.filter(AtletaModel.cpf == id)
        else:
            query = query.filter(AtletaModel.nome.ilike(f"%{id}%"))

    atleta = (await db_session.execute(query)).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado com identificador: {id}')

    return AtletaResumo(
        nome=atleta.nome,
        categoria={"nome": atleta.categoria.nome},
        centro_treinamento={"nome": atleta.centro_treinamento.nome}
    )


@router.get('/', summary="List athletes with pagination", status_code=status.HTTP_200_OK, response_model=Page[AtletaResumo])
async def query_all(db_session: DatabaseDependency) -> Page[AtletaResumo]:
    atletas = (
        await db_session.execute(
            select(AtletaModel)
            .options(
                selectinload(AtletaModel.categoria),
                selectinload(AtletaModel.centro_treinamento)
            )
        )
    ).scalars().all()

    atletas_resumo = [
        AtletaResumo(
            nome=a.nome,
            categoria={"nome": a.categoria.nome},
            centro_treinamento={"nome": a.centro_treinamento.nome}
        ) for a in atletas
    ]

    return paginate(atletas_resumo)

@router.patch('/{id}', summary="Edit a athlete for id", status_code=status.HTTP_200_OK, response_model=AtletaOut,)
async def get(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no id: {id}')

    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)
    
    await db_session.commit()
    await db_session.refresh(atleta)
    return atleta

@router.delete('/{id}', summary="Delete a athlete for id", status_code=status.HTTP_204_NO_CONTENT)
async def get(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no id: {id}')
    
    await db_session.delete(atleta)
    await db_session.commit()
    return atleta