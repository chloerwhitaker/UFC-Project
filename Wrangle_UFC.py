#!/usr/bin/env python
# coding: utf-8

# ## Acquire and Prepare

# In[1]:


# Function to wrangle the UFC data


# In[2]:


def get_n_prep_ufc(): 
    
    # imports
    import pandas as pd
    # Ignore Warnings
    import warnings
    warnings.filterwarnings("ignore")
    
    # read .csv
    ufc = pd.read_csv('ufc-master-cleaned.csv')
    
    # add the columns I would like to work with into a new df
    ufc_cleaned = ufc[['event_name', 'fullname', 'fighter_two_name', 'w', 'l', 'd', 'nc', 'total_rounds', 'belt', 'womens_bout', 'interim_bout', 'strawweight', 'flyweight', 'bantamweight', 'featherweight', 'lightweight', 'middleweight', 'light_heavyweight', 'heavyweight', 'catch_weight', 'open_weight', 'super_heavyweight', 'superfight', 'fight_city', 'fight_state', 'fight_country', 'height', 'weight', 'reach', 'stance', 'slpm', 'stracc', 'sapm', 'strdef', 'tdavg', 'tdacc', 'tddef', 'subavg', 'age_days', 'age']].copy(0)
    
    # Drop duplicates if any
    df = ufc_cleaned.drop_duplicates()
    
    # combine w, l, d, nc into on target column called outcome
    cols = ['w', 'l', 'd', 'nc']
    ufc_cleaned['outcome'] = ufc_cleaned[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    
    # rename the labels in outcome to be human readable 
    ufc_cleaned['outcome'].replace({'1_0_0_0': 'win', '0_1_0_0': 'loss', '0_0_1_0': 'draw', '0_0_0_1': 'no_contest'}, inplace=True)
    
    # rename fullname and fighter_two_name to fighter and opponent respectively
    ufc_cleaned.rename(columns={'fullname': 'fighter', 'fighter_two_name': 'opponent'}, inplace=True)
    
    # clean height column
    
    # replace the -- with 0' 0" so my function below will work
    ufc_cleaned['height'].replace({'--': "0' 0\""}, inplace=True)
    
    # convert ft to in
    def parse_ht(ht):
        # format: 7' 0.0"
        ht_ = ht.split("' ")
        ft_ = float(ht_[0])
        in_ = float(ht_[1].replace("\"",""))
        return (12*ft_) + in_
    
    # apply parse_ht
    ufc_cleaned["height_in"] = ufc_cleaned["height"].apply(lambda x:parse_ht(x))

    # convert float to int
    ufc_cleaned['height_in'] = ufc_cleaned.height_in.astype(int) 
    
    # handle null values
    
    # fill fight_state null values with the mode which is Navada
    ufc_cleaned['fight_state'] = ufc_cleaned.fight_state.fillna(ufc_cleaned.fight_state.mode()[0])
    
    # drop null rows in specific columns
    ufc_cleaned = ufc_cleaned[ufc_cleaned.weight.notnull()]
    ufc_cleaned = ufc_cleaned[ufc_cleaned.reach.notnull()]
    ufc_cleaned = ufc_cleaned[ufc_cleaned.stance.notnull()]
    ufc_cleaned = ufc_cleaned[ufc_cleaned.age.notnull()]
    ufc_cleaned = ufc_cleaned[ufc_cleaned.fight_country.notnull()]
    
    # drop nulls to make sure none were missed
    df = df.dropna()
    
    # create dummy columns for stance column and concat to df
    dummy_df = pd.get_dummies(ufc_cleaned[['stance']], dummy_na=False, drop_first=[False])
    ufc_cleaned = pd.concat([ufc_cleaned, dummy_df], axis=1)
    
    # Drop height column
    cols_to_drop = ['height']
    ufc_cleaned = ufc_cleaned.drop(columns=cols_to_drop)

    return ufc_cleaned
    


# In[3]:


# ufc_cleaned = get_n_prep_ufc()


# In[4]:


# ufc_cleaned.head()


# ## Split Data

# In[5]:


def train_validate_test_split(ufc_cleaned):
    '''
    This function takes in a dataframe (df) and returns 3 dfs
    (train, validate, and test) split 20%, 24%, 56% respectively. 
    
    Also takes in a random seed for replicating results.  
    '''
    
    from sklearn.model_selection import train_test_split
     
    train_and_validate, test = train_test_split(
        ufc_cleaned, test_size=0.2, random_state=123, stratify=ufc_cleaned.outcome
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=123,
        stratify=train_and_validate.outcome,
    )
    return train, validate, test


# In[6]:


# train, validate, test = train_validate_test_split(ufc_cleaned)


# In[7]:


# train.head(1)


# In[8]:


def get_prep_n_split_ufc_data():
    ''' 
    This function runs get_n_prep_ufc and train_validate_test_split functions.
    It takes in the original df and returns the split dfs train, validate, test (in that order).
    '''
    
    # imports
    import pandas as pd
    # Ignore Warnings
    import warnings
    warnings.filterwarnings("ignore")
    from sklearn.model_selection import train_test_split
    
    
    ufc_cleaned = get_n_prep_ufc()
    train, validate, test = train_validate_test_split(ufc_cleaned)
    return train, validate, test


# In[9]:


train, validate, test = get_prep_n_split_ufc_data()


# In[10]:


train.head(1)


# In[14]:


# train.shape


# In[15]:


# validate.shape


# In[16]:


# test.shape


# In[ ]:




