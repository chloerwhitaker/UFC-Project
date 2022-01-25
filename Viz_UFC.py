#!/usr/bin/env python
# coding: utf-8

# ## UFC VIZ Functions

# This is my notebook for the visual functions for my UFC project. 

# ### imports

# In[1]:


# imports
import numpy as np
import pandas as pd

# Visualizing
import matplotlib.pyplot as plt
import seaborn as sns

# My files
from Wrangle_UFC import *

# Remove Limits On Viewing Dataframes
pd.set_option('display.max_columns', None)


# #### Visualizing what makes a winner: 

# In[36]:


# acquire data using function from Wrangle_UFC.py
final_df, fighter_stat_diff = ufc_stats_difference()


# In[37]:


# use function from Wrnagle_UFC to split data
train, validate, test = train_validate_test_split(final_df)


# In[39]:


# add numeric columns to df 
df_num = train.select_dtypes(include='int64')


# In[46]:


def winning_corr_viz():
    '''
    heatmap of how the different values correlate to fighter1 winning
    ''' 
    plt.figure(figsize=(8, 12))
    heatmap = sns.heatmap(df_num.corr()[['win']].sort_values(by='win', ascending=False), vmin=-1, vmax=1, annot=True, cmap='cubehelix_r')
    heatmap.set_title('Features Correlating with Winning', fontdict={'fontsize':18}, pad=16);
    plt.show();
    


# In[48]:


# winning_corr = winning_corr_viz()


# #### How does Colby Covington and Jorge Masvidal's stats compare to the values with the highest correlation to winning?

# In[2]:


# acquire last 10 colby fights using a function from Wrangle_UFC.py
colby_diff = get_colby()


# In[49]:


# confirm acquire
# colby_diff.head(1)


# In[4]:


# acquire last 10 jorge fights using a function from Wrangle_UFC.py
jorge_diff = get_jorge()


# In[50]:


# confirm acquire
# jorge_diff.head(1)


# In[60]:


def win_loss_viz():

    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    fig, ax =plt.subplots(1,2)
    fig.suptitle('Colby Covinvton has won 8 out of his last 10 fights and Jorge Masvidal has won 6 out of his last 10 fights.')

    sns.countplot(x="outcome", data=colby_diff, palette="husl", ax=ax[0])
    ax[0].set_title('Colby')

    sns.countplot(x="outcome", data=jorge_diff, palette="husl", ax=ax[1])
    ax[1].set_title('Jorge')
    fig.show();


# In[72]:


# win_loss = win_loss_viz()


# In[62]:


def strikes_defense_viz():

    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    fig, ax =plt.subplots(1,2)
    fig.suptitle('Colby Covinvton Usually has Worse Strike Defense and Jorge Masvidal Usually has Better Strike Defense than his Opponent.')

    sns.countplot(x="strikes_defense_diff", data=colby_diff, palette="husl", ax=ax[0])
    ax[0].set_title('Colby')

    sns.countplot(x="strikes_defense_diff", data=jorge_diff, palette="husl", ax=ax[1])
    ax[1].set_title('Jorge')
    fig.show();


# In[73]:


# stike_def = strikes_defense_viz()


# In[64]:


def takedown_defense_viz():

    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    fig, ax =plt.subplots(1,2)
    fig.suptitle('Colby Covinvton Usually has Better Takedown Defense and Jorge Masvidal has the Takedown Defense Advantage as Often as his Opponent.')

    sns.countplot(x="takedown_defense_diff", data=colby_diff, palette="husl", ax=ax[0])
    ax[0].set_title('Colby')

    sns.countplot(x="takedown_defense_diff", data=jorge_diff, palette="husl", ax=ax[1])
    ax[1].set_title('Jorge')
    fig.show();


# In[74]:


# takedown_def = takedown_defense_viz()


# In[66]:


def strike_acc_viz():

    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    fig, ax =plt.subplots(1,2)
    fig.suptitle('Colby Covinvton Always has Worse Strike Accuracy and Jorge Masvidal Usually has Better Strike Accuracy than his Opponent.')

    sns.countplot(x="strike_acc_diff", data=colby_diff, palette="husl", ax=ax[0])
    ax[0].set_title('Colby')

    sns.countplot(x="strike_acc_diff", data=jorge_diff, palette="husl", ax=ax[1])
    ax[1].set_title('Jorge')
    fig.show();


# In[75]:


# strike_acc = strike_acc_viz()


# In[68]:


def age_diff_viz():

    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    fig, ax =plt.subplots(1,2)
    fig.suptitle('Colby Covinvton Usually Younger than his Opponent and Jorge Masvidal was Younger than his Opponent 50%.')

    sns.countplot(x="age_diff", data=colby_diff, palette="husl", ax=ax[0])
    ax[0].set_title('Colby')

    sns.countplot(x="age_diff", data=jorge_diff, palette="husl", ax=ax[1])
    ax[1].set_title('Jorge')
    fig.show();


# In[76]:


# age_diff = age_diff_viz()


# In[70]:


def takedown_defense_viz():

    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    fig, ax =plt.subplots(1,2)
    fig.suptitle('Colby Covinvton Usually has Better Takedown Accuracy and Jorge Masvidal always has better Takedown Accuracy than his Opponent.')

    sns.countplot(x="takedown_acc_diff", data=colby_diff, palette="husl", ax=ax[0])
    ax[0].set_title('Colby')

    sns.countplot(x="takedown_acc_diff", data=jorge_diff, palette="husl", ax=ax[1])
    ax[1].set_title('Jorge')
    fig.show();


# In[77]:


# takedown_def = takedown_defense_viz()


# In[ ]:




