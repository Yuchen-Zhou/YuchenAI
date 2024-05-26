from BackEnd.Postgresql import Session, AsyncSession

def postgresql(fn):
    def wrapper(*args, **kwargs):
        with Session() as session:
            kwargs['postgresql'] = session
            return fn(*args, **kwargs)
    return wrapper

async def async_postgresql(fn):
    async def wrapper(*args, **kwargs):
        async with AsyncSession() as session:
            async with session.begin():
                kwargs['postgresql'] = session
                return await fn(*args, **kwargs)
    return wrapper