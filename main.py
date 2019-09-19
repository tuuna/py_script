#!/usr/bin/python
# -*- coding: utf-8 -*-

from faker import Faker
import random
import logging
import time
import json
import os


faker = Faker("zh-CN")

# print("尝试连接mongodb数据库...")
#
# client = pymongo.MongoClient(host="localhost", port=20000)
# db = client.testdb
#
# print("连接数据库成功.")
#
# col = db.user
# db.user.create_index("uid")
# print("尝试向testdb.user表中插入数据...")

data1 = ""
# data2 = []
f = open("./user.json", "a")
for i in range(2):

    for j in range(10):
        uid = "uid" + "%06d" % (i * 10000 + j)
        name = faker.name()
        age = random.randint(15, 60)
        phone = faker.phone_number()
        address = faker.address()

        info = {"uid": uid, "name": name, "age": age, "phone": phone, "address": address}

        data1 += (str(info)+",")
        print("插入成功第%d次的第%d条user数据，等待下一次插入" %(i , j))
    
        if i == 0 and j == 0:
            f.write("[")
            f.write(str(data1))
        else :
            f.write(str(data1))
f.close()
file = open("./user.json","rb+")
file.seek(-1, os.SEEK_END)
file.truncate()
file.write(b"]")
file.close()


print("第%d加载入文件完成..." %i)


print("向testdb.user表中插入数据完成\n开始尝试向testdb.order表中插入数据...")
#
# col = db.order
# db.order.create_index("uid")
#
# for i in range(20000):
#    for j in range(10000):
#        uid = "uid" + "%06d" % (random.randint(0, 200000))
#        name = "商品" + "%03d" % random.randint(1, 1000)
#        money = round(random.uniform(8, 1000), 2)
#
#        data2.append({"uid": uid, "name": name, "money": money})
#        print("插入成功第%d次的第%d条user数据，等待下一次插入" % (i,j))
#
#    # order_jso
# with open("./order.json", "a", encoding='utf-8') as f:
#    json.dump(data,f,ensure_ascii=False)
#    # f.write(order_json_str)
#    print("第%d加载入文件完成..." %i)
# print("向testdb.user表中插入数据完成")
