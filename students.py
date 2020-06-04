#!/usr/bin/env python3
n = int(input('Enter the number of students: '))
data = {}
Subjects = ('Pythsics', 'Math', 'History')
for i in range(0, n):
	name = input('Enter the name of student {}: '.format(i+1))
	marks = []
	for x in Subjects:
		marks.append(int(input('Enter the marks of {}: '.format(x))))
	data[name] = marks
for x, y in data.items():
	total = sum(y)
	print('{} total marks {}'.format(x, total))
	if total < 120:
		print(x, "failed :(.")
	else:
		print(x, "passed :).")
