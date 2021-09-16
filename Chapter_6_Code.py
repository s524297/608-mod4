#!/usr/bin/env python
# coding: utf-8

# In[31]:


#6.2.1 country-name keys dictionary 

country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}


# In[32]:


country_codes


# In[33]:


len(country_codes)


# In[34]:


#conditon to determin eif its empty 

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empy')


# In[35]:


# showing an empty dictionary evaluates to False 

country_codes.clear()


# In[36]:


if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')


# In[37]:


# Self Check #3. 

states = {'Missouri': 'MO', 'Kansas': 'KA', 'South Dakota': 'SD'}


# In[38]:


states


# In[39]:


# 6.2.2 Iterating through a Dictionary 

days_per_month = {'January': 31, 'Febuary': 28, 'March': 31}


# In[40]:


days_per_month


# In[41]:


for month, days in days_per_month.items():
    print(f'{month} has {days} days')


# In[42]:


days_per_month.items()


# In[43]:


#6.2.3 Basic Dictionary Operations 

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}


# In[44]:


roman_numerals


# In[45]:


# accessing the values of an existing numeral 

roman_numerals['V']


# In[46]:


# Updating the Value of an Existing Key-Value Pair

roman_numerals['X'] = 10 


# In[47]:


roman_numerals


# In[48]:


# Adding a New Key-Value Pair

roman_numerals['L'] = 50


# In[49]:


roman_numerals


# In[50]:


# Removing a Key-Value Pair

del roman_numerals['III']

roman_numerals


# In[51]:


# Removing a Key-Value Pair with pop

roman_numerals.pop('X')


# In[52]:


roman_numerals


# In[53]:


# Attempting to access a Nonexistent Key 

roman_numerals['III']


# In[54]:


roman_numerals.get('III')


# In[55]:


roman_numerals.get('III', 'III not in dictionary')


# In[56]:


roman_numerals.get('V')


# In[57]:


# Testing Whether a Dictionary Contains a Specified Key 

'V' in roman_numerals


# In[58]:


'III' in roman_numerals


# In[59]:


'III' not in roman_numerals 


# In[60]:


# Self check #3. 

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}


# In[61]:


roman_numerals['x'] = 10 


# In[62]:


roman_numerals 


# In[63]:


# Dictionary Methods keys and values 

months = {'January': 1, 'February': 2, 'March': 3}


# In[67]:


for month_name in months.keys():
    print(month_name, end = ' ')


# In[69]:


for month_number in months.values():
    print (month_number, end = ' ')


# In[72]:


# Dictionary Views 

months_view = months.keys()


# In[73]:


for key in months_view:
    print(key, end=' ')


# In[74]:


months['December'] = 12 


# In[75]:


months


# In[76]:


for key in months_view:
    print(key, end=' ')


# In[77]:


# Converting Dictionary Keys, Values and Key-Value Pairs to Lists

list(months.keys())


# In[78]:


list(months.values())


# In[79]:


list(months.items())


# In[82]:


# Processing Keys in Sorted Order 

for month_name in sorted(months.keys()):
    print(month_name, end=' ')


# In[83]:


# Self Check #3.

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}


# In[84]:


list(roman_numerals.keys())


# In[85]:


list(roman_numerals.values())


# In[86]:


list(roman_numerals.items())


# In[87]:


# Dictionary Comparisons 

country_capitals1 = {'Belgium': 'Brussels', 'Haiti': 'Port-au-Prince'}


# In[93]:


country_capitals2 = {'Nepal': 'Katmandu', 'Uruguay': 'Montevideo'}


# In[89]:


country_capitals3 = {'Haiti': 'Port-au_Prince', 'Belgium': 'Brussels'}


# In[94]:


country_capitals1 == country_capitals2


# In[96]:


country_capitals1 != country_capitals2


# In[97]:


# 6.2.6 Example: Dictionary of student Grades 

"""Using a dictionary to represent an instructor's grade book."""
grade_book = {            
    'Susan': [92, 85, 100], 
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],  
    'Pantipa': [97, 91, 92] 
}

all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)
    
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")


# In[98]:


# 6.2.7 Example: Word Counts

"""Tokenizing a string and counting unique words."""

text = ('this is sample text with several words ' 
        'this is more sample text with some different words')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))


# In[99]:


from collections import Counter 


# In[100]:


text = ('this is sample text with several words ' ' this is more sample text with some different words')


# In[102]:


counter = Counter(text.split())


# In[103]:


for word, count in sorted(counter.items()):
    print(f'{word:>12} {count}')


# In[104]:


print('Number of unique keys:', len(counter.keys()))


# In[105]:


# Self Check #2. 

import random 


# In[106]:


numbers = [random.randrange(1, 6) for i in range(50)]


# In[108]:


from collections import Counter


# In[109]:


