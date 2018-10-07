pymango数据库.py

from pymango import MangoClient


添加文档
#连接服务器
conn = MangoClient("localhost",27017)
#连接数据库
db=conn.mydb
#获取集合
collection = db.student
#添加文档
collection.insert({})
#collection.insert([{},{},{}])  添加多个文档
#断开
conn.close()

查询文档
#连接服务器
conn = MangoClient("localhost",27017)
#连接数据库
db=conn.mydb
#获取集合
collection = db.student
#查询所有文档
res = collection.find()
#查询部分文档
res = collection.find()
for row in res:
	print(row)
	print(type(row))
#统计查询文档
res = collection.find({}).count()
print(res)
#根据id查询,添加三方库
from bson.objectid import ObjectID
res = collection.find({"_id":ObjectID("id")})
print(res[0])
#排序
res = collection.find().sort("age")
#分页查询
res = collection.find().skip(3).limit(3)
??????????????
#断开
conn.close()





删除文档
#连接服务器
conn = MangoClient("localhost",27017)
#连接数据库
db=conn.mydb
#获取集合
collection = db.student
#删除文档
collection.remove({文档})
#删除全部
collection.remove()
#断开
conn.close()