primes = [2, 3, 5, 7]
print("For loop demo")
for prime in primes:
    print(prime)

for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7 (it means print from 3 to 8 with step of 2)
for x in range(3, 8, 2):
    print(x)

print("While loop demo")

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


print("While and for loop with else demo")

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4 so break would ignore else block as well
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


my_tuple_list=[(1,2,3),(4,5,6),(7,8,9)]
for tuple in my_tuple_list:
    print(tuple)

#tuple unpacking
for (a,b,c) in my_tuple_list:
    print(a)
    print(b)

#tuple handling for loops
simeple_tuple=(100,2,3,4,5,6,7,8)
for x in simeple_tuple:
    print(x)

#tuple handling for loops slice objects (which are created implicitly when you do a[:]) take 3 arguments -- start,stop,stride
print("every 2nd element")
for x in simeple_tuple[::2]:
    print(x)

#in dictionary
dict_my={"some1":2,"other2":3,"other4":4,"other5":5,"other6":6}

# default iteration over keys
for x in dict_my:
    print(x)

#iteration over values

for x in dict_my.values():
    print(x)
# iteration over items (key value pair)
for x in dict_my.items():
    print(x)
