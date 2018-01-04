#!/user/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/3/28 16:16
# @Author  : felix
# @Contact : wi1024u@gmail.com
# @File    : Data2UC.py
# @Desc    : Transform b2c user to uc database

import MySQLdb
from com.study.python.mgr import UserMgr
from com.study.python.model import UserDTO

dbConnection = None
try:
    ''' 1. open mysql database '''
    dbConnection = MySQLdb.connect('192.168.30.71', 'root', 'xbntest', 'soadb')

    ''' 2. assign the cursor class '''
    cursor = dbConnection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute("insert into tb_user(name,mobile,email,gender,register_date) values('test-user-01','18610132535','songfei@gmail.com',1,'2016-03-25 19:06:00')")
    # dbConnection.commit()
    cursor.execute("select id, name , mobile,email,password,register_time,avatar_id,gender from xbn_user order by register_time desc ")

    rows = cursor.fetchmany(10)

    ''' 3. fetch TwitterSnowFlake id'''


    ''' 4. change password '''

    ''' 5. save bizUserId '''

    for row in rows:
        user = UserDTO.UserDTO(row['id'], row['name'], row['mobile'], row['email'], row['gender'])
        UserMgr.UserMgr().desc(user)
except BaseException , e:
    # dbConnection.rollback()
    print "[err] : " , e
finally:
    if dbConnection:
        dbConnection.close()
