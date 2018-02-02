from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类：
Base = declarative_base()

# 定义User对象:
class User(Base):
	__tablename__ = 'user'
	
	# 表的结构
	id = Column(String(20), primary_key= True)
	name = Column(String(20))


# 初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://jump:jump@localhost:3306/python_db')
# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)

# 创建session对象：
session = DBSession()
# # 创建新User对象：
# new_user = User(id=3, name='小刚')
# # 添加到session:
# session.add(new_user)
# session.commit()
# session.close()
user = session.query(User).filter(User.id == '2').one()
print('Type:', type(user))
print('name:', user.name)
session.close()
