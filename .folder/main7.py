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

'''
| Задание 44 |
| --- |
| В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() |

Статья про one hot вид

Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет".
"Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание.

Критерии оценивания:
1 - Слушатель написал корректный код для задачи, результат работы правильный за счет, которого можно перевести его в one hot вид и все корректно работает без ошибок.
'''

'''''
import numpy as np
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
  whoAmI
0   human
1   human
2   human
3   robot
4   robot
5   human
6   human
7   robot
8   human
9   robot
10  robot
11  human
12  robot
13  human
14  human
15  robot
16  human
17  robot
18  robot
19  robot

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)
    human  robot
0       1      0
1       1      0
2       1      0
3       0      1
4       0      1
5       1      0
6       1      0
7       0      1
8       1      0
9       0      1
10      0      1
11      1      0
12      0      1
13      1      0
14      1      0
15      0      1
16      1      0
17      0      1
18      0      1
19      0      1
'''''