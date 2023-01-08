from dataclasses import dataclass
@dataclass()
class User:
    name: str
    surname: str = 'Sher'
    email: str = 'email@mail.com'
    phone: str = '9991234567'
    b_day: str = '31 October 1995'
    birth_day: str = '31'
    birth_month: str = 'October'
    birth_year: str = '1995'
    gender: str = 'Female'
    subjects: str ='sport'
    hobbies: str ='reading'
    prof_picture: str = 'pic.jpg'
    state_and_city: str = 'NCR Delhi'


ana = User(name='Ana')