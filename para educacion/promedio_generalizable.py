name = input('Hi, please type your name: ')
grades = int(input('how many grades will you have for this semester?: '))


class Student:
	amountGrades = grades
	Grades = {}

	while amountGrades != 0:
		Grades["Grade " + str(amountGrades)] = \
			int(input("Please, Type here the grade " + str(amountGrades) + ": "))
		amountGrades = amountGrades - 1


alumn = Student()
		
		
class average:
	lst = [*alumn.Grades.values()]
	lst = sum(lst)
	lst = lst / grades
	if lst >= 3:
		print('Congratz! dear ' + name + ' you are promoted!')
	else:
		print('oh no, its not enough to pass, try again.')
	

final = average()
print('Your score is ' + str(final.lst))
