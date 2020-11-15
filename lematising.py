#!/usr/bin/env python
# coding: utf-8

# In[1]:


#this is same like stemming but only difference is instead of giving root it can give adjective,verb,etc... default giving is noun


# In[2]:


from nltk.stem import WordNetLemmatizer


# In[3]:


lemmatizer = WordNetLemmatizer()


# In[4]:


print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a")) #giving it is an adjective
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))


# In[ ]:




