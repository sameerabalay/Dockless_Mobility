import pandas as pd

def dockless_data_pipeline(data, columns_to_drop):
    '''
    Take a pandas dataframe and construct the data as part of the pipeline for dockless scooter data
        Arguments:
            data (pandas DataFrame): DataFrame used for the data pipeline
            columns_to_drop (string list):    Columns to drop from the dataframe
        Returns:
            pandas dataframe with the dropped columns
    """
    '''

    data.drop(columns_to_drop, axis=1, inplace=True)

    return data

def weather_data_pipeline(data):
    '''
    TTake a pandas dataframe and construct the data as part of the pipeline for austin weather data
        Arguments:
            data (pandas DataFrame): DataFrame used for the data pipeline
            columns_to_drop (string list):    Columns to drop from the dataframe
        Returns:
            pandas dataframe with the dropped columns
    """
    '''
    weather_columns_to_drop = ['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION',
       'AWND_ATTRIBUTES', 'PGTM', 'PGTM_ATTRIBUTES', 'PRCP_ATTRIBUTES',
       'SNOW_ATTRIBUTES', 'SNWD', 'SNWD_ATTRIBUTES',
       'TAVG_ATTRIBUTES', 'TMAX_ATTRIBUTES', 'TMIN_ATTRIBUTES',
       'WDF2', 'WDF2_ATTRIBUTES', 'WDF5', 'WDF5_ATTRIBUTES', 'WSF2',
       'WSF2_ATTRIBUTES', 'WSF5', 'WSF5_ATTRIBUTES', 'WT01', 'WT01_ATTRIBUTES',
       'WT02', 'WT02_ATTRIBUTES', 'WT03', 'WT03_ATTRIBUTES', 'WT04',
       'WT04_ATTRIBUTES', 'WT05', 'WT05_ATTRIBUTES', 'WT06', 'WT06_ATTRIBUTES',
       'WT08', 'WT08_ATTRIBUTES']
    data.drop(weather_columns_to_drop, axis=1, inplace=True)
    # Initial Analysis of the weather data revealed some null values of the data. 
    # The data was not available for the day the data was downloaded and also there 
    # was an additional missing values. Both '2019-03-01' and '2019-03-02' 
    # had missing TAVG data. From the current analysis I concluded the data was missing 
    # at random (MAR) so decided to impede the null values with the data from 
    # the previous record.
    # Fill the data from the previous record using 'ffill' method on pandas dataframe
    data.fillna(method='ffill', inplace=True)
    return data