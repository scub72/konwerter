import pandas as pd
import time
pd.set_option('display.max_columns',10)

filename = "C:\Users\skubala\Desktop\Pkosz.csv"
df = pd.read_csv(filename, sep=';', header=0, skiprows=7)

date = pd.read_csv(filename, sep=';', engine = 'python', header=1, skipfooter =df.__len__()+1)
df['Date']=pd.to_datetime(date.iloc[0,1]+' '+date.iloc[1,1], format='%Y-%m-%d %H:%M:%S.%f')
df=df.drop(columns=['ACT value','ACT value.1'])

df['Time [s] / Points']= pd.to_datetime(df['Time [s] / Points'], format='%H:%M:%S,%ms')
print(df)



#print(df)
#df.info()




