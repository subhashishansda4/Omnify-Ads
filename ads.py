# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 03:16:31 2022

@author: VAGUE
"""

import pandas as pd
import numpy as np

# DATA ANALYSIS
# -----------------------------------------------------------------------------
# Google Ads
# checking columns
print('')
print('Google_Ads')
google_ads = pd.read_csv('google_ads.csv')
print(google_ads.columns)
# unique values
campaign_gs = google_ads['Campaign'].unique()
ad_group_gs = google_ads['Ad group'].unique() #no use since we have both search keyword and keyword type
search_keyword_gs = google_ads['Search Keyword'].unique() #consists of rubbish and null values
currency_gs = google_ads['Currency'].unique() #no use since only one variable
country_gs = google_ads['Country'].unique() #no use since only one variable
keyword_type_gs = google_ads['Keyword type'].unique()
payment_gs = google_ads['Payment ($)'].unique()
payment_date_gs = google_ads['Payment Date'].unique()
week_gs = google_ads['Week'].unique()

# Listing Site
# checking columns
print('')
print('Listing_Site')
listing_site = pd.read_csv('listing_site.csv')
print(listing_site.columns)
# unique values
product_name_ls = listing_site['Product Name'].unique() #no use since only one variable
categories_ls = listing_site['Categories'].unique()
channel_ls = listing_site['Channel'].unique()
location_ls = listing_site['Location'].unique() #consists of duplicate values
date_report_ls = listing_site['Date of Report'].unique()

# Statistical Analysis
google_ads_stats = google_ads.describe()
listing_site_stats = listing_site.describe()
# -----------------------------------------------------------------------------

# DATA CLEANING
# -----------------------------------------------------------------------------
# Google Ads
# dataframe for null and rubbish values in search keyword
search_keyword_null = google_ads.loc[google_ads['Ad group'] == 'Pool_Reservation_Software_Open_Broad']

# removing rubbish and null values
clean_google_ads = pd.read_csv('google_ads.csv')
clean_google_ads.drop(clean_google_ads.index[clean_google_ads['Ad group'] == 'Pool_Reservation_Software_Open_Broad'], inplace=True)
clean_google_ads.drop(['Currency', 'Country', 'Ad group'], axis = 1, inplace = True)
clean_google_ads['Payment ($)'] = clean_google_ads['Payment ($)'].replace(np.nan, '0')
clean_google_ads['Payment Date'] = clean_google_ads['Payment Date'].replace(np.nan, '0')
# clean column ['Search Keyword']
clean_search_keyword_gs = clean_google_ads['Search Keyword'].unique()
# deleting columns with no data


# statistical analysis
clean_google_ads_stats = clean_google_ads.describe()
# dataframe to csv
clean_google_ads.to_csv('clean_google_ads.csv')

# Listing Site
clean_listing_site = pd.read_csv('listing_site.csv')
# removing duplicate values
# USA
clean_listing_site['Location'] = clean_listing_site['Location'].replace(['UNITED STATES', 'USA', 'US', 'United States'], 'USA')
# UK
clean_listing_site['Location'] = clean_listing_site['Location'].replace(['UNITED KINGDOM', 'UK', 'United Kingdom'], 'UK')
# Singapore
clean_listing_site['Location'] = clean_listing_site['Location'].replace(['SINGAPORE', 'Singapore'], 'Singapore')
# Australia
clean_listing_site['Location'] = clean_listing_site['Location'].replace(['AUSTRALIA', 'Australia'], 'Australia')
# Canada
clean_listing_site['Location'] = clean_listing_site['Location'].replace(['CANADA', 'Canada'], 'Canada')
clean_listing_site.drop(['Product Name'], axis = 1, inplace = True)
# replacing nan values with 0
clean_listing_site['Leads'] = clean_listing_site['Leads'].replace(np.nan, '0')
clean_listing_site['Prospects'] = clean_listing_site['Prospects'].replace(np.nan, '0') 
# clean column ['Location']
clean_location_ls = clean_listing_site['Location'].unique()

# statistical analysis
clean_listing_site_stats = clean_listing_site.describe()
# dataframe to csv
clean_listing_site.to_csv('clean_listing_site.csv')
# -----------------------------------------------------------------------------

# DATA PROCESSING
# -----------------------------------------------------------------------------

