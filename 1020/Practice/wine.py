import pandas as pd
red_df = pd.read_csv('/Users/taehwan/School/Python/1020/data/winequality-red.csv', sep=';', header=0, engine='python')
white_df = pd.read_csv('/Users/taehwan/School/Python/1020/data/winequality-white.csv', sep=';', header=0, engine='python')
red_df.to_csv('/Users/taehwan/School/Python/1020/data/winequality-red2.csv', index = False)
white_df.to_csv('/Users/taehwan/School/Python/1020/data/winequality-white2.csv', index = False)

print("red_df.head():\n", red_df.head())
red_df.insert(0, column = 'type', value = 'red')
print("\nred_df.head():\n", red_df.head())
print("\nred_df.shape:\n", red_df.shape)

print("\nwhite_df.head():\n", white_df.head())
white_df.insert(0, column = 'type', value = 'white')
print("\nwhite_df.head():\n", white_df.head())
print("\nwhite_df.shape:\n", white_df.shape)

wine = pd.concat([red_df, white_df])
print("\nwine.shape:\n", wine.shape)
wine.to_csv('/Users/taehwan/School/Python/1020/data/wine.csv', index = False)

print("\nwine.info():")
print(wine.info())

wine.columns = wine.columns.str.replace(' ', '_')
print("\nwine.head():\n", wine.head())
print("\nwine.describe():\n", wine.describe())

print("\nwine.quality.unique():\n", sorted(wine.quality.unique()))
print("\nwine.quality.value_counts():\n", wine.quality.value_counts())

print("\nwine.groupby('type')['quality'].describe():\n", wine.groupby('type')['quality'].describe())
print("\nwine.groupby('type')['quality'].mean():\n", wine.groupby('type')['quality'].mean())
print("\nwine.groupby('type')['quality'].std():\n", wine.groupby('type')['quality'].std())
print("\nwine.groupby('type')['quality'].agg(['mean', 'std'):\n", wine.groupby('type')['quality'].agg(['mean', 'std']))

from scipy import stats
from statsmodels.formula.api import ols, glm
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']   #type이 red인 것의 quality 추출
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
print("\nstats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False):\n", stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False))
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + \
            residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide +\
            density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data = wine).fit()
print("\nregression_result.summary():\n", regression_result.summary())

#보유 데이터를 기반으로 와인 샘플 예측
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predict = regression_result.predict(sample1)
print("\nsample1_predict:\n", sample1_predict) #예측 등급
print("\nwine[0;5]['quality]:\n", wine[0:5]['quality']) #실제 와인 등급

data = {"fixed_acidity" : [8.5, 8.1], "volatile_acidity":[0.8, 0.5],"citric_acid":[0.3, 0.4], "residual_sugar":[6.1, 5.8], "chlorides":[0.055,0.04], "free_sulfur_dioxide":[30.0, 31.0], "total_sulfur_dioxide":[98.0,99], "density":[0.996, 0.91], "pH":[3.25, 3.01], "sulphates":[0.4, 0.35],"alcohol":[9.0, 0.88]}
sample2 = pd.DataFrame(data, columns = sample1.columns)
print("\nsample2:\n", sample2)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')
sns.distplot(white_wine_quality, kde = True, label = 'white wine')
plt.title("Quality of Wine Type")
plt.legend()
plt.show()

import statsmodels.api as sm
others = list(set(wine.columns).difference(set(["quality", "fixed acidity"])))
p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data = wine, ret_coords = True)
plt.show()
fig = plt.figure(figsize = (8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig = fig)
plt.show()
