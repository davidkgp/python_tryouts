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

print("almost there")
def almost_there(n):
    return (n<=110 and n>=90) or (n<=210 and n>=190)

print(almost_there(90)) #--> True
print(almost_there(104)) #--> True
print(almost_there(150)) #--> False
print(almost_there(209)) #--> True
print("almost there")

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

def paper_doll(str):
    list=[1,2,3]
    return "".join([x for x in str for y in list])

print(paper_doll("Hello"))
print(paper_doll('Mississippi'))

def sum1(a,b,c):
    return a+b+c

def blackjack(a,b,c):
    if sum1(a,b,c) <= 21:
        return sum1(a,b,c)
    elif sum1(a,b,c) > 21:
        if a==11 or b==11 or c==11:
            val=sum1(a,b,c)-10
            if val > 21:
                return "BUST"
            else:
                return val
        else:
            return "BUST"


print(blackjack(5,6,7)) #--> 18
print(blackjack(9,9,9)) #--> 'BUST'
print(blackjack(9,9,11)) #--> 19

def summer_69(arr):
    if 6 in arr and 9 in arr:
        return sum(arr[:arr.index(6):])+sum(arr[arr.index(9)+1::])
    else:
        return sum(arr)


print(summer_69([1, 3, 5])) #--> 9
print(summer_69([4, 5, 6, 7, 8, 9])) #--> 9
print(summer_69([2, 1, 6, 9, 11])) #--> 14
print(summer_69([])) #--> 0
print(summer_69([6,8,9])) #--> 0
print(summer_69([6,9])) #--> 0



def spy_game(nums):
    list007=[str(x) for x in nums if x==0 or x ==7]
    val="".join(list007)
    return val=="007"


print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False

