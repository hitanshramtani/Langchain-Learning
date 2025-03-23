from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int
    email: str
new_Person: Person = {'name':"Hitansh", 'age': "20", 'email':""}
print(new_Person)