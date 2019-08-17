import quandl
import pandas as pd
import matplotlib.pyplot as p
import numpy as np
s=quandl.get("HKEX/02382", authtoken="----------", paginate=True)
print s
sw=40
lw=100
sig=pd.DataFrame(index=s.index)
sig['signal']=0.0
sig['shot']=s['Nominal Price'].rolling(window=sw,min_periods=1,center=False).mean()
sig['long']=s['Nominal Price'].rolling(window=lw,min_periods=1,center=False).mean()
sig['signal'][sw:]=np.where(sig['shot'][sw:]>sig['long'][sw:],1.0,0.0)
sig['positions']=sig['signal'].diff()
print sig
fig=p.figure(figsize=(5,5))
axl=fig.add_subplot(111,ylabel='Price in $')
s['Nominal Price'].plot(ax=axl, color='black', lw=1)
sig[['shot','long']].plot(ax=axl,lw=1.)
axl.plot(sig.loc[sig.positions==1.0].index,sig.shot[sig.positions==1.0],'^',markersize=5,color='g')
axl.plot(sig.loc[sig.positions==-1.0].index,sig.shot[sig.positions==-1.0],'v',markersize=5,color='r')
p.show()
