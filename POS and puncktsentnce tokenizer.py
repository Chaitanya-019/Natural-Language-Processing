#!/usr/bin/env python
# coding: utf-8

# In[12]:


import nltk
from nltk.tokenize import PunktSentenceTokenizer  #its an unsupervised model tokeniser for sent_tokenisatino
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize


# In[1]:


"""
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent‘s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go ‘to‘ the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
"""


# In[7]:


train = state_union.raw("2005-GWBush.txt")
test = state_union.raw("2006-GWBush.txt")


# In[9]:


pst = PunktSentenceTokenizer(train)  #training the tokenizer


# In[10]:


tokenised = pst.tokenize(test)


# In[13]:


pos = []
for i in tokenised:
    words = word_tokenize(i)
    pos.append(nltk.pos_tag(words))
    


# In[14]:


pos


# In[ ]:




