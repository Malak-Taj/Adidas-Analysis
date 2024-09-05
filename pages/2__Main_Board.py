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
Adidas = pd.read_csv(r"Adidas_cleaned.csv")
#Some definitions:
night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)','rgb(36, 55, 57)', 'rgb(6, 4, 4)']
blue_colors =  ['cyan','royalblue','darkblue','lightsalmon']
sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)','rgb(129, 180, 179)', 'rgb(124, 103, 37)']
irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)','rgb(175, 49, 35)', 'rgb(36, 73, 147)']
cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)','rgb(175, 51, 21)', 'rgb(35, 36, 21)']
labels = ['Foot Locker', 'Walmart', 'Sports Direct', 'West Gear', "Kohl's", 'Amazon']
values = [2637, 2374, 2032, 1030 ,949, 626]
product_list = ['', "Men's Street Footwear", "Men's Athletic Footwear",
                    "Women's Street Footwear", "Women's Athletic Footwear",
                    "Men's Apparel", "Women's Apparel"]

#Overall:
def counts(parameter):
     return Adidas[str(parameter)].value_counts().nlargest(5).reset_index()
def angle(fig , angle):
     return fig.update_xaxes(tickangle=angle)
Method = counts('Sales Method')
Method_bar =  px.bar(Method , x ='Sales Method' , y = 'count', color = 'Sales Method', color_discrete_sequence = blue_colors ,
                      title = 'Sales Method Strategy',labels={"Sales Method": "Sales Method",
                     "count": ""}, width=300,height=400)
angle(Method_bar,30)

Method_Profit = Adidas.groupby(['Year','Sales Method'])['Operating Profit'].mean().reset_index()
Method_Profit_fig = px.histogram(Method_Profit , x = 'Sales Method' , y = 'Operating Profit' ,color = 'Sales Method',
                                 labels={"Sales Method": "Sales Method","sum of Operating Profit": "  "},
                                  title='AVG Of Profit Per Sale Method',
                                 color_discrete_sequence = blue_colors,width=300,height=400)
angle(Method_Profit_fig , 30)

city = counts('City')
city_histogram = px.histogram(city , x =  'City', y = 'count', color = 'City',color_discrete_sequence = blue_colors ,
                               title= 'Cities Took Large Market Area' , labels={"City": "",
                     "sum of count": ""}, width=320,height=450)
angle(city_histogram , 30)

high_sales_cities = Adidas[(Adidas['City'] == 'Portland') |( Adidas['City'] == 'Charleston')]
Port_Char = high_sales_cities.groupby('City')['Sales Method'].value_counts().reset_index()
Port_Char_fig = px.sunburst(Port_Char, path=['City','Sales Method'] , values='count',
                            title = 'The Sales Method By PORT. & CHAR.',
                            color_discrete_sequence = px.colors.sequential.RdBu , width=400 , height= 450)

Retailer_pie = go.Figure(data=[go.Pie( labels=labels , values= values , marker_colors = px.colors.sequential.RdBu , pull=[0.3, 0.2, 0.1, 0 ,0, 0])])
Retailer_pie.update(layout_title_text='Retailers Share')

#Year-2020 / 2021 :
def city_profit(year):
    return Adidas[Adidas['Year'] == year].groupby('City')['Operating Margin'].sum().nlargest(9).sort_values(ascending=False).reset_index()
def city_profit_fig(df,color,width,height):
    return px.bar(df, x = 'City', y = 'Operating Margin',
                            title='Cities Of High Margin Profit',
                            color_discrete_sequence = [str(color)],width=width , height = height)
def retailer_profit(year):
     return Adidas[Adidas['Year'] == year].groupby(['Year','Retailer'])['Operating Margin'].sum().sort_values(ascending = False).reset_index()
def retailer_profit_fig(color):
     return px.bar(Retailers_profit_2020 , x ='Retailer' , y = 'Operating Margin' ,
                            title='AVG  Of Profits By Each Retailer',
                            color_discrete_sequence = [str(color)] ,width=350)

def product_track(year, product , color1 , color2, color3):
    product_track_year = Adidas[(Adidas['Year'] == year ) & (Adidas['Product'] == str(product))].groupby(['Year','Month'])[['Price per Unit','Total Sales','Operating Margin']].agg({"Price per Unit":np.mean, "Total Sales":np.sum  , "Operating Margin":np.sum}).reset_index()
    return px.line(product_track_year , x = 'Month' , y = ['Price per Unit','Total Sales','Operating Margin'] ,
                               title='Tracking Prices , Total Sales And Margin Profits.',
                               color_discrete_map={'Price per Unit':str(color1),'Total Sales':str(color2),'Operating Margin':str(color3)})

city2020_profit = city_profit(2020)
city2020_profit_fig = city_profit_fig(city2020_profit,'rgb(33, 75, 99)', 300 ,500)
angle(city2020_profit_fig , 50)

city2021_profit = city_profit(2021)
city2021_profit_fig = city_profit_fig(city2021_profit,'rgb(151, 179, 100)', 300 ,470)
angle(city2021_profit_fig , 50)

Retailers_profit_2020 = retailer_profit(2020)
Retailers_profit_2020_fig = retailer_profit_fig('rgb(33, 75, 99)')
angle(Retailers_profit_2020_fig , 30)

Retailers_profit_2021 = retailer_profit(2021)
Retailers_profit_2021_fig = retailer_profit_fig('rgb(151, 179, 100)')

profit_year = Adidas.groupby(['Year','Month'])['Operating Margin'].mean().reset_index()
profit_year_fig = px.line(profit_year , x = 'Month', y = 'Operating Margin', color = 'Year', color_discrete_map = {2020:'rgb(175, 49, 35)' , 2021:'lightsalmon'},
title= 'Profit over the years 2020 and 2021' , markers = True)

