import pandas as pd
import datetime as dt

def dockless_data_pipeline(data):
    '''
    Take a pandas dataframe and construct the data as part of the pipeline for dockless scooter data
        Arguments:
            data (pandas DataFrame): DataFrame used for the data pipeline
            columns_to_drop (string list):    Columns to drop from the dataframe
        Returns:
            pandas dataframe with the dropped columns
    """
    '''

    '''
    Initial Analysis of the Scooter Data revealed that are 46695 rows are null out of 2746505 rows. 
    Out of them 2088 of them have either Origin Cell ID or Destination Cell ID has 'OUT_OF_BOUNDS' 
    value. I will be follow up with City of Austin transportation department regarding null values. 
    For the first pass I will be deleting all the rows which have 'OUT_OF_BOUNDS' in the Origin or 
    Destination Cell ID as it is required for the data analysis
    '''
    '''
    Remove all the data that is not Scooter data.
    Remove all the data which does not have Origin Cell ID or Destination Cell ID
    Remove all the data 
    '''
    data.drop(data.index[(data['Origin Cell ID'] == 'OUT_OF_BOUNDS') 
                          | (data['Destination Cell ID'] == 'OUT_OF_BOUNDS')], inplace = True)
    data.drop(data.index[(data['Vehicle Type'] != 'scooter')], inplace = True)
    data.drop(data.index[(data['Origin Cell ID'].isnull()) | (data['Destination Cell ID'].isnull())], inplace = True)
    data.drop(data.index[(data['Start Latitude'].isnull()) | (data['End Latitude'].isnull())], inplace = True)
    
    # After all the null data removal drop the columns which are not required
    mobility_columns_to_drop = ['ID', 'Device ID', 'Vehicle Type', 'Modified Date']

    # Convert the datetime columns
    data['Start Time'] = data['Start Time'].apply(lambda x: dt.datetime.strptime(x,'%m/%d/%Y %I:%M:%S %p'))
    data['End Time'] = data['End Time'].apply(lambda x: dt.datetime.strptime(x,'%m/%d/%Y %I:%M:%S %p'))

    # Create START_DATE and END_DATE so they can be merged with Weather Data
    data['START_DATE'] = data['Start Time'].dt.date
    data['END_DATE'] = data['End Time'].dt.date

    # Convert the month, hour, Day of Week, Council District(Start, End), Year to integers instead of floats
    int_columns = ['Month', 'Hour', 'Day of Week', 'Council District (Start)', 'Council District (End)', 'Year']
    data[int_columns] = data[int_columns].astype(int)

    data['count'] = 1

    '''
    Trip duration - UOM in seconds, Trip distance - UOM in meters, 
    Month - where 1 = January, etc., 
    Hour - The hour of the day during which trip occurred, in local time (US/Central), 
    Day of Week - where Sunday = 0, and so on,¶
    '''

    data.drop(mobility_columns_to_drop, axis=1, inplace=True)
    data = data.set_index('Start Time')
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
    data.rename(columns={'AWND': 'AVG_DAILY_WIND_SPEED', 'PRCP': 'PRECIPITATION','TAVG': 'AVG_TEMPERATURE', 'TMAX': 'MAX_TEMPERATURE','TMIN': 'MIN_TEMPERATURE' }, inplace=True)
    # Convert the date in weather dataframe to datetime object

    data['DATE'] = data['DATE'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d'))
    # Convert it to Date
    data['DATE'] = data['DATE'].dt.date
    '''
    Weather Data Details. Precipitation - Units of Measure -  inches, 
    Snow - Units of Measure - inches, 
    Avg_Daily_Wind_Speed - Units of Measure - MPH, 
    AVG_TEMPERATURE, MAX_TEMPERATURE, MIN_TEMPERATURE- Units of Measure - Degrees Fahrenheit
    '''
    data.set_index('DATE')
    #data = data.drop(['index'], axis=1)
    return data

def find_top_group_by_column_list(data, group_by_column, sort_by_column, agg_column, n=10):
    grouped_origin_cell_id = data.groupby([group_by_column]).agg(agg_column)
    grouped_origin_cell_id = grouped_origin_cell_id.sort_values([sort_by_column], ascending=False)
    top_origin_cell_ids = grouped_origin_cell_id[sort_by_column]
    top_origin_cell_ids = top_origin_cell_ids.to_frame().reset_index()
    top_n_origin_cells = top_origin_cell_ids.head(n)
    top_10_origin_cells = top_n_origin_cells[0:n]
    top_10_origin_cells = top_10_origin_cells[group_by_column].values
    top_10_origin_cells_list = top_10_origin_cells.tolist()
    return top_10_origin_cells_list

def remove_invalid_trips(dockless_data):
    dockless_data = dockless_data[(dockless_data['Trip Distance'] > 1609.34) & (dockless_data['Trip Distance'] < 804673)]
    dockless_data = dockless_data[(dockless_data['Trip Duration'] > 60) & (dockless_data['Trip Duration'] < 86400)]
    return dockless_data

def prepare_cell_data(dockless_data, weather_data, cell_id):
    origin_cell_data = dockless_data[['Origin Cell ID', 'count']]

    # Hardcoded Cell ID '014391'
    ind_cell_data = origin_cell_data[origin_cell_data['Origin Cell ID'] == cell_id]

    trip_counts_cell = ind_cell_data.groupby([ind_cell_data.index.get_level_values(0),'Origin Cell ID']).count()
    trip_counts_cell = trip_counts_cell.unstack(level=1)
    trip_counts_cell = trip_counts_cell.fillna(0)

    # # Make a regular dataframe for processing the Time Series
    t2 = trip_counts_cell.reset_index()['count']
    # Hardcoded Cell ID '014391'
    counts = t2[cell_id].values
    data = {'Start Time':trip_counts_cell.index.values, 'Trip Counts':counts} 
    trip_counts_cell_data = pd.DataFrame(data)
    trip_counts_cell_data = trip_counts_cell_data.set_index("Start Time")

    # Remove the data which is inconsistent 
    trip_counts_cell_data = trip_counts_cell_data[(trip_counts_cell_data.index > '2018-07-15')]
    trip_counts_cell_data = trip_counts_cell_data[(trip_counts_cell_data.index < '2019-01-15')]

    data_cell_data_hour = trip_counts_cell_data.resample('H', how='sum')
    data_cell_data_hour = data_cell_data_hour.fillna(0)

    # Do the resampling before you add all the features

    data_cell_data_hour['MONTH'] = pd.DatetimeIndex(data_cell_data_hour.index).month
    data_cell_data_hour['YEAR'] = pd.DatetimeIndex(data_cell_data_hour.index).year
    data_cell_data_hour['HOUR'] = pd.DatetimeIndex(data_cell_data_hour.index).hour
    data_cell_data_hour['DAY'] = pd.DatetimeIndex(data_cell_data_hour.index).day
    data_cell_data_hour['WEEK'] = pd.DatetimeIndex(data_cell_data_hour.index).week
    data_cell_data_hour['DAY_OF_WEEK'] = pd.DatetimeIndex(data_cell_data_hour.index).weekday
    data_cell_data_hour['WEEKEND'] = ((pd.DatetimeIndex(data_cell_data_hour.index).weekday) // 5 == 1).astype(float)
    data_cell_data_hour['WEEKDAY'] = ((pd.DatetimeIndex(data_cell_data_hour.index).weekday) // 5 == 0).astype(float)
    data_cell_data_hour['DATE'] = pd.DatetimeIndex(data_cell_data_hour.index).date
    hours=[0, 6, 10, 15, 19, 23]
    data_cell_data_hour['HOUR_LABEL'] = pd.cut(data_cell_data_hour['HOUR'], hours, include_lowest=True, right=True, labels=['0', '1', '2', '3', '4'])
    data_cell_data_hour = data_cell_data_hour.reset_index().merge(weather_data, on='DATE', how="left").set_index('Start Time')
    data_cell_data_hour = data_cell_data_hour.drop(['DATE'], axis=1)


    return data_cell_data_hour

if __name__ == '__main__':
    # Read the dockless data from S3 bucket
    # Load the data and and call the clean method automatically to call the work flow
    dockless_data = pd.read_csv("https://s3.amazonaws.com/sameera-bucket-1/dockless_mobility/raw_data/Austin_Dockless_Vehicle_Trips.csv")
    dockless_vehicles_columns = dockless_data.columns
    print_eda_stats(dockless_data, dockless_vehicles_columns, "Austin Dockless Mobility Data")
    # Call the dockless_data_pipeline()
    dockless_data_pipeline(dockless_data)
    dockless_vehicles_columns = dockless_data.columns
    print_eda_stats(dockless_data, dockless_vehicles_columns, "Austin Dockless Mobility Data")

    #Read the weather data from S3 bucket
    weather_data = pd.read_csv("https://s3.amazonaws.com/sameera-bucket-1/dockless_mobility/raw_data/Austin_Bergstom_Airport_Weather.csv")
    weather_columns = weather_data.columns
    print_eda_stats(weather_data, weather_columns, "Austin Weather Data")
    weather_data_pipeline(weather_data)
    weather_columns = weather_data.columns
    print_eda_stats(weather_data, weather_columns, "Austin Weather Data")



