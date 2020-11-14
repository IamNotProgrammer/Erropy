#!/usr/bin/python3

from sympy import *
import numpy as np
import curses as cs
import curses.panel as csp

"""
fun = input("Funkcja: ") ;

s = ['x', 'y'] ;

x = np.zeros(2) ;
dx = np.zeros(2) ;

x[0] = symbols(s[0]) ;
x[1] = symbols(s[1]) ;

f = sympify(fun) ;

c = diff(f, x[0]) ;

g = pretty( c ) ;

print(g) ;
"""


######################
## SOME BS SETTINGS ##

scr = cs.initscr() ;

# colurs for buttons and everything

cs.start_color() ;
cs.init_pair(1, cs.COLOR_BLACK, cs.COLOR_WHITE) ;
cs.init_pair(2, cs.COLOR_GREEN, cs.COLOR_RED) ;
cs.init_pair(3, cs.COLOR_BLACK, cs.COLOR_BLUE) ;
cs.init_pair(4, cs.COLOR_BLACK, cs.COLOR_WHITE) ;
cs.init_pair(5, cs.COLOR_BLACK, cs.COLOR_GREEN) ;
cs.noecho() ;

scr.bkgd( ' ', cs.color_pair(3) ) ;
scr.addstr( 1, 2, "Function", cs.color_pair(1) ) ;
scr.addstr( 6, 2, "Result", cs.color_pair(1) )  ;

height, width = scr.getmaxyx() ;

fx = 1 ;
fy = 2 ;
fw = width - 30 ;

# buttons

buttons = ["EXIT", "CHECK", "NEXT"]

scr.addstr( 1, fw + 10, "EXIT", cs.color_pair(4) ) ;
scr.addstr( 3, fw + 3, "CHECK", cs.color_pair(5) ) ;
scr.addstr( height - 3, fw + 3, "NEXT", cs.color_pair(4) ) ;

butt_sel = 1 ; #selected button
butt_num = len(buttons) ; # number of buttons

fb = cs.newwin(3, fw, fy, fx) ;
fb.border() ;
fb.bkgd( ' ', cs.color_pair(2) ) ;

fun = cs.newwin( 1, fw - 2, fy + 1, fx + 1) ;
fun.move(0, 0) ;
fun.keypad(True) ;
fun.bkgd( ' ', cs.color_pair(1) ) ;

check = cs.newwin(height - 10, fw - 2, fy + 6, fx + 1) ;
check.bkgd( ' ', cs.color_pair(1) ) ;

check_box = cs.newwin(height - 8, fw, fy + 5, fx) ;
check_box.border() ;
check_box.bkgd( ' ', cs.color_pair(2) ) ;

scr.refresh() ;
fb.refresh() ;
fun.refresh() ;
check_box.refresh() ;
check.refresh() ;

fun.move(0, 0) ;

cx = 0 ;
cy = 0 ;
n = 0 ;

end = False ;


##################
## FIRST SCREEN ##

while True:

	key = fun.getch() ;

	if key == 27:
		break ;


	elif key == cs.KEY_LEFT:
		if cx > 0:
			cx = cx - 1 ;
			fun.move(cy, cx) ;

	
	elif key == cs.KEY_UP:
		if butt_sel > 0:
			if butt_sel == 1:
				scr.addstr( 3, fw + 3, buttons[1], cs.color_pair(4) ) ;
				scr.addstr( 1, fw + 10, buttons[0], cs.color_pair(5) ) ;

			elif butt_sel == butt_num - 1: 
				scr.addstr( 3, fw + 3, buttons[1], cs.color_pair(5) ) ;
				scr.addstr( height - 3, fw + 3, buttons[butt_num - 1], cs.color_pair(4) ) ;
	
			butt_sel = butt_sel - 1 ;

			fun.move(cy, cx) ;
			scr.refresh() ;			


	elif key == cs.KEY_DOWN:
		if butt_sel < butt_num - 1:
			if butt_sel == 0:
				scr.addstr( 3, fw + 3, buttons[1], cs.color_pair(5) ) ;
				scr.addstr( 1, fw + 10, buttons[0], cs.color_pair(4) ) ;

			elif butt_sel == butt_num - 2: 
				scr.addstr( 3, fw + 3, buttons[1], cs.color_pair(4) ) ;
				scr.addstr( height - 3, fw + 3, buttons[butt_num - 1], cs.color_pair(5) ) ;
	
			butt_sel = butt_sel + 1 ;

			fun.move(cy, cx) ;
			scr.refresh() ;			


	elif key == cs.KEY_RIGHT:
		if cx < n:
			cx = cx + 1 ;
			fun.move(cy, cx) ;


	elif key == 127:
		if cx > 0:
			cx = cx - 1 ;
			fun.move(cy, cx) ;
			fun.delch(cy, cx) ;
			n = n - 1 ;


	elif key == 10:

		if butt_sel == 0:
			end = True ;
			break ;

		elif butt_sel == 1:

			check.clear() ;

			g = str( fun.instr(0, 0, n) ) ;

			try:		
				f = sympify(g[2:-1]) ;
				s = pretty(f) ;

			except Exception as err:
				s = "Error!\n\n" ;
				s = s + str(err) ;

			check.move(0, 0) ;
			check.addstr(s) ;

			check.refresh() ;
			fun.move(cy, cx) ;

		elif butt_sel == butt_num - 1:
			break ;


	else:
		if cx < (fw - 3) and n < (fw - 3):
			s = fun.instr(cy, cx, n - cx) ;
			fun.addch(key) ;
			cx = cx + 1 ;
			fun.addstr(cy, cx, s) ;
			fun.move(cy, cx) ;
			n = n + 1 ;


###################
## SECOND SCREEN ##


cs.endwin() ;











