from random import choice, choices
from time import sleep

from pynput.keyboard import Key, Controller, Listener

# Global variable indicating if 
done = False

# List of usernames
usernames = []

# Key press listener
def on_press(key):
	global done
	
	# Choose random username
	username = choice(usernames)
	
	try:
		key = key.char
	except AttributeError: # Non-alphanumeric character
		print(f'{username:>25}: X')
		done = True

	if key == 'a': # 'a' = A
		print(f'{username:>25}: A')
	elif key == 's': # 's' = B
		print(f'{username:>25}: B')
	elif key == 'i': # 'i' = ↑
		print(f'{username:>25}: ↑')
	elif key == 'j': # 'j' = ←
		print(f'{username:>25}: ←')
	elif key == 'k': # 'k' = ↓
		print(f'{username:>25}: ↓')
	elif key == 'l': # 'l' = →
		print(f'{username:>25}: →')
	elif key == 'o': # 'o' = START
		print(f'{username:>25}: S')
	elif key == 'p': # 'p' = SELECT
		print(f'{username:>25}: L')
	else: # Stop the program on any other key
		print(f'{username:>25}: ?')
		done = True

if __name__ == '__main__':
	# pynput.keyboard.Controller instance
	keyboard = Controller()

	# Username text file. 1 username per line.
	filename = input('Enter the filename of a text file with usernames: ')

	# Fill up usernames list from file
	usernames = []
	with open(filename, 'r') as file:
		for line in file:
			usernames.append(line[:-1])
	
	# Start Key press listener
	listener = Listener(
		on_press=on_press)
	listener.start()
	
	# Possible Keys: 'a' = A, 's' = B, 'i' = ↑, 'j' = ←, 'k' = ↓, 'l' = →, 'o' = START, 'p' = SELECT
	keys = ['a', 's', 'i', 'j', 'k', 'l']#, 'o', 'p']
	while not done:
		# Alternative choice, differing weights for key choice
		# TODO: Detect when in battle, more weight to A
		#       When not in battle, less weight to A + B
		# key = choices(keys, cum_weights=[1, 2, 4, 5, 6, 7])[0]
		
		# Choose random key, equal weights
		key = choice(keys)
		
		# Press the key
		keyboard.press(key)
		sleep(0.01)
		keyboard.release(key)
