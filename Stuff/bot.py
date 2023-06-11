# BotTurn /--------------------------------------------------------------------------------------\
import helper as hp
import random

def bot_turn(win,grid_table,bot_table,client_table):

	# Pick Winning position
	for i in range(len(grid_table)):
		win_table = bot_table[:]

		if win_table[i-1] == 0:
			win_table[i-1] = 2

			if hp.check_win(win_table,2) == False:
				hp.draw_circle(win,grid_table[i-1])
				client_table.append(grid_table[i-1])
				bot_table[i-1] = 2
				return client_table,bot_table
			else:
				win_table[i-1] = 3

	# Sees if Opponet is gonna win
	for i in range(len(grid_table)):
		block_grid_table = bot_table[:]

		if block_grid_table[i-1] == 0:
			block_grid_table[i-1] = 1

			if hp.check_win(block_grid_table,1) == False:
				hp.draw_circle(win,grid_table[i-1])
				client_table.append(grid_table[i-1])
				bot_table[i-1] = 2
				return client_table,bot_table
			else:
				block_grid_table[i-1] = 3

	# Random on the free spaces
	while (True):
		r = random.randrange(0,4)

		if r == 1:
			# Mid
			if hp.if_repeat(grid_table[4],client_table) != True:
				client_table.append(grid_table[4])
				bot_table[4] = 2
				hp.draw_circle(win,grid_table[4])
				return client_table,bot_table
		elif r == 2:
			# Corners
			for i in [0,2,6,8]:
				if hp.if_repeat(grid_table[i],client_table) != True:
					client_table.append(grid_table[i])
					bot_table[i] = 2
					hp.draw_circle(win,grid_table[i])
					return client_table,bot_table
		elif r == 3:
			# OuterMid
			for i in [1,3,5,7]:
				if hp.if_repeat(grid_table[i],client_table) != True:
					client_table.append(grid_table[i])
					bot_table[i] = 2
					hp.draw_circle(win,grid_table[i])
					return client_table,bot_table