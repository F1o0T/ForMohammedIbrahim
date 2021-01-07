import sys

def animal():
	print('Please specify an animal')

def dog():
	print('This is the dog branch')

def cat():
	print("I am a cat")

def goat():
	print("This is a goat")

def main():
	if sys.argv[1] == 'cat':
		cat()
	elif sys.argv[1] == 'dog':
		dog()
	elif sys.argv[1] == 'goat':
		goat()
	else:
		animal()

if __name__ == '__main__':
	main()
