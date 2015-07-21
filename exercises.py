#Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 



def LetterChanges(str):
	exiDic = [n for n in 'abcdefghijklmnopqrstuvwxyz'] #creating a list with the alphabet
	vowels = [n for n in 'aeiouAEIOU'] #creating a list with vowels since they'll have to be uppercase
	newStrList = [] 
	for n in str:
		if n.lower() not in exiDic: #if it's not in the alphabet it means it's a number or punctuation and it should stay the same in the new string
			newStrList.append(n)
		else:
			exiDicIndex = exiDic.index(n.lower()) #putting to lower case because some letters may not be caught in exiDic otherwise
			if exiDicIndex == len(exiDic) - 1: #if the letter is Z or z then it needs to return A no matter what, hence the exception
				newStrList.append('A')
			elif exiDic[exiDicIndex+1] in vowels: #if the new letter is a vowel it needs to be uppercase
				newStrList.append(exiDic[exiDicIndex+1].upper())
			else:
				newStrList.append(exiDic[exiDicIndex+1])
	return ''.join(newStrList)

print LetterChanges("Argument Goes Here") 


#Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. 
#The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 

#Use the Parameter Testing feature in the box below to test your code with different arguments.

#we can use indexes to see if for all on both left and right there's a + sign, except for the 1st and last char.

def SimpleSymbols(str):
	strList = [n for n in str]
	strListLength = len(strList)
	responses = []
	if strList[0] != '+' or strList[strListLength-1] != "+":
		return "false"
	else:
		for n in strList:
			if n not in [letter for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']:
				responses.append(1)
			else:
				if strList[strList.index(n)-1] and strList[strList.index(n)+1] == "+":
					responses.append(1)
				else:
					responses.append(0)
	if 0 in responses:
		return "false"
	else:
		return "true"

print SimpleSymbols("+d+=3=+s+")


#Using the Python language, have the function CountingMinutesI(str) take the str parameter being 
#passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and 
#return the total number of minutes between the two times. 
#The time will be in a 12 hour clock format. 
#For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320. 

#Use the Parameter Testing feature in the box below to test your code with different arguments.

#tests: Input = "12:30pm-12:00am"Output = 690  | Input = "1:23am-1:08am"Output = 1425   Input is a string 


def CountingMinutesI(str):
	hoursList = str.split("-") # create a list with the two hours
	firstHour = [hoursList[0][0:len(hoursList[0])-2], hoursList[0][-2:]] #getting the hour numbers and whether it's am or pm
	secondHour = [hoursList[1][0:len(hoursList[1])-2], hoursList[1][-2:]] #getting the hour numbers and whether it's am or pm
	

print CountingMinutesI("9:00am-10:00am")