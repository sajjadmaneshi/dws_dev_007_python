

from sqlalchemy import create_engine

def check_db_connection(databaseUrI):
    try:
        engine=create_engine(databaseUrI)
        engine.connect()
        return 0
    except:
        return 1