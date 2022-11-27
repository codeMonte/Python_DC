import seaborn as sns
import pandas as pd
titanic = sns.load_dataset("titanic")
titanic.to_csv('/Users/taehwan/School/Python/1020/data/titanic.csv', index = False)

print("titanic.isnull().sum():\n", titanic.isnull().sum())
#비어있는 데이터를 중간값으로 채운다
titanic['age'] = titanic['age'].fillna(titanic['age'].median())

print("\ntitanic['embarked'].value_counts():\n", titanic['embarked'].value_counts())
#제일 많은 S로 채운다
titanic['embarked'] = titanic['embarked'].fillna('S')

print("\ntitanic['embark_town'].value_counts():\n", titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')

print("\ntitanic['deck'].value_counts():\n", titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')

print("\ntitanic.isnull().sum():\n", titanic.isnull().sum())
print("\ntitanic.info():")
titanic.info()

import matplotlib.pyplot as plt
f, ax = plt.subplots(1, 2, figsize = (10, 5))
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0, 0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0, 0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
ax[0].set_title("Survived (Male)")
ax[1].set_title("Survived (Female)")
plt.show()

sns.countplot(x = 'pclass', hue = 'survived', data = titanic)
plt.title('Pclass vs Survived')
plt.show()

titanic_corr = titanic.corr(method = 'pearson')
print("\ntitanic_corr:\n", titanic_corr)
titanic_corr.to_csv('/Users/taehwan/School/Python/1020/data/titanic_corr.csv', index = False)

#특정 변수 사이의 상관 계수 구하기
print("\ntitanic['survived'].corr(titanic['adult_male']):\n", titanic['survived'].corr(titanic['adult_male']))
print("\ntitanic['survived'].corr(titanic['fare']):\n", titanic['survived'].corr(titanic['fare']))
sns.pairplot(titanic, hue = 'survived')
plt.show()

sns.catplot(x = 'pclass', y = 'survived', hue = 'sex', data = titanic, kind = 'point')
plt.show()

def category_age(x):
    if x < 10:
        return 0
    elif x < 20:
        return 1
    elif x < 30:
        return 2
    elif x < 40:
        return 3
    elif x < 50:
        return 4
    elif x < 60:
        return 5
    elif x < 70:
        return 6
    else:
        return 7
titanic['age2'] = titanic['age'].apply(category_age)
titanic['sex'] = titanic['sex'].map({'male': 1, 'female': 0})
titanic['family'] = titanic['sibsp'] + titanic['parch'] + 1
titanic.to_csv('/Users/taehwan/School/Python/1020/data/titanic3.csv', index = False)
heatmap_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
colormap = plt.cm.RdBu
sns.heatmap(heatmap_data.astype(float).corr(), linewidths = 0.1, vmax= 1.0, square = True, cmap = colormap, linecolor = 'white', annot = True, annot_kws = {"size": 10})
plt.show()
