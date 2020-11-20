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
    
    def standerdize_currency(self):
        data = {'Currency':['Botswana Pula(p)','Brazilian Real(R$)','Dollar($)','Emirati Diram(AED)','Indian Rupees(Rs.)','Indonesian Rupiah(IDR)','NewZealand($)','Pounds(£)','Qatari Rial(QR)','Rand(R)','Sri Lankan Rupee(LKR)','Turkish Lira(TL)'],
        'Currency To Dollars':[11.08,5.74287,1,3.67,74.14,14210.10,1.3284,0.772346,3.64,16.2402,185.17,7.65]}
        currency_df = pd.DataFrame(data)
        self.dataframe = pd.merge(self.dataframe,currency_df, on='Currency')
        self.dataframe['Average Cost for two in dollars'] = self.dataframe['Average Cost for two']/self.dataframe['Currency To Dollars']
        
    def avg_cost_per_country(self):
        return self.dataframe[['Country','Average Cost for two in dollars']].groupby('Country').mean().reset_index().sort_values('Average Cost for two in dollars',ascending=False)
    def count_rest_per_country(self):
        new_df = self.dataframe['Country'].value_counts().reset_index()
        new_df.columns = ['Country','Count']
        new_df
        return new_df
    def count_rating_text_rest(self):
        new_df = self.dataframe['Rating text'].value_counts().reset_index()
        new_df.columns = ['Rating','Count']
        new_df['Percentage'] = new_df.Count.apply(lambda x: (x*100)/sum(new_df.Count))
        return new_df
    
