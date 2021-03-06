# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 
from sys import stdin
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.linear_model import LinearRegression
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
data = pd.read_csv("../input/kc_house_data.csv")

price = data["price"]
space = data["sqft_living"]
x = np.array(space).reshape(-1, 1)
y = np.array(price)
model = LinearRegression()
model.fit(x, y)

d = 2000
pred = model.predict(d)
for i in pred:
    i = str(int(i))
    print("Predicted House Price: " + "$" + i)
