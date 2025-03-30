from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from Database.models import User, Group, Channel, GroupChannel, Subscription

class CRUD:
    @staticmethod
    async def get_user(session: AsyncSession, user_id: int):
        result = await session.execute(
            select(User).where(User.user_id == user_id)
        )
        return result.scalars().first()

    @staticmethod
    async def create_user(session: AsyncSession, user_data: dict):
        user = User(**user_data)
        session.add(user)
        await session.commit()
        return user

    # Add 30+ more CRUD operations for all models...
