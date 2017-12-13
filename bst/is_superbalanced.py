from bt import BTNode

def is_superbalanced(node):
	depth_list = []

	def get_depth(node, depth=0):
		if node is not None:
			if node.left is not None:
				get_depth(node.left, depth=depth + 1)
			if node.right is not None:
				get_depth(node.right, depth=depth + 1)
			if node.left is None and node.right is None:
				depth_list.append(depth)

	get_depth(node)

	return True if max(depth_list) - min(depth_list) < 2 else False

if __name__ == '__main__':
	# Create BST
	root = BTNode(1)
	root.insert_left(2)
	root.insert_right(6)
	root.left.insert_left(3)
	root.left.insert_right(4)
	root.left.right.insert_left(5)
	root.right.insert_right(7)

	print(is_superbalanced(root))