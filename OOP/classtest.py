#!/usr/bin/env python3

class UserData:
    def __init__(self, iden, name):
        self.name = name
        self.iden = iden

    def __repr__(self):
        return "ID:{} Name:{}".format(self.name, self.iden)


if __name__ == '__main__':
    user1 = UserData(101, 'Jack')
    user2 = UserData(102, 'Louplus')
    print(user1)
    print(user2)
