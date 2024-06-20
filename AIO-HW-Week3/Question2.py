class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob


class Student(Person):

    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe_method(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):

    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe_method(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):

    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe_method(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:

    def __init__(self, name):
        self.name = name
        self.people = []

    def add_people(self, person):
        self.people.append(person)

    def describe_method(self):
        print(f"Ward - Name: {self.name}")
        for person in self.people:
            person.describe_method()

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1

        print(f"The number of doctor in the ward is :{count}")

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)
        for person in self.people:
            person.describe_method()

    def calculate_average_yob(self):
        total_yob = 0
        count_yob = 0

        for person in self.people:
            if isinstance(person, Teacher):

                total_yob = total_yob + person.yob

                count_yob += 1

                avg_yob = total_yob / count_yob

        print(f"The average year of birth of Teacher is: {avg_yob} ")


student1 = Student('John', 2005, 12)
student2 = Student('Mike', 2006, 11)

teacher1 = Teacher('James', 1990, 'Mathematic')
teacher2 = Teacher('Ben', 1988, 'Data Science')


doctor1 = Doctor('Will', 1986, 'Endocrinologist')
doctor2 = Doctor('Max', 1983, 'Cardiologist')

ward = Ward('Ward1')
ward.add_people(student2)
ward.add_people(doctor1)
ward.add_people(teacher2)
ward.add_people(doctor2)
ward.add_people(student1)

ward.calculate_average_yob()
