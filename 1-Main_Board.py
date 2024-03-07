#Importing Libraries: 
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as ps
from plotly.subplots import make_subplots
import streamlit as st
import streamlit.components.v1 as comp
#Data Preprocessing:
Adidas = pd.read_excel(r"c:\Users\ooo\Downloads\archive(41)\Adidas US Sales Datasets.xlsx")
Adidas.drop_duplicates()
Adidas = Adidas.drop(Adidas.index[:3])
Adidas.drop("Unnamed: 0", axis = 1, inplace = True)
Adidas.columns = Adidas.iloc[0]
Adidas = Adidas.drop(Adidas.index[0])
Adidas =Adidas.reset_index(drop=True)
Adidas['Invoice Date']=pd.to_datetime(Adidas['Invoice Date'])
Adidas['Units Sold'] = Adidas['Units Sold'].astype("int")
Adidas[['Price per Unit', 'Total Sales','Operating Profit', 'Operating Margin']] = Adidas[['Price per Unit', 'Total Sales','Operating Profit', 'Operating Margin']].astype("float")
Adidas['Year'] = Adidas['Invoice Date'].dt.year
Adidas['Month'] = Adidas['Invoice Date'].dt.month
Adidas['Day'] = Adidas['Invoice Date'].dt.day
Adidas['Calendering Year'] = pd.cut(Adidas['Month'],2,labels=["First Half","Second Half"])
#Some definitions:
night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)','rgb(36, 55, 57)', 'rgb(6, 4, 4)']
blue_colors =  ['cyan','royalblue','darkblue','lightsalmon']
sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)','rgb(129, 180, 179)', 'rgb(124, 103, 37)']
irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)','rgb(175, 49, 35)', 'rgb(36, 73, 147)']
cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)','rgb(175, 51, 21)', 'rgb(35, 36, 21)']
labels = ['Foot Locker', 'Walmart', 'Sports Direct', 'West Gear', "Kohl's", 'Amazon']
values = [2637, 2374, 2032, 1030 ,949, 626]

city = Adidas['City'].value_counts().nlargest(10).reset_index()
city_histogram = px.histogram(city , x =  'City', y = 'count', color = 'City',color_discrete_sequence = blue_colors ,
                               title= 'Cities Took Large Market Area' , labels={"City": "",
                     "sum of count": "Count"}, width=400,height=450)

Method = Adidas['Sales Method'].value_counts().reset_index()
Method_bar =  px.bar(Method , x ='Sales Method' , y = 'count', color = 'Sales Method', color_discrete_sequence = blue_colors ,
                      title = 'Sales Method Strategy',labels={"Sales Method": "Sales Method",
                     "count": ""}, width=300,height=400)

Product = Adidas['Product'].value_counts().reset_index()
product_pie = px.pie(Product , names = 'Product', values ='count' , title = 'Categories Of Products Sales ',color_discrete_sequence = night_colors,width=400,height=400)

Retailer_pie = go.Figure(data=[go.Pie( labels=labels , values= values , marker_colors = px.colors.sequential.RdBu , pull=[0.3, 0.2, 0.1, 0 ,0, 0])])
Retailer_pie.update(layout_title_text='Retailers Share')

price_per_unit_year = Adidas.groupby(['Year','Month'])['Price per Unit'].mean().reset_index()
fig_price = px.line(price_per_unit_year , x = 'Month', y = 'Price per Unit', color = 'Year', color_discrete_map = {2020:'rgb(175, 49, 35)' , 2021:'rgb(36, 73, 147)'},
title= 'Average of prices 2020/2021' ,width=350,height=400, markers = True)

Method_Profit = Adidas.groupby(['Year','Sales Method'])['Operating Profit'].mean().reset_index()
Method_Profit_fig = px.histogram(Method_Profit , x = 'Sales Method' , y = 'Operating Profit' , color='Year' , title='AVG Of Profit Per Sale Method',
                                 color_discrete_sequence = blue_colors, width=300)

