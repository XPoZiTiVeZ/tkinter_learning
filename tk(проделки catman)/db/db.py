from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



engine = create_engine("sqlite:///db.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(16))
    password = Column(String(64))
    role = Column(String(32))

    def authenticate(login, password):
        user = session.query(User).filter(User.login==login, User.password==password).first()
        if user != None:
            return user
        else:
            return None



class Product(Base):
    __tablename__ = "Product"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    num = Column(String(16))
    name = Column(String(64))
    product = Column(String(32))
    quantity = Column(String(32))
    time = Column(String(32))

    def all():
        prodlist=[]
        for a in session.query(Product).all():
          prodlist.append([a.num, a.name, a.product, a.quantity, a.time ])
        return prodlist






Base.metadata.create_all(engine)

