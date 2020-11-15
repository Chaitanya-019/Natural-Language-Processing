#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import wordnet


# In[3]:


syn = wordnet.synsets("legend")


# In[15]:


syn


# In[16]:


syn[0].lemmas()


# In[18]:


syn[0].name()


# In[20]:


syn[0].lemmas()[0]


# In[25]:


print(syn[0].lemmas()[0].name())
print(syn[0].lemmas()[1].name())
print(syn[1].lemmas()[0].name())
print(syn[1].lemmas()[1].name())


# In[31]:


print(syn[0].definition())
print(syn[1].definition())


# In[38]:


synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            print(l.antonyms())
            antonyms.append(l.antonyms()[0].name())
        else:
            print(l.antonyms())

# print(set(synonyms))
# print(set(antonyms))


# In[ ]:





# In[39]:


#Similarity based on the meaning of words

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))


# In[ ]:




