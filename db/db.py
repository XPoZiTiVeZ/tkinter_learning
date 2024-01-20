from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///db.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True)
    login = Column(String(16))
    password = Column(String(64))
    role = Column(String(32))
    
    def authenticate(login, password):
        user = session.query(User).filter(User.login==login, User.password==password).first()
        if user != None:
            return user
        else:
            return None


Base.metadata.create_all(engine)