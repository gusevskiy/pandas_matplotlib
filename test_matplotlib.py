import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
fig,ax = plt.subplots()
df=pd.DataFrame({'A':[1,2,3,4,5,6,7,8,9,10,11,12],
                 'B':[1,2,3,1,2,3,1,2,3,1,2,3],
                 'C':[1,3,2,4,5,4,3,5,6,9,11,8]})
ax.plot(df.index,df.C)
ax.xaxis.set_major_locator(ticker.IndexLocator(3,0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xticklabels(df.A[::3])

plt.show()