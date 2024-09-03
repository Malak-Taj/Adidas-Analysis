import streamlit as st
import streamlit.components.v1 as comp
st.header("Adidas Sales Analysis !")
col1, col2 = st.columns(2)
with col1:
   st.write(""" * This Analysis includes information on the sales of Adidas products, regions, states, prices of different products, total sales, units sold, profts and more.
            [ Check Adidas Profile .](https://www.adidas-group.com/en/about/profile/)""")
with col2:
   comp.iframe("https://lottie.host/embed/468caf1a-2b58-4ac7-87f4-ed9cad81de5e/LfGF8D7ZI2.json")
st.write("""
Data Description :

- Retailer:         The company or group that sells Adidas goods.
- Retailer ID:      a unique number that each merchant is given.
- Invoice Date:     The date when the sales transaction occurred.
- Region:           The store's operational geographic territory.
- State:            The state within the region where the retailer is located.
- City:             The retailer's location in the city.
- Product:          The item for sale is an Adidas product.
- Price per Unit:   The price of a single Adidas product unit.
- Units Sold:       The amount of Adidas merchandise sold in a certain transaction, expressed in units.
- Total Sales:      The amount of money made from the sale of Adidas goods in a certain transaction.
- Operating Profit: The amount of money made from the sale of Adidas goods in a certain transaction.
- Operating Margin: The proportion of operational profit to overall sales.
- Sales Method:     The process used to carry out the sales transaction.

"""
)
st.markdown(
"""
Here are some analytic questions needed to compete the market depending on the observations:
- What are the most effective Sale Methods that must be included in the analysis strategy ?
- What are the top Retailers and thier states and regions ?
- Which year witnessed high prices and its effects ?
- Which year is of high profits (tracking the profits over time) ?
- What about the total sales in each months , year and region as well ?
- What are the factors led to the drop of profits on different months ?
""")
# Link to the dataset in kaggle
if st.button("Go to the dataset in Kaggle"):
    st.markdown("[Click here to view the dataset](https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset)", unsafe_allow_html=True)
