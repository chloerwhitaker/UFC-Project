#!/usr/bin/env python
# coding: utf-8

# ## Acquire and Clean

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
    ufc_cleaned['outcome'].replace({'1_0_0_0': 'fighter1', '0_1_0_0': 'fighter2', '0_0_1_0': 'draw', '0_0_0_1': 'no_contest'}, inplace=True)
    
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


# ## Prepare

# In[5]:


def combined_ufc():
    ''' 
    This function:
    reads in clean data
    creates a new df with desired columns, then
    resets the index
    create column with the name of the fighter and opponent concatenated
    create column with the reverse (opponent and fighter)
    creates list of column names
    creates df with column names above
    join the concat and reverse together and add it to the df created
    drop unwanted columns
    renames columns
    returns a df with the fighter1 and fighter2 stats in the same row
    '''
    
    # imports
    import pandas as pd
    import numpy as np
    # Ignore Warnings
    import warnings
    warnings.filterwarnings("ignore")
    
    # Read and clean data
    ufc_cleaned = get_n_prep_ufc()
    
    # Create df desired columns
    fighter_stats = ufc_cleaned[['event_name', 'fighter', 'opponent', 'outcome', 'w', 'l', 'd', 'nc', 'weight', 'reach', 'stance', 'slpm',
       'stracc', 'sapm', 'strdef', 'tdavg', 'tdacc', 'tddef', 'subavg',
       'age_days', 'age', 'outcome', 'height_in', 'stance_Orthodox',
       'stance_Southpaw', 'stance_Switch']].copy(0)
    
    # reset the index
    fighter_stats.reset_index(drop = True, inplace = True)
    
    # Create column with the name of the fighter and opponent
    # Create column with the reverse (opponent and fighter)
    fighter_stats['concat'] = fighter_stats.fighter + fighter_stats.opponent
    fighter_stats['reverse'] = fighter_stats.opponent + fighter_stats.fighter
    
    # Create list of columns
    columns = ['event_name1','fighter1', 'fighter2', 'outcome1', 'w1', 'l1', 'd1', 'nc1', 'weight_f1', 'reach_f1', 'stance_f1', 'strikes_f1',
       'strike_acc_f1', 'strikes_absorbed_f1', 'strike_defense_f1', 'takedowns_f1', 'takedown_acc_f1', 'takedown_def_f1', 'sub_attempt_f1',
       'age_days_f1', 'age_f1', 'outcome_f1', 'height_in_f1', 'stance_Orthodox_f1',
       'stance_Southpaw_f1', 'stance_Switch_f1', 'concat', 'reverse', 'event_name2', '2fighter1', '2fighter2', 'outcome2', 'w2', 'l2', 'd2', 'nc2', 'weight_f2', 'reach_f2', 'stance_f2', 'strikes_f2',
       'strike_acc_f2', 'strikes_absorbed_f2', 'strike_defense_f2', 'takedowns_f2', 'takedown_acc_f2', 'takedown_def_f2', 'sub_attempt_f2',
       'age_days_f2', 'age_f2', 'outcome_f2', 'height_in_f2', 'stance_Orthodox_f2',
       'stance_Southpaw_f2', 'stance_Switch_f2', 'concat2', 'reverse2']
    
    # Create DF with column names above
    final_df = pd.DataFrame(columns = columns)
    
    # join the concat and reverse 
    for i in range(len (fighter_stats)):
        lineconcat = fighter_stats.iloc[i].concat
        linereverse = fighter_stats.iloc[i].reverse

        arrayf1 = fighter_stats.iloc[i].values
        print (arrayf1)
        arrayf2_index = list(fighter_stats[(fighter_stats.concat == linereverse) & (fighter_stats.reverse == lineconcat)].index)
        print (arrayf2_index)

        if len(arrayf2_index) == 0:
            continue
        elif len(arrayf2_index) > 1:
            continue 

        arrayf2 = fighter_stats.iloc[arrayf2_index].values[0]
        print (arrayf2)

        joined = np.concatenate((arrayf1, arrayf2))

        final_df.loc[len(final_df.index)] = joined
    
    # Drop columns
    final_df = final_df.drop(columns=['concat', 'reverse', 'concat2', 'reverse2', 'event_name2', '2fighter1', '2fighter2', 'outcome2', 'w2', 'l2', 'd2', 'nc2'])

    # Rename Columns 
    final_df = final_df.rename(columns = {'event_name1': 'event_name', 'outcome1': 'outcome', 'w1': 'win', 'l1': 'loss', 'd1': 'draw', 'nc1': 'no_contest'})
    
    
    return final_df


