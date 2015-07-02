#!//usr/bin/env python3

import random


class IllegalResultException(Exception):
	pass

# generate all possible coordinates
positions = [(x,y) for x in "abcdefghij" for y in range(10)]

def get_random():
	choice = random.choice(positions)
	positions.remove(choice)
	return choice


def kill_it(choice):
	""" A hit, a veritable hit.
	"""
	adjacents = [(chr(ord(choice[0])-1),choice[1]),
				 (chr(ord(choice[0])+1),choice[1]),
				 (choice[0],choice[1]-1),
				 (choice[0],choice[1]+1),]

	adjacents = list(set(positions)&set(adjacents))
	choice = random.choice(adjacents)

	return choice



if __name__ == '__main__':
	result = 'm'
	while True:
		if result == 'm' or result == 's':
			choice = get_random()
		elif result == 'h':
			choice = kill_it(choice)
		else:
			raise IllegalResultException('why do you hate us?')
		print("{}{}".format(choice[0],choice[1]))

		result = input()


