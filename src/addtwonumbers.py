
"""
    https://leetcode.com/problems/add-two-numbers/
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    input 
    [2,4,3]
    [5,6,4]

    output
    [7,0,8]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNunbers:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        tVal = l1.val + l2.val
        if tVal < 10:
            tNode = ListNode(tVal, self.addTwoNumbers(l1.next, l2.next))
        else:
            tNode = ListNode(tVal-10)
            tNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
        return tNode
    
