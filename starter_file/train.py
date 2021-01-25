# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:56:16 2021

@author: PC-Fujitsu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 14:03:26 2021

@author: PC-Fujitsu
""" 

#Import needed libraries:
import pre_preprocess as pp
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from azureml.core.run import Run
import argparse
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

#-----------------------------------------------------------------------------
#Import data:
data = pp.load_data('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')

#-----------------------------------------------------------------------------
#Clean Data
#Define clean data function
def clean_data(df):

    df = pp.replace_question_marks(df)
    
    df['cabin'] = df['cabin'].apply(pp.get_first_cabin)
    
    df['title'] = df['name'].apply(pp.get_title)
    
    # cast numerical variables as floats
    df['fare'] = df['fare'].astype('float')
    df['age'] = df['age'].astype('float')
    
    # drop unnecessary variables
    df.drop(labels=['name','ticket', 'boat', 'body','home.dest'], axis=1, inplace=True)
    
    #Define Target Variable:
    target = 'survived'
    
    #Extract only the letter (and drop the number) from the variable Cabin:
    df['cabin'] = df['cabin'].str[0] # captures the first letter
    df['cabin'] = df['cabin'].str[0] # captures the first letter
    
    
    # - Fill in Missing data in numerical variables:
        #- Add a binary missing indicator
        #- Fill NA in original variable with the median
    
    for var in ['age', 'fare']:
    
        # add missing indicator
        df[var+'_NA'] = np.where(df[var].isnull(), 1, 0)
    
        # replace NaN by median
        median_val = df[var].median()
    
        df[var].fillna(median_val, inplace=True)
    
    #Divide the variables in numerical and categorical
    vars_num = [c for c in df.columns if df[c].dtypes!='O' and c!=target]
    
    vars_cat = [c for c in df.columns if df[c].dtypes=='O']
    
    
    # - Replace Missing data in categorical variables with the string Missing
    df[vars_cat] = df[vars_cat].fillna('Missing')
    
    # - Remove rare labels in categorical variables:
    for var in vars_cat:
        
        # find the frequent categories
        frequent_ls = pp.find_frequent_labels(df, var, 0.05)
        
        # replace rare categories by the string "Rare"
        df[var] = np.where(df[var].isin(
            frequent_ls), df[var], 'Rare')
        
    for var in vars_cat:
        
        # to create the binary variables, we use get_dummies from pandas
        
        df = pd.concat([df,pd.get_dummies(df[var], prefix=var, drop_first=True)],
                       axis=1)
    
    #Drop the original labels:
    df.drop(labels=vars_cat, axis=1, inplace=True)
    
    #Prepare the independent variables and the dependent one
    x_df = df.drop('survived',axis=1)
    y_df = df.survived
    
    return x_df, y_df

x, y = clean_data(data)

#-----------------------------------------------------------------------------
# create scaler
variables = x.columns.tolist()

scaler = StandardScaler()
scaler.fit(x[variables]) 

x = scaler.transform(x[variables])
#-----------------------------------------------------------------------------
#Split the data

x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                    test_size = 0.2,
                                                    random_state=0)

run = Run.get_context()

#Define the main class

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")
    parser.add_argument('--penalty', type=str, default='l2', help="Specify the norm used in the penalization")
    parser.add_argument('--solver', type=dict, default= 'lbfgs', help="Algorithm to use in the optimization problem")
    

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))
    run.log("Penalization:", args.penalty)
    run.log("Algorithm Solver:", args.solver)

    model = LogisticRegression(C=args.C, 
                               max_iter=args.max_iter,
                               penalty=args.penalty,
                               solver=args.solver
                               ).fit(x_train, y_train)

    
    
    # make predictions for test set
    pred = model.predict_proba(x_test)[:,1]
    rocAucScore = roc_auc_score(y_test, pred)
    
    run.log("roc-auc", rocAucScore)

if __name__ == '__main__':
    main()

























#----------------------------------------------------------------------------
#Next Steps:
# - Import the above created functions and afterwards:    
# - cast numerical variables as floats
# - drop unnecessary variables
# - Extract only the letter (and drop the number) from the variable Cabin
# - Fill in Missing data in numerical variables:
    #- Add a binary missing indicator
    #- Fill NA in original variable with the median
# - Divide the variables in numerical and categorical
# - Replace Missing data in categorical variables with the string Missing
# - Remove rare labels in categorical variables
# - Encode the categorical variables
# - Scale the variables
# - Split Data in Train/Test
# - Train the Logistic Regression model

