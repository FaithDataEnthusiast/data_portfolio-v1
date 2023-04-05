import pandas as pd


def removing_duplicate_data(df):
    if df.duplicated().sum() > 0:
        print("_" * 50)
        print('Number of duplicates rows:', df.duplicated().sum())
        print("_" * 50)
        df_clean = df.drop_duplicates(keep='first')
        print('Duplicated rows have been deleted leaving the first instance in place')
        print("This table now contains rows :", df_clean.shape[0])
        print("_" * 50)
        return df_clean
    else:
        print('No duplicates found')

# def convert_datatype_to_datetime(df, variable):
#   print('Initial datatype of column of interest was:', df[variable].dtype)
#  df[variable] = pd.to_datetime(df[variable], format="%Y-%m-%d")
# print('Duplicated rows have been deleted leaving the first instance in place. The new data type is :', df[variable].dtype)
# return df[variable]
