from graphics import *
# Checking Stuff /--------------------------------------------------------------------------------------\
def if_repeat(table,client_table):
	for i in client_table:
		if table == i:
			return True
	return False

def check_win(window_table,num):

	if (window_table[0] == num and window_table[1] == num and window_table[2] == num) or (window_table[3] == num and window_table[4] == num and window_table[5] == num) or (window_table[6] == num and window_table[7] == num and window_table[8] == num) or (window_table[0] == num and window_table[3] == num and window_table[6] == num) or (window_table[1] == num and window_table[4] == num and window_table[7] == num) or (window_table[2] == num and window_table[5] == num and window_table[8] == num) or (window_table[0] == num and window_table[4] == num and window_table[8] == num) or (window_table[2] == num and window_table[4] == num and window_table[6] == num):
		return False

	return True

def check_draw(window_table):
	draw = 0
	for i in window_table:
		if i != 0:
			draw += 1

		if draw == 9:
			return False
	return True

# Drawing things
# Draw Circle /--------------------------------------------------------------------------------------\
def draw_circle(win,table):
	circle = Circle(Point(table[0]+50,table[1]+50),50)
	circle.draw(win)
# Draw Cross /--------------------------------------------------------------------------------------\
def draw_cross(win,table):
	line = Line(Point(table[0],table[1]),Point(table[2],table[3]))
	line.draw(win)

	line2 = Line(Point(table[0],table[3]),Point(table[2],table[1]))
	line2.draw(win)
# Grid /--------------------------------------------------------------------------------------\
def grid_layout(win):
	table = []

	for column in range(0,300,100):
		for row in range(0,300,100):
			temp_table = []
			temp_table.extend([row,column,row+100,column+100])

			square = Rectangle(Point(row, column), Point(row+100, column+100))
			square.draw(win)

			table.append(temp_table)

	return table