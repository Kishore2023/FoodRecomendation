

import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel

st. set_page_config(layout="wide")

st.markdown("<h1 style='text-align: right aign; color: green;'>🏞 WATERFALL RESTAURANT MULTI CUSINE 🏝 </h1>", unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.title('🍗 FOOD RECOMMENDATION TO NEW CUSTOMER 🍰')

breakfast_list = pickle.load(open('BreakfastVeg.pkl','rb'))
Orderbreakfast = pd.DataFrame(breakfast_list)


lunch_list = pickle.load(open('LunchVeg.pkl','rb'))
Orderlunch = pd.DataFrame(lunch_list)

dinner_list = pickle.load(open('DinnerVeg.pkl','rb'))
Orderdinner = pd.DataFrame(dinner_list)

#-------------------------------

breakfastNV_list = pickle.load(open('BreakfastNV.pkl','rb'))
OrderbreakfastNV = pd.DataFrame(breakfastNV_list)


lunchNV_list = pickle.load(open('LunchNV.pkl','rb'))
OrderlunchNV = pd.DataFrame(lunchNV_list)

dinnerNV_list = pickle.load(open('DinnerNV.pkl','rb'))
OrderdinnerNV = pd.DataFrame(dinnerNV_list)

#------------------------------------------------------------------------

breakfastBoth_list = pickle.load(open('BreakfastBoth.pkl','rb'))
OrderbreakfastBoth = pd.DataFrame(breakfastBoth_list)

lunchBoth_list = pickle.load(open('LunchBoth.pkl','rb'))
OrderlunchBoth = pd.DataFrame(lunchBoth_list)

dinnerBoth_list = pickle.load(open('DinnerBoth.pkl','rb'))
OrderdinnerBoth = pd.DataFrame(dinnerBoth_list)

#--------------------------------------------------------------
food_list = pickle.load(open('Firstorder.pkl','rb'))
data = pd.DataFrame(food_list)
similarity = pickle.load(open('similarity.pkl','rb'))

food_lista = pickle.load(open('Secondorder.pkl','rb'))
dataa = pd.DataFrame(food_lista)
similaritya = pickle.load(open('similaritya.pkl','rb'))

food_listb = pickle.load(open('Thirdorder.pkl','rb'))
datab = pd.DataFrame(food_listb)
similarityb = pickle.load(open('similarityb.pkl','rb'))

#-----------------------------------------------

Itemlist =""

def recommend(food):
    food_index = data[data["OrderName"] == food].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6] 

    recommended_foods= []
    for i in food_list:
        recommended_foods.append(data.iloc[i[0]].OrderName)
    return recommended_foods
    
def recommenda(food):
    food_indexa = dataa[data["OrderName"] == food].index[0]
    distancesa = similaritya[food_indexa]
    food_lista = sorted(list(enumerate(distancesa)), reverse = True, key = lambda x:x[1])[1:6] 

    recommended_foodsa= []
    for i in food_lista:
        recommended_foodsa.append(dataa.iloc[i[0]].OrderName)
    return recommended_foodsa

def recommendb(food):
    food_indexb = datab[data["OrderName"] == food].index[0]
    distancesb = similarityb[food_indexb]
    food_listb = sorted(list(enumerate(distancesb)), reverse = True, key = lambda x:x[1])[1:6] 

    recommended_foodsb= []
    for i in food_listb:
        recommended_foodsb.append(datab.iloc[i[0]].OrderName)
    return recommended_foodsb

Dining_type = st.selectbox('Select Dining Type',('Select Meal Type','Breakfast','Lunch','Dinner'))
Variety = st.selectbox('Choose your Variety', ('Select','Vegetarian','NonVegetarian', 'Both'))

if Dining_type == ('Breakfast') and Variety == ('Vegetarian'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', Orderbreakfast)
   
if Dining_type == ('Lunch') and Variety ==('Vegetarian'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', Orderlunch)
        
if Dining_type == ('Dinner') and Variety ==('Vegetarian'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', Orderdinner)    
        
if Dining_type == ('Breakfast') and Variety ==('NonVegetarian'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', OrderbreakfastNV) 

if Dining_type == ('Lunch') and Variety ==('NonVegetarian'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', OrderlunchNV) 
        
if Dining_type == ('Dinner') and Variety ==('NonVegetarian'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', OrderdinnerNV)       

if Dining_type == ('Breakfast') and Variety ==('Both'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', OrderbreakfastBoth) 

if Dining_type == ('Lunch') and Variety ==('Both'):
    food_select = st.selectbox('CONFIRM YOUR ORDER?', OrderlunchBoth) 
        
if Dining_type ==('Dinner') and Variety ==('Both'):
    food_select = st.selectbox('CAN YOU CONFIRM YOUR FIRST ORDER?', OrderdinnerBoth)         

if st.button('FIRST RECOMMENDATION'):
    if Dining_type == ('Select Meal Type') or Variety == ('Select'):
        st.warning('PLEASE SELECT THE DINING TYPE AND VARIETY', icon="⚠️")
    else :
        st.warning('THANKS FOR ORDERING YOUR FIRST FOOD', icon="🛒")
        Itemlist = Itemlist + food_select
        st.write(Itemlist)
        recommendations = recommend(food_select)
        st.subheader("CAN YOU ALSO TRY THE BELOW RECOMMENDED FOOD")
        for i in recommendations:
            st.write(i)

if st.button('SECOND RECOMMENDATION'):
    if Dining_type == ('Select Meal Type') or Variety == ('Select'):
        st.warning('PLEASE SELECT THE DINING TYPE AND VARIETY', icon="⚠️")
    else :
        st.warning('THANKS FOR ORDERING YOUR SECOND FOOD', icon="🛒")
        Itemlist = Itemlist + food_select
        st.write(Itemlist)
        recommendationsa = recommenda(food_select)
        st.subheader("CAN YOU ALSO TRY THE BELOW RECOMMENDED FOOD")
        for i in recommendationsa:
            st.write(i)

if st.button('THIRD RECOMMENDATION'):
    if Dining_type == ('Select Meal Type') or Variety == ('Select'):
        st.warning('PLEASE SELECT THE DINING TYPE AND VARIETY', icon="⚠️")
    else :
        st.warning('THANKS FOR ORDERING YOUR THIRD FOOD', icon="🛒")
        Itemlist = Itemlist + food_select
        st.write(Itemlist)
        recommendationsb = recommendb(food_select)
        st.subheader("CAN YOU ALSO TRY THE BELOW RECOMMENDED FOOD")
        for i in recommendationsb:
            st.write(i)


st.title('😀 THANK YOU ---  VISIT AGAIN 😀')
