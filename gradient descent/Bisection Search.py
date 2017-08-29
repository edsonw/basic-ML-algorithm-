#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 11:46
# @Author  : sunday
# @Site    : 
# @File    : Bisection Search.py
# @Software: PyCharm


import numpy as np
def bisection(dfun,theta,args,d,low,high,maxiter=1e4):
    """
    #funtionality:find the root of the function(fun) in the interval [low,high]
    #使用二分搜索的方式查找最优学习率
    :param dfun:compute the gradient of function f(x)
    :param theta:Parameters of the model
    :param args: other variavles needed ti compute the value of dfun
    :param d:
    :param [low,high]:the interval which contains the root
    :param maxiter: the max number of iterations
    :return:
    """
    eps=1e-6
    val_low = np.sum(dfun(theta+low*d,args)*d.T)
    val_high = np.sum(dfun(theta+high*d,args)*d.T)

    if val_low*val_high>0:
        raise  Exception('Invalid interval!')

    inter_num=1
    while inter_num<maxiter:
        mid=(low+high)/2
        val_mid=np.sum(dfun(theta+mid*d,args)*d.T)
        if abs(val_mid<eps or abs(high-low)<eps):
            return mid
        elif val_mid*val_low>0:
            low=mid
        else:
            high=mid
        iter_num=iter_num+1

    def loss_funtion(theta,args):
        pass
