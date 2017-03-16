import sys



def avgCalcUI():
	"""
	Simple mean/avg calculator implementation -- 
	takes in User-Input via command prompt then 
	computes and displays average
	"""

### Local Vars
	array = []
	numerator = 0
	denominator = 0
	avg = 0

	try:
		
		print("\n----- Welcome! ------")
		user_input = input("Please input a number: ")
	except ValueError:
		print("Error: Input must be of type 'int'")
	else:
		while user_input != "end":
			array.append(user_input)
			user_input = input("Please input a number -- input 'end' to stop: ")
			
		for i in range(len(array)):
			numerator += int(array[i])

		denominator = len(array)

		# for i in range(len(array)):
		# 	print(array[i])
		# 	print(type(array[i]))
		# 	if type(array[i]) not in [int]:
		# 		array.pop()

		avg = numerator/denominator

		return "\nComputing average of your inputs...\n\n\nYour average is: " + str(avg)




def maxValInArray(l):
	"""
	Return max value in list
	"""
	temp = l[0]
	for i in range(len(l)-1):
		if l[i] > temp:
			temp = l[i]

	maxVal = temp
	return maxVal



def findElementInArray(l,n):
	"""
	Find element in array 
	first implementation is python-specific, 
	second (in comments) is general
	"""
	if n in l:
		return True
	return False
	# boolVar = False
	# for i in range(len(l)-1):
	# 	if n == l[i]:
	# 		boolVar = True
	# return boolVar



def binarySearchForElement(l,n):	
	"""
	Binary Search for an element in sorted array, return position of element
	"""
	low = 0
	high = len(l)-1
	while low <= high:
		mid = int((low+high)/2)
		if n < l[mid]:
			high = mid-1
		elif n > l[mid]:
			low = mid+1
		else:
			return mid
	return "Element not in array"





def inputIntoHashMap(n):
	"""
	Input elements in array arg as key elements in a dict (hashmap)
	"""
	d = {}
	position = 0
	#d[n] = "hello world"
	for i in n:
		d[i] = position
		position += 1
	return d


def checkStringHasOnlyUniqueChars(word):
	"""
	Basically, make sure there are no diplicates; 
	Return true if there are duplicate(s); else false
	"""
	return len(word) != len(set(word)) #set removes duplicates;

###iterative version
	# seen = set()
	# for x in word:
	# 	if x in seen: return True
	# 	seen.add(x)
	# return False


def duplicatesInString(word):
	"""
	Return duplicates in a string argument as a list
	"""
	s = set()
	duplicates = [x for x in word if x in s or s.add(x)]
	return duplicates



def reverseString(word):
	"""
	Reverse a string, return result as a string
	"""
	result = ""
	j = -1
	for i in range(len(word)):
		result += (word[j-i])
	return result



def removeDuplicates(word):
	"""
	Remove duplicates in string arg, return answer as string
	"""
	ans = ""
	for i in word:
		if i not in duplicatesInString(word):
			ans += i
	return ans



def verifyAnagram(word1, word2):
	"""
	Anagram is how 'iceman' and 'cinema' use same letters but in different combination
	This function verifies if two word arguments are an anagram of eachother 
	"""
	for i in word1:
		for j in word2:
			if i in set(word2) and j in set(word1) and (len(set(word1)) == len(set(word2))):
				return True
	return False 


def placeCharInSpaces(words):
	"""
	Place '%20' in empty spaces of string arg; return modified string
	"""
	ans = ""
	for i in words:
		if i == " ":
			i = "%20"
		ans += i
	return ans


def allPermsOfString(string, step = 0):
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        allPermsOfString(string_copy, step + 1)


def sortArrayRecur(arg):
	
	if len(arg) == 0:
		return arg 
	pivot = arg[0]
	smaller = ([i for i in arg[1:] if i<pivot])
	larger = ([i for i in arg[1:] if i>=pivot])
	return sortArrayRecur(smaller) + [pivot] + sortArrayRecur(larger)


if __name__ == '__main__':

	#print(avgCalcUI())

	#lst = [1,2,3,7,4,5,6]
	#print(maxValInArray(lst))

	#lst = [1,2,3,7,4,5,6]
	#print(findElementInArray(lst,4))


	#lst = [1,2,3,4,5,6,7]
	#print(binarySearchForElement(lst,3))

	#lst = [1,2,3,4,5,6,7]
	#print(inputIntoHashMap(lst))

	#arg = "helol"
	#print(checkStringHasOnlyUniqueChars(arg))

	#arg = "test"
	#print(duplicatesInString(arg))

	#arg = "test"
	#print(reverseString(arg))

	#arg = "test"
	#print(removeDuplicates(arg))

	#arg1 = "testx"
	#arg2 = "etstt"
	#print(verifyAnagram(arg1, arg2))

	#arg = "collection of words"
	#print(placeCharInSpaces(arg))

	#arg = "abcde"
	#print(allPermsOfString(arg))

	#arg = [1,3,2,5,6]
	#print(sortArrayRecur(arg))
