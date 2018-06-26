import inline as inline
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("kc_house_data.csv")
data['bedrooms'].value_counts().plot(kind='bar')
plt.title('number_of_bedroom')
plt.xlabel('bedrooms')
plt.ylabel('count')
plt.show()
