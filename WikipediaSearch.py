import wikipedia


print("WikipediaSearch provides a short summary to Questions (English)")
wikipedia.set_lang("en") 

while 1:
    print(wikipedia.summary(input("Enter Question:\n"), sentences=5)) #Modify sentences attribute according to size of answer
    
