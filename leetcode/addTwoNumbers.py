# -*- coding:UTF-8 -*-
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1, l2):
    newNode = ListNode(0)
    ansNode = newNode
    flag = 0

    while l1.val >= 0 or l2.val >= 0:
        x = l1.val if l1.val >= 0 else 0
        y = l2.val if l2.val >= 0 else 0

        sum = x + y + flag
        flag = sum // 10
        newNode.val = sum % 10

        l1 = l1.next if l1.next else ListNode(-1)
        l2 = l2.next if l2.next else ListNode(-1)
        if l1.val>=0 or l2.val>=0 or flag:
            newNode.next = ListNode(0)
            newNode = newNode.next

    if flag ==1:
        newNode.val = 1

    return ansNode

# def addTwoNumbers(self, l1, l2):
#     weight = 1
#     sum1 = 0
#     tmp = l1
#     while True:
#         sum1 += tmp.val * weight
#         if tmp.next is None:
#             break
#
#         tmp = tmp.next
#         weight *= 10
#
#     weight = 1
#     sum2 = 0
#     tmp = l2
#     while True:
#         sum2 += tmp.val * weight
#         if tmp.next is None:
#             break
#
#         tmp = tmp.next
#         weight *= 10
#
#     sum = sum1 + sum2
#     sum_str = [i for i in str(sum)].reverse()
#
#     head = ListNode(int(sum_str[0]))
#     head_insert = head
#     for i in range(1, len(sum_str)):
#         tmp_link = ListNode(int(sum_str[i]))
#         head_insert.next = tmp_link
#         head_insert = head_insert.next
#
#     return head


# sum_str=['0', '1', '2']
# head = ListNode(int(sum_str[0]))
# head_insert = head
# for i in range(1, len(sum_str)):
#     tmp_link = ListNode(int(sum_str[i]))
#     head_insert.next = tmp_link
#     head_insert = head_insert.next
