import statsmodels.api as sm
import pandas as pd
  
# reading data from the csv
data = pd.read_csv('Boston.csv').drop("Unnamed: 0", axis=1)
  
# defining the variables
# x = data.drop("medv", axis=1)
x = data["lstat"].tolist()
y = data['medv'].tolist()
  
# adding the constant term
x = sm.add_constant(x)
  
# performing the regression
# and fitting the model
result = sm.OLS(y, x).fit()
  
# printing the summary table
# print(result.summary())
print(result.params)