# In[85]:


# final_df = combined_ufc()


# In[86]:


# final_df.head()


# In[9]:


def get_ufc_combined_data():
    
    # imports
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    import os
   

    '''
    This function checks for a local csv file and reads it into a pandas dataframe, if it exists. 
    If not, it uses a function to request the data and write it locally to a csv file.
    '''
    # If csv file exists locally, read in data from csv file.
    if os.path.isfile('UFC_Fighters_Combined.csv'):
        df = pd.read_csv('UFC_Fighters_Combined.csv', index_col=0)
        
    else:
        
        # read data from original csv
        df = combined_ufc()
        
        # Cache data
        df.to_csv('UFC_Fighters_Combined.csv')
        
    return df


# In[87]:


# df = get_ufc_combined_data()


# In[88]:


# df.head(1)


# In[46]:


def ufc_stats_difference():
    ''' 
    This function: 
    reads csv
    calculates the difference in stats between fighter1 and fighter2
    saves difference to new column
    creates df with desired difference columns
    returns a df with fighter1 and fighter2 and the difference between fighter1 and fighter2's stats as fighter_stat_diff
    also returns df with the fighter1 and fighter2 individual stats remaining as final_df
    '''
    
    # imports
    import pandas as pd
    import numpy as np
    # Ignore Warnings
    import warnings
    warnings.filterwarnings("ignore")
    
    # read .csv
    ufc = pd.read_csv('UFC_Fighters_Combined.csv')
    
    # Calculate the difference in stats between fighter1 and fighter2. Save to new column. 
    final_df['weight_diff'] = final_df.weight_f1 - final_df.weight_f2
    final_df['reach_diff'] = final_df.reach_f1 - final_df.reach_f2
    final_df['strike_diff'] = final_df.strikes_f1 - final_df.strikes_f2
    final_df['strike_acc_diff'] = final_df.strike_acc_f1 - final_df.strike_acc_f2
    final_df['strikes_absorbed_diff'] = final_df.strikes_absorbed_f1 - final_df.strikes_absorbed_f2
    final_df['strikes_defense_diff'] = final_df.strike_defense_f1 - final_df.strike_defense_f2
    final_df['strikes_defense_diff'] = final_df.strike_defense_f1 - final_df.strike_defense_f2
    final_df['takedown_attempts_diff'] = final_df.takedowns_f1 - final_df.takedowns_f2
    final_df['takedown_acc_diff'] = final_df.takedown_acc_f1 - final_df.takedown_acc_f2
    final_df['takedown_defense_diff'] = final_df.takedown_def_f1 - final_df.takedown_def_f2
    final_df['submission_attempt_diff'] = final_df.sub_attempt_f1 - final_df.sub_attempt_f2
    final_df['age_diff'] = final_df.age_days_f1 - final_df.age_days_f2
    final_df['height_diff'] = final_df.height_in_f1 - final_df.height_in_f2

    # Change data types
    final_df['strike_acc_diff'] = final_df.strike_acc_diff.astype(float) 
    final_df['strikes_defense_diff'] = final_df.strikes_defense_diff.astype(float)
    final_df['takedown_acc_diff'] = final_df.takedown_acc_diff.astype(float) 
    final_df['takedown_defense_diff'] = final_df.takedown_defense_diff.astype(float) 
    final_df['age_diff'] = final_df.age_diff.astype(float) 
    final_df['height_diff'] = final_df.height_diff.astype(float) 
    
    # Create df with desired difference columns
    fighter_stat_diff = final_df[['event_name', 'fighter1', 'fighter2', 'outcome', 'stance_f1', 'stance_f2', 'weight_diff', 'reach_diff', 'strike_diff', 'strike_acc_diff', 'strikes_absorbed_diff', 'strikes_defense_diff', 'takedown_attempts_diff', 'takedown_acc_diff', 'takedown_defense_diff', 'submission_attempt_diff', 'age_diff', 'height_diff']].copy(0)
    
    return final_df, fighter_stat_diff


