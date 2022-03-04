#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import modules
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[2]:


# read the DataFrame
candy_hierarchy = pd.read_csv('E:/hazem/Technology/Data science/CAT/Data Cleaning/task/candyhierarchy2017.csv')
pd.set_option('display.max_columns',120)


# In[3]:


#chaning the names of the columns
candy_hierarchy.columns=['ID','Going_Out','Gender','Age','Country','State' ,'Grand_Bar','Brown_Globs','Candy_bar','Black_jacks',
                        'Bonkers_Candy','Bonkers_Game','Bottle_caps','Raisins_Box','Broken_stick','Butterfinger',
                        'Cadbury_CremeEggs' , 'Candy_Corn','Resturant_FreeCandy','Caramellos','Cash','Chardonnay','Chick-O-Sticks',
                        'Chiclets','Coffee Crisp','Creepy_Religious_comics','paraphenalia','Dots','Dove_Bars','Fuzzy_Peaches',
                        'Generic_Brand_Acetaminophen' ,'Glow_Sticks',' GooGoo_Clusters','GoodN_Plenty', 'Gum_cards','Gummy_Bears',
                        'Hard_Candy','Healthy_Fruit','Health_Bar','Hersheys_DarkChocolate','Hersheys_MilkChocolate',
                        'Hersheys_Kisses','Hugs','Bad_JollyRancher','Good_JollyRancher','JoyJoy' ,'Junior_Mints' ,'senior Mints',
                        'Kale_smoothie','Kinder','KitKat','LaffyTaffy','LemonHeads','NotBlack_Licorice','Black_Licorice',
                        'Lindt_Truffle','Lollipops','Mars','Maynards','Mike&Ike','Milk_Duds','Milky Way','Regular-M&M',
                        'Peanut_M&M','Blue_M&M','Red_M&M','Green_M&M','Independant_M&M','Abstained_M&M','Minibags_Chips','Mint_Kisses',
                        'Mint_Juleps','Mr.Goodbar','NeccoWafers','Nerds','NestleCrunch',"Now'n'Laters",'Peeps','Pencils','Pixy_Stix',
                        'Housewives','Reese’sButter',"Reese'sPieces",'JacksonBar','Rolos','BooBerry_Sandwich','Skittles','American_Smarties',
                        'CommonWealth_Smarties','Snickers','Sourpatch_Kids','Spotted_Dick','Starburst','Sweet_Tarts','Swedish Fish',
                        'Sweetums','Take5','TicTacs','Marshmallow','Musketeers','Tolberone','Trail-Mix','Twix','fructose corn syrup',
                        'Vicodin','Whatchamacallit_Bars','White_Bread','Whole Wheat anything','Peppermint Patties','JOY OTHER',
                        'DESPAIR OTHER','OTHER COMMENTS','Dress','Unnamed:113','Day',"Media DailyDish","Media Science",'Media ESPN',
                        'Media Yahoo',"Click Coordinates (x, y)"]


# In[4]:


#Show some general properties of the DataFrame
candy_hierarchy.head()
candy_hierarchy.info()
candy_hierarchy.dtypes


# In[5]:


#chanind the datatypes of some columns
candy_hierarchy['ID'] = candy_hierarchy['ID'].astype('O')
assert candy_hierarchy['ID'].dtype == 'O'
#Making Sure there isnot dupliacted values
duplicates=candy_hierarchy.duplicated(subset=['ID'],keep=False)
candy_hierarchy[duplicates]         #No duplicated Value


# In[6]:


#Droping the usless columns 
candy_hierarchy.drop(columns=['ID','Unnamed:113'],inplace=True)


# In[7]:


#Droping the rows which have Nan values for all columns
candy_hierarchy.dropna(axis='index',how='all',inplace=True)
#drop the rows which have Nan values for all Q6 Column 
columns_name=[ 'Grand_Bar','Brown_Globs','Candy_bar','Black_jacks','Bonkers_Candy','Bonkers_Game','Bottle_caps','Raisins_Box','Broken_stick','Butterfinger',
                        'Cadbury_CremeEggs' , 'Candy_Corn','Resturant_FreeCandy','Caramellos','Cash','Chardonnay','Chick-O-Sticks',
                        'Chiclets','Coffee Crisp','Creepy_Religious_comics','paraphenalia','Dots','Dove_Bars','Fuzzy_Peaches',
                        'Generic_Brand_Acetaminophen' ,'Glow_Sticks',' GooGoo_Clusters','GoodN_Plenty', 'Gum_cards','Gummy_Bears',
                        'Hard_Candy','Healthy_Fruit','Health_Bar','Hersheys_DarkChocolate','Hersheys_MilkChocolate',
                        'Hersheys_Kisses','Hugs','Bad_JollyRancher','Good_JollyRancher','JoyJoy' ,'Junior_Mints' ,'senior Mints',
                        'Kale_smoothie','Kinder','KitKat','LaffyTaffy','LemonHeads','NotBlack_Licorice','Black_Licorice',
                        'Lindt_Truffle','Lollipops','Mars','Maynards','Mike&Ike','Milk_Duds','Milky Way','Regular-M&M',
                        'Peanut_M&M','Blue_M&M','Red_M&M','Green_M&M','Independant_M&M','Abstained_M&M','Minibags_Chips','Mint_Kisses',
                        'Mint_Juleps','Mr.Goodbar','NeccoWafers','Nerds','NestleCrunch',"Now'n'Laters",'Peeps','Pencils','Pixy_Stix',
                        'Housewives','Reese’sButter',"Reese'sPieces",'JacksonBar','Rolos','BooBerry_Sandwich','Skittles','American_Smarties',
                        'CommonWealth_Smarties','Snickers','Sourpatch_Kids','Spotted_Dick','Starburst','Sweet_Tarts','Swedish Fish',
                        'Sweetums','Take5','TicTacs','Marshmallow','Musketeers','Tolberone','Trail-Mix','Twix','fructose corn syrup',
                        'Vicodin','Whatchamacallit_Bars','White_Bread','Whole Wheat anything','Peppermint Patties']
