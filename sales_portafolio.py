import streamlit as st
import sales_mock as mock
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/AReyH/sales_mock_data/master/all_months.csv')

st.title("Mock Sales Analysis")
st.markdown("### By Arturo Rey")

st.markdown('The dataset used in the following analysis is generated via code. This is not a real store/company, however it follows a trend based on personal experience.')

st.markdown('The company is a pastry shop based in Florida, USA. They have several locations across the state. ')

st.markdown('During the year 2019, the company stored all purchase information for it to be analyzed by the end of the year. The company wanted to know how they performed during the year.')

if st.sidebar.checkbox("Show data sample", False):
    st.sidebar.dataframe(df[['Order ID','Product', 'Quantity Ordered','Price Each','Order Date', 'Purchase Address']].sample(10))

# Earned by month
st.markdown('#### What was the best month for sales? How much was earned that month?')
mock.earned_in_month(data=df)
st.pyplot()
st.markdown('According to the bar graph shown above, the best month for sales was December, and the worst was February. Questions might arise from this information, like did the company spend more money on advertisment in November/December compared to February?')

# Most profitable city
st.markdown('#### What city had the highest number of sales?')
mock.most_profit_city(data=df)
st.pyplot()
st.markdown('According to the bar graph shown above, Jacksonville had the most sales. We may want to analyze why Cape Coral had such a low number of sales, or if it is still profitable?')

# Best time for ads
st.markdown("#### What time should we display advertisements to maximize likelihood of customer's buying pastries?")
mock.best_time_ad(data=df)
st.pyplot()
st.markdown('The graph above makes a lot of sense because customers will most likely consume pastries during lunchtime throughout dinner. The company should display advertisements before or during lunchtime, and before dinner to maximize profit.')

# Most sold products
st.markdown('#### What product sold the most?')
mock.most_sold(data=df)
st.pyplot()
st.markdown('The most sold product throughout 2019 was the water bottles. Followed by a close draw between Oreo Cupcakes, Strawberry Cheesecakes, Oreo Cake, Merengue Cheesecake, and Carrot Cheesecake.')
st.markdown('The water bottle being one of the cheapest items in the menu, it makes sense that it would be the most sold item.')

# Products sold together
st.markdown('#### What products are most often sold together?')
sold_ = mock.sold_together(df)
st.dataframe(sold_)
st.markdown('The products that were most often sold together were the Carrot Cheesecake and the Fountain Drink, followed by the Carrot Cheesecake and Juice.')
st.markdown('This last analysis is crucial because with it, the company is able to know what items are being most often sold together, and which ones are not. The company may also promote lesser sold products with sales and special offers.')


if st.sidebar.checkbox("About Me", False):
    st.sidebar.markdown('## About Me:')
    st.sidebar.markdown('My name is Arturo and I work as a mechanical engineer and a freelance data analyst. I graduated as a Mechanical Engineer from Universidad del Norte.')
    
    st.markdown('')