#method that checks if the sentence can be parsed
def isValid(sentence):
    words = sentence.split()
    for word in words:
        if word.isalpha() == False:
            return False
        else:
            return True


#Asks user for input
sentence = input("Please enter a sentence: ")

#run validation method
while (isValid(sentence) == False):
    sentence = input("Please enter a valid sentence: ")
words = sentence.split()


#set first letter to lower
words[0] = words[0].lower()

#converts the words in the rest of the sentence to camelcase
index = 1
for word in words[1:len(words)]:
    lowerLetters = word[1:len(word)].lower()
    firstLetter = word[0].upper()
    newWord = firstLetter + lowerLetters
    words[index]=  newWord
    index += 1

#stings all the words together and prints correct format
sentence = ""
for word in words:
    sentence = sentence + word

print(sentence)