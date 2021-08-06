from os import environ

class Config:
	
	ENV= environ.get("TESTـENV","production")
	
	DEBUG=int(environ.get("TESTـDEBUG","0"))
	
	
	SQLALCHEMY_DATABASE_URI=environ.get("DATABASE_URI",'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='', server='localhost', database='mydb'))
	
	
	SQLALCHEMY_TRACK_MODIFICATIONS=DEBUG
	
