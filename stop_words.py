#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import docx


# In[2]:


data="This is  a story of two young boys who have two fathers one is rich dad and anotheer is a poor dad. the por dad alwaays says to geet good marks ,get good job with best payheck and be safe always where as te rich dad who waas a professttional busssiness says to work smart and try to make money work for you not you working for maney and has taaught financial educationand foundation ehich is never taught in any of the school."


# In[3]:


data


# In[4]:


stop_words = set(stopwords.words("english"))


# In[5]:


stop_words


# In[6]:


words= word_tokenize(data)


# In[7]:


new_data = []
for i in range(len(words)):
    if words[i] not in stop_words:
        new_data.append(words[i])


# In[8]:


" ".join(new_data)


# In[ ]:




