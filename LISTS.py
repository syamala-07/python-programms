#print all numbers in list
numbers=[1,2,3,4,5,6,7,8,9]
print(numbers)

#print elements  one by one
numbers=[1,2,3,4,5,6,7,8,9]
print(numbers)
for i  in numbers:
    print(i)


#printing even numbers from list
numbers=[1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num%2==0:
        print(num)


#printing odd numbers from list
numbers=[1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num%2!=0:
        print(num)