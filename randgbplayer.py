from random import choice, choices
from time import sleep

from pynput.keyboard import Key, Controller, Listener

# Global variable indicating if main loop should stop
done = False

# Weights for choosing which key to press
weights = [2, 3, 4, 5, 6, 7]#, 8, 9]

# List of usernames
usernames = []

# Key press listener
def on_press(key):
	global done, weights
	
	# Choose random username
	username = choice(usernames)
	
	try:
		key = key.char
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
		elif key == '1':
			weights = [2, 3, 4, 5, 6, 7]
		else: # Stop the program on any other key
			print(f'{username:>25}: {key}')
			done = True
		
	except AttributeError: # Non-alphanumeric character
		if key == Key.up:
			weights = [1, 2, 4, 5, 6, 7]
		elif key == Key.left:
			weights = [1, 2, 3, 5, 6, 7]
		elif key == Key.down:
			weights = [1, 2, 3, 4, 6, 7]
		elif key == Key.right:
			weights = [1, 2, 3, 4, 5, 7]
		else:
			print(f'{username:>25}: {key}')
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
	
	sleep(3) # Give 3 seconds to change windows
	
	# Possible Keys: 'a' = A, 's' = B, 'i' = ↑, 'j' = ←, 'k' = ↓, 'l' = →, 'o' = START, 'p' = SELECT
	keys = ['a', 's', 'i', 'j', 'k', 'l']#, 'o', 'p']
	while not done:
		# Alternative choice, differing weights for key choice
		# TODO: Detect when in battle, more weight to A
		#       When not in battle, less weight to A + B
		key = choices(keys, cum_weights=weights)[0]
		
		# Press the key
		keyboard.press(key)
		sleep(0.01)
		keyboard.release(key)
