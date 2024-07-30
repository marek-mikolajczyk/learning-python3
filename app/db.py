import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from json import loads, dumps


######################### get the data #########################
df =  pd.read_csv(
        'passwd', sep=':', 
        header=None, 
        names=[
            'username', 
            'ispwdset',
            'UID',
            'GID',
            'GECOS',
            'homedir',
            'shell'
            ])

preresult = df[['username', 'UID', 'GID', 'homedir', 'shell']]
result = preresult.to_json(orient='records')
parsed = loads(result)
#sprint(dumps(parsed, indent=4))

######################### end of the data #########################

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine(
   "mariadb+mariadbconnector://user:password@127.0.0.1:3306/db",
   echo=False)

# create catalog of future classes
Base = declarative_base()


# create schema for table employee
class User(Base):
   __tablename__ = 'Users'
   username = sqlalchemy.Column(sqlalchemy.String(length=100), primary_key=True)
   UID = sqlalchemy.Column(sqlalchemy.Integer)
   GID = sqlalchemy.Column(sqlalchemy.Integer)
   homedir = sqlalchemy.Column(sqlalchemy.String(length=100))
   shell = sqlalchemy.Column(sqlalchemy.String(length=100))
  

Base.metadata.create_all(engine)

# Create a session - orm, sql querries
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def addUser(username, uid, gid, shell, homedir):
   newUser = User(username=username, UID=uid, GID=gid, shell=shell, homedir=homedir)
   session.add(newUser)
   session.commit()




def selectAll():
   users = session.query(User).all()
   for user in users:
        pass
        # print(" - " + user.username + ' ' + str(user.uid))



session.query(User).delete()
session.commit()

for r in parsed:
        print(r)
        addUser(r['username'],r['UID'],r['GID'],r['shell'],r['homedir'])


# Show all users
#print('All Users')
#selectAll()
#print("----------------")
