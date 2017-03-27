#!/user/bin/python
# -*- coding: UTF-8 -*-

from com.study.python.model import UserDTO


class UserMgr:
    def __init__(self):
        pass

    def desc(self,user):
        if user is None or not isinstance(user, UserDTO.UserDTO):
            raise ValueError
        else:
            print(user)


    def save(self,user):
        if user is None or not isinstance(user, UserDTO.UserDTO):
            raise ValueError
        else:
            pass

    def update(self,user):
        if user is None or not isinstance(user, UserDTO.UserDTO):
            raise ValueError
        else:
            pass

    def delete(self,user):
        if user is None or not isinstance(user, UserDTO.UserDTO):
            raise ValueError
        else:
            pass

    def get(self,id):
        if id is None:
            raise ValueError
        else:
            pass

    def list(self,param):
        pass