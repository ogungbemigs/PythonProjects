wordlist = [] #empty list to hold words input
reversedWords = []#empty list to hold reversed words

number_of_words = int(input("number of words to be reversed: ")) #number of input the program can take

for i in range(0, number_of_words): #iteratint through the number of inputs
    words = input ("Enter the words: ") #where words are inputted
    
    wordlist.append(words)
    
    backward_text = ''.join(reversed(words))
    reversedWords.append(backward_text)
    

set(wordlist) & set(reversedWords)
usingset = set(wordlist).intersection(set(reversedWords))
print ("The Palindrome found is {} ".format(usingset))
print (wordlist)
print (reversedWords)