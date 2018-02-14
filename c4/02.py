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

#if __name__ == '___main_':
root = Node(0)
c1 = Node(1)
c2 = Node(2)
c3 = Node(3)
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)

for c in root:
    print(c)
