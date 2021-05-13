intro=input("your introduction:")
print(intro)
characterCount=0
wordCount=1
for i in intro:
    characterCount=characterCount+1

    if(i==' '):
        wordCount=wordCount+1
print("number of characters in intro are:")
print(characterCount)
print("number of words in intro are:")
print(wordCount)