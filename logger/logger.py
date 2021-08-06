import sys
from connect_db import check_db_connection





def stdout_logger(data_base_uri):
    stdout_fileno=sys.stdout

    db_connection_status=check_db_connection(data_base_uri)

    if db_connection_status==0:
        stdout_fileno.write("connected success" + '\n')
    elif db_connection_status==1:
        stdout_fileno.write("connection failed" + '\n')
        
