#
#  Node Depths
#
#  Write a function that takes in a Binary Tree and returns the sum of its
#  nodes' depths.
#

def nodeDepthRecursive(root, depth=0):
	# f(n, d) = d + f(n.left, d+1) + f(n.right, d+1)
	if root == None:
		return 0
	return (depth + 
		nodeDepthRecursive(root.left, depth + 1) + 
		nodeDepthRecursive(root.right, depth + 1))

def nodeDepthIterative(root):
	stack = [[root, 0]]
	count = 0
	while stack != []:
		node = stack.pop()
		depth = node[1]
		count += depth
		if node[0].left != None:
			stack.append([node[0].left, depth+1])
		if node[0].right != None:
			stack.append([node[0].right, depth+1])
	return count
		

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)
tree.right = BinaryTree(3)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

sol = nodeDepthRecursive(tree)
assert sol == 16
print(sol)

sol = nodeDepthIterative(tree)
assert sol == 16
print(sol)
