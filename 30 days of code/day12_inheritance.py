class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        if not scores:
            self.scores = []
        else:
            self.scores = scores


    def calculate(self):
        avg = sum(scores)/len(scores)
        if avg >= 90:
            return 'O'
        if avg >= 80:
            return 'E'
        if avg >= 70:
            return 'A'
        if avg >= 55:
            return 'P'
        if avg >= 40:
            return 'D'
        if avg < 40:
            return 'T'

line = input().split()
