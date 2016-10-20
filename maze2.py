#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# put all imports here:
import math
import random

#наличие ходов (непройденных клеток) во всем лабиринте
def check_possibility(full):
	for x in range(1, dlin-1, 2):
		if maze[x].count(full) > 0:
			return 'yes'
			break
		elif maze[x].count(full) == 0:
			if x == dlin-2:
				return 'no'
				break
			elif x < dlin-1:
				continue
			else:
				print ('exception')
				break
		else:
			print ('exception')
			break

#проверка на тупик (отсутствие ходов из данной позиции)
def check_dead_end():
	if (x == dlin-2 or maze[x+2][y] == space) and (y == shir-1 or maze[x][y+4] == space) and (x == 1 or maze[x-2][y] == space) and (y == 2 or maze[x][y-4] == space):
		return 'yes'
	else:
		return 'no'	


#основное движение с запоминанием ходов
def check_direction():
	global x
	global y
	global keychain
	key = random.randint(0, 3)
	if key == 0:
		if x < dlin-2 and maze[x+2][y] == full:
			maze[x+1][y] = maze[x+1][y-1] = maze[x+1][y+1] = space
			x = x+2
			keychain.append(key)
			return x		
			return keychain
	elif key == 1:
		if y < shir-1 and maze[x][y+4] == full:
			maze[x][y+1] = maze[x][y+2] = maze[x][y+3] = space
			y = y+4
			keychain.append(key)
			return y	
			return keychain
	elif key == 2:
		if x > 1 and maze[x-2][y] == full:
			maze[x-1][y] = maze[x-1][y-1] = maze[x-1][y+1] = space
			x = x-2
			keychain.append(key)
			return x
			return keychain
	elif key == 3:
		if y > 4 and maze[x][y-4] == full:
			maze[x][y-1] = maze[x][y-2] = maze[x][y-3] = space
			y = y-4
			keychain.append(key)
			return y
			return keychain
	else:
		print ('exception')




#выход из тупика
def recheck_direction():
	global x
	global y
	global keychain
	if check_dead_end() == 'yes':
		last_key = keychain[-1]
		if last_key == 0:
			x = x-2
			del keychain[-1]
			return x
			return keychain
			return recheck_direction()
		elif last_key == 1:
			y = y-4
			del keychain[-1]
			return y
			return keychain
			return recheck_direction()
		elif last_key == 2:
			x = x+2
			del keychain[-1]
			return x
			return keychain
			return recheck_direction()
		elif last_key == 3:
			y = y+4
			del keychain[-1]
			return y
			return keychain
			return recheck_direction()

	elif check_dead_end() == 'no':
		return x
		return y
		return keychain



#вводные

space = ' '
full = 'x'
line_hor = '_'
line_ver = '|'

'''
space = u'\u0020'.encode('utf-8')
full = u'\u2573'.encode('utf-8')
line_hor = u'\u2501'.encode('utf-8')
line_ver = u'\u2503'.encode('utf-8')
cross = u'\u254B'.encode('utf-8')
right = u'\u2523'.encode('utf-8')
left = u'\u252B'.encode('utf-8')
down = u'\u2533'.encode('utf-8')
up = u'\u253B'.encode('utf-8')
corner_up_left = u'\u2513'.encode('utf-8')
corner_up_right = u'\u250F'.encode('utf-8')
corner_down_left = u'\u251B'.encode('utf-8')
corner_down_right = u'\u2517'.encode('utf-8')
'''

#канва лабиринта

n = int(input('Input maze width: '))
a = [line_ver, space, full, space]

shir = len(a) * n -1
dlin = shir//2

maze = [a * n for x in range(dlin)]
for x in range(0, dlin, 2):
	for y in range(0, shir, 2):
		maze[x][y] = line_hor
		maze[x][y+1] = line_hor


for x in range(dlin):
	maze[x][-1:-1] = maze[x][-1]
	maze[x][0] = maze[x][-1] = line_ver


#вход и выход лабиринта	
x = 1
y = 2
key = 5
keychain = []
maze[1][2] = space
maze[1][0] = maze[-1][-2] = maze[-1][-3] = maze[-1][-4] = space

##################### MAIN ############################
##################### MAIN ############################
while check_possibility(full) == 'yes':

	maze[x][y] = space

	if check_dead_end() == 'no':
		check_direction()

	elif check_dead_end() == 'yes':
		recheck_direction()
##################### MAIN ############################
##################### MAIN ############################
		
