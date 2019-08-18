
mySquare=lambda x:x**2

list1=[1,2,3,4,5,6,7]

squareList = [x for x in map(mySquare,list1)]
newSquareList = list(map(mySquare,list1))
print(squareList)
print(newSquareList)

listNames=["Sharon","Lee","carter"]
print(list(map(lambda x:x[::-1],listNames)))