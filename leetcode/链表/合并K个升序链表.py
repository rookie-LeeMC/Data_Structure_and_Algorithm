# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/merge-k-sorted-lists/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    if not lists: return None

    head = ListNode(0)
    ans = head

    import heapq
    heap = []

    # 将每个链表的头结点放入堆中
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    # 弹出堆，再压入对应位置的链表
    while heap:
        val, i = heapq.heappop(heap)
        head.next = ListNode(val)
        head = head.next

        if lists[i]:
            heapq.heappush(heap,(lists[i].val, i))
            lists[i] = lists[i].next

    return ans.next
