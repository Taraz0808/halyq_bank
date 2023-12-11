import pandas as pd
# Полный путь к файлу
file_path = r'C:\Users\abdie\Downloads\archive (1)\Global_Education.csv'

df = pd.read_csv(r'C:\Users\abdie\Downloads\archive (1)\Global_Education.csv', encoding='latin1')

print(df.head())
print(df.isnull().sum())
print(df.describe())