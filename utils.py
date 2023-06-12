from pydantic import BaseModel
from sqlalchemy import insert, update, select, delete, Table
from sqlalchemy.ext.asyncio import AsyncSession


async def create_new_element(session: AsyncSession, table: Table, data: BaseModel):
    try:
        await session.execute(
            insert(table).
            values(**data.dict())
        )
        await session.commit()
    except:
        await session.rollback()
        raise


async def update_element(session: AsyncSession, table: Table, data: BaseModel, item_id):
    try:
        await session.execute(
            update(table).
            where(table.c.id == item_id).
            values(**data.dict())
        )
        await session.commit()
    except:
        await session.rollback()
        raise


async def get_element(session: AsyncSession, table: Table, item_id: int):
    result = await session.execute(
        select(table).
        where(table.c.id == item_id))
    return result.fetchone()


async def get_elements_list(session: AsyncSession, table):
    result = await session.execute(
        select(table)
    )
    return result.fetchall()


async def delete_element(session: AsyncSession, table: Table, item_id: int):
    try:
        await session.execute(
            delete(table).
            where(table.c.id == item_id)
        )
        await session.commit()
    except:
        await session.rollback()
        raise
