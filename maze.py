#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# put all imports here:
import math
import random

#основное движение
def check_direction():
	global x
	global y
	if (x+3>dlin or maze[x+2][y] == ' ') and (y+4>shir or maze[x][y+2] == ' ') and (x-2<0 or maze[x-2][y] == ' ') and (y-2<0 or maze[x][y-2] == ' '):
		x = 1
		y = 1
		recheck_direction()
	elif 0 < x < dlin-1 or 0 < y < shir:
		key = random.randint(0, 3)
		if key == 0:
			if x < dlin-2 and maze[x+2][y] == '*':
				maze[x+1][y] = ' '
				x = x+2
				return x
			else:
				return check_direction()
		elif key == 1:
			if y < shir-3 and maze[x][y+2] == '*':
				maze[x][y+1] = ' '
				y = y+2
				return y
			else:
				return check_direction()
		elif key == 2:
			if x > 2 and maze[x-2][y] == '*':
				maze[x-1][y] = ' '
				x = x-2
				return x
			else:
				return check_direction()
		elif key == 3:
			if y > 2 and maze[x][y-2] == '*':
				maze[x][y-1] = ' '
				y = y-2
				return y
			else:
				return check_direction()
		else:
			recheck_direction()
	else:
		recheck_direction()


#выход из тупика
def recheck_direction():
	global x
	global y
	for x in range(1, dlin, 2):
		for y in range(1, shir-3, 2):
			if maze[x][y+2] == '*':
				maze[x][y+1] = ' '
				y = y+2
				return x
				return y
			if x+2 < dlin-1 and maze[x+2][y] == '*':
				maze [x+1][y] = ' '
				x = x+2
				return x
				return y
			else:
				continue


#канва лабиринта
n = input('Input maze level: ')
a = ['/','*']

shir = len(a) * n
dlin = shir+1

maze = [a * n for x in range(dlin)]
for x in range(0, dlin, 2):
	for y in range(0, shir, 2):
		maze[x][y] = ' '
		maze[x][y+1] = '-'

for x in range(dlin):
	del maze[x][-1]

#вход и выход лабиринта	
x = 1
y = 1
maze[x][y] = ' '
maze[1][0] = ' '
maze[-2][-1] = ' '

#прогрызаем!
for z in range(dlin*shir):
	maze[x][y] = ' '
	if 0 < x < dlin-1 and 0 < y < shir:
		check_direction()


#вывод лабиринта
for row in maze:
	print(' '.join(list(map(str, row))))