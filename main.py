from matplotlib import pylab as plt
import pandas as pd

# pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("TESLA.csv")
print(df1.head())
df1["Date"] = pd.to_datetime(df1.Date)
# print(df1.head())

df2 = pd.read_csv("KFC.csv")
print(df2)
df2["Date"] = pd.to_datetime(df2.Date)
# indexes = []
# for date2 in df2.Date:
#     for index, date1 in enumerate(df1.Date):
#         if date2 == date1:
#             indexes.append(index)
# print(indexes)

index2 = []
for date2 in df2.Date:
    if df1.index[df1.Date == date2].values.size:
        index2.append(int(df1.index[df1.Date == date2].values[0]))
print(index2)


mean = df1["Close"].mean()
mean2 = df2["Close"].mean()


plt.figure("Tesla's and KFC's Stock")
plt.plot(df1["Date"], df1["Close"]*2, "r-", linewidth=0.6, label="TESLA Stock price, mean="+str(mean), data=df1)
# or the same can be:
# plt.plot("Date", "Close", 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean), data=df1)
plt.plot(df2["Date"], df2["Close"], 'b-', linewidth=0.6, label="KFC Stock price, mean="+str(mean2), data=df2)
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
