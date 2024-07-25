
from fastapi import status
from dbaccess.db_connection import DevDbSession,ProdDbSession
from models.model import User,User1
import traceback
from fastapi.encoders import jsonable_encoder
import sqlalchemy as sa
from sqlalchemy import func, select
class DbListController:
    #here we are declear all method to access data from data base
    def dblist(self):
        try:
          
          #here we are access dev databases here we are using
          with DevDbSession() as session:
            result = session.query(User1).all()
            return jsonable_encoder(result)
          
       
          
        except Exception as e:
          traceback.format_exc()
          raise Exception (str(e))
          
