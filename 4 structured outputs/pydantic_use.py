from pydantic import BaseModel,EmailStr, Field

from typing import Optional

class Student(BaseModel):
    name: str = "Hitansh"
    age: Optional[int] = None
    gpa: float = Field(gt=0,lt=10,description="The gpa/cgpa of the student")
    email: EmailStr

new_student = { "age":20, "gpa":9.9,"email":"abc@yahoo.com"}

student = Student(**new_student)
print(student)