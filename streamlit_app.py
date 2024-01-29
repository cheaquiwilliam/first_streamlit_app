
import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
   
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 $ Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach $ Rocket Smoothie')
streamlit.text('🐔 Hard-Boilded Free-Range Egg')
streamlit.text('🥑🍞 Avacado Tast')

# adding Build your own Smoothie Menu
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt').set_index('Fruit')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), [])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

