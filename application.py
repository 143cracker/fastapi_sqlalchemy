from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routes.db_list_routes import DblistRoute


app=FastAPI()


application = app = FastAPI(
    title="Fnc Internal",
    version="dev-1",
    description="Fnc Internal APIs for UI Integration ",
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(DblistRoute().app, tags=["DB LIST"])

if __name__=="__main__":
   uvicorn.run(app,reload=True)

