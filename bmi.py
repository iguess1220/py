#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
Height=input("please input your height: ")
Weight=input("please input your weight: ")
height=float(Height)
weight=float(Weight)
bmi=weight/(height*height)
if bmi <= 18.5:
    print("您的BMI指数为：",'%.2f'  %bmi,'\t',"过轻!!")
elif    18.5 < bmi <= 25:
    print("您的BMI指数为：",'%.2f' %bmi,'\t',"正常!")
elif  25 < bmi <= 28:
    print("您的BMI指数为：",'%.2f' %bmi,'\t',"过重!")
elif  28 < bmi <= 32:
    print("您的BMI指数为：",'%.2f' %bmi,'\t',"肥胖!!")
elif bmi > 32:
    print("您的BMI指数为：",'%.2f' %bmi,'\t',"严重肥胖!")
else:
    print("您的BMI指数为：",'%.2f' %bmi,'\t',"你不是人!")



