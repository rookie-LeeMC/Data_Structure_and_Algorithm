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
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return ans.next


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
