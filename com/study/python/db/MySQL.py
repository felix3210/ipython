#!/user/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/3/28 16:16
# @Author  : felix
# @Contact : wi1024u@gmail.com
# @File    : MySQL.py
# @Desc    : Example how to connection to MySQL db

import MySQLdb
from com.study.python.mgr import UserMgr
from com.study.python.model import UserDTO

dbConnection = None
try:
    ''' 1. open mysql database '''
    dbConnection = MySQLdb.connect('127.0.0.1', 'root', 'root', 'pydb')

    ''' 2. assign the cursor class '''
    cursor = dbConnection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute("insert into tb_user(name,mobile,email,gender,register_date) values('test-user-01','18610132535','songfei@gmail.com',1,'2016-03-25 19:06:00')")
    # dbConnection.commit()
    cursor.execute("select * from tb_user order by register_date desc ")

    rows = cursor.fetchmany(10)
    for row in rows:
        user = UserDTO.UserDTO(row['id'], row['name'], row['mobile'], row['email'], row['gender'])
        UserMgr.UserMgr().desc(user)
except BaseException , e:
    # dbConnection.rollback()
    print "[err] : " , e
finally:
    if dbConnection:
        dbConnection.close()