#Streamlit Code:
col1, col2 = st.columns(2)
with col1:
    st.header("Adidas Market on 2020/2021")
    tab1, tab2 , tab3 , tab4= st.tabs(["Overall" ,"Year-2020", "Year-2021","Insights"])
with col2:
   comp.iframe("https://lottie.host/embed/a5ccfbfe-91e5-4a4f-b5f4-dc6704cf1217/21ORN17YX3.json")
with tab1:
     col1, col2 ,col3= st.columns([1,7,1])
     with col1:
          st.plotly_chart(Method_bar)
     with col3:
          st.plotly_chart(Method_Profit_fig)
     note1 = st.checkbox('Read Sales Notes')
     if note1:
          st.text("The preferred sales method is (Online), but the profitable method is (Instore).")
     col1, col2 , col3= st.columns([1,7,1,])
     with col1:
          st.plotly_chart(city_histogram)
     with col3:
          st.plotly_chart(Port_Char_fig)
     note2 = st.checkbox('Read Cities Notes')
     if note2:
          st.text("Active sales cities are Portland and Charleston With Online Market.")
     st.plotly_chart(Retailer_pie)
     note3 = st.checkbox('Read Retailers Notes')
     if note3:
          st.text("The strong Adidas Sellers are FootLocker , Walmart and Sports Direct.")

with tab2:
     col1, col2 ,col3 = st.columns([1,7,1])
     with col1:
          st.plotly_chart(city2020_profit_fig)
     with col3:
          st.plotly_chart(Retailers_profit_2020_fig)
     note1 = st.checkbox('Retailers/Cities Notes')
     if note1:
          st.text("Houstan, Las Vegas and New York are profitable ... West Gear at the top of retailers.")
     option = st.selectbox(
    " Select the product you want to track it's price in 2020 ! ", product_list)
     if option == product_list[0] :
          st.write("")
     elif option == product_list[1]:
          fig1 = product_track(2020 ,"Men's Street Footwear" ,'cyan','orange','lightsalmon' )
          st.plotly_chart(fig1)
     elif option == product_list[2]:
          fig2 = product_track(2020,"Men's Athletic Footwear" , 'cyan','orange','lightsalmon')
          st.plotly_chart(fig2)
     elif option == product_list[3]:
          fig3 = product_track(2020,"Women's Street Footwear",'cyan','orange','lightsalmon')
          st.plotly_chart (fig3)
     elif option == product_list[4]:
          fig4 = product_track(2020,"Women's Athletic Footwear",'cyan','orange','lightsalmon')
          st.plotly_chart(fig4)
     elif option == product_list[5]:
          fig5 = product_track(2020,"Men's Apparel",'cyan','orange','lightsalmon')
          st.plotly_chart(fig5)
     elif option == product_list[6]:
          fig6 = product_track(2020,"Women's Apparel",'cyan','orange','lightsalmon')
          st.plotly_chart(fig6)

with tab3:
     col1, col2 ,col3 = st.columns([1,7,1])
     with col1:
          st.plotly_chart(city2021_profit_fig)
     with col3:
          st.plotly_chart(Retailers_profit_2021_fig)
     note2 = st.checkbox('Retailers / Cities Notes')
     if note2:
          st.text("Portland and Charleston are profitable ... Wset Gear and Foot Locker at the top of retailers.")
     option = st.selectbox(
    " Select the product you want to track it's price in 2021! ", product_list)
     if option == product_list[0] :
          st.write("")
     elif option == product_list[1]:
          fig1 = product_track(2021,"Men's Street Footwear",'rgb(151, 179, 100)','rgb(175, 49, 35)','lightsalmon')
          st.plotly_chart(fig1)
     elif option == product_list[2]:
          fig2 = product_track(2021,"Men's Athletic Footwear",'rgb(151, 179, 100)','rgb(175, 49, 35)','lightsalmon')
          st.plotly_chart(fig2)
     elif option == product_list[3]:
          fig3 = product_track(2021,"Women's Street Footwear", 'rgb(151, 179, 100)','rgb(175, 49, 35)','lightsalmon')
          st.plotly_chart (fig3)
     elif option == product_list[4]:
          fig4 = product_track(2021 , "Women's Athletic Footwear" , 'rgb(151, 179, 100)','rgb(175, 49, 35)','lightsalmon')
          st.plotly_chart(fig4)
     elif option == product_list[5]:
          fig5 = product_track(2021,"Men's Apparel" ,'rgb(151, 179, 100)','rgb(175, 49, 35)','lightsalmon')
          st.plotly_chart(fig5)
     elif option == product_list[6]:
          fig6 = product_track(2021,"Women's Apparel",'rgb(151, 179, 100)','rgb(175, 49, 35)','lightsalmon')
          st.plotly_chart(fig6)
      
with tab4:
     st.plotly_chart(profit_year_fig)
     st.header("Last Insights :")
     st.write("""
                    
          -  Amazon Sales were weak.
               
          -  West Gear was the top in both years.
               
          -  Sales were obviously of higher rate in 2021 than that of 2020.
               
          -  Although the sales method preferred is online, but the rate of profits in store sales was higher.
               
          -  The months witnessed high total sales in 2020 were April, August and September(Summer & Autumn), and there
             was a big variation in prices, it may be due to corona virus on that year.(particularly in June).
               
          -  The months witnessed high total sales in 2021 were June and  August, and there
             was obvious weak sales in the first part of the year(particularly in March).
              
          -  In both years, the big sales were done in August.
              
          -  Although there was variation in prices but the units sold in two halves of years 2020 / 2021 were of approximate rate.
                    """)
