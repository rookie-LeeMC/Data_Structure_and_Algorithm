# -*- coding:UTF-8 -*-
'''
参考资料：https://blog.csdn.net/m0_38008539/article/details/97262421
'''


class node:  # 用链表实现队列 只用来记录节点
    def __init__(self):
        self.data = None
        self.next = None
