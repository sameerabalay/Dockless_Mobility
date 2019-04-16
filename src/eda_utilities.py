import pandas as pd
from prettytable import PrettyTable

def print_eda_stats(df, column_list, table_title=""):
    '''
    Takes a list of columns to print summary statistics 
        Arguments:
            df (pandas DataFrame): DataFrame used to print the summary statistics
            columns_list (string list):    Columns used for summary statistics
            table_title (string): Title of the table
        Returns:
        Nothing
    """
    '''
    
    df_total_rows = df.shape[0]
    t = PrettyTable(['Column Name', 'dtype', 'Total_Count', 'Unique_Values', 'df_totalrows', 'Null Value counts'])
    t.title = table_title
    for val in column_list:
        t.add_row([val, df[val].dtype, df[val].count(), len(df[val].unique()), df_total_rows, (df_total_rows - df[val].count()) ])
    print(t)
