from tree import BinaryTree

root = BinaryTree('a')
root.insert_left('b')
root.insert_right('c')

b_node = root.left_child
b_node.insert_right('d')

c_node = root.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(root.value)
print(b_node.value)
print(c_node.value)
print(d_node.value)
print(e_node.value)
print(f_node.value)
