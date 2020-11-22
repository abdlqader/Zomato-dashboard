#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:59:31 2020

@author: abdulkader
"""
import pandas as pd

class df_proccess:
    def __init__(self):
        df = pd.read_csv('zomato/zomato.csv',encoding='latin-1')
        country_code_df = pd.read_excel('zomato/Country-Code.xlsx')
        self.dataframe = pd.merge(df,country_code_df,on='Country Code')
        self.standerdize_currency()
        self.cuisines_tolist()
        self.df_countries = None
        self.df_cuisines = None
        self.df_cost_rating = None
    
    def standerdize_currency(self):
        data = {'Currency':['Botswana Pula(p)','Brazilian Real(R$)','Dollar($)','Emirati Diram(AED)','Indian Rupees(Rs.)','Indonesian Rupiah(IDR)','NewZealand($)','Pounds(£)','Qatari Rial(QR)','Rand(R)','Sri Lankan Rupee(LKR)','Turkish Lira(TL)'],
        'Currency To Dollars':[11.08,5.74287,1,3.67,74.14,14210.10,1.3284,0.772346,3.64,16.2402,185.17,7.65]}
        currency_df = pd.DataFrame(data)
        self.dataframe = pd.merge(self.dataframe,currency_df, on='Currency')
        self.dataframe['Average Cost for two in dollars'] = self.dataframe['Average Cost for two']/self.dataframe['Currency To Dollars']
        
    def cuisines_tolist(self):
        self.dataframe['Cuisines'] = self.dataframe.Cuisines.apply(lambda x: '' if type(x) == float else x)
        self.dataframe['Cuisines List'] = self.dataframe.Cuisines.apply(lambda x:[x.strip() for x in x.split(',')])
        
    def count_rating_text_rest(self):
        new_df = self.dataframe['Rating text'].value_counts().reset_index()
        new_df.columns = ['Rating','Count']
        new_df['Percentage'] = new_df.Count.apply(lambda x: (x*100)/sum(new_df.Count))
        return new_df
    
    def count_cost_range_rating(self):
        new_df = self.dataframe['Rating text'].value_counts().reset_index()
        new_df.columns = ['Rating','Count']
        new_df['Percentage'] = new_df.Count.apply(lambda x: (x*100)/sum(new_df.Count))
        return new_df
    

    def make_df_cost_rating(self):
        def price_range_toStrings(x):
          if x == 1:
            return 'One'
          elif x == 2:
            return 'Two'
          elif x == 3:
            return 'Three'
          else:
            return 'Four'
        self.df_cost_rating = self.dataframe[['Price range','Aggregate rating','Rating text','Average Cost for two in dollars','Votes']]
        self.df_cost_rating['Price range text'] = self.df_cost_rating['Price range'].apply(lambda x : price_range_toStrings(x))
        return self.df_cost_rating
        
    def make_df_country(self):
        data_mean = self.dataframe[['Country','Average Cost for two in dollars']].groupby('Country').mean().reset_index()
        data_count = self.dataframe[['Country','Average Cost for two in dollars']].groupby('Country').count().reset_index()
        dict_cuisine = {'Country': [],
                'Count Cuisines' : []}
        for country in data_mean.Country:
            my_df = self.dataframe[self.dataframe['Country'] == country]
            count = set([i for x in my_df['Cuisines List'] for i in x])
            dict_cuisine['Country'].append(country)
            dict_cuisine['Count Cuisines'].append(len(count))
        data_total = pd.merge(data_mean,data_count,on='Country')
        self.df_countries = pd.merge(data_total,pd.DataFrame(dict_cuisine),on='Country')
        self.df_countries.columns = ['Country','Mean Cost for two in dollars','Count Restaurants','Count Cuisines']
        return self.df_countries
    
    def make_df_cuisine(self):
        dict_cuisine = {}
        dict_avg_cuisine = {}
        for i,Cuisines in enumerate(self.dataframe['Cuisines List']):
          for Cuisine in Cuisines:
            if Cuisine in dict_cuisine:
              dict_cuisine[Cuisine] += 1
              dict_avg_cuisine[Cuisine] += self.dataframe.iloc[i]['Average Cost for two in dollars']
            else:
              dict_cuisine[Cuisine] = 1
              dict_avg_cuisine[Cuisine] = self.dataframe.iloc[i]['Average Cost for two in dollars']
        self.df_cuisines = pd.DataFrame(data={'Cuisines':list(dict_cuisine.keys()),
                   'Count':list(dict_cuisine.values()),
                   'Sum':list(dict_avg_cuisine.values())}).sort_values('Count').reset_index(drop=True)
        self.df_cuisines['Average Cost for two in dollars'] = self.df_cuisines['Sum']/self.df_cuisines['Count']
        return self.df_cuisines
