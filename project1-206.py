import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	# get a list of dictionary objects from the file
	#Input: file name
	#Ouput: return a list of dictionary objects where
	#the keys are from the first row in the data. and the values are each of the other rows
	inFile = open(file, "r")
	singleLine = inFile.readline()
	firstLine = singleLine.split(",")
	listOfObjects = []

	# for each line, assign each key to a value
	lines = inFile.readlines()
	inFile.close()
	for line in lines:
		d = {}
		# create all keys for dictionary
		for i in range(len(firstLine)):
			firstLine[i] = firstLine[i].replace("\n","")
			d[firstLine[i]] = ""

		values = line.split(",")

		for i in range(len(values)):
			value = str(values[i])
			value = value.replace("\n","")
			d[firstLine[i]] = value

		# add dictionary to list
		listOfObjects.append(d)

	return listOfObjects


def mySort(data,col):
	# Sort based on key/column
	#Input: list of dictionaries and col (key) to sort on
	#Output: Return the first item in the sorted list as a string of just: firstName lastName
	firstValue = data[0][col]
	dictOfFirstValue = data[0]
	# loop through each data set and keep track of lowest alphabetically ranked col and what dict it belongs to
	for i in range(len(data)):
		if firstValue > data[i][col]:
			firstValue = data[i][col]
			dictOfFirstValue = data[i]

	return dictOfFirstValue["First"] + " " + dictOfFirstValue["Last"]


def classSizes(data):
	# Create a histogram
	# Input: list of dictionaries
	# Output: Return a list of tuples sorted by the number of students in that class in
	# descending order
	# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	t = ["", "", "", "" ]
	freshmanCount = 0
	sophomoreCount = 0
	juniorCount = 0
	seniorCount = 0

	# counts how many people each class has 
	for i in range(len(data)):
		if data[i]["Class"] == "Freshman":
			freshmanCount += 1
		elif data[i]["Class"] == "Sophomore":
			sophomoreCount += 1
		elif data[i]["Class"] == "Junior":
			juniorCount += 1
		else:
			seniorCount += 1

	# adds each grade's count as a tuple to the list
	t[0] = ("Freshman", freshmanCount)
	t[1] = ("Sophomore", sophomoreCount)
	t[2] = ("Junior", juniorCount)	
	t[3] = ("Senior", seniorCount)

	# sorts the tuples by the highest to lowest grade count
	t.sort(key=lambda tup: tup[1], reverse = True)
	                                                       
	return t


def findMonth(a):
	# Find the most common birth month form this data
	# Input: list of dictionaries
	# Output: Return the month (1-12) that had the most births in the data

	# variables to keep track of amount of times each month is included in data
	janCount = 0
	febCount = 0
	marCount = 0
	aprCount = 0
	mayCount = 0
	junCount = 0
	julCount = 0
	augCount = 0
	septCount = 0
	octCount = 0
	novCount = 0
	decCount = 0

	# for each month, counts how many people were born in it
	for i in range(len(a)):
		dob = a[i]["DOB"].split("/")
		month = dob[0]

		if month == "1":
			janCount += 1
		elif month == "2":
			febCount += 1
		elif month == "3":
			marCount += 1
		elif month == "4":
			aprCount += 1
		elif month == "5":
			mayCount += 1
		elif month == "6":
			junCount += 1
		elif month == "7":
			julCount += 1
		elif month == "8":
			augCount += 1
		elif month == "9":
			septCount += 1	
		elif month == "10":
			octCount += 1
		elif month == "11":
			novCount += 1
		else:
			decCount += 1

	t = ["", "", "", "", "", "", "", "", "", "", "", ""]

	# adds each month's count as a tuple to the list
	t[0] = (1, janCount)
	t[1] = (2, febCount)
	t[2] = (3, marCount)
	t[3] = (4, aprCount)
	t[4] = (5, mayCount)
	t[5] = (6, junCount)
	t[6] = (7, julCount)
	t[7] = (8, augCount)
	t[8] = (9, septCount)
	t[9] = (10, octCount)
	t[10] = (11, novCount)
	t[11] = (12, decCount)

	# sorts the tuples by the highest to lowest month count 
	t.sort(key=lambda tup: tup[1], reverse = True)

	return t[0][0]


def mySortPrint(a,col,fileName):
	#Similar to mySort, but instead of returning single
	#Student, the sorted data is saved to a csv file.
	# as fist,last,email
	#Input: list of dictionaries, col (key) to sort by and output file name
	#Output: No return value, but the file is written

	file = open(fileName, "w")

	# loops through data until all dictionaries have been sorted alphabetically by col
	while len(a) > 0:
		dictToDelete = 0
		firstValue = a[0][col]
		dictOfFirstValue = a[0]
		# repeatedly loop through data and keep track of lowest alphabetically ranked col and what dict it belongs to
		for i in range(len(a)):
			if firstValue > a[i][col]:
				firstValue = a[i][col]
				dictOfFirstValue = a[i]
				dictToDelete = i
		
		# write the dictionary with the lowest alphabetically ranked col to the file
		file.write(dictOfFirstValue["First"] + "," + dictOfFirstValue["Last"]+ "," + dictOfFirstValue["Email"] + "\n")

		# del the dictionary you've already written to the file
		del a[dictToDelete]

	file.close()
		

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
