'''
Author:Ashley Muka
Assignment Title: Dean's List
Assignment Description: Implement class Course to return a list of students that made the dean's list
Due Date: 09/01/2023
Date Created:08/29/2023
Date Last Modified:08/31/2023
'''


class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa
        
    def get_gpa(self):
        return self.gpa
        
    def get_last(self):
        return self.last

    def to_string(self):
        return self.first + ' ' + self.last + ' (GPA: ' + str(self.gpa) + ')'


class Course:
    def __init__(self):
        self.roster = []
        
    def add_student(self, Student):
        self.roster.append(Student)
        
    def get_deans_list(self):
        deans_list = []
        for student in self.roster:
            if student.gpa >= 3.5:
                deans_list.append(student)
        return deans_list


if __name__ == "__main__":
    #Data abstraction
    
    course = Course()
    
    #input
    
    course.add_student(Student('Henry','Nguyen',3.5))
    course.add_student(Student('Brenda','Stern',2.0))
    course.add_student(Student('Lynda','Robinson',3.2))
    course.add_student(Student('Sonya','King',3.9))

    #process
    
    deansList = course.get_deans_list()

    #output

    print("Dean's list:")
    for student in deansList:
            print(student.to_string())


    
