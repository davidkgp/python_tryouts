#Use for, .split(), and if to create a Statement that will print out words that start with 's':
str='Print only the words that start with s in this sentence'

for word in str.split():
    if word.startswith('s'):
        print(word)


#Use range() to print all the even numbers from 0 to 10.
for num in range(0,10):
    if num%2==0:
        print(num)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
listDivisibleBy3=[x for x in range(1,50) if x%3 == 0]
print(listDivisibleBy3)

#Go through the string below and if the length of a word is even print "even!"
strBelow='Print every word in this sentence that has an even number of letters'
for word in str.split():
    if len(word)%2 == 0:
        print(word)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for item in range(1,100):
    if item%3==0 and item%5==0:
        print("FizzBuzz")
    elif item%5==0:
        print("Buzz")
    elif item%3==0:
        print("Fizz")
    else:
        print(item)

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

stForm=[item[:1] for item in st.split()]
print(stForm)
