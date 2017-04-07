#Create a tuple named zoo that contains your favorite animals.
zoo = 'monkey', 'turtle', 'elephant', 'walrus', 'lemur', 'gibbon'

#Find one of your animals using the .index(value) method on the tuple.
walrus_index = zoo.index('walrus')
print('walrus_index: {}'.format(walrus_index))

#Determine if an animal is in your tuple by using for value in tuple.
def find_animal(value, tuple):
	'''
	checks a tuple to see if it contains a value
		args:
			value--value to check for 
			tuple--tuple to search
		returns:
			string
	'''
	if value in tuple:
		print('found your {} at index {}'.format(value, tuple.index(value)))
	else:
		print('sorry no {}'.format(value))

find_animal('jaguar', zoo)
find_animal('monkey', zoo)
find_animal('lemur', zoo)



#Create a variable for each of the animals in your tuple 
#with this cool feature of Python.
a, b, c, d, e, f = zoo
print('a: {}'.format(a))
print('b: {}'.format(b))
print('c: {}'.format(c))
print('d: {}'.format(d))
print('e: {}'.format(e))
print('f: {}'.format(f))

# example
#(lizard, fox, mammoth) = zoo
#print(lizard)


#Convert your tuple into a list.
list_zoo = list(zoo)
print('list_zoo: {}'.format(list_zoo))

#Use extend() to add three more animals to your zoo.
list_zoo.extend(['sloth','parrot','meerkat'])
print('zoo extended: {}'.format(list_zoo))

#Convert the list back into a tuple.
tuple_zoo = tuple(list_zoo)
print('back to tuple: {}'.format(tuple_zoo))


