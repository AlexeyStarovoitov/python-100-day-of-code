import datetime

class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.age()
        
    
    def age(self):
        today = datetime.date.today()
        if hasattr(self, "_date") is False:
            self._date = today
        
        if today.day == self._date.day:
            return
            
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        
        self._age = age
        self._date = today
        
        return age
    
    def list_attr(self):
        print(f'Listing {type(self)} attributes')
        for key,val in self.__dict__.items():
            print(f'{key} --> {val}')
    

class Person2():
    
    TITLES = ('Mr', 'Mrs', 'Ms')
    name = 'Alexandr'
    pets = []
    
    def __init__(self, title, name, surname):
        
        if title not in self.TITLES:
            raise ValueError(f"{title} is not a title")
        
        self.title = title
        self.name = name
        self.surname = surname
    
    @classmethod
    def cls_person_init(cls, person_params):
        return cls(*person_params)
        
    def add_pet(self, pet):
        self.pets.append(pet)
    
    @staticmethod
    def print_titles_ending_with(endwith):
        return [t for t in Person2.TITLES if t.endswith(endwith)]
    
    
#Exercise 3
class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession
    
#Exercise 4:

class Numbers:
    MULTIPLIER = 2
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y 
    
    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER*a
        
    @staticmethod
    def subtract(b,c):
        return b - c
    
    @property
    def value(self):
        return (self.x, self.y)
    
    @value.setter
    def value(self, xy):
        self.x,self.y = xy
    
    @value.deleter
    def value(self):
        del self.x
        del self.y

#Overloading

class Person_overload():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname
    
    def __gt__(self, other):
        
        if self.surname == other.surname:
            return self.name > other.name
        
        return self.surname > other.surname

    def __ne__(self, other):
        return not (self == other)
     
    def __le__(self,other):
        return not (self > other)
    
    def __lt__(self, other):
        return not (self > other or self == other)
        
    def __ge__(self, other):
        return not (self < other)
        
#Exercise 6

class Generic_Class:
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        s = ""
        for key, val in self.__dict__.items():
            s += f'{key} --> {str(val)}\n'
        
        return s
        
        

if __name__ == '__main__':
    alex = Person(
    'Alexey','Starovoitov', 
    datetime.date(1996, 10, 9), 
    'Moscow Area, Lesnoy Gorodok, Fasadnya St, 2, 325', 
    '111111112222333', 
    'starovoitov@example.com'
    )
    '''
        Exercise 1:
        
        Person - class name, global scope,
        person - inctanse of the Person class, global scope
        surname - __init__ parameter, local scope
        self - general instance of Person class used in functions, local scope
        age - method of the Person class, enclosing scope
        age - parameter in age function, local scope
        self.email - attribute of general instance, enclosing scope
        person.email - attribute of a concrete instance, enclosing scope
    '''
    print(f"Name: {alex.name}\nSurname: {alex.surname}\nAge: {alex.age()}")
    
    #Exercise 2
    print('\nExperimenting with set/get/has attribute')
    print('\nGetattr:')
    print(f'Name: {getattr(alex, "name", None)},\nSurname: {getattr(alex, "surname")}\nAge: {getattr(alex, "_age", None)}')
   
    print('\nSetattr:')
    print('Setting new name/surname:')
    setattr(alex, 'name', 'Alex')
    setattr(alex, 'surname', 'Oldvoight')
    print(f'Name: {getattr(alex, "name", None)}\nSurname: {getattr(alex, "surname", None)}')
    
    print('\nHasattr:')
    print(f'Does the person instance have mail attr?:\n{hasattr(alex, "mail")}')
    print(f'Does the person instance have email attr?:\n{hasattr(alex, "email")}')
    
    print('\nExperimenting with class attributes:')
    alex2 = Person2('Mr', 'Alexey', 'Starovoitov')
    print(f'alex2.TITLES: {getattr(alex2,"TITLES")}')
    print(f'Person2.TITLES: {getattr(Person2,"TITLES")}')
    
    print('\nInstantaneous attributes vs class attributes:')
    print(f'alex2.name: {getattr(alex2, "name")}')
    print(f'Person2.name: {getattr(Person2, "name")}')
    
    
    print('\nShowing danger of sharing mutable object:')
    lera2 = Person2('Ms', 'Lera', 'Olenich')
    
    print('\nAdding pet to alex2 instance:')
    alex2.add_pet('french bulldog')
    print(f'alex2.pets: {alex2.pets}')
    print(f'lera2.pets: {lera2.pets}')
    
    print('\nExercise 3:')
    smith = Smith('alex', 'IT-specialist')
    
    print(f'smith.profession: {smith.profession}')
    print(f'Smith.profession: {Smith.profession}')
    print(f'smith.surname: {smith.surname}')
    
    print('\nExperimenting with class methods:')
    print("Creating Person2 object via class method")
    alex22 = Person2.cls_person_init(('Mr', 'Alex', 'Oldvoight'))
    print(f'alex22.name: {getattr(alex22, "name")}\nalex22.surname: {getattr(alex22, "surname")}')
    
    print('\nExperimenting with static methods:\n')
    endwith = 's'
    print(f'Printing allowed index ending with {endwith}: {Person2.print_titles_ending_with(endwith)}')
    
    print('\n Exercise 4:')
    number = Numbers(1,2)
    print(f"{number.x} + {number.y} is {number.add()}")
    print(f'Numbers.multiply(3) is {Numbers.multiply(3)}')
    b = 5.1
    c = 3.2
    print(f'{b} - {c} is {Numbers.subtract(b,c)}')
    print(f'number.value is {number.value}')
    number.value = (6,7)
    print(f'number.value after set is {number.value}')
    print('Deleting number.value')
    del number.value
    print('\nHasattr:')
    print(f'Does the number instance have x attr?:\n{hasattr(number, "x")}')
    print(f'Does the number instance have y attr?:\n{hasattr(number, "y")}')
    
    print('\nExercise 5')
    print(f'dir(alex):\n{dir(alex)}')
    print(f'type(alex): {type(alex)}')
    print(f'type(Person): {type(Person)}')
    alex.list_attr()
    
    print('\nExercise 6')
    gen_obj = Generic_Class(name = 'ha', surname = 'haha', birthdate = datetime.date(year = 1996, month = 10, day = 9))
    print(str(gen_obj))
        
        