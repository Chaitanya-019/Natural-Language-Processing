#!/usr/bin/env python
# coding: utf-8

# In[1]:


#chunking is simple way of extracting specific regular expression sentences or words


# In[1]:


import nltk
from nltk.tokenize import PunktSentenceTokenizer  #its an unsupervised model tokeniser for sent_tokenisatino
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize


# In[2]:


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


# In[9]:


"""
Reg exp

Identifiers:

\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.

Modifiers:

{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code

White Space Charts:

\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!

. + * ? [ ] $ ^ ( ) { } | \
Brackets:

[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z"""


# In[3]:


train = state_union.raw("2005-GWBush.txt")
test = state_union.raw("2006-GWBush.txt")


# In[4]:


pst = PunktSentenceTokenizer(train)  #training the tokenizer


# In[5]:


tokenised = pst.tokenize(test)


# In[7]:


for i in tokenised:
    words = word_tokenize(i)
    tokenise = nltk.pos_tag(words)
    
    chunkgram = r"""chunk :{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkprase = nltk.RegexpParser(chunkgram)
    chunkd = chunkprase.parse(tokenise)
    print(chunkd)


# In[11]:


def process_content():
    try:
        for i in tokenised:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""  #we can give any name not only Chunk.
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()      #it shows every thing but if the required word or sentence is formed then it is given a name name and shows as the branch of tree or sub tree 
    except Exception as e:
        print(str(e))

process_content()


# In[ ]:




