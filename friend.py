from datetime import datetime


class Friend:
    def __init__(self):
        self.name = ""
        self.nick = ""
        self.birthday = datetime.date(datetime.now())
        self.phone = ""
        self.email = ""
        self.address = ""

    def __init__(self, name, nick, birthday, phone, email, address):
        self.name = name
        self.nick = nick
        self.birthday = birthday
        self.phone = phone
        self.email = email
        self.address = address

    def get_d_until_birthday(self):
        today = datetime.now()
        birthday = datetime(today.year, self.birthday.month, self.birthday.day)
        if birthday < today:
            birthday = datetime(today.year + 1, self.birthday.month, self.birthday.day)
        return (birthday - today).days

    def get_d_of_week_birthday(self):
        days = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
        return days[int(self.birthday.strftime("%u")) - 1]


    def print_friend(self):
        print(f"{self.name} ({self.nick})")
        print(f"{self.birthday.strftime('%m.%d')} {self.get_d_of_week_birthday()} {self.get_d_until_birthday()} nap múlva")
        print(f"{self.phone} {self.email}")
        if self.address != "":
            print(f"{self.address}")


    def serialize(self):
        return f"{self.name};{self.nick};{self.birthday};{self.phone};{self.email};{self.address}"

    @staticmethod
    def deserialize(string):
        data = string.split(";")
        return Friend(data[0], data[1], datetime.date(datetime.strptime(data[2], "%Y-%m-%d")), data[3], data[4], data[5])