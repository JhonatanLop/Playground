# pip install windows-curses
import curses
import time

stdscr = curses.initscr()
cont = 0

ok = input("isso é um teste? s/n")

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

start = time.time()
a = time.sleep(2)
try:
    while cont < 2:
        stdscr.addstr(0, 0, "Loading:")
        stdscr.addstr(0, 10, "\\")
        stdscr.refresh()
        time.sleep(0.1)
        stdscr.addstr(0, 10, "|")
        stdscr.refresh()
        time.sleep(0.1)
        stdscr.addstr(0, 10, "/")
        stdscr.refresh()
        time.sleep(0.1)
        stdscr.addstr(0, 10, "-")
        stdscr.refresh()
        time.sleep(0.1)
        cont +=1
finally:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

print ("aaaaaaaaaaa")