# In[89]:


# final_df, fighter_stat_diff = ufc_stats_difference()


# In[90]:


# fighter_stat_diff.head(1)


# In[91]:


# final_df.head(1)


# In[50]:


def get_ufc_stats_diff_data():
    
    # imports
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    import os
   

    '''
    This function checks for a local csv file and reads it into a pandas dataframe, if it exists. 
    If not, it uses a function to request the data and write it locally to a csv file.
    '''
    # If csv file exists locally, read in data from csv file.
    if os.path.isfile('UFC_Final.csv.csv'):
        df = pd.read_csv('UFC_Final.csv', index_col=0)
        
    else:
        
        # read data from original csv
        final_df, fighter_stat_diff = ufc_stats_difference()
        
        # Cache data
        fighter_stat_diff.to_csv('UFC_Final.csv')
        
    return fighter_stat_diff


# In[92]:


# df = get_ufc_stats_diff_data()


# In[93]:


# df.head()


# ## Split Data

# In[53]:


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


# In[94]:


# train, validate, test = train_validate_test_split(final_df)


# In[95]:


# train.head(1)


# In[96]:


# train, validate, test = train_validate_test_split(fighter_stat_diff)


# In[97]:


# train.head(1)


# In[58]:


#def get_prep_n_split_ufc_data():
    #''' 
    #This function runs get_n_prep_ufc and train_validate_test_split functions.
    #It takes in the original df and returns the split dfs train, validate, test (in that order).
    #'''
    
    # imports
    #import pandas as pd
    # Ignore Warnings
    #import warnings
    #warnings.filterwarnings("ignore")
    #from sklearn.model_selection import train_test_split
    
    
    #ufc_cleaned = get_n_prep_ufc()
    #train, validate, test = train_validate_test_split(ufc_cleaned)
    #return train, validate, test


# In[59]:


#train, validate, test = get_prep_n_split_ufc_data()


# In[60]:


#train.head(1)


# In[61]:


# train.shape


# In[62]:


# validate.shape


# In[63]:


# test.shape


# In[98]:


# train.dtypes


# ## Scale Data

# In[72]:


def split_tvt_into_variables(train, validate, test, target):

#    split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target, 'event_name','fighter1','fighter2',
                                    'stance_f1', 'stance_f2'])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target, 'event_name','fighter1','fighter2',
                                    'stance_f1', 'stance_f2'])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target, 'event_name','fighter1','fighter2',
                                    'stance_f1', 'stance_f2'])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test


# In[99]:


# train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test = split_tvt_into_variables(train, validate, test, target='outcome')


# In[100]:


# X_train.head()


# In[77]:


def Min_Max_Scaler(X_train, X_validate, X_test):
    """
    Takes in X_train, X_validate and X_test dfs with numeric values only
    Returns scaler, X_train_scaled, X_validate_scaled, X_test_scaled dfs 
    """
    
    #imports
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    import sklearn.preprocessing
    
    #Fit the thing
    scaler = sklearn.preprocessing.MinMaxScaler().fit(X_train)
    
    #transform the thing
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), index = X_train.index, columns = X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index = X_validate.index, columns = X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index = X_test.index, columns = X_test.columns)
    
    return scaler, X_train_scaled, X_validate_scaled, X_test_scaled


# In[101]:


# scaler, X_train_scaled, X_validate_scaled, X_test_scaled = Min_Max_Scaler(X_train, X_validate, X_test)


# In[102]:


# X_train_scaled.head()


# In[103]:


# X_train_scaled.shape


# In[104]:


# X_validate_scaled.shape


# In[105]:


# X_test_scaled.shape


# In[ ]:




