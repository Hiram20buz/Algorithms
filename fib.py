import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.spatial.distance import cosine
from matplotlib import pyplot

y_true = [1, 1]
for i in range(1_000):
    y_true.append(y_true[-1] + y_true[-2])

data = []
for index, val in enumerate(y_true):
    data.append({'time': 1672646504 + 300*index, 'val': val})

df = pd.DataFrame(data)
# Convert Unix timestamp to datetime
df['datetime'] = pd.to_datetime(df['time'], unit='s')

# Set the datetime as the index
df.set_index('datetime', inplace=True)
df = df.reset_index()

train = df[:500]
test = df[500:]

# Plotting the result
plt.figure(figsize=(10, 6))
plt.plot(train['datetime'], train['val'], marker='o', linestyle='-', color='b')
plt.title('Temperature over time')   
plt.xlabel('Time')
plt.ylabel('Temperature °C')
plt.grid(True)
plt.show()

# Create lag features
train['val_lag1'] = train['val'].shift(1)
train['val_lag2'] = train['val'].shift(2)
train = train.dropna()
# Create lag features
test['val_lag1'] = test['val'].shift(1)
test['val_lag2'] = test['val'].shift(2)
test = test.dropna()

train = train.rename(columns={'datetime': 'ds', 'val': 'y'})
test = test.rename(columns={'datetime': 'ds', 'val': 'y'})

m = Prophet()
m.add_regressor('val_lag1')
m.add_regressor('val_lag2')
m.fit(train)



forecast = m.predict(train)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


fig1 = m.plot(forecast)
y_true = train['y'].values
y_pred = forecast['yhat'].values
mse = mean_squared_error(y_true, y_pred)
print(f'MSE: {mse}')

mae = mean_absolute_error(y_true, y_pred)
print(f'MAE: {mae}')


# plot expected vs actual
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()


forecast = m.predict(test)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