Retailers_profit_2020 = Adidas[Adidas['Year'] == 2020].groupby(['Year','Retailer'])['Total Sales'].sum().sort_values(ascending = False).reset_index()
Retailers_profit_2020_fig = px.bar(Retailers_profit_2020 , x ='Retailer' , y = 'Total Sales' ,
                            title='AVG  Of Profits By Each Retailer',
                            color_discrete_sequence = ['rgb(33, 75, 99)'] ,width=350)

Retailers_profit_2021 = Adidas[Adidas['Year'] == 2021].groupby(['Year','Retailer'])['Total Sales'].sum().sort_values(ascending = False).reset_index()
Retailers_profit_2021_fig = px.bar(Retailers_profit_2021 , x ='Retailer' , y = 'Total Sales' ,
                            title='AVG  Of Profits By Each Retailer',
                           color_discrete_sequence = ['rgb(151, 179, 100)'],width=350)

profit_track_2020 = Adidas[Adidas['Year'] == 2020].groupby(['Year','Month'])[['Price per Unit','Total Sales','Operating Margin']].agg({"Price per Unit":np.mean, "Total Sales":np.sum  , "Operating Margin":np.sum}).reset_index()
profit_track2020_fig = px.line(profit_track_2020, x = 'Month' , y = ['Price per Unit','Total Sales','Operating Margin'] ,
                               title='Tracking Prices , Total Sales And Margin Profits.',
                               color_discrete_map={'Price per Unit':'cyan','Total Sales':'orange','Operating Margin':'lightsalmon'})

profit_track_2021 = Adidas[Adidas['Year'] == 2021].groupby(['Year','Month'])[['Price per Unit','Total Sales','Operating Margin']].agg({"Price per Unit":np.mean, "Total Sales":np.sum  , "Operating Margin":np.sum}).reset_index()
profit_track2021_fig = px.line(profit_track_2021, x = 'Month' , y = ['Price per Unit','Total Sales','Operating Margin'] ,
                               title='Tracking Prices , Total Sales And Margin Profits.',
                               color_discrete_map={'Price per Unit':'rgb(151, 179, 100)','Total Sales':'rgb(175, 49, 35)','Operating Margin':'lightsalmon'})

profit_year = Adidas.groupby(['Year','Month'])['Operating Margin'].sum().reset_index()
profit_year_fig = px.line(profit_year , x = 'Month', y = 'Operating Margin', color = 'Year', color_discrete_map = {2020:'rgb(175, 49, 35)' , 2021:'lightsalmon'},
title= 'Profit over the years 2020 and 2021' , markers = True)

Total_Sales_year = Adidas.groupby(['Year','Month'])['Total Sales'].sum().reset_index()
Total_Sales_year_fig = px.line(Total_Sales_year , x = 'Month', y = 'Total Sales', color = 'Year', color_discrete_map = {2020:'rgb(175, 49, 35)' , 2021:'lightsalmon'},
title= 'Profits Of The Years 2020 And 2021' , markers = True)

city_state2020 = Adidas[Adidas['Year'] == 2020].groupby(['City','State'])['Operating Margin'].sum().sort_values(ascending=False).reset_index()
city_state2020_fig = px.bar(city_state2020, x = 'State', y = 'Operating Margin',
                            title='States Of High Margin Profit',
                            color_discrete_sequence = ['rgb(33, 75, 99)'],width=300 , height = 500)

city_state2021 = Adidas[Adidas['Year'] == 2021].groupby(['City','State'])['Operating Margin'].sum().nlargest(9).sort_values(ascending=False).reset_index()
city_state2021_fig = px.bar(city_state2021, x = 'State', y = 'Operating Margin',
                            title='States Of High Margin Profit',
                           color_discrete_sequence = ['rgb(151, 179, 100)'],width=300 , height = 470)

high_sales_cities = Adidas[(Adidas['City'] == 'Portland') |( Adidas['City'] == 'Charleston')]
Port_Char = high_sales_cities.groupby('City')['Sales Method'].value_counts().reset_index()
Port_Char_fig = px.sunburst(Port_Char, path=['City','Sales Method'] , values='count',
                            title = 'The Sales Method By PORT. & CHAR.',
                            color_discrete_sequence = px.colors.sequential.RdBu , width=400 , height= 450)

