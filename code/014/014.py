# github.com/bryangoodrich/python-exercises
# code/0014/0014.py

import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Description before filling missing values in Age")
print(df.describe())
#        PassengerId    Survived      Pclass         Age       SibSp
# count   891.000000  891.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008
# std     257.353842    0.486592    0.836071   13.002015    1.102743

print(f"Percent of Missing\n{round(df.isnull().mean()*100, 2)}")
# Age 19.87%

df.Age.fillna(df.Age.mean(), inplace=True)

print("Description after filling missing values in Age")
print(df.describe())
#        PassengerId    Survived      Pclass         Age       SibSp
# count   891.000000  891.000000  891.000000  714.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008
# std     257.353842    0.486592    0.836071   14.526497    1.102743

age_by_class = df.groupby('Pclass')['Age'].mean()
ax = age_by_class.plot(kind='bar', color='skyblue')
ax.set_xticklabels(age_by_class.index, rotation=0)
plt.xlabel('Passenger Class')
plt.ylabel('Mean Age')
plt.title('Mean Age by Passenger Class')
plt.savefig("plot.png")
