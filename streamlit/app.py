import streamlit as st
import pandas as pd
import json

st.title("西夏語料庫")
st.write("This is a simple corpus of 西夏 language.")

with open('../論語全解.json', 'r', encoding='utf-8') as file:
    data = json.load(file)



st.title("Corpus Data Display")

for item in data['corpus_data']:
    id_value = item['id']
    meaning_value = item['metadata']['meaning']
    
    df = pd.DataFrame(item['text'])
    
    st.write(f"**ID**: {id_value}")
    st.write(f"**Meaning**: {meaning_value}")
    
    st.dataframe(df.T)

    st.write("---")


# edited_df = st.data_editor(df) 
# st.dataframe(edited_df)
