import psycopg2
import sys
from logger.logger import Logger
class DB2Connector:
    __connection = None
    __logger = None
    def __init__(self):
        self.__logger = Logger()

    def getConnection(self, db_detail):
        try:
            if self.__connection == None:
                conn = psycopg2.connect(user=db_detail.get_user(), password=db_detail.get_password(),
                                        host=db_detail.get_host(),
                                        port=db_detail.get_port(),
                                        database=db_detail.get_database())
                self.__logger.log("Info", "Connection established sucessfully--------")
                self.__connection = conn
            else:
                return self.__connection
        except Exception as e:
            self.__logger.log("Info", "Can't connect to postgres database {}".format(e))
            #sys.exit(1)
        return self.__connection
