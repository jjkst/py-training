class Person:
    greet = 'Hello and welcome'
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def greeting(self):
        print(f'{Person.greet} {self.firstname}, {self.lastname}')

class Employer(Person):
    def __init__(self, firstname, lastname, id):
        super().__init__(firstname, lastname)
        self.id = id
    
    def employergreeting(self):
        print(f'Employer ID for {self.firstname}, {self.lastname} is {self.id}')

employer = Employer('Team', 'Member', 1)
employer.greeting()
employer.employergreeting()
