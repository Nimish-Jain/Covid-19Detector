#importing libaries
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv('E:/Machine Learning/COVID19_line_list_data_final.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

clas=LogisticRegression()
clas.fit(x,y)

#INPUT
age = int(input('age: '))
gender = int(input('gender: '))
fever = int(input('fever: '))
cough = int(input('cough: '))
SoB = int(input('shortness of breath: '))
MP = int(input('muscle pain: '))
nausea = int(input('nausea: '))
diarrhea = int(input('diarrhea: '))

xinp = []
if gender == 0:
    xinp.append(0)
    xinp.append(1)
else:
    xinp.append(1)
    xinp.append(0)
xinp.append(age)
xinp.append(fever)
xinp.append(cough)
xinp.append(SoB)
xinp.append(MP)
xinp.append(nausea)
xinp.append(diarrhea)

xinp_np = np.array(xinp)
xinp_np = xinp_np.reshape(1, 9)

ypred = clas.predict_proba(xinp_np)
print(ypred)
ypred = ypred.reshape(2, 1)
print(ypred[1])


import requests
import bs4

resno = requests.get('https://www.worldometers.info/coronavirus/')
resno.text
soupno = bs4.BeautifulSoup(resno.text, 'lxml')
casesNo = soupno.find(class_ = 'maincounter-number').get_text()
print("current no of cases globally: ",casesNo)