'''
################# прихорашиваем #######################	
# сливаем соседние вертикали
for x in range(1, dlin-2, 2):
	for y in range(0, shir, 2):
		if maze[x][y] == line_ver and maze[x+2][y] == line_ver:
			maze[x+1][y] = line_ver

# ответвления вверх и вниз		
for x in range(0, dlin, 2):
	for y in range(0, shir-1, 2):
		if maze[x][y] == line_hor:
			if x+1<dlin and maze[x+1][y] == line_ver:
				maze[x][y] = down
			elif x>1 and maze[x-1][y] == line_ver:
				maze[x][y] = up

# ответвления направо и налево, перекрестки
for x in range(1, dlin-1):
	for y in range(0, shir+2, 2):
		if maze[x][y] == line_ver:
			if maze[x-1][y] == line_ver and maze[x+1][y] == line_ver:
				if 2 < y < shir+1 and maze[x][y-1] == line_hor and maze[x][y+1] == line_hor:
					maze[x][y] = cross
				elif 2 < y and maze[x][y-1] == line_hor:
					maze[x][y] = left
				elif y < shir-2 and maze[x][y+1] == line_hor:
					maze[x][y] = right

# углы и кончики
for x in range(1, dlin-1, 2):
	for y in range(4, shir, 4):
		if x >= 1 and y >= 2 and maze[x][y] == line_ver and maze[x-1][y] == down:
			if maze[x-1][y-1] != maze[x-1][y+1]:
				if maze[x-1][y-1] == line_hor:
					maze[x-1][y] = corner_up_left
				elif maze[x-1][y+1] == line_hor:
					maze[x-1][y] = corner_up_right
			elif maze[x-1][y-1] == maze[x-1][y+1] == space:
				maze[x-1][y] = u'\u257B'.encode('utf-8')

		if x < dlin-1 and y < shir and maze[x][y] == line_ver and maze[x+1][y] == up:
			if maze[x+1][y-1] != maze[x+1][y+1]:
				if maze[x+1][y-1] == line_hor:
					maze[x+1][y] = corner_down_left
				elif maze[x+1][y+1] == line_hor:
					maze[x+1][y] = corner_down_right
			elif maze[x+1][y-1] == maze[x+1][y+1] == space:
				maze[x+1][y] = u'\u2579'.encode('utf-8')

maze[0][0] = corner_up_right
maze[0][-1] = corner_up_left
maze[-1][0] = corner_down_right
maze[-1][-1] = corner_down_left
################# прихорашиваем #######################	
'''

f = open('maze_output.html', 'w')
maze_source = open('maze_source2.html', 'r')
f.write(maze_source.read())
maze_source.close()

pattern_width = 40 #это чтобы правильно задать ширину подложки


#выбираем рандомный цвет из спец. файла (можно пополнять)
z = open('web_colors.txt')
A = z.read().replace('\t', ' ').replace('\n', ' ').split(' ')
background_color = str(A[random.randint(0, len(A))])
z.close()

#стиль подложки с переменными, поэтому тут
f.write('\n' + '    width: ' + str(n*pattern_width+pattern_width//4) + 'px;' + '\n' + '    height: ' + str(n*pattern_width-pattern_width*3//4) + 'px;' + '\n' +
 '    background: #' + background_color + ';\n' +  '}' + '\n' + ' </style>' + '\n' + ' </head>'  + '\n' + ' <body>'  + '\n' + '  <div id="maze" class="main">' + '\n')
for x in range(dlin):
	for y in range(shir+2):
		if maze[x][y] == line_ver:
			if x % 2 == 0:
				f.write('   <div class="corner"></div>' + '\n')
			else:
				f.write('   <div id="' + 'wall_' + str(x//2+1) + '_' + str(y//4+1) + '", class="line_ver"></div>' + '\n')
		elif maze[x][y] == line_hor:
			if y % 4 == 0:
				f.write('   <div class="corner"></div>' + '\n')
			elif (y+1) % 4 == 0:
				f.write('   <div class="line_hor_3"></div>' + '\n')
			elif y % 2 == 0:
				f.write('   <div id="' + 'ceil_' + str(x//2+1) + '_' + str(y//4+1) + '", class="line_hor_2"></div>' + '\n')
			else:
				f.write('   <div class="line_hor_1"></div>' + '\n')
		elif maze[x][y] == space:
			if x % 2 == 0:
				f.write('   <div class="space"></div>' + '\n')
			elif y % 2 == 0 and y % 4 != 0:
				f.write('   <div id="' + 'cell_' + str(x//2+1) + '_' + str(y//4+1) + '", class="runner invsbl"></div>' + '\n') #координаты ряд_столбец
			else:
				f.write('   <div class="high_space"></div>' + '\n')
		else:
			f.write('   <div class="corner"></div>' + '\n')



'''f.write('  </div>' + '\n' + ' </body>' + '\n' + '</html>')'''
f.write('  </div>' + '\n')
f.close()

f = open ('maze_output.html', 'ab')
b = open('js.txt')
f.write(b.read())
b.close()
f.close()



'''
#вывод лабиринта
for row in maze:
	 print(''.join(list(map(str, row))))'''