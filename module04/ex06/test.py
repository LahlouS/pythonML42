import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index = ['a', 'b', 'c'])

plts = plt.plot(df, marker = 'o')
plt.legend(plts, df.columns)
print(df)
plt.show()


