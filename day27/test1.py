class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time


class Grade(object):
    def __init__(self, name, course):
        self.name = name
        self.course = course


course = Course('python', 20000, 12)

grade = Grade('三年二班', course)

print(grade.course.name)
print(grade.course.price)
