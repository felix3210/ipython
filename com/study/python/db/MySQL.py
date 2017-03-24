#!/user/bin/python
# -*- coding: UTF-8 -*-

import UserDTO
import UserManger
import MySQLdb

dbConnection = None
try:
    ''' 1. open mysql database '''
    dbConnection = MySQLdb.connect('192.168.30.71', 'root', 'xbntest', 'soadb')

    ''' 2. assign the cursor class '''
    cursor = dbConnection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("select * from xbn_user order by register_time desc ")

    rows = cursor.fetchmany(10)
    for row in rows:
        user = UserDTO.UserDTO(row['id'], row['name'], row['mobile'], row['email'], row['gender'])
        UserManger.UserManager().desc(user)
except BaseException , e:
    print "[err] : " , e
finally:
    if dbConnection:
        dbConnection.close()
