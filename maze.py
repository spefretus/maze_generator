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
a = [u'\u2503'.encode('utf-8'),'*']

shir = len(a) * n
dlin = shir+1
cross = u'\u254B'.encode('utf-8')
line_hor = u'\u2501'.encode('utf-8')
line_ver = u'\u2503'.encode('utf-8')
right = u'\u2523'.encode('utf-8')
left = u'\u252B'.encode('utf-8')
down = u'\u2533'.encode('utf-8')
up = u'\u253B'.encode('utf-8')
corner_up_left = u'\u2513'.encode('utf-8')
corner_up_right = u'\u250F'.encode('utf-8')
corner_down_left = u'\u251B'.encode('utf-8')
corner_down_right = u'\u2517'.encode('utf-8')

maze = [a * n for x in range(dlin)]
for x in range(0, dlin, 2):
	for y in range(0, shir, 2):
		maze[x][y] = ' '
		maze[x][y+1] = line_hor

for x in range(dlin):
	del maze[x][-1]


#вход и выход лабиринта	
x = 1
y = 1
maze[x][y] = ' '
maze[1][0] = maze[-2][-1] = u'\u279d'.encode('utf-8')

#прогрызаем!
for z in range(dlin*shir):
	maze[x][y] = ' '
	if 0 < x < dlin-1 and 0 < y < shir:
		check_direction()



# прихорашиваем

# сливаем соседние горизонтали
for x in range(0, dlin):
	for y in range(1, shir-3):
		if maze[x][y] == maze[x][y+2] == line_hor:
			maze[x][y+1] = maze[x][y]
			maze[x][y+2] = maze[x][y]

# сливаем соседние вертикали
for x in range(1, dlin-2, 2):
	for y in range(0, shir, 2):
		if maze[x][y] == line_ver and maze[x+2][y] == line_ver:
			maze[x+1][y] = line_ver

# ответвления вверх и вниз		
for x in range(0, dlin, 2):
	for y in range(0, shir-2, 2):
		if maze[x][y] == line_hor:
			if x+1<dlin and maze[x+1][y] == line_ver:
				maze[x][y] = down
			elif x>1 and maze[x-1][y] == line_ver:
				maze[x][y] = up
	
# ответвления направо и налево, перекрестки
for x in range(1, dlin-1):
	for y in range(0, shir, 2):
		if maze[x][y] == line_ver:
			if maze[x-1][y] == line_ver and maze[x+1][y] == line_ver:
				if 2 < y < shir-2 and maze[x][y-1] == line_hor and maze[x][y+1] == line_hor:
					maze[x][y] = cross
				elif 2 < y and maze[x][y-1] == line_hor:
					maze[x][y] = left
				elif y < shir-2 and maze[x][y+1] == line_hor:
					maze[x][y] = right

# углы
for x in range(1, dlin-1):
	for y in range(1, shir-1):
		if x > 1 and y > 1 and maze[x][y] == line_ver and maze[x-1][y] == ' ':
			if maze[x-1][y-1] == line_hor:
				maze[x-1][y] = corner_up_left
			elif maze[x-1][y+1] == line_hor:
				maze[x-1][y] = corner_up_right

		if x < dlin-1 and y < shir-2 and maze[x][y] == line_ver and maze[x+1][y] == ' ':
			if maze[x+1][y-1] == line_hor:
				maze[x+1][y] = corner_down_left
			elif maze[x+1][y+1] == line_hor:
				maze[x+1][y] = corner_down_right
maze[0][0] = corner_up_right
maze[0][shir-2] = corner_up_left
maze[dlin-1][0] = corner_down_right
maze[dlin-1][shir-2] = corner_down_left


#вывод лабиринта
for row in maze:
	 print(''.join(list(map(str, row))))
