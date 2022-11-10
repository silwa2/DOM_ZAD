spinWords = "This is another test" 
x = spinWords.split(' ')

def spin_words(spinWords):
    for i in x:
        if len(i) > 5:
            i = i[::-1]
        print (i, end = " ")
    return spinWords

spin_words(spinWords)

