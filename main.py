import streamlit as st
import pandas as pd
csv_content = """Mien,San luong,Nam,Don vi tinh
Bac,150000,2025,tan
Trung,1000000,2025,tan
Nam,2000000,2025,tan
"""
with open('pro5.4.csv','w',encoding='utf-8')as f:
    f.write(csv_content)
df = pd.read_csv('pro5.4.csv')
st.subheader('dl goc :')
st.dataframe(df)
df_chart = pd.DataFrame({
    'c': df['Mien'],
    'v': df['San luong'],
    'o': df[1,2,3]
})
st.subheader('Bieu do tron san luong')
st.vega_lite_chart(df_chart,{
    'mark': 'arc',
    'encoding': {
        'theta': {'field': 'v','type':'quanitative'},
        'scale':{'range': [2.356,8.640]},

    'color': {
        'field':'c','type': 'nominal',
        'scale':{
            'domain': ['Bac','Trung','Nam'],
            'range': ['#416D9D','#674028','#DEAC59']

        },
        'legend':{'title': 'Mien'}

    },
    'order': {'field':'o'}
}}
                   )
