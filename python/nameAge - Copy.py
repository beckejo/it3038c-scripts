import time
start_time = time.time()

print('What is your name?')
myName = input()
print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = str(int(input()))
programAge = str(int(time.time() - start_time))
print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))

