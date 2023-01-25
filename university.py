import pandas as pd

import numpy as np

import streamlit as st

import plotly.express as px

from PIL import Image

df=pd.read_csv("Data/University Students Monthly Expenses.csv")


df_1 = df.copy()                          
df_1.dropna(inplace = True)                      

df_1['Gender']=df_1['Gender'].astype(object)

df_1['Age']=np.where((df_1['Age']<=17),'LT 17',
           np.where((df_1['Age']>17)&(df_1['Age']<=20),"17-20",
           "GT 20"))


df_1['Study_year']=df_1['Study_year'].astype(object)

df_1['Living']=df_1['Living'].astype(object)

df_1['Scholarship']=df_1['Scholarship'].astype(object)

df_1['Part_time_job']=df_1['Part_time_job'].astype(object)

df_1['Transporting']=df_1['Transporting'].astype(object)

df_1['Smoking']=df_1['Smoking'].astype(object)

df_1['Drinks']=df_1['Drinks'].astype(object)

df_1['Games_&_Hobbies']=df_1['Games_&_Hobbies'].astype(object)

df_1['Cosmetics_&_Self-care']=df_1['Cosmetics_&_Self-care'].astype(object)

df_1['Monthly_Subscription']=df_1['Monthly_Subscription'].astype(object)


st.title('University Students Monthly Expenses')
def home():
    st.title("Welcome to the presentation of University Students Monthly Expenses")
    image = Image.open('pic.png')
    st.image(image, caption='university') 
def data():
    st.header('Header of Dataframe')
    st.write(df_1.head())

def per():
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8  = st.tabs(['Gender', 'Age', 'Part_time_job', 'Smoking', 'Drinks', 'Games_&_Hobbies','Cosmetics_&_Self-care', 'Living'])

    with tab1:
        st.header("Gender")
        fig = px.box(df_1, x='Gender', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab2:
        st.header("Age")
        fig = px.scatter(df_1, x='Age', y='Monthly_expenses_$')
        st.plotly_chart(fig)
   
    with tab3:
        st.header("Part time job")
        fig = px.box(df_1, x='Part_time_job', y='Monthly_expenses_$')
        st.plotly_chart(fig)
   
    with tab4:
        st.header("Smoking")
        fig = px.box(df_1, x='Smoking', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab5:
        st.header("Drinks")
        fig = px.box(df_1, x='Drinks', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab6:
        st.header("Games & Hobbies")
        fig = px.box(df_1, x='Games_&_Hobbies', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab7:
        st.header("Cosmetics & Self care")
        fig = px.box(df_1, x='Cosmetics_&_Self-care', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab8:
        st.header("Living")
        fig = px.box(df_1, x='Living', y='Monthly_expenses_$')
        st.plotly_chart(fig)

def uni():
    tab1, tab2, tab3, tab4 = st.tabs(['Study_year', 'Scholarship', 'Transporting', 'Monthly_Subscription'])

    with tab1:
        st.header("Study year")
        fig = px.box(df_1, x='Study_year', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab2:
        st.header("Scholarship")
        fig = px.box(df_1, x='Scholarship', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab3:
        st.header("Transporting")
        fig = px.box(df_1, x='Transporting', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    with tab4:
        st.header("Monthly Subscription")
        fig = px.box(df_1, x='Monthly_Subscription', y='Monthly_expenses_$')
        st.plotly_chart(fig)
    
def rep():
    st.header("REPORT")
    st.write("*   We can see that mostly male students use monthly expenses when compared to female students.")
    st.write("*   Most students who do part time job are spending more monthly expenses.")
    st.write("*   Students spending there monthly expenses on smoking and drinking.")
    st.write("*   Students also spend monthly expenses on Cosmetics and self care.")
    st.write("*   The students who come for college from hostel are getting more monthly expenses rather than students who live in home.")
    st.write("*   The 4th year students are spending more monthly expenses when compare to any other study years.")
    st.write("*   Students who have scholarship are spending more monthly expenses.")
    st.write("*   Students who come to college by car are getting more expenses than the students who come by motorcycle or other travelling sources.")
    st.write("*   Most students spend their money on monthly subscription.")
             
st.sidebar.title('Navigation')
side = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Header', 'Personal Info', 'University Info', 'Report'])
if side == 'Home':
 home()
elif side == 'Data Header':
 data()
elif side == 'Personal Info':
 per()
elif side == 'University Info':
 uni()
elif side == 'Report':
 rep()
