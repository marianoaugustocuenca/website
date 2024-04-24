import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title('The Best Company')
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Suspendisse at quam lacus. Fusce vitae ante vel ex pulvinar elementum eget eget dui.
  Sed porttitor sapien et purus elementum, at rhoncus erat tristique. 
  Nulla vitae ligula in nisl pulvinar mollis at ac erat. Donec eros massa,
   hendrerit luctus luctus in, convallis malesuada eros. Maecenas lorem elit,
    tristique vel justo et, pellentesque faucibus est. Suspendisse malesuada 
    orci quam, et laoreet lacus pharetra sit amet. Cras euismod ac massa non 
    dapibus. Pellentesque pellentesque libero eu placerat semper.
     Sed a suscipit libero, non feugiat enim. Suspendisse eget vehicula lectus.
"""
st.write(content)

st.title('Our Team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv')

with col1:
    for index, row in df[:4].iterrows():
        st.header((row['first name'] + ' ' + row['last name']).title())
        st.text(row['role'].title())
        st.image('images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.header((row['first name'] + ' ' + row['last name']).title())
        st.text(row['role'].title())
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header((row['first name'] + ' ' + row['last name']).title())
        st.text(row['role'])
        st.image('images/' + row['image'])
