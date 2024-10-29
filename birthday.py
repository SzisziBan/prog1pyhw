import os
from datetime import datetime

from friend import Friend


class Program:
    def __init__(self):
        self.friends = None

    def main(self):
        self.friends = []
        if os.path.exists("friends.txt"):
            with open("friends.txt", "r") as file:
                for line in file:
                    self.friends.append(Friend.deserialize(line))

        code = self.print_menu()
        while code != 5:
            code = self.print_menu()

    def print_menu(self):
        print("1. Következő születésnap")
        print("2. Minden ismerős kilistázása")
        print("3. Keresés")
        print("4. Új ismerős felvétele")
        print("5. Kilépés")
        option = int(input())
        if option == 1:
            self.print_next_birthday()
        elif option == 2:
            self.print_all_friends()
        elif option == 3:
            self.search()
        elif option == 4:
            self.add_friend()

        return option

    def print_next_birthday(self):
        if len(self.friends) == 0:
            print("Nincs egy ismerős sem")
            return

        nearest = self.friends[0]
        for friend in self.friends:
            if friend.get_d_until_birthday() < nearest.get_d_until_birthday():
                nearest = friend

        nearest.print_friend()

    def print_all_friends(self):
        for friend in self.friends:
            friend.print_friend()
            print()

    def search(self):
        text = input("Keresett szöveg: ")

        found = []
        for friend in self.friends:
            if text in friend.name or text in friend.nick or text in friend.phone or text in friend.email or text in friend.address:
                found.append(friend)
        if len(found) == 0:
            print("Nincs találat")
            return
        for friend in found:
            print("1. ", end="")
            friend.print_friend()
            print()
        chosen = int(input("Válassz egyet: "))
        chosenFriend = found[chosen - 1]
        chosenFriend.print_friend()
        print("1. Módosítás")
        print("2. Törlés")
        print("3. Főmenü")
        option = int(input())
        if option == 1:
            self.modify_friend(chosenFriend)
        elif option == 2:
            self.delete_friend(chosenFriend)

    def modify_friend(self, friend):
        print("1. Név")
        print("2. Becenév")
        print("3. Születésnap (hh.nn)")
        print("4. Telefonszám")
        print("5. Email")
        print("6. Cím")
        option = int(input())
        modified = input("Módosított érték:")
        if option == 1:
            friend.name = modified
        elif option == 2:
            friend.nick = modified
        elif option == 3:
            friend.birthday = datetime.date(datetime.strptime(modified, "%m.%d"))
        elif option == 4:
            friend.phone = modified
        elif option == 5:
            friend.email = modified
        elif option == 6:
            friend.address = modified
        self.save_friends()


    def delete_friend(self, friend):
        self.friends.remove(friend)
        self.save_friends()

    def add_friend(self):
        name = input("Név: ")
        nick = input("Becenév: ")
        birthday = datetime.date(datetime.strptime(input("Születésnap (hh.nn): "), "%m.%d"))
        phone = input("Telefonszám: ")
        email = input("Email: ")
        address = input("Cím: ")
        self.friends.append(Friend(name, nick, birthday, phone, email, address))
        self.save_friends()

    def save_friends(self):
        with open("friends.txt", "w") as file:
            for friend in self.friends:
                file.write(friend.serialize() + "\n")


def main():
    prog = Program()
    prog.main()

main()
