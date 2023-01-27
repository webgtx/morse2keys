from pynput import keyboard
from pynput.keyboard import Key
from time import sleep 

input_buffer = [None, None, None]
controller = keyboard.Controller()
mod_key = Key.ctrl_r

def combination2key(mod, option, key, timeout):
	if input_buffer[1] == mod and input_buffer[0] == option:
		print("emulate virtual key")
		sleep(timeout)
		controller.tap(key)

def on_press(self):
	if len(input_buffer) >= 2: input_buffer.pop() 
	input_buffer.insert(0, self)

	print(input_buffer)

	# if self == Key.esc:
	# 	exit(0)

	combination2key(
		mod=mod_key,
		option=Key.alt_l,
		key="Z",
		timeout=.5
	)

	combination2key(
		mod=mod_key,
		option=Key.shift_l,
		key="z",
		timeout=.5
	)

	combination2key(
		mod=mod_key,
		option=Key.ctrl_l,
		key="4",
		timeout=.5
	)

with keyboard.Listener(on_press=on_press) as l:
	l.join()
