import streamlit as st
import pandas as pd
import json

st.title("西夏語料庫")
st.write("This is a simple corpus of 西夏 language.")

# 論語全解
with open('論語全解.json', 'r', encoding='utf-8') as file:
    data = json.load(file)



st.title("Corpus Data Display")

dataframes = []

for item in data['corpus_data']:
    id_value = item['id']
    meaning_value = item['metadata']['meaning']
    
    df = pd.DataFrame(item['text'])
    
    st.write(f"**ID**: {id_value}")
    st.write(f"**Meaning**: {meaning_value}")
    
    edited_df = st.data_editor(df.T, use_container_width=True)
    
    dataframes.append(df.T.reset_index(drop=True))
    
    st.write("---")

combined_df = pd.concat(dataframes, axis=1, ignore_index=True)

st.write("**Combined DataFrame**:")
st.dataframe(combined_df)


chinese_all = ''.join(combined_df.iloc[3].astype(str))
pronounciation_all = ' '.join(combined_df.iloc[2].astype(str))

st.write("**Concatenated 'chinese' row**:")
st.write(chinese_all)

st.write("**Concatenated 'pronounciation' row**:")
st.write(pronounciation_all)