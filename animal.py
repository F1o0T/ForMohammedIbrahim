import sys

def animal():
	print('Please specify an animal')

def dog():
	print('This is the dog branch')

def cat():
	print("I am a cat")

def main():
	if sys.argv[1] == 'cat':
		cat()
	elif sys.argv[1] == 'dog':
		dog()
	else:
		animal()

if __name__ == '__main__':
	main()