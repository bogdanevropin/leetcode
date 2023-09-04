"""
Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
	
	def __init__(self):
		self.stack = []
		self.min_stack = []
	
	def push(self, val: int) -> None:
		self.stack.append(val)
		if not len(self.min_stack) or val < self.min_stack[-1]:
			self.min_stack.append(val)
		else:
			self.min_stack.append(self.min_stack[-1])
	
	def pop(self) -> None:
		self.stack = self.stack[:-1]
		self.min_stack = self.min_stack[:-1]
	
	def top(self) -> int:
		return self.stack[-1]
	
	def getMin(self) -> int:
		return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