#Streamlit Code:
col1, col2 = st.columns(2)
with col1:
    st.header("Adidas Market on 2020/2021")
    tab1, tab2 , tab3 , tab4= st.tabs(["Overall" ,"Year-2020", "Year-2021","Insights"])
with col2:
   comp.iframe("https://lottie.host/embed/a5ccfbfe-91e5-4a4f-b5f4-dc6704cf1217/21ORN17YX3.json")
with tab1:
      col1, col2 ,col3, col4 , col5 ,col6 , col7, col8 ,col9,col10 , col11, col12 ,col13= st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1])
      with col1:
           st.plotly_chart(Method_bar)
      with col2:
           st.write("")
      with col3:
           st.write("")
      with col4:
           st.write("")
      with col5:
           st.write("")
      with col6:
           st.write("")
      with col7:
           st.write("")
      with col8:
           st.write("")
      with col9:
           st.write("")
      with col10:
           st.write("")
      with col11:
           st.write("")
      with col12:
           st.write("")
      with col13:
           st.plotly_chart(city_histogram)
      col1, col2 , col3, col4 , col5 , col6 ,col7,col8 ,col9,col10,col11, col12,col13,col14,col15 = st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
      with col1:
           st.plotly_chart(Method_Profit_fig)
      with col2:
           st.write("")
      with col3:
           st.write("")
      with col4:
           st.write("")
      with col5:
           st.write("")
      with col6:
           st.write("")
      with col7:
           st.write("")
      with col8:
           st.write("")
      with col9:
           st.write("")
      with col10:
           st.write("")
      with col11:
           st.write("")
      with col12:
           st.write("")
      with col13:
           st.write("")
      with col14:
           st.write("")
      with col15:
           st.plotly_chart(Port_Char_fig)
      st.plotly_chart(Retailer_pie)

with tab2:
      col1, col2 ,col3, col4 , col5 ,col6 , col7, col8 , col9, col10 , col11, col12 ,col13= st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1])
      with col1:
           st.plotly_chart(city_state2020_fig)
      with col2:
           st.write("")
      with col3:
           st.write("")
      with col4:
           st.write("")
      with col5:
           st.write("")
      with col6:
           st.write("")
      with col7:
           st.write("")
      with col8:
           st.write("")
      with col9:
           st.write("")
      with col10:
           st.write("")
      with col11:
           st.write("")
      with col12:
           st.write("")
      with col13:
           st.write("")
      with col13:
           st.plotly_chart(Retailers_profit_2020_fig)
      st.plotly_chart(profit_track2020_fig)
          
with tab3:
      col1, col2 ,col3, col4 , col5 ,col6 , col7, col8 ,col9,col10 , col11, col12 ,col13= st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1])
      with col1:
           st.plotly_chart(city_state2021_fig)
      with col2:
           st.write(" ")
      with col3:
           st.write("")
      with col4:
           st.write("")
      with col5:
           st.write("")
      with col6:
           st.write("")
      with col7:
           st.write("")
      with col8:
           st.write("")
      with col9:
           st.write("")
      with col10:
           st.write("")
      with col11:
           st.write("")
      with col12:
           st.write("")
      with col13:
           st.plotly_chart(Retailers_profit_2021_fig)
      st.plotly_chart(profit_track2021_fig)
     
with tab4:
     st.plotly_chart(profit_year_fig)
     st.header("Last Insights :")
     st.write("""
                    
          -  Amazon was not there in 2020.
               
          -  West Gear was the top in 2020, While Foot Locker , Sports Direct became strong competitors in 2021.
               
          -  Sales were obviously of higher rate in 2021 than that of 2020.
               
          -  Although the sales method preferred is online, but the rate of profits in store sales was higher.
               
          -  Average of prices per unit in 2020 increased on the first half of the year and then decreased, 
             but in 2021 increased at the second half of the year, and no
             big variationin prices as 2020. so generally, the products were expensive , it may be due to corona virus on that year.
               
          -  Although there was variation in prices but the units sold in two halves of years 2020 / 2021 were of approximate rate.
               
          -  In 2020, Prices rised, then the total sales decreased which led to dropping the profit.
               
          -  In 2021, Prices were constant and suitable, then the total sales increased which led to increasing the profit.
               
                    """)