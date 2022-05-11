import numpy as np
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join('../')))




    """
        Functions for cleaning padas data from frame
    """

    def __init__(self):
        pass



    def percent_missing_values(self,df):
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()
        totalMissing = missingCount.sum()
        print("The Telecom dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")
    
    
    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """drop duplicate rows
        Args:
            df (pd.DataFrame): pandas data frame
        Returns:
            pd.DataFrame: pandas data frame
        """
        df.drop_duplicates(inplace=True)
        return df
        
    
    def fixLabel(self, label: list) -> list:
        """convert list of labels to lowercase separated by underscore
        Args:
            label (list): list of labels 
        Returns:
            list: list of labels in lower case, separated by underscore
        """
        label = label.strip()
        label = label.replace(' ', '_').replace('.', '').replace('/', '_')
        return label.lower()
    
    def columns_too_much_null(self, df: pd.DataFrame, percentage: int) -> pd.DataFrame:
        """drops columns with big persentage of null values
        Args:
            df (pd.DataFrame): pandas data frame
            percentage (int): persentage of null values
        Returns:
            [type]: pandas data frame columns dropped
        """
        columns = []
        for index, row in df.iterrows():
            if float(row["none_percentage"].replace("%", '')) > percentage:
                columns.append(index)

        return columns
    
    # Function to calculate missing values by column
    def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
    
        # Percentage of missing values
        mis_val_percent = 100 * mis_val / len(df)
    
        # dtype of missing values
        mis_val_dtype = df.dtypes
    
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)
    
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns= {0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})
        # Sort the table by percentage of missing descending and remove columns with no missing values
        mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,0] != 0].sort_values(
                '% of Total Values', ascending=False).round(2)

        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

        if mis_val_table_ren_columns.shape[0] == 0:
            return

        # Return the dataframe with missing information
        return mis_val_table_ren_columns
    
    def fix_missing_bfill(df, columns):
        for col in columns:
             df[col] = df[col].fillna(method='bfill')
        return df[col]
    
    def fix_missing_ffill(df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(method='ffill')
        return df
    
    def fill_with_mode(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].mode()[0])
        return df
    
    def fix_missing_value(df, col, value):
        count = df[col].isna().sum()
        df[col] = df[col].fillna(value)
        if type(value) == 'str':
            print(f"{count} missing values in the column {col} have been replaced by '{value}'.")
        else:
            print(f"{count} missing values in the column {col} have been replaced by {value}.")
        return df[col]
    
    def convert_to_datetime( df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to datetime
        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels
        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = pd.to_datetime(df[col])
        return df

    def convert_to_string(df, columns):
        for col in columns:
            df[col] = df[col].astype("string")
            
    def convert_to_int(df, columns):
        for col in columns:
            df[col] = df[col].astype('int64')
        return df