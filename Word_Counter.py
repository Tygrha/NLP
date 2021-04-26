#!/usr/bin/env python
# coding: utf-8

# In[19]:


with open('text.txt') as f:
    contents = f.read()


# In[20]:


word_list=contents


# In[21]:


for char in '-.,\n':
    word_list=word_list.replace(char,' ')
word_list = word_list.lower()
# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
word_list = word_list.split()
saved_list = word_list


# In[22]:


from collections import Counter
print(Counter(word_list).most_common())

