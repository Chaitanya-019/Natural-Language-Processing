#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# In[5]:


data = "This is  a story of two young boys who have two fathers one is rich dad and anotheer is a poor dad. the por dad alwaays says to geet good marks ,get good job with best payheck and be safe always where as te rich dad who waas a professttional busssiness says to work smart and try to make money work for you not you working for maney and has taaught financial educationand foundation ehich is never taught in any of the school."


# In[8]:


words= word_tokenize(data)


# In[9]:


ps = PorterStemmer()


# In[11]:


new_words = []
for i in words:
    new_words.append(ps.stem(i))


# In[12]:


new_words


# In[ ]:




