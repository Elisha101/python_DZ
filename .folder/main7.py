'''
Задание
Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

Решение:
Вариант 1:
df[df['population']<501]['median_house_value'].agg(['mean'])
# mean    206799.951402
# Name: median_house_value, dtype: float64

Вариант 2:

df[df['population']<501]['median_house_value'].mean()
206799.95140186916

Задача 42: Узнать какая максимальная households в зоне минимального значения population

Решение:
Вариант 1:

df[df['population']==df['population'].min()]['households'].max()
# 4.0

Вариант 2:
df[df['population']==df['population'].min()]['households'].agg(['max'])
# max    4.0
# Name: households, dtype: float64
'''