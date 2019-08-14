#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def even(x):
    return x%2 ==0

def less(x,y):
    print(x)
    print(y)

    if x > y:
        return y
    else:
        return x

def lesser_of_two_evens(x,y):
    if even(x) and even(y):
        if x > y:
            return y
        else:
            return x
    else:
        if y > x:
            return y
        else:
            return x

print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(5,7))
print(lesser_of_two_evens(10,11))
print(lesser_of_two_evens(10,12))

#Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(str):
    first_set=set()
    for x in str.split():
        first_set.add(x[0].lower())

    if len(first_set) ==1 :
        return True
    else:
        return False



print(animal_crackers("hi there"))

print(animal_crackers("hi here"))
print(animal_crackers("hi Here"))

def makes_twenty(x,y):
    if (x==20 or y==20) or (x+y==20):
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

def old_macdonald(name):
    return name[:3:].capitalize()+name[3::].capitalize()


print(old_macdonald("Sango"))
print(old_macdonald("macdonald"))

def master_yoda(text):
    return " ".join(reversed([x for x in text.split()]))

print(master_yoda("Sango but"))
print(master_yoda("I am home"))


def almost_there(n):
    if (n<=110 and n>=90) or (n<=210 and n>=190):
        return True
    else:
        return False

print(almost_there(90)) #--> True
print(almost_there(104)) #--> True
print(almost_there(150)) #--> False
print(almost_there(209)) #--> True

def has_33(list):
    pivot=0
    for x in list:

        if pivot ==3 and x ==3:
            return True
        else:
            pivot=0
        pivot = x

    return False

print(has_33([1, 3, 3])) #→ True
print(has_33([1, 3, 1, 3])) #→ False
print(has_33([3, 1, 3])) #→ False
print(has_33([3, 1, 3,5,6,9,3,8,3])) #→ False



