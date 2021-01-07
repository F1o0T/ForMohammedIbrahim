import sys

def animal():
	print('Please specify an animal')

def cat():
	print("I am a cat")

def main():
	if sys.argv[1] == 'cat':
		cat()
	else:
		animal()

if __name__ == '__main__':
	main()