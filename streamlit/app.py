import streamlit as st
import pandas as pd
import json

st.title("西夏語料庫")
st.write("This is a simple corpus of 西夏 language.")


# JSONファイルを読み込む
with open('../論語全解.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# JSONデータからデータフレームを作成する
rows = []
for entry in data['corpus_data']:
    row = {
        'ID': entry['id'],
        'Meaning': entry['metadata']['meaning']
    }
    # textフィールドを処理して連番のカラムに展開
    for i, text in enumerate(entry['text'], 1):
        text_representation = f"{{'unicode': '{text['unicode']}', 'character': '{text['character']}', 'pronunciation': '{text['pronunciation']}', 'chinese': '{text['chinese']}'}}"
        row[f'text_{i}'] = text_representation
    rows.append(row)

df = pd.DataFrame(rows)

# Streamlitアプリでデータフレームを表示
st.title('論語テキストデータ')
st.write('以下は論語のテキストデータの一部です。')

edited_df = st.data_editor(df) 
st.dataframe(edited_df)
