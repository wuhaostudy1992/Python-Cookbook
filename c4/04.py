from collections import Iterable

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __repr__(self):
        return 'Node({!r}), haha'.format(self._value)
        
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)
        
    def DFS(self):
        yield self
        for c in self:
            yield from c.DFS()
    
    '''def DFS_2(self):
        if isinstance(self, Iterable):
            yield from self._children
        else:
            yield self._children'''

#if __name__ == '___main_':
root = Node(0)
c1 = Node(1)
c2 = Node(2)
c3 = Node(3)
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)
c1.add_child(Node(4))
c1.add_child(Node(5))
c2.add_child(Node(6))

#for c in root.DFS():
    #print(c)
'''for c in root.DFS_2():
    print(c)'''
