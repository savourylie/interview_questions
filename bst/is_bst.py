from bt import BTNode, dfs_show

def is_bst(root):
	if root is None:
		return True

	if root.left is None and root.right is None:
		return True

	min_val, max_val = float('-inf'), float('inf')

	nodes = [(root, min_val, max_val)]

	while len(nodes) > 0:
		current, min_val, max_val = nodes.pop()
		print(current.value, min_val, max_val)

		if current.value <= min_val or current.value >= max_val:
			return False

		if current.right:
			nodes.append((current.right, current.value, max_val))

		if current.left:
			nodes.append((current.left, min_val, current.value))

	return True


if __name__ == '__main__':
	root = BTNode(3)
	root.insert_left(2)
	root.left.insert_left(1)
	root.insert_right(5)
	root.right.insert_left(4)
	root.right.insert_right(6)

	# dfs_show(root)
	print(is_bst(root))