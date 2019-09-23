#!/usr/bin/env python3

class UserData(object):
    def __init__(self, id, _name):
        self.id = id
        self._name = _name

class NewUser(UserData):
    group = 'shiyanlou-louplus'

    def __init__(self, iden, _name):
        UserData.__init__(self, id, _name)

    @classmethod
    def get_group(cls):
        return cls.group
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            print("ERROR")

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