candy_hierarchy.dropna(axis='index',how='all',subset=columns_name,inplace=True)


# In[8]:


candy_hierarchy


# In[9]:


#Cleaning the Going_out Column
#1-Knowing the unique values of the column
candy_hierarchy['Going_Out'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'Going_Out' : 'No'},inplace=True)


# In[10]:


#Cleaning the Gender Column
#1-Knowing the unique values of the column
candy_hierarchy['Gender'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'Gender' :"I'd rather not say"},inplace=True)
candy_hierarchy['Gender'].value_counts()


# In[11]:


#Cleaning the Age column
#1-Knowing the dtype of the column
candy_hierarchy['Age'].dtype
#2-Knowing the unique values of the column
candy_hierarchy['Age'].unique()
#3-Replace some values
NonSense_values= ['I can remember when Java was a cool new language',  'MY NAME JEFF','ancient','1000','See question 2','older than dirt',
                  'Enough','312','hahahahaha','?', 'no', 'Many','4']
Old_People = ['old enough','old','OLD','Old enough','Over 50']
for state in NonSense_values:
    candy_hierarchy['Age'].replace(state,np.nan,inplace=True)

for person in Old_People:
    candy_hierarchy['Age'].replace(person,55,inplace=True)
    
candy_hierarchy['Age'].replace('45-55',50,inplace=True)
candy_hierarchy['Age'].replace('24-50',37,inplace=True)
candy_hierarchy['Age'].replace('46 Halloweens.',46,inplace=True)
candy_hierarchy['Age'].replace('59 on the day after Halloween',59,inplace=True)

#4-Parsing the age column
candy_hierarchy['Age']=candy_hierarchy['Age'].astype('float')
#5-Using the more suitable way
candy_hierarchy['Age'].describe()
Age_Median = candy_hierarchy['Age'].median()
#6-Replace the Non values
candy_hierarchy.fillna({'Age':Age_Median},inplace=True)
candy_hierarchy['Age'].unique()


# In[12]:


#Cleaning the Country column
#1-Knowing the unique values of the column
candy_hierarchy['Country']=candy_hierarchy['Country'].str.lower()
candy_hierarchy['Country'].unique()
#2-Replace some values
Missed_Countries=["i don't know anymore",'fear and loathing','subscribe to dm4uz3 on youtube','a','insanity lately','earth',
                 'atlantis',]
USA_Country = ['usa usa usa!!!!','u s a', 'united statea','u.s. ','ussa', 'united stated','united statss','united sates',
              'i pretend to be from canada, but i am really from the united states.','usa? hard to tell anymore..',
               'the united states of america', 'the united states', 'unites states', 'united states of america ',
              'u.s.a.', 'usausausa','united states ','united states of america','united states', 'united staes',
              'usa ', 'us', 'usa','united states','us of a','u s', 'u.s.']
Canda_Country =['canada','canada ','canae','canada`']
America_Country =['america',"'merica",'ahem....amerca','n. america', 'murrika']
France_Country =['france', 'france ']
Uk =['uk','united kingdom']
England = ['england','endland']

for country in Missed_Countries:
    candy_hierarchy['Country'].replace(country,'Unknown',inplace=True)

for country in USA_Country:
    candy_hierarchy['Country'].replace( country,'United States',inplace=True)
    
for country in Canda_Country:
    candy_hierarchy['Country'].replace( country,'Canda',inplace=True)

for country in America_Country:
    candy_hierarchy['Country'].replace( country,'America',inplace=True)

for country in France_Country:
    candy_hierarchy['Country'].replace( country,'France',inplace=True)

for country in Uk:
    candy_hierarchy['Country'].replace( country,'United kingdom',inplace=True)
    
for country in England:
    candy_hierarchy['Country'].replace( country,'England',inplace=True)
    
#3-Fill the Nan Value
candy_hierarchy.fillna({'Country':'Unknown'},inplace=True)
candy_hierarchy['Country']=candy_hierarchy['Country'].str.capitalize()
candy_hierarchy['Country'].value_counts().sort_values()


# In[13]:


#Cleaning Q6 Column
for Column in columns_name:
    candy_hierarchy.fillna({Column :'Other'} ,inplace=Tru


# In[ ]:


#Cleaning the JOY OTHER Column
#1-Knowing the unique values of the column
candy_hierarchy['JOY OTHER'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'JOY OTHER' : 'No'},inplace=True)
        
        


# In[ ]:


#Cleaning the DESPAIR OTHER Column
#1-Knowing the unique values of the column
candy_hierarchy['DESPAIR OTHER'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'DESPAIR OTHER' : 'No'},inplace=True)


# In[ ]:


#Cleaning the OTHER COMMENTS Column
#1-Knowing the unique values of the column
candy_hierarchy['OTHER COMMENTS'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'OTHER COMMENTS' : 'No'},inplace=True)


# In[ ]:


#Cleaning the Day Column
#1-Knowing the unique values of the column
candy_hierarchy['Day'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'Day' : 'Other'},inplace=True)


# In[ ]:


#Cleaning the Dress Column
#1-Knowing the unique values of the column
candy_hierarchy['Dress'].unique()
#2-Replace the Nan values
candy_hierarchy.fillna({'Dress' : 'Other'},inplace=True)


# In[ ]:




