def averager():
    sum = 0
    num = 0
    while True:
        s = (yield  sum / num if num > 0 else 0)
        sum += s
        num += 1
        print(s)


x = averager()
x.send(None)
x.send(1)
x.send(2)
x.send(3)
