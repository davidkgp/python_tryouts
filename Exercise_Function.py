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
    for x in str.split():
        print(x)

animal_crackers("hi there")