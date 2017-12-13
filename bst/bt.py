class BTNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert_left(self, value):
		self.left = BTNode(value)

		return self.left

	def insert_right(self, value):
		self.right = BTNode(value)

		return self.right


def dfs_show(node):
	print("DFS: ")
	if node is None:
		return

	nodes = [node]

	while len(nodes) > 0:
		current = nodes.pop(0)
		print(current.value)

		if current.right is not None:
			nodes.insert(0, current.right)
		if current.left is not None:
			nodes.insert(0, current.left)


def bfs_show(node):
	print("BFS: ")
	if node is None:
		return

	nodes = [node]

	while len(nodes) > 0:
		current = nodes.pop(0)
		print(current.value)

		if current.left is not None:
			nodes.append(current.left)	
		if current.right is not None:
			nodes.append(current.right)


if __name__ == '__main__':
	# Create BST
	root = BTNode(1)
	root.insert_left(2)
	root.insert_right(6)
	root.left.insert_left(3)
	root.left.insert_right(4)
	root.left.right.insert_left(5)
	root.right.insert_right(7)

	dfs_show(root)
	bfs_show(root)

