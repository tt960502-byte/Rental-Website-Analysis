import pandas as pd

file_path = '清洗後的淡水租屋資料.csv'
df = pd.read_csv(file_path)

address_stats = df.groupby('地址').agg({
    '價格': 'mean',
    '坪數': 'mean',
    '標題/社區': 'count'
}).rename(columns={
    '價格': '平均價格', 
    '坪數': '平均坪數', 
    '標題/社區': '物件數量'
})

sorted_address_stats = address_stats.sort_values(by='平均價格', ascending=False)

type_stats = df.groupby('建物類型_新').agg({
    '價格': 'mean',
    '坪數': 'mean',
    '標題/社區': 'count'
}).rename(columns={
    '價格': '平均價格', 
    '坪數': '平均坪數', 
    '標題/社區': '物件數量'
}).sort_values(by='平均價格', ascending=False)

sorted_address_stats.to_csv('區域租金統計.csv', encoding='utf-8-sig')
type_stats.to_csv('類型租金統計.csv', encoding='utf-8-sig')