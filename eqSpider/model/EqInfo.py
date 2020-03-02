from sqlalchemy import Column,String,Integer,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()
class EqInfo(Base):
    __tablename__ = "eq_info"
    # id = Column(Integer , primary_key=True , autoincrement=True)
    Cata_id = Column(String(40), primary_key=True)
    Eq_type = Column(Integer)
    O_time = Column(DateTime, default=datetime.datetime.utcnow)
    Lat = Column( Float(10))
    Lon = Column( Float(10))
    geom = Column( String(100))
    Depth = Column( Float(10))
    M = Column( Float(10))
    Location_cname = Column( String(128))
    is_create_pic = Column(Integer)  
    def __init__(self, **items):
        for key in items:
            if hasattr(self,key):
                setattr(self,key,items[key])
    def __str__(self):
        return "<EqInfo(Cata_id %s,Location_cname %s)>" %(self.Cata_id,self.Location_cname)

class MyShinyClass(object):
    __tablename__ = "eq_info"
    # id = Column(Integer , primary_key=True , autoincrement=True)
    Cata_id = Column(String(40), primary_key=True)
    Eq_type = Column(Integer)
    O_time = Column(DateTime, default=datetime.datetime.utcnow)
    Lat = Column( Float(10))
    Lon = Column( Float(10))
    geom = Column( String(100))
    Depth = Column( Float(10))
    M = Column( Float(10))
    Location_cname = Column( String(128))
    is_create_pic = Column(Integer)
    def __init__(self, **items):
        for key in items:
            if hasattr(self,key):
                setattr(self,key,items[key])
    def __str__(self):
        return "<EqInfo(Cata_id %s,Location_cname %s)>" %(self.Cata_id,self.Location_cname)