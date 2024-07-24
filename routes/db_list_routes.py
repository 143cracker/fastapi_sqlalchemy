from fastapi import Response,Query,APIRouter ,Depends
from controller.db_list_controller import DbListController
from fastapi.responses import JSONResponse
from starlette.requests import Request
from utils.custom_response import gen_response
class DblistRoute:
    application = app = {}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            print("creating DblistRoute object12")
            cls.instance = super(DblistRoute, cls).__new__(cls)
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""

        return cls.instance

    def __init__(self):
        self.app = APIRouter()
        self.esc_controller = DbListController()
        self.application = self.app
        self.__add_routes()


    def __add_routes(self):
        self.app.add_api_route(path="/getdblist",endpoint=self.get_db_list,
            methods=["POST"],
        )

    async def get_db_list(self):
    
        try:
           db_list = self.esc_controller.dblist()
           return JSONResponse(
                status_code=200,
                content= gen_response(False,True,"DB Info got successfully",db_list)
           
            )
        except Exception as error:
            return JSONResponse(
                status_code=500,
                content= gen_response(True,False,"something went wrong:{}".format(str(error)),None)
           
            )
