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
search_keyword_gs = google_ads['Search Keyword'].unique()
currency_gs = google_ads['Currency'].unique() #no use since only one variable
country_gs = google_ads['Country'].unique() #no use since only one variable

# Listing Site
# checking columns
print('')
print('Listing_Site')
listing_site = pd.read_csv('listing_site.csv')
print(listing_site.columns)
# unique values
categories_ls = listing_site['Categories'].unique()
channel_ls = listing_site['Channel'].unique()
location_ls = listing_site['Location'].unique()

# Statistical Analysis
print('')
print('Stats for Google_Ads')
google_ads_stats = google_ads.describe()
print('Stats for Listing Site')
listing_site_stats = listing_site.describe()
# -----------------------------------------------------------------------------

# DATA CLEANING
# -----------------------------------------------------------------------------
# Google Ads
# dataframe for null and rubbish values in search keyword
search_keyword_null = google_ads.loc[google_ads['Ad group'] == 'Pool_Reservation_Software_Open_Broad']

# Removing Unwanted and Duplicate Categorical Variables
clean_google_ads = pd.read_csv('google_ads.csv')
clean_google_ads.drop(clean_google_ads.index[clean_google_ads['Ad group'] == 'Pool_Reservation_Software_Open_Broad'], inplace=True)
clean_google_ads.drop(['Currency', 'Country', 'Ad group'], axis = 1, inplace = True)
# clean column ['Search Keyword']
clean_search_keyword = clean_google_ads['Search Keyword'].unique()

# statistical analysis
clean_google_ads_stats = clean_google_ads.describe()
# dataframe to csv
clean_google_ads.to_csv('clean_google_ads.csv')

# Listing Site
