#!/user/bin/python
# -*- coding: UTF-8 -*-

import UserDTO


class UserManager:
    def __init__(self):
        pass

    def desc(self,user):
        if user is None or not isinstance(user, UserDTO.UserDTO):
            raise ValueError
        else:
            print(user)