import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')

streamlit.text('🥗 Spinach Omelette - $8.50')
streamlit.text('🥣 Fruit Parfait - $6.75')
streamlit.text('🥑 Kale, Avocado, Strawberry, and Banana Smoothie - $4.95')
streamlit.text('🐔 Toasted Chicken and Cream Cheese Bagel - $8.75') 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.

streamlit.dataframe(my_fruit_list)
