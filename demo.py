# -- coding:utf-8 --
author = 'wuzhiyong'

def consumer():
    r = ''
    while True:
        n = yield r   #r表示接收send的参数，每次遇到yield，相当于我要去拿数据，也就是生产部拿生产出来的东西就行消费
        if not n:
            return
        print('消费者说:我拿到了一个包子，是 %s 号包子，已经被我吃了...' % n)
        r = '200 OK'    #表示消费完这个包子了

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('生产者生产了一个包子，是 %s 号包子...' % n)
        r = c.send(n)
        print('生产者说:消费者拿走了我的包子，并给我返回了值: %s' % r)
    c.close()
c = consumer()
produce(c)