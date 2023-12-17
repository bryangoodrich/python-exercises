from dataclasses import dataclass

@dataclass   
class LeafNode:
    value: int

@dataclass
class InnerNode:
    left: 'Node' 
    right: 'Node'

Node = LeafNode | InnerNode

def sum_leaves(node: Node):
    match node: 
        case LeafNode(value):
            return value
        case InnerNode(left, right):
            return sum_leaves(left) + sum_leaves(right)


node1 = LeafNode(10)
node2 = LeafNode(20)
node3 = InnerNode(node1, node2)
node4 = LeafNode(30) 
node5 = LeafNode(40)
node6 = InnerNode(node4, node5)
root = InnerNode(node3, node6)
#          (root)
#        /       \
#     (node3)   (node6)
#    /     \        /   \
# (node1) (node2) (node4)(node5)
#  /          \   /          \
# 10          20 30          40


print(f"Sum of Tree = {sum_leaves(root)}")
# Sum of Tree = 100
print(f"Sum of Node3 = {sum_leaves(node3)}")
# Sum of Node3 = 30
print(f"Sum of Node6 = {sum_leaves(node6)}")
# Sum of Node6 = 70
