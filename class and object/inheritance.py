class Student(object):
    total_students = 0
    
    def __init__(self, name, age, major, gpa, year):
      self.name = name
      self.age = age
      self.major = major
      self.gpa = gpa
      self.year = year
      
      Student.total_students += 1
        
    def get_details(self):
      print(f'''Name: {self.name}
Age: {self.age}
Major: {self.major}
GPA: {self.gpa}
Year: {self.year}

Total number of students in class: {self.total_students}''')
      
    def update_age(self):
      self.age += 1
      
    def update_major(self, new_major):
      self.major = new_major

class HonorsStudent(Student):
    def __init__(self, name, age, major, gpa, year, honors_program):
        super().__init__(name, age, major, gpa, year)
        self.honors_program = honors_program

    def get_details(self):
      print(f'''Name: {self.name}
Age: {self.age}
Major: {self.major}
GPA: {self.gpa}
Year: {self.year}
Honors Program: {self.honors_program}

Total number of students in class: {self.total_students}''')
      
# Create an instance of the HonorsStudent class
honor_student = HonorsStudent(
  name="David Kim", 
  age=20, 
  major="Computer Science", 
  gpa=3.9, 
  year="Junior", 
  honors_program="STEM Honors"
)

honor_student.update_age()
honor_student.get_details()