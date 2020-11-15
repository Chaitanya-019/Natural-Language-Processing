#!/usr/bin/env python
# coding: utf-8

# In[3]:


sample="""	Home Life and Death:
•	Bridgman was an American physicist who was born on 21-04-1882 in New England.
•	His father name is Raymond london Bridgman who works as a newspaper reporter and his mother name is Marry Ann Maria Williams.
•	Bridgman completed his primary and secondary education in Auburndale.
•	He studied in Hardward university.
•	He got Noble prize in 1946 for his works on physics under high pressures.
•	He died on 20-08-1961
	Works:
•	He invented a special seal which has a selfhealing property.
•	He discovered that electron in ceasium undergo rearrangement at certain transition pressure.
•	His main work involves measurements of compressibilities of liquid and solids.
•	His works also involves studies of phase changes in solids under high pressures.
	Bridgman-stockbarger method:               
•	This is a special which is invented by by Bridgman along with a famous scientist Stockbarger which is mostly  used for preparation of single crystal solids.
•	In this process a crucible ,containing the pure melt, is slowly moved down to the cooler region of the furnace.
•	Then crystal begins to grow as the temperature falls down the furnace.
•	This is a process mainly  used for synthesis of gem stones.
•	This method is used for solidifying polycrystalline materials.
•	This method is used for  preparing semi conductor  crystals like gallium arsenide (mainly used in laser diodes, solar cells.
	Bridgman method:
•	This method is similar to the previous method but the only difference is , in this method the impurities were removed based on their speed in their molten state.
•	In this the ceramic mould is taken in a cu plate and taken to the furnace and heated until the whole material is at a uniform temperature.
•	Then it is allowed into the vaccum and cooled and molten liquid is allowed into the mould through a starter selector. 
•	Then impurities will be out due to difference in speeds and pure material is obtained.
	Advantages:
	It is most popular among all high temperature methods.
	It has faster growth rate and improves electrical transfer.
	It forms large uniform crystals and improves its metallurgical properties.
	Disadvantages:
	It generates stress related dislocations.
	It has contamination by impurities.
	The impurities are mainly Quartz.
	Crucible can be the problem.
	Work for Nobel Prize:
•	Bridgman says that “At high  pressure  matter  takes other  properties than   under normal conditions.”
•	He studied properties and structures under high pressures( about 100,000 atm) for about 100 different materials.
•	 He Initially started with 6,500atm and then experimented untill 100,000 atm and then reached maximum 400,000atm.
	Awards and Prizes:
•	He got Noble prize in physics, Elliott cresson medal
•	He got Rumford prize, Royal society bakerian medal
•	He got Comstock medal in physics, Josiah williard gibbs lectureship.
	Conclusion:
•	Even after his methods many methods have come like binary3 and 5 but even these were not able to dominate this method in terms of the properties of material formed.
•	Bridgman  method dominates in crystal growth of semiconductors compounds with M.P<2000k and decomposition pressure <10bar.
	
"""


# In[4]:


sample.replace("•","")
sample.replace("","")


# In[5]:


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import BlanklineTokenizer


# In[6]:


sentences=sent_tokenize(sample)


# In[9]:


example = """Hey this is chaitanya. How are you. Be safe in this pandemic situation. which when taken lite can be a trageting situation ever"""


# In[10]:


example


# In[11]:


words= word_tokenize(example)


# In[12]:


words


# In[ ]:




