#!/usr/bin/env python3

class UserData(object):
    def __init__(self, iden, name):
        self.name = name
        self.iden = iden

    def __repr__(self):
        return "ID:{} Name:{}".format(self.name, self.iden)

class NewUser(UserData):
    group = 'shiyanlou-louplus'

    @classmethod
    def get_group(cls):
        return cls.group
    
    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value

    @staticmethod
    def format_userdata(id, name):
        return "{}'s id is {}".format(name, id)

if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109, 'Lucy'))
