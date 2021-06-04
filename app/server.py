from fastapi import FastAPI
from app.views import routes
from app.db import db_engine

app = FastAPI(title='Zaim test')
app.include_router(routes)


@app.on_event("startup")
async def startup() -> None:
    await db_engine.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await db_engine.close()
