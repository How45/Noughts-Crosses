import helper as hp
# Player One /--------------------------------------------------------------------------------------\
def cross_point(win,lst,table,c_list):
	check_same = False
	index = 0

	while index != 1:
		table_pos = 0
		user = win.getMouse()

		for i in lst:
			if user.x>i[0] and user.y>i[1] and user.x<i[2] and user.y<i[3]:
				check_same = hp.CheckIfRepeat(i,c_list)
				break
			else:
				table_pos += 1

		if check_same == False:
			c_list.append(i)
			table[table_pos] = 1
			hp.draw_cross(win,i)
			index = 1

		elif check_same == True:
			print("Can't do it there")

	return c_list,table
# PlayerTwo /--------------------------------------------------------------------------------------\
def cirlce_point(win,lst,table,c_list):
	check_same = False
	index = 0

	while index == 0:
		table_pos = 0
		user = win.getMouse()

		for i in lst:
			if user.x>i[0] and user.y>i[1] and user.x<i[2] and user.y<i[3]:
				check_same = hp.CheckIfRepeat(i,c_list)
				break
			else:
				table_pos += 1

		if check_same == False:
			c_list.append(i)
			table[table_pos] = 2
			hp.draw_circle(win,i)
			index = 1

		elif check_same == True:
			print("Can't do it there")

	return c_list,table