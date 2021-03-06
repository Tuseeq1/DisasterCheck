import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """load data from csv files
    
    Parameters
    ----------
    messages_filepath : str
        Path to csv file to load message data
    categories_filepath : str
        Path to csv file to load categories data
    
    Returns
    -------
    DataFrame :
        combined dataframe from both files
       """
    
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df =  pd.merge(messages, categories, on="id")
    
    return df


def clean_data(df):
    """Clean the data in given data frame to appropriate structure
    
    Parameters
    ----------
    df : pandas.DataFrame
        data in dataframe
    
    Returns
    -------
    DataFrame :
        cleaned dataframe
       """
    
    # make genre column into seprate features
    dummies = pd.get_dummies(df['genre'], prefix='genre')
    df = pd.concat([df, dummies], axis=1)
    
    # create soperate column for each category 
    categories = df['categories'].str.split(';', expand=True)
    
    # select the first row of the categories dataframe
    row = df['categories'].loc[0].split(';')
    category_colnames = [col_name.split('-')[0] for col_name in row]
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: int(x[-1]))
    
    df = df.drop('categories', 1)
    df = pd.concat([df, categories], axis=1)
    
    # remove Duplicate
    df = df.drop_duplicates()
    
    # make all the 2s in related column to 1 to make it binary
    df['related'] = df['related'].replace([2],1)
    
    return df


def save_data(df, database_filename):
    """Save clean  data to .db file on given path
   
    Parameters
    ----------
    df : object
        trained model to test
    database_filename : str
        path where to save data
    """
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('Disaster', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()