
from md5 import md5
#import os
#import hashlib
import random

class LinkedList:
	def __init__(self):
		self.next = None

	def append(self, node):
		if self.next == None:
			self.next = node
		else:
			cur = self.next
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def __repr__(self):
		cur = self.next
		#print "first:", cur.value
		#print "next val", cur.next.value
		i = 0
		output = ""
		while cur != None:
			output += "Node%s: %s \n" % (i, cur.value)
			i += 1
			cur = cur.next
		return output

	def __len__(self):
		cur = self.next
		i = 0
		while cur != None:
			i += 1
			cur = cur.next
		return i

class LLNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

class ChainHashMap:
	def __init__(self, size = 1024):
		self.size = int(size)
		self.buckets = [LinkedList() for i in xrange(self.size)]

	def getaddress(self, key):
		hasher = md5()
		hasher.update(key)
		digest = hasher.hexdigest()
		number = int(digest, 16)
		return number % self.size

	def getbucket(self, key):
		hasher = md5()
		hasher.update(key)
		digest = hasher.hexdigest()
		number = int(digest, 16)
		return self.buckets[number % self.size]

	def set(self, key, value):
		address = self.getaddress(key)
		cur = self.buckets[address].next
		if cur == None: ## totally empty
			self.buckets[address].next = LLNode(key, value)
		else:
			prev = self.buckets[address]
			while cur != None:
				if cur.key == key:
					prev.next = LLNode(key, value)
					return True
				prev = cur
				cur = cur.next
			prev.next = LLNode(key, value)
		return True

	def get(self, key):
		address = self.getaddress(key)
		cur = self.buckets[address].next
		while cur != None:
			if cur.key == key:
				return cur.value
			cur = cur.next
		return None


def test_add():
	hm = ChainHashMap(size = 1024)
	key = "test"
	value = 5
	hm.set(key, value)
	print hm.get(key)
	assert value == hm.get(key)


def test_replace():
	hm = ChainHashMap(size = 1024)
	key = "test"
	value = 5
	hm.set(key, value)
	print hm.get(key)
	assert value == hm.get(key)

	newvalue = 6
	hm.set(key, newvalue)
	print hm.get(key)
	assert newvalue == hm.get(key)

def test_overload_ononebucket(number):
	global hm
	hm = ChainHashMap(size = 1024)
	cheatsheet = []
	key = str(random.randint(0, 2000000))
	for i in xrange(number):
		value = i
		hm.set(key, value)
		cheatsheet.append({'key':key, 'value':value})

	for i in xrange(number):
		print "--------------"		
		print "key", cheatsheet[i]['key']
		print "value", cheatsheet[i]['value']
		print "bucket", hm.getbucket(cheatsheet[i]['key'])
		try:
			assert cheatsheet[i]['value'] == hm.get(cheatsheet[i]['key'])
		except AssertionError:
			print "assertion error!!!"



def test_overload(number):
	print "test_overload ===="
	global hm
	hm = ChainHashMap(size = 1024)
	cheatsheet = []
	for i in xrange(number):
		key = str(random.randint(0, 200000000000))
		value = i
		hm.set(key, value)
		cheatsheet.append({'key':key, 'value':value})

	for i in xrange(number):
		try:
			assert cheatsheet[i]['value'] == hm.get(cheatsheet[i]['key'])
		except AssertionError:
			print "--------------"		
			print "key", cheatsheet[i]['key']
			print "value", cheatsheet[i]['value']
			print "bucket", hm.getbucket(cheatsheet[i]['key'])
			print "assertion error!!!"


if __name__ == "__main__":
	test_add()
	test_replace()
	test_overload_ononebucket(20)
	test_overload(3000)




