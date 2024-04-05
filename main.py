import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.controller import controller

app = FastAPI(title='Simple-Crud-Sqlite', version='v0.0.1', description='Simple CRUD Using Sqlite Database', docs_url='/')

app.include_router(router=controller.router, prefix='/api', tags=['CRUD'])

if __name__ == '__main__':
    uvicorn.run(app, port=7373, host="0.0.0.0")