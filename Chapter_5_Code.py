#!/usr/bin/env python
# coding: utf-8

# In[1]:


c = [-45, 6, 0, 72, 1543]


# In[2]:


c


# In[3]:


c[0]


# In[4]:


c[4]


# In[5]:


len(c)


# In[6]:


c[-1]


# In[7]:


c[-5]


# In[8]:


c[100]


# In[9]:


c[0] + c[1] + c[2]


# In[10]:


a_list = []


# In[12]:


for number in range(1,6):
    a_list += [number]


# In[13]:


a_list


# In[20]:


list1 = [10,20,30]


# In[21]:


list2 = [40,50]


# In[22]:


concatenated_list = list1 + list2


# In[23]:


concatenated_list


# In[35]:


for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')


# In[36]:


a = [1, 2, 3]


# In[37]:


b = [1, 2, 3]


# In[38]:


c= [1, 2, 3, 4]


# In[39]:


a == b 


# In[40]:


a == c


# In[41]:


a < c


# In[42]:


a >= b


# In[43]:


a > c


# In[44]:


def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3 


# In[46]:


numbers = []


# In[47]:


for number in range(1,11):
    numbers += [number]


# In[48]:


cube_list(numbers)


# In[49]:


numbers


# In[50]:


student_tuple = 'John', 'Green', 3.3


# In[51]:


student_tuple


# In[52]:


another_student_tuple = ('Mary', 'Red', 3.3)


# In[54]:


another_student_tuple


# In[55]:


time_tuple = (9,16,1)


# In[56]:


time_tuple


# In[57]:


time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2]


# In[58]:


tuple1 = (10,20,30)


# In[59]:


tuple2 = tuple1


# In[60]:


tuple2


# In[61]:


tuple1 += (40,50)


# In[70]:


tuple1


# In[71]:


tuple2


# In[74]:


student_tuple = ('Amanda', [98,75,87])


# In[75]:


first_name, grades = student_tuple


# In[76]:


first_name 


# In[77]:


grades


# In[78]:


numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')


# In[82]:


#21.


# In[100]:


numbers = list(range(1,16))


# In[101]:


numbers


# In[102]:


numbers[1:len(numbers):2]


# In[103]:


numbers[5:10] = [0] * len(numbers[5:10])


# In[104]:


numbers


# In[105]:


numbers[5:] = []


# In[106]:


numbers


# In[107]:


numbers[:] = []


# In[108]:


numbers


# In[109]:


characters = ['Romeo', 'Juliet']


# In[110]:


characters


# In[112]:


characters = [name if name != 'Romeo' else 'Daniel' for name in characters]


# In[113]:


characters


# In[114]:


#22. using exisiting character list for this problem. 


# In[115]:


del characters[-1]


# In[116]:


characters


# In[117]:


#23.


# In[119]:


def modify_elements(items):
    """Multiplies all elements values in items by 2."""
    for i in range(len(items)):
        items[i] *= 2


# In[125]:


numbers = [10, 3, 7, 1, 9]


# In[126]:


modify_elements(numbers)


# In[127]:


numbers


# In[128]:


#24. 


# In[131]:


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]


# numbers.sort()

# In[132]:


numbers.sort()


# In[133]:


numbers


# In[134]:


numbers.sort(reverse=True)


# In[135]:


numbers


# In[139]:


#25. read this section


# In[140]:


#26.


# In[141]:


foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']


# In[142]:


foods.sort()


# In[143]:


foods


# In[145]:


#27. working through 5.9


# In[146]:


numbers = [3, 7, 1, 4, 2, 8, 5, 6]


# In[147]:


numbers.index(5)


# In[149]:


numbers *= 2


# In[150]:


numbers


# In[151]:


numbers.index(5,7)


# In[152]:


numbers.index(7, 0, 4)


# In[153]:


1000 in numbers


# In[154]:


5 in numbers


# In[155]:


1000 not in numbers


# In[156]:


5 not in numbers


# In[157]:


key = 1000


# In[160]:


if key in numbers:
    print(f'found{key} at index {numbers.index(search_key)}')
else:
    print(f'{key} not found')


# In[161]:


for num in numbers:
    if num > 0:
        print('positive_number')
    if num < 0:
        print('negative_number')


# In[162]:


#28. I have read through the rest of the list functions in this chapter section 


# In[172]:


#29.
list2 = [item for item in range(1600)] 


# In[177]:


#print list from 1-19 to show the created list in range 1600 works but shown in consice manner. 
list2[1:20]


# In[178]:


#30. I have read about filter map and reduce 


# In[179]:


#31. I have read about Lambda functions 

list(filter(lambda x: x % 2 != 0, numbers))


# In[ ]:


#32. I do enjoy working with data spreadsheets. It was very interesting working with the grades example. 

