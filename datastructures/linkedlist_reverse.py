
## write linked list

class LinkedList:
	def __init__(self):
		self.first = None

	def append(self, node):
		if self.first == None:
			self.first = node
		else:
			cur = self.first
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def __repr__(self):
		cur = self.first
		print "first:", cur.value
		print "next val", cur.next.value
		i = 0
		output = ""
		while cur != None:
			output += "Node%s: %s \n" % (i, cur.value)
			i += 1
			cur = cur.next
		return output

	def __len__(self):
		cur = self.first
		i = 0
		while cur != None:
			i += 1
			cur = cur.next
		return i


class LLNode:
	def __init__(self, value):
		self.value = value
		self.next = None


def reverse(ll):
	ll_len = len(ll)
	print "length:", len(ll)
	if ll_len <= 1:
		return ll

	prev = ll.first
	redirect = prev.next
	next = redirect.next

	while redirect != None:
		# redirect
		redirect.next = prev
		# increment
		prev = redirect
		redirect = next
		if next != None:
			next = next.next
		else:
			next = None
	ll.first.next = None
	ll.first = prev

	print ll
	return ll



if __name__ == '__main__':
	ll = LinkedList()
	for i in range(12):
		ll.append(LLNode(i))
	
	# ll.append(LLNode(3))
	# ll.append(LLNode(5))
	# ll.append(LLNode(8))
	print ll
	reverse(ll)