counter = Counter(numbers)


# In[110]:


for value, count in sorted(counter.items()):
    print(f'{value:<4}{count}')


# In[111]:


# 6.2.8 Dictionary Method update

country_codes = {}


# In[112]:


country_codes.update({'South Africa': 'za'})


# In[113]:


country_codes


# In[114]:


country_codes.update(Australia='ar')


# In[115]:


country_codes 


# In[116]:


# Dictionary comprehensions 

months = {'January': 1, 'February': 2, 'March': 3}


# In[117]:


months2 = {number: name for name, number in months.items()}


# In[118]:


months2


# In[119]:


grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}


# In[120]:


grades2 = {k: sum(v) / len(v) for k, v in grades.items()}


# In[121]:


grades2


# In[123]:


# Self Check 

{number: number ** 3 for number in range(1,6)}


# In[124]:


# 6.3 Creating a Set with Curly Braces 

colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}


# In[125]:


colors


# In[126]:


# Determing a Set's Length 

len(colors)


# In[132]:


# Checking Whether a Value Is in a Set

'red' in colors


# In[133]:


'purple' in colors


# In[134]:


'purple' not in colors


# In[135]:


# Iterating Through a Set

for color in colors:
       print(color.upper(), end=' ')


# In[136]:


# Creating a Set with the Built-In set Function 

numbers = list(range(10)) + list(range(5))


# In[137]:


numbers


# In[138]:


set(numbers)


# In[139]:


set()


# In[141]:


# Frozenset: an Immutable Set Type self check #3. 

text = 'to be or not to be that is the question'


# In[142]:


unique_words = set(text.split())


# In[144]:


for word in sorted(unique_words):
    print(word, end=' ')


# In[145]:


# 6.3.1 Comparing Sets 

{1, 3, 5} == {3, 5, 1}


# In[146]:


{1, 3, 5} != {3, 5, 1}


# In[147]:


# proper subsets
{1, 3, 5} > {3, 5, 1}


# In[148]:


{1, 3, 5} > {7, 3, 5, 1}


# In[149]:


# imporoper subsets

{1, 3, 5} <= {3, 5, 1}


# In[150]:


{1, 3} <= {3, 5, 1}


# In[151]:


# issubset 

{1, 3, 5}.issubset({3, 5, 1})


# In[152]:


{1, 2}.issubset({3, 5, 1})


# In[153]:


# proper superset 

{1, 3, 5} > {3, 5, 1}


# In[154]:


{1, 3, 5, 7} > {3, 5, 1}


# In[155]:


# improper superset

{1, 3, 5} >= {3, 5, 1}


# In[156]:


{1, 3, 5} >= {3, 1}


# In[157]:


{1, 3} >= {3, 1, 7}


# In[158]:


# issuperset

{1, 3, 5}.issuperset({3, 5, 1})


# In[159]:


{1, 3, 5}.issuperset({3, 2})


# In[160]:


#6.3.2 Mathematical Set Operations/ Union

{1, 3, 5} | {2, 3, 4}


# In[161]:


{1, 3, 5}.union([20, 20, 3, 40, 40])


# In[162]:


# Intersection 

{1, 3, 5} & {2, 3, 4}


# In[163]:


{1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])


# In[164]:


# Difference 

{1, 3, 5} - {2, 3, 4}


# In[165]:


{1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4])


# In[166]:


# Symmetric difference 

{1, 3, 5} ^ {2, 3, 4}


# In[167]:


{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4])


# In[168]:


# Disjoint 

{1, 3, 5}.isdisjoint({2, 4, 6})


# In[169]:


{1, 3, 5}.isdisjoint({4, 6, 1})


# In[174]:


# Self Check #2. 

{10, 20, 30} - {5, 10, 15, 20}


# In[171]:


{10, 20, 30} ^ {5, 10, 15, 20}


# In[172]:


{10, 20, 30} | {5, 10, 15, 20}


# In[173]:


{10, 20, 30} & {5, 10, 15, 20}


# In[182]:


# Mutable Set Operators and Methods 

numbers = {1, 3, 5}


# In[185]:


numbers |= {2, 3, 4}


# In[186]:


numbers 


# In[187]:


numbers.update(range(10))


# In[188]:


numbers


# In[189]:


# Methods for Adding and Removing Elements 

numbers.add(17)


# In[190]:


numbers.add(3)


# In[191]:


numbers


# In[192]:


numbers.remove(3)


# In[193]:


numbers


# In[195]:


numbers.discard(3)


# In[196]:


numbers.pop()


# In[197]:


numbers


# In[198]:


numbers.clear()


# In[199]:


numbers


# In[200]:


# Set comprehensions 

numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]


# In[219]:


evens = {item for item in numbers if item % 2 == 0}


# In[220]:


evens 


# In[ ]:




