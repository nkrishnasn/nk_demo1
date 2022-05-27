class numval:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		x = self.a
		self.a+=1
		return x
v1=numval()
myiter=iter(v1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
