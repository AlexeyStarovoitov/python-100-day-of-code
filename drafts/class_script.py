import datetime

class Person:
    def __init__(self, \
                 name, surname, age, birthdate, \
                 address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
    
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdata.year
        
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        
        return age


if __name__ == '__main__':
    person = Person(
            'Alexey',
            'Starovoitov',
             datetime.date(1996, 10, 9)),
             'Moscow Area, Lesnoy Gorodok, Fasadnya St, 2, 325',
             "111111112222333",
             "starovoitov@example.com"
             )
             
    print(f"Name: {person.name}\nSurname: {person.surname}\nAge: {self.age()}")
        
        
        