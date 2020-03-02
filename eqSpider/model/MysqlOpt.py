from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from eqSpider.model import EqInfo
import datetime
import time
class MysqlOpt(object):
    def __init__(self):
        # 创建连接对象，并使用 pymsql 引擎
        self.engine = create_engine("mysql+mysqlconnector://root:123456@localhost/eq?charset=utf8",echo=False,max_overflow=5)
        self.session = sessionmaker(bind=self.engine)
        self.sess = self.session()
    def insert(self,item,tb_name):
        eqInfo = EqInfo.EqInfo()
        Base = declarative_base()
        if not hasattr(self,tb_name):
            self.Article = type(tb_name, (Base,EqInfo.MyShinyClass,), {'__tablename__': tb_name, })
        if tb_name not in self.engine.table_names(): #create table for this spider
            self.Article.metadata.create_all(self.engine)
        dt1 = self.queryMaxDateTime()        
        dt2 = time.mktime(item['O_time'].timetuple())
        isUpdate = False
        if not dt1:
            isUpdate = True
        if dt1 and (dt2-dt1) > 0 :            
            isUpdate = True
        if isUpdate and not self.queryIsExist(item):
            self.sess.add(self.Article(**item))
            self.sess.commit()
    def queryMaxDateTime(self):
        a = self.sess.query(self.Article).order_by(self.Article.O_time.desc()).first()
        if a:
            return time.mktime(a.O_time.timetuple())
    def queryIsExist(self,item):
        return self.sess.query(self.Article).filter(self.Article.Cata_id == item['Cata_id']).all()
    def close_session(self):#关闭爬虫时
        self.sess.close()