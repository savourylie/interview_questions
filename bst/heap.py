class MinHeap(object):
	def __init__(self, value_list=[]):
		self.heap = []
		
		if len(value_list) > 0:		
			for x in value_list:
				self.add(x)

	def add(self, value):
		self.heap.append(value)
		self.heapify_up()

	def pull(self):
		min_element = self.heap.pop(0)
		last_element = self.heap.pop()
		self.heap.insert(0, last_element)
		self.heapify_down()

	def get_left_child_index(self, current_index):
		return current_index * 2 + 1

	def get_right_child_index(self, current_index):
		return current_index * 2 + 2

	def has_left_child(self, current_index):
		return True if self.get_left_child_index(current_index) < len(self.heap) else False
	
	def has_right_child(self, current_index):
		return True if self.get_right_child_index(current_index) < len(self.heap) else False

	def get_parent_index(self, current_index):
		return int((current_index - 1) / 2)

	def has_parent(self, current_index):
		if current_index == 0:
			return False
		return True if self.get_parent_index(current_index) >= 0 else False

	def swap(self, index1, index2):
		self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

	def heapify_up(self):
		current_index = len(self.heap) - 1

		while self.has_parent(current_index):
			parent_index = self.get_parent_index(current_index)

			if self.heap[parent_index] < self.heap[current_index]:
				return current_index

			self.swap(parent_index, current_index)
			current_index = parent_index
			  
		return current_index

	def heapify_down(self):
		current_index = 0

		while self.has_left_child(current_index):
			smaller_child_index = self.get_left_child_index(current_index)
			
			if self.has_right_child(current_index) and self.heap[self.get_right_child_index(current_index)] < self.heap[smaller_child_index]:
				smaller_child_index = self.get_right_child_index(current_index)

			if self.heap[smaller_child_index] > self.heap[current_index]:
				return current_index

			self.swap(current_index, smaller_child_index)
			current_index = smaller_child_index

		return current_index


if __name__ == '__main__':
	minheap = MinHeap([5, 3, 18, 1, 6])
	print(minheap.heap)

	minheap.pull()
	print(minheap.heap)

	minheap.add(2)
	print(minheap.heap)	











