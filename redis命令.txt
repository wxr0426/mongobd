redis命令.py

一、String
	概述：string是redis最基本的类型，最大能存储512MB的数据，string
	类型是二进制安全的，既可以存储任何数据，比如数字、图片、序列化对象等
	1、设置
		a、设置键值
			set key value
		b、设置键值及过期时间，以秒为单位
			setex key seconds value
		c、设置多个键值
			mset key value [key value ....]
	2、获取
		a、根据键获取值，如果键不存在则返回None
			get key
		b、根据多个键获取多个值
			mget key [key ...]
	3、运算
		要求：只是字符串类型的数字
		a、将key对应值加1
			incr key
		b、减1
			decr key
		c、加整数
			incrby key intnum
		d、减整数
			decrby key intnum
	4、其他
		a、追加值
			append key value
		b、	获取值长度
			strlen key
二、key
	1、查找键，参数支持正则
		keys pattern
	2、判断键是否存在，存在返回1，不存在返回0
		exists key
	3、查看键对应的value类型
		type key
	4、删除键及对应的值
		del key [key ...]
	5、设置过期时间，以秒为单位
		expire key seconds
	6、查看有效时间，以秒为单位
		ttl key
三、hash
	概述：hash用于存储对象
	{
		name:"tom",
		age:18
	}

	1、设置
	 	a、设置单个值
	 		hset key field value
	 	b、设置多个值
	 		hmset key field value [value,value,...]
	 		示例：hmset p1 name "" age 14
	2、获取
		a、获取一个属性的值
			hget key field
		b、获取多个属性的值
			hmget key field [field....]
		c、获取所有的属性和值
			hgetall key
		d、获取所有属性
			hkeys key
		e、获取所有的值
			hvals key
		f、返回包含数据的个数
			hlen key
	3、其他
		a、判断属性是否存在，存在返回1，不存在返回0
			hexists key field
		b、删除属性及值
			hdel key field [field....]
		c、返回值的字符串长度
			hstrlen key value
四、list
	概述：列表的元素类型为string，按照插入的顺序排序，在列表的
	头部或尾部添加元素
	1、设置
		a、在头部插入
			lpush key value [value ...]
		b、在尾部插入
			rpush key value [value ...]
		c、在一个元素的前|后插入新元素
			linsert key before|after pivot value
		d、设置指定索引的元素值
			lset key index value
			注意：index从0开始
			注意：索引数可以为负数，表示偏移量是从list的尾部
			开始，如-1表示最后一个元素
	2、获取
		a、移除并返回key对应的list的第一个元素
			lpop key
		b、移除并返回key对应的list的最后一个元素
			rpop key
		c、返回存储在key的列表中的指定范围元素
			lrange key start end
	3、其他
		a、裁剪列表，改为原集合的一个子集
			
		b、返回
		c、返回列表中索引对应的值
			lindex key index
五、set
六、zset