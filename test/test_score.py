#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: test_score.py
@time: 2018/9/25 17:16
"""
a = [5,8,10]
b = [5,8,10]
c = [5,8,10]
d = [5,8,10]
e = [5,8,10]
count_dict = {}
a_count = 0
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            for l in range(len(d)):
                for m in range(len(e)):
                    count = a[i] + b[j] + c[k] + d[l] + e[m]
                    if str(count) not in count_dict:
                        count_dict[str(count)] = 1
                    else:
                        count_dict[str(count)] = count_dict[str(count)] + 1
                    a_count += 1

print [{key:count_dict[key]} for key in sorted(count_dict.keys())]
print(len(count_dict))
print(a_count)