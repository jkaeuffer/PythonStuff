# from sys import argv

# (script,fileForSaving) = argv 

def initNewFile(filename):
	f = open (str(filename), 'w')
	columns = ["Original Word", "Original Language", "Translated Word", "Translated Language"]
	for n in columns:
		f.write(n)
		f.write("|")
	f.write("\n")
	f.close()

def createNewFile():
	decision = raw_input("Do you want to create a new file?")
	if decision == "Yes":
		fileToCreate = raw_input("Name your file")
		fileName = "%s.csv" % fileToCreate
		initNewFile(fileName)
	else:
		None

class Cards():
	def __init__(self, original_lang, translated_lang, original_word, translated_word):
		self.original_lang = original_lang
		self.translated_lang = translated_lang
		self.original_word = original_word
		self.translated_word = translated_word	

def newRow(filename,original_word, original_lang, translated_word, translated_lang):
	filename.write(original_word)
	filename.write("|")
	filename.write(original_lang)
	filename.write("|")
	filename.write(translated_word)
	filename.write("|")
	filename.write(translated_lang)
	filename.write("|")
	filename.close()

def userPrompt():
	original_word = raw_input("What word are you adding? \n > ")
	original_lang = raw_input("What language is that? \n > ")
	translated_word = raw_input("What is its translation? \n > ")
	translated_lang = raw_input("In which language? \n > ")
	return original_word, original_lang, translated_word, translated_lang

def addUserCards(userCards):
	fileToWorkOn = open("flashcards_data.csv", "a")
	fileToWorkOn.write("\n")
	newRow(fileToWorkOn,userCards.original_word, userCards.original_lang, userCards.translated_word, userCards.translated_lang)

def addRecord():
	additions = int(raw_input("How many new cards? \n > "))
	for n in range(additions):
		(original_word, original_lang, translated_word, translated_lang) = userPrompt()
		newRecord = Cards(original_lang, translated_lang, original_word, translated_word)
		fileToWorkOn = open("flashcards_data.csv", "a")
		fileToWorkOn.write("\n")
		newRow(fileToWorkOn,newRecord.original_word, newRecord.original_lang, newRecord.translated_word, newRecord.translated_lang)

addRecord()
# fileToWorkOn = open(fileForSaving, "a")
# newRow(newWordToAdd.original_word, newWordToAdd.original_lang, newWordToAdd.translated_word, newWordToAdd.translated_lang)

