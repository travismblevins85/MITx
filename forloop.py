letters = "aefhilmnorsxAEFHILMORSX"

word = input("I will cheer for you!  Enter a word: ")

times = int(input("Enthusiam level is a 1-10?: "))

i = 0
while i < len(word):
    char = word[i]
    if char in letters:
        print('Give me a ' + char + '!' + char)
  
    
print("What does that spell?")            
for i in range(times):
    print(word, '!!!!')