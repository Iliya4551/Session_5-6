name = input("What is your name? ")
print("hello", name)
age = input("How old are you? ")
try:
    age = int(age) #I'm just trying to convert it into a number
    print("you were probably born in", 2024-age)
 #   new_age = age / 0 (putting a hashtag js to cancel it out because we dont want it in the code)
except ValueError:
    print("You are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("you can't divide by zero")
except:
    print("something unexpected happened")
else: #this happens if no error occurs
    print("you were probably born in", 2024 - age)
finally:
    print("thanks for playing")
#finally happens no matter what, while else happens if there are no exceptions
