import sys
import glob
import serial

import tkinter as tk
from tkinter import ttk

def serial_ports():
		""" Lists serial port names

				:raises EnvironmentError:
						On unsupported or unknown platforms
				:returns:
						A list of the serial ports available on the system
		"""
		if sys.platform.startswith('win'):
				ports = ['COM%s' % (i + 1) for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
				# this excludes your current terminal "/dev/tty"
				ports = glob.glob('/dev/tty[A-Za-z]*')
		elif sys.platform.startswith('darwin'):
				ports = glob.glob('/dev/tty.*')
		else:
				raise EnvironmentError('Unsupported platform')

		result = []
		for port in ports:
				try:
						s = serial.Serial(port)
						s.close()
						result.append(port)
				except (OSError, serial.SerialException):
						pass
		return result



def com_changed(event):
	print(TK_COM_PORT.get())

### Main Program ###
root = tk.Tk()
root.geometry("300x200")
root.title("Feedback Module Testing App")

COM_PORTS = serial_ports()
TK_COM_PORT = tk.StringVar(root)
TK_COM_PORT.set([COM_PORTS[0]])
print(COM_PORTS[0])

frm = ttk.Frame(root, padding=10)
frm.grid()

label = ttk.Label(frm, text=TK_COM_PORT).grid(column=0, row=0)
label.grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# select
ttk.Label(frm, text="Please select a COM port: ").grid(column=1, row=1)

com_select = ttk.Combobox(root, values=COM_PORTS, state="readonly", textvariable=TK_COM_PORT)
com_select.bind("<<ComboboxSelected>>", com_changed)
com_select.grid(column=0, row=1)

root.mainloop()