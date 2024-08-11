from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.settings import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)
