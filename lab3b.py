import random
import string
def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
print("Random String with the combination of lowercase and uppercase letters")
n=int(input("enter the number of words in password"))
print (randomString(n) )
#print ("second Random String is ", randomString(8) )
