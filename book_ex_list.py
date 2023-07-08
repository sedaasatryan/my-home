# Exercise 110: Sorted Order
# mylist = []
# while True:
#     n = int(input("Enter a number: "))
#     if n != 0:
#         mylist.append(n)
#     else:
#         mylist.sort()
#         print(mylist)
#         break
 
# Exercise 111: Reverse Order
# mylist = []
# while True:
#     n = int(input("Enter an integer: "))
#     if n == 0:
#         for i in mylist[::-1]:
#             print(i)
#         break
#     else:
#         mylist.append(n)

# Exercise 112: Remove Outliers
# mylist = []
# while True:
#     n = int(input("Enter 10 numbers: "))
#     mylist.append(n)
#     if len(mylist) == 10:
#         mylist.sort()
#         print(f'''Smallest values {mylist[0]}, {mylist[1]}
# Largest values {mylist[-1]}, {mylist[-2]}''')

#Exercise 113: Avoiding Duplicates
# words = []
# while True:
#     word = input("Enter a word: ")
#     if word != "":
#         if word not in words:
#             words.append(word)
#     else:
#         print(words)
#         break

# Exercise 114: Negatives, Zeros and Positives
# mylist = []
# while True:
#     n = input("Enter an integer: ")
#     if n != "":
#         mylist.append(int(n))
#     else:
#         break
# for i in mylist.copy():
#     if i < 0: 
#         print(i)
#         mylist.remove(i)
# for i in mylist.copy():
#     if i == 0:
#         print(i)
#         mylist.remove(i)
# for i in mylist:
#     print(i)

# Exercise 115: List of Proper Divisors
# mylist = []
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         mylist.append(i)
# print(mylist)

# Exercise 116: Perfect Numbers
# for n in range(1, 10000):
#     summ = 0
#     for i in range(1, n//2 +1):
#         if n % i == 0:
#             summ += i
#     if summ == n:
#         print(n)

# Exercise 117: Only the Words
# text = "Contractions include: don't, isn't, and! wouldn't."
# mylist = text.split(" ")
# new_list = []
# for i in mylist:
#     if i[-1].isdigit() or i[-1] == "'":
#         new_list.append(i)
#         continue
#     elif i[-1].isalpha():
#         new_list.append(i)
#         continue
#     else:
#         list_i = list(i)
#         list_i.pop()
#         list_i = ''.join(list_i)
#         new_list.append(list_i)
# print(new_list)

# Exercise 118:Word by Word Palindromes
# char = "!@#$%^&*()_+.;,"
# text = "Herb the sage eats sage, the herb"
# count = 0
# text = text.lower()
# for i in text:
#     if i in char:
#         text = text.replace(i, "")
# mylist = text.split(" ")
# for i in range(len(mylist)//2):
#     if mylist[i]== mylist[len(mylist)-1-i]:
#         count += 1
#     if count == len(mylist)//2:
#         print("Word by Word Palindromes")


# Exercise 119: Below and Above Average
# mylist = []
# below = []
# above = []
# averagelist = []
# summ = 0
# while True:
#     n = input("Enter a number: ")
#     if n != "":
#         mylist.append(int(n))
#     else:
#         for i in mylist:
#             summ += i
#             average = summ/len(mylist)    
#         print(f"Average = {average}")
#         break
# for j in mylist:
#     if j < average:
#         below.append(j)
#     elif j > average:
#         above.append(j)
#     else:
#         averagelist.append(j)    
# print(f'''Below values-> {below},
# Average values -> {averagelist},
# Above values -> {above}
# ''')

# Exercise 120: Formatting a List
# text = input("Enter the text: ")
# mylist = text.split(" ")
# if len(mylist) == 1:
#     print(text)
# elif len(mylist) == 2:
#     mylist.insert(1, " and ")
# elif len(mylist) == 3:
#     mylist.insert(1, ", ")
#     mylist.insert(3, " and ")
# elif len(mylist) == 4:
#     mylist.insert(1, ", ")
#     mylist.insert(3, ", ")
#     mylist.insert(5, " and ")
# txt = "".join(mylist)
# print(txt)

# Exercise 121: Random Lottery Numbers
# import random
# mylist = []
# while len(mylist) < 6:
#     num = random.randint(1,49)
#     if num not in mylist:
#         mylist.append(num)
# mylist.sort()
# print(mylist)

# Exercise 122: Pig Latin
# text = "computer think office"
# mylist = text.split(' ')
# new_list = []
# vowel = 'aeiou'
# print(mylist)
# for j in mylist:
#     index_start = 0
#     s = ''
#     for i in j:
#         if j[0] not in vowel:
#             if i not in vowel:
#                 s += i
#                 index_start += 1
#             else:
#                 new_text = j[index_start::] + s + "ay"
#                 new_list.append(new_text)
#                 break
#         else:
#             new_text = j + 'way'
#             new_list.append(new_text)
#             break
# print(new_list)        

# Exercise 127: Is a List already in Sorted Order?
# mylist = [6, -2, 0, 1, 2, 3, 5]
# newlist = mylist.copy()
# newlist.sort()
# if mylist == newlist:
#     print(True)
# else:
#     print(False)
