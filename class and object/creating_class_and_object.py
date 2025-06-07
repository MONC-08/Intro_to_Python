class Patient():
    status = 'patient'
    total_patients = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

        Patient.total_patients += 1

    def get_details(self):
        print(f'{Patient.total_patients}. {self.name} is {self.age} years old.' \
              f' Current condition is : {self.conditions}')
           
    def add_info(self, information):
        self.conditions.append(information)

steve = Patient('Steven Smith', 52)
steve.add_info('patient treated to be ear infection.')
steve.get_details()

huge = Patient('Carlos Huge', 60)
huge.add_info('patient treated to be heart diseases.')
huge.get_details()