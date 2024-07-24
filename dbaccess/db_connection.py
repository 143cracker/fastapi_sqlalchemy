from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from urllib.parse import quote_plus
from sqlalchemy.orm import declarative_base
Base1 = declarative_base()
Base2 = declarative_base()
class ProdDbSession:
    _instance = None

    def __new__(cls):
        # if cls._instance is None:
        #     print('Inside the Db Calls1')
        #     cls._instance = super(ProdDbSession, cls).__new__(cls)
        #     conn_string = "mysql://{}:%s@{}:{}/{}".format(
        #         config.db_user,
        #         config.db_host,
        #         config.db_port,
        #         config.lab_database
        #     ) % quote_plus(config.db_password)
        #     print(f"DB conn string : {conn_string}")
        #     try:
        #         cls._instance.engine = create_engine(
        #             conn_string,
        #             pool_size=config.db_conn_pool,
        #             max_overflow=config.db_conn_pool_max,
        #             pool_recycle=60,
        #             echo=False
        #         )
        #         cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        #         cls._instance.session = cls._instance.Session()
        #     except Exception as e:
        #         raise Exception(f"Error creating db engine:")
        #         cls._instance = None
        # return cls._instance
        try:
            if  cls._instance is None:
                print('Inside the Db Calls2')
                SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" 
                engine = create_engine(SQLALCHEMY_DATABASE_URL)
                SessionLocal=  sessionmaker(autocommit=False, autoflush=False, bind= engine )
                Base1.metadata.create_all(bind=engine)
                cls._instance= SessionLocal()
                
            return cls._instance
        except Exception as e:
            raise Exception(f"Error creating db engine:")
            cls._instance = None

   


class DevDbSession:
    _instance = None

    def __new__(cls):
        # if cls._instance is None:
        #     print('Inside the Db Calls1')
        #     cls._instance = super(ProdDbSession, cls).__new__(cls)
        #     conn_string = "mysql://{}:%s@{}:{}/{}".format(
        #         config.db_user,
        #         config.db_host,
        #         config.db_port,
        #         config.lab_database
        #     ) % quote_plus(config.db_password)
        #     print(f"DB conn string : {conn_string}")
        #     try:
        #         cls._instance.engine = create_engine(
        #             conn_string,
        #             pool_size=config.db_conn_pool,
        #             max_overflow=config.db_conn_pool_max,
        #             pool_recycle=60,
        #             echo=False
        #         )
        #         cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        #         cls._instance.session = cls._instance.Session()
        #     except Exception as e:
        #         raise Exception(f"Error creating db engine:")
        #         cls._instance = None
        # return cls._instance
        try:
            if  cls._instance is None:
                SQLALCHEMY_DATABASE_URL = "sqlite:///./test2.db" 
                engine = create_engine(SQLALCHEMY_DATABASE_URL)
                SessionLocal=  sessionmaker(autocommit=False, autoflush=False, bind= engine )
                Base2.metadata.create_all(bind=engine)
                cls._instance= SessionLocal()
                
            return cls._instance
        except Exception as e:
            raise Exception(f"Error creating db engine:")
            cls._instance = None

   

   
