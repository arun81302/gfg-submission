'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        value=count
        if value%2==0:
            temp=head
            a=value//2
            b=(value//2)+1
            count=1
            while count!=b:
                temp=temp.next
                count+=1
            return temp.data
        if value%2!=0:
            temp=head
            value=(value//2)+1
            count=1
            while count!=value:
                temp=temp.next
                count+=1
            return temp.data
                
        
