#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import state_union


# In[1]:


#these are the lasssifications madde by ne_chunk and shows the classified words with the type like organisation,person,etc..

"""NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian"""


# In[3]:


data = state_union.raw("2005-GWBush.txt")


# In[4]:


sentences = sent_tokenize(data)


# In[5]:


for i in sentences:
    words = word_tokenize(i)
    tokenised_pos = nltk.pos_tag(words)   
    classified = nltk.ne_chunk(tokenised_pos,binary = True)  #when binary is used then the type of word like person time,date is not shown.
    classified.draw()


# In[ ]:





# In[ ]:




