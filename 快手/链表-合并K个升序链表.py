# -*- coding:UTF-8 -*-
'''

'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeKLists_20210612(lists):
    if not lists: return None

    # 思路-用python最小堆，维持堆的长度为链表的个数，首先插入头结点，然后弹出最小的，并加入最小的值所在的链表的下一个节点
    import heapq
    heap = []
    head = ans = ListNode(-1)

    for i in range(len(lists)):
        if lists[i]:  # 非空判定
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    # 最小堆，先弹出，然后压入弹出节点的下一个节点
    while heap:
        val, i = heapq.heappop(heap)
        head.next = ListNode(val)
        head = head.next

        # 弹出节点所在链表的下一个元素
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return head.next


def mergeKLists_20210627(lists):
    if not lists: return None

    head = ans = ListNode(-1)

    import heapq
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    while heap:
        val, i = heapq.heappop(heap)
        head.next = ListNode(val)
        head = head.next

        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return ans


import heapq

heap = [5, 2, 3, 1, 6]
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)
