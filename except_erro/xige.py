# !usr/bin/env python3
# -*- coding: utf-8 -*-
from sympy import *


x = Symbol('x')    # 本科生
y = Symbol('y')    # 研究生
print(solve([x + y - 9180, (x * 100)/98 + (y*100)/110 - 9000], [x, y]))

# x 6点x分，y 差y分到7点
t = Symbol('t')
print(solve([180-(x/60)*360+(x/60)*30-110, 150-(y/60)*360+(y/60)*30-110, 60-x-y-t], [x, y, t]))
