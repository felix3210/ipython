#!/user/bin/python
# -*- coding: UTF-8 -*-

class UserDTO:

    def __init__(self, id, name, mobile, email, gender):
        self.__id = id
        self.__name = name
        self.__mobile = mobile
        self.__email = email
        self.__gender = gender

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, value):
        self.__mobile = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.email = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    # override __str__ func
    def __str__(self):
        return 'id: %s, name: %s, mobile: %s, email: %s, gender: %s' % (self.__id, self.__name, self.__mobile, self.__email, self.__gender)