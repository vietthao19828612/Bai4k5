import streamlit as st
import pandas as pd
csv_content = """mien,san luong ,nam,don vi tinh
Bac,150000,2025,tan
Trung,100000,2025,tan
Nam,200000,2025,tan
"""
with open('pro5.4.csv', 'w', encoding='utf-8')as f:
   f.write(csv_content)
df =  pd.read_csv('pro5.4.csv')
st.subheader('DL goc:')
st.dataframe(df)

df_chart = pd.DataFrame({
  'c': df['mien'],
  'v': df['san luong '],
  'o': [1, 2, 3]
})
st.subheader('Bieu do san luong')
st.vega_lite_chart(df_chart, {
  'mark': 'arc',
  'encoding':{
    'theta': {'field': 'v', 'type': 'quantitative'},
    'scale': {'range': [2.356, 8.640]}
   ,
    'color': {
      'field': 'c', 'type': 'nominal',
      'scale':{
        'domain': ['Bac', 'Trung', 'Nam'],
        'range':['#416D9D', '#674028','#DEAC59']
      },
      'legend':{'title':'mien'}
    },
    'order':{'field': 'o'}
}}
                  )
