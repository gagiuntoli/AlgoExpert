def findClosestValueInBst_Recursive(tree, target):
	return findClosestValueInBst_Helper(tree, target, tree.value)

def findClosestValueInBst_Helper(tree, target, closest):

	if tree == None:
		return closest

	if abs(tree.value - target) < abs(closest - target):
		closest = tree.value

	if target < tree.value:
		return findClosestValueInBst_Helper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBst_Helper(tree.right, target, closest)
	else:
		return closest
	

def findClosestValueInBst_Iterative(tree, target):

	closest = tree.value
	node = tree
	while node != None:
		if abs(node.value - target) < abs(closest - target):
			closest = node.value
		if target < node.value:
			node = node.left
		elif target > node.value:
			node = node.right
		else:
			return closest
	return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.left.left.left = BST(1)
root.right.left = BST(13)
root.right.right = BST(22)
root.right.left.right = BST(14)

assert findClosestValueInBst_Recursive(root, 10) == 10
print ("test case A Passed")
assert findClosestValueInBst_Recursive(root, 12) == 13
print ("test case B Passed")
assert findClosestValueInBst_Recursive(root, 0) == 1
print ("test case C Passed")

assert findClosestValueInBst_Iterative(root, 10) == 10
print ("test case D Passed")
assert findClosestValueInBst_Iterative(root, 12) == 13
print ("test case E Passed")
assert findClosestValueInBst_Iterative(root, 0) == 1
print ("test case F Passed")
