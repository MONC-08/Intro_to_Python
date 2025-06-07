class Patient():
    status = 'patient'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self):
        print(f'{self.name} is {self.age} years old.' \
              f' Current condition is : {self.conditions}')
           
    def add_info(self, information):
        self.conditions.append(information)

steve = Patient('Steven Smith', 52)
steve.add_info('patient treated to be ear infection.')
steve.get_details()