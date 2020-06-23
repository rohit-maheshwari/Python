size = 0

while True:
    try:
        size = int(input("Please enter the number of characters to move to the end (1 - 3): "))
        if (size >= 1) and (size <= 3):
            break
        else:
            print("Try again")
    except:
        print ("Try Again")
            

sentence = input("Please enter a word, phrase or sentence: ")

words = str.split(sentence)

piglatin = ""

for word in words:               
    word = word.lower()
    firstChar = word[0]
    if firstChar in "aeiou":
        word = word + "\way"
    else:
        firstPart = word[0:size]
        lastPart = word[size:len(word) + 1]
        word = lastPart + "\\"
        word = word + firstPart + "ay"
    piglatin = piglatin + word + " "

print (sentence)
print (piglatin)

