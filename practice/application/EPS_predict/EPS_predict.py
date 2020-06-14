#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from numpy import dot
from numpy.linalg import inv
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


def least_squares(x, y):

    theta = dot(dot(inv(dot(x.T, x)), x.T), y)
    return theta

datasets_Year = []
datasets_EPS = []
fr = open("01810.txt", 'r',)
lines = fr.readlines()
for line in lines[1:]:
    items = line.strip().split('\t')
    if '' in items:
        continue
    datasets_Year.append(int(items[0]))
    datasets_EPS.append(float(items[1]))
    print(items)
    # while '' in items  == False:
    #
    #     datasets_Year.append(int(items[0]))
    #     datasets_EPS.append(float(items[2]))
    #     break


print(datasets_Year,'---------------------------------', datasets_EPS)
fr.close()
length = len(datasets_Year)
datasets_Year = np.array(datasets_Year).reshape([length,1])
datasets_EPS = np.array(datasets_EPS)

minX = min(datasets_Year)
maxX = max(datasets_Year+4)
X = np.arange(minX,maxX).reshape([-1,1])

Cal_of_dim = 3
poly_reg = PolynomialFeatures(degree = Cal_of_dim)
X_poly = poly_reg.fit_transform(datasets_Year)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly, datasets_EPS)

x_label =  poly_reg.fit_transform(X).reshape(-1,1)
# a1=lin_reg_2.predict(x_label[0])
print ('X= ',X)
print ('len:',len(X))
# print (x_label[0])
# print (lin_reg_2.predict(poly_reg.fit_transform(X))[0])
y_pred = lin_reg_2.predict(poly_reg.fit_transform(X))
#RMSE
sum_mean=0
for i in range(len(datasets_Year)):
    sum_mean += (y_pred[i]-datasets_EPS[i])**2
sum_erro=np.sqrt(sum_mean/14)

print (sum_erro)
print (y_pred)

eps_growth_rate = (y_pred[-1]/datasets_EPS[-1])**(1/3)-1
print('EPS未来3年的复合增长率',eps_growth_rate)

# Visualization
# plt.axis([2009,2024,0,2])

plt.scatter(datasets_Year, datasets_EPS, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue',label='Pre_Value')
plt.title('RMSE='+str(sum_erro)+' | '+'degree='+str(Cal_of_dim))
plt.xlabel('Year')
plt.ylabel('EPS')
plt.legend(loc='upper left')
plt.show()

