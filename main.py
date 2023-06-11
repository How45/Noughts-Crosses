import helper as hp
import bot
import players as pl

def main():
	win = hp.GraphWin("Noughts&Crosses",300,300)
	win_grid = [0,0,0,
			   0,0,0,
			   0,0,0] # Contaias the points were the player has placed something (Atm no one has done anything)

	list_grid_layout = hp.grid_layout(win) # [[0,0,100,100],[100,0,200,200],...,[200,200,300,300]]
	check_list = [] # This will look like list_grid_layout if there is a draw (A cord is added each time a player places a X or O)
	draw = 0

	bot_or_not = int(input("Play with Bot [1] or Player2 [2]: "))
	if bot_or_not != 1 and bot_or_not != 2:
		print("Invaild")
		main()

	while(True):

		check_list, win_grid = pl.cross_point(win,list_grid_layout,win_grid,check_list)
		winner = hp.check_win(win_grid,1)
		draw = hp.CheckDraw(win_grid)

		if winner == False:
			print("X Won!")
			win.close()
			break

		if draw == False:
			print("Draw")
			win.close()
			break

		if bot_or_not == 2:
			check_list, win_grid = pl.cirlce_point(win,list_grid_layout,win_grid,check_list)
		elif bot_or_not == 1:
			check_list, win_grid = bot.bot_turn(win,list_grid_layout,win_grid,check_list)
		winner = hp.CheckWin(win_grid,2)

		if winner == False:
			print("O Won!")
			win.close()
			break

	again = input("GG, Play Again (Y/N): ")
	if again.lower() == "y" or again.lower() == "yes":
		main()
	else:
		print("Bye")

if __name__ == ("__main__"):
	main()
