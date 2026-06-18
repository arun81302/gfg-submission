'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        cur=head
        while cur!=None:
            if cur.data==key:
                return True
            cur=cur.next
        return False
        #Code here
        