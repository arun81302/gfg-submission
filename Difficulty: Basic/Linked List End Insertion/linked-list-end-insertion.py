'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        z=Node(x)
        temp=head
        if temp==None:
            return z
        while temp.next!=None:
            temp=temp.next
        temp.next=z
        return head
        
        #code here 
        