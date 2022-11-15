
import pickle
import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer

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

st.title('🍗FOOD RECOMMENDATION TO EXISTING CUSTOMER 🍰')

#-----------------------------------------------------------------

UserID = pickle.load(open('UserID.pkl','rb'))
userid = pd.DataFrame(UserID)

EmailID = st.selectbox('CONFIRM YOUR EMAIL ID', userid)

CustomerID_list = pickle.load(open('CustomerID.pkl','rb'))
df = pd.DataFrame(CustomerID_list)
df_new = df[df['EmailID'] == EmailID]

if st.button('VIEW YOUR HISTORY'):
    if EmailID == ('PLEASE CONFIRM YOUR EMAIL ID'):
        st.warning('PLEASE SELECT YOUR EMAILID TO PROCEED', icon="⚠️")

    else: 
        st.title('YOUR PREVIOUS ORDERED FOOD')
        st.dataframe(df_new)  

        st.title('🙏   THANKS FOR VISITING AGAIN  🙏')

if EmailID != ('PLEASE CONFIRM YOUR EMAIL ID'):

    alpha = df_new['Order1'].values[1]
    st.markdown(alpha, unsafe_allow_html=True)
#-----------------------------------------------------------------------------------------------

    food_list = pickle.load(open('Firstorder.pkl','rb'))
    data = pd.DataFrame(food_list)
    similarity = pickle.load(open('similarity.pkl','rb'))

    food_lista = pickle.load(open('Secondorder.pkl','rb'))
    dataa = pd.DataFrame(food_lista)
    similaritya = pickle.load(open('similaritya.pkl','rb'))

    food_listb = pickle.load(open('Thirdorder.pkl','rb'))
    datab = pd.DataFrame(food_listb)
    similarityb = pickle.load(open('similarityb.pkl','rb'))

    #-----------------------------------------------------------------------------------

    def recommend(food):
        food_index = data[data["OrderName"] == food].index[0]
        distances = similarity[food_index]
        food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6] 

        recommended_foods= []
        for i in food_list:
            recommended_foods.append(data.iloc[i[0]].OrderName)
        return recommended_foods

    recommendations = recommend(alpha)
    st.subheader("FOOD RECOMMENDATION BASED ON YOUR PREVIOUS FIRST ORDER")
    for i in recommendations:
        st.write(i)    

    st.write('----------------------------------------------------------------------------------------------------------------------------')

    alphaa = df_new['Order2'].values[1]
    st.markdown(alphaa, unsafe_allow_html=True)

    def recommenda(food):
        food_indexa = dataa[data["OrderName"] == food].index[0]
        distancesa = similaritya[food_indexa]
        food_lista = sorted(list(enumerate(distancesa)), reverse = True, key = lambda x:x[1])[1:6] 

        recommended_foodsa= []
        for i in food_lista:
            recommended_foodsa.append(dataa.iloc[i[0]].OrderName)
        return recommended_foodsa

    recommendations = recommenda(alphaa)
    st.subheader("FOOD RECOMMENDATION BASED ON YOUR PREVIOUS SECOND ORDER")
    for i in recommendations:
        st.write(i)

    st.write('***********************************************************************************************************************')

    alphab = df_new['Order3'].values[1]
    st.markdown(alphab, unsafe_allow_html=True)

    def recommendb(food):
        food_indexb = datab[data["OrderName"] == food].index[0]
        distancesb = similarityb[food_indexb]
        food_listb = sorted(list(enumerate(distancesb)), reverse = True, key = lambda x:x[1])[1:6] 

        recommended_foodsb= []
        for i in food_listb:
                recommended_foodsb.append(datab.iloc[i[0]].OrderName)
        return recommended_foodsb

    recommendations = recommendb(alphab)
    st.subheader("FOOD RECOMMENDATION BASED ON YOUR PREVIOUS THIRD ORDER")
    for i in recommendations:
            st.write(i)

    st.title('😀 THANK YOU ---  VISIT AGAIN 😀')

#-----------------------------------------------








