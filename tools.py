import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches

def load_merge_header_and_production_csv(headerCSV, productionCSV):
    # Load header data
    headerDF = pd.read_csv(headerCSV, dtype={'API/UWI': str})

    # Convert date columns to datetime
    date_columns = [col for col in headerDF.columns if 'date' in col.lower()]
    headerDF[date_columns] = headerDF[date_columns].apply(pd.to_datetime, errors='coerce')

    # Force certain columns to be float
    float_columns = ['BE Oil EUR', 'BE Oil EUR NORM 10kft', 
                     'BE Oil Delta EUR', 'BE Oil Delta EUR Percent', 
                     'BE Gas EUR', 'BE Oil GAS NORM 10kft', 
                     'BE Gas Delta EUR', 'BE Gas Delta EUR Percent', 
                     'BE B-Factor', 'BE Initial Rate',
                     'BE Final Rate', 'BE Initial Decline', 
                     'BE Oil RRR', 'BE Gas RRR', 
                     'Perforated Interval Length']

    headerDF[float_columns] = headerDF[float_columns].apply(pd.to_numeric, errors='coerce')

    # Load time-series data
    timeSeriesDF = pd.read_csv(productionCSV, dtype={'API/UWI': str})

    # Drop unneeded columns
    timeSeriesDF = timeSeriesDF.drop(['Entity ID', 'API/UWI List', 'Days'], axis=1)

    # Convert production date to datetime
    timeSeriesDF['Production Date'] = pd.to_datetime(timeSeriesDF['Production Date'])

    # Merge header data and timeseries data
    wellDF = pd.merge(timeSeriesDF, headerDF, on='API/UWI', how='right')
    wellDF['Production Date'] = pd.to_datetime(wellDF['Production Date'])
    wellDF['API/UWI'] = wellDF['API/UWI'].astype(str)

    print('%i wells available' % len(set(wellDF['API/UWI'])))

    return wellDF

def add_BOE_per_day_column(wellDF):
    wellDF['BOE per day'] = ((wellDF['Liquid (bbl)'] + (wellDF['Gas (mcf)'] / 6.0)) / wellDF['Perforated Interval Length']) * 10000 / 30.4
    return wellDF

def swap_production_dates_for_time_delta(wellDF):
    for api in set(wellDF['API/UWI']):
        subset = wellDF[wellDF['API/UWI'] == api]
        peak_date = subset.loc[subset['Liquid (bbl)'].idxmax()]['Production Date']
        wellDF.loc[subset.index, 'Time Delta'] = subset['Production Date'] - peak_date

    return wellDF

def current_selection(dataFrame):
    print('You currently have these wells selected:')
    allWells = list(set(dataFrame['API/UWI']))
    
    for i, well in enumerate(allWells):
        print('%i -- %s' % (i, well))

    print('%i wells selected' % len(allWells))

def handle_numerical_variables(dataFrame, colName):
    print('\nThe remaining wells in your selection have the following details for the column "%s"\n(Note: missing data is excluded): ' % colName)
    print(dataFrame[colName].dropna().describe())

    print('\nYou have the following options for this variable "%s":' % colName)
    print("\n  1 -- greater than or equal to [>=]\n  2 -- less than or equal to [<=]\n  3 -- equal to [==]\n  4 -- between x0 and x1 [x0 < variable < x1]")

    selection = input('\nSelect how you would like to subset the data based on the variable "%s": ' % colName)

    while selection not in ('1', '2', '3', '4'):
        selection = input('Please select 1, 2, 3, or 4: ')

    if selection == '1':
        criteria = float(input('\nSelect all wells with "%s" >= ' % colName))
        dataFrame = dataFrame[dataFrame[colName] >= criteria]

    if selection == '2':
        criteria = float(input('\nSelect all wells with "%s" <= ' % colName))
        dataFrame = dataFrame[dataFrame[colName] <= criteria]

    if selection == '3':
        criteria = float(input('\nSelect all wells with "%s" == ' % colName))
        dataFrame = dataFrame[dataFrame[colName] == criteria]

    if selection == '4':
        limits = input('\nSelect all wells with "%s" between the following values: <lower limit, upper limit> ' % colName)
        limits = [float(x.strip()) for x in limits.split(',')]
        dataFrame = dataFrame[(dataFrame[colName] >= limits[0]) & (dataFrame[colName] <= limits[1])]

    return dataFrame

# Define other helper functions here (handle_dateTime_variables, handle_object_variables, plot_map, decline_curve, fit_decline_curve, nominal_decline)

# Main script
if __name__ == "__main__":
    headerCSV = './data/Well_header_data.csv'
    productionCSV = './data/Production_Time_Series.CSV'

    wellDF = load_merge_header_and_production_csv(headerCSV, productionCSV)
    wellDF = add_BOE_per_day_column(wellDF)
    wellDF = swap_production_dates_for_time_delta(wellDF)

    # Call other functions as needed for your analysis

    current_selection(wellDF)

    # Plot map example
    # plot_map(wellDF[['API/UWI', 'Surface Latitude (WGS84)', 'Surface Longitude (WGS84)', 'Cum Oil']], userLocation=None)

    # Fit decline curve example
    # fit_decline_curve(wellDF)
