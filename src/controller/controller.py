from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from http import HTTPStatus

from ..model import BodyResponse
from ..service import Service

class Controller:
    def __init__(self) -> None:
        self.router = APIRouter()
        self.service = Service()

        self.router.get('/create')(self.__create)
        self.router.get('/read')(self.__read)
        self.router.get('/update')(self.__update)
        self.router.get('/delete')(self.__delete)
        ...

    def __create(self,
            name: str = Query(..., description='Enter FullName'),
            username: str = Query(..., description='Enter username'),
            ages: int = Query(..., description='Enter Ages')) -> JSONResponse:

        try:
            response: dict | str = self.service.create(name, username, ages)
            if isinstance(response, str):
                return JSONResponse(content=BodyResponse(HTTPStatus.OK, response, None).__dict__, status_code=HTTPStatus.OK)

            return JSONResponse(content=BodyResponse(HTTPStatus.OK, 'succees', response).__dict__, status_code=HTTPStatus.OK)

        except Exception as err:
            return JSONResponse(content=BodyResponse(HTTPStatus.INTERNAL_SERVER_ERROR, str(err), None).__dict__, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        ...

    def __read(self, username: str = Query(..., description='Enter username')) -> JSONResponse:

        try:
            response: dict | str = self.service.read(username)
            if isinstance(response, str):
                return JSONResponse(content=BodyResponse(HTTPStatus.OK, response, None).__dict__, status_code=HTTPStatus.OK)

            return JSONResponse(content=BodyResponse(HTTPStatus.OK, 'succees', response).__dict__, status_code=HTTPStatus.OK)

        except Exception as err:
            return JSONResponse(content=BodyResponse(HTTPStatus.INTERNAL_SERVER_ERROR, str(err), None).__dict__, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        ...

    def __update(self,
            name: str = Query(..., description='Enter FullName'),
            username: str = Query(..., description='Enter username'),
            ages: int = Query(..., description='Enter Ages')) -> JSONResponse:

        try:
            response: dict | str = self.service.update(name, username, ages)
            if isinstance(response, str):
                return JSONResponse(content=BodyResponse(HTTPStatus.OK, response, None).__dict__, status_code=HTTPStatus.OK)
            
            return JSONResponse(content=BodyResponse(HTTPStatus.OK, 'succees', response).__dict__, status_code=HTTPStatus.OK)

        except Exception as err:
            return JSONResponse(content=BodyResponse(HTTPStatus.INTERNAL_SERVER_ERROR, str(err), None).__dict__, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        ...

    def __delete(self, username: str = Query(..., description='Enter username')) -> JSONResponse:

        try:
            response: dict | str = self.service.delete(username)
            if isinstance(response, str):
                return JSONResponse(content=BodyResponse(HTTPStatus.OK, response, None).__dict__, status_code=HTTPStatus.OK)

            return JSONResponse(content=BodyResponse(HTTPStatus.OK, 'succees', response).__dict__, status_code=HTTPStatus.OK)

        except Exception as err:
            return JSONResponse(content=BodyResponse(HTTPStatus.INTERNAL_SERVER_ERROR, str(err), None).__dict__, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        ...