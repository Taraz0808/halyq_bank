import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Полный путь к файлу
file_path = r'C:\Users\abdie\Downloads\archive (1)\Global_Education.csv'


# Загрузим данные с использованием другой кодировки
df = pd.read_csv(file_path, encoding='latin1')

# Построим матрицу корреляции для числовых переменных
numeric_columns = df.select_dtypes(include=['float64', 'int64'])

# Построим матрицу корреляции для числовых переменных
correlation_matrix = numeric_columns.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Матрица корреляции')
plt.show()

# Построим гистограммы числовых переменных
numeric_columns.hist(bins=20, figsize=(15, 10))
plt.suptitle('Гистограммы числовых переменных', y=0.92)
plt.show()

plt.figure(figsize=(15, 8))
sns.barplot(x='Country Name', y='Some Variable', data=df)
plt.xticks(rotation=90)
plt.title('Распределение по странам')
plt.show()


