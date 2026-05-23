import pandas as pd

df = pd.read_csv('淡水租屋資料.csv')

df['價格'] = pd.to_numeric(df['價格'].astype(str).str.replace(r'[^\d]', '', regex=True), errors='coerce')
df = df.dropna(subset=['價格'])

df = df.drop_duplicates()
df = df[~df['標題/社區'].isin(['.', '..', '...'])]
df = df.dropna(subset=['標題/社區'])

df = df[(df['坪數'] >= 2) & (df['坪數'] <= 150)]

def extract_type(text):
    text = str(text)
    if '電梯' in text or '大樓' in text:
        return '電梯大樓'
    elif '公寓' in text:
        return '公寓'
    elif '別墅' in text or '透天' in text:
        return '透天厝'
    else:
        return '其他'
df['建物類型_新'] = df['建物類型'].apply(extract_type)

df = df.drop(columns=['樓層'])
df['房型'] = df['房型'].fillna('未知')

df.to_csv('清洗後的淡水租屋資料.csv', index=False, encoding='utf-8-sig')