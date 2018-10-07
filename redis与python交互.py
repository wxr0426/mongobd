redis与python交互.py

import redis
#连接
r= redis.StringRedis("localhost",port=6379,password="haolj")

#方法一、根据数据类型的不同，调用相应的方法
#写
#r.set("key","value")
#读
#print(r.get("key"))
#方法二、pipline （管道）
#缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set(key,value)
pipe.set(key,value)
pipe.set(key,value)
pipe.execute()