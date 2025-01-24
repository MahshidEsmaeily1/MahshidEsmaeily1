import pandas as pd
import matplotlib.pyplot as plt



smsDF=pd.read_csv('SMSSpamCollection', sep='\t', names=['Label', 'Message'])

print(smsDF)
smsDF['LenOfMessage'] = smsDF['Message'].apply(len)




print(smsDF.describe())
print(smsDF.groupby('Label').describe())
print(smsDF['Label'].value_counts())
smsDF.hist(column='LenOfMessage',by='Label', bins=50, figsize=(13,5))
plt.show()

#The longest spam Message
print(smsDF.LenOfMessage.describe())
print(smsDF.query('LenOfMessage==910'))
print(smsDF[smsDF['LenOfMessage']==910]['Message'].iloc[0])