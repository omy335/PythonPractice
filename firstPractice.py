# Python Practice 

# Employee Class
class Employee(object):
	__firstName = ''
	__lastName = ''
	__id = ''
	__payRate = ''

	def __init__(self, fname, lname, idNum):
		self.__firstName = fname
		self.__lastName = lname
		self.__id = idNum
		self.__payRate = 10.50

	def setPayRate(self, newPayRate):
		self.__payRate = newPayRate

	def getPayRate(self):
		return self.__payRate

	def getID(self):
		return self.__id

	def toString(self):
		return 'Name: {} {} | ID: {} | Pay Rate: {}\n'.format(self.__firstName, self.__lastName, self.__id, self.__payRate)

# Creating a place to store all employees with its own functions.
class EmployeeList(Employee, object):
	__employeeList = []
	__tempEmployee = ''

	def __init__(self):
		__employeeList = []
		super(Employee, self).__init__()

	def addEmployee(self, employee):
		self.__employeeList.append(employee)
		print('Employee was added.')

	# Removing employee whose id matches from list.
	def removeEmployee(self, idNum):
		for employee in self.__employeeList:
			if employee.getID() == idNum:
				self.__employeeList.remove(employee)
				print('Employee Removed.')
				break
			else:
				print('Employee Not Found.')

	# Formatting the output of the entire list.
	def toString(self):
		listInfo = '\nNumber of Employees: {} |\n'.format(len(self.__employeeList))
		for employee in self.__employeeList:
			listInfo += employee.toString()

		return listInfo

	# Writing entire Employee List into a file.
	def writeToFile(self, filename):
		with open(filename, 'w') as f:
			f.write(self.toString())


# Example of Employee Class
e1 = Employee('John', 'Doe', 123321)
e2 = Employee('Mark', 'Doe', 123123)
e3 = Employee('Jill', 'Smith', 112233)

print(e1.toString())

e1.setPayRate(13)

print(e1.toString())

eList = EmployeeList()

eList.addEmployee(e1)
eList.addEmployee(e2)
eList.addEmployee(e3)

print(eList.toString())

eList.removeEmployee(e1.getID())

print(eList.toString())

eList.writeToFile('eList.txt')





