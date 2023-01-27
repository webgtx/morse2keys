from pynput import keyboard
from pynput.keyboard import Key
from time import perf_counter

timepoint = perf_counter()
counter = 0 

def on_release(self):
	global counter
	global timepoint

	if self == Key.ctrl_r:
		second = round(perf_counter() - timepoint)
		counter += 1 
		if counter > 2 or second > 2:
			print(second, self)
			counter = 0
			timepoint = perf_counter()

with keyboard.Listener(on_release=on_release) as l:
	l.join()
