#-*- coding:utf-8 -*-

import tkinter as tk
#from tkinter import tix
from tkinter import ttk

class mainWindow(object):
	def __init__(self, master=None):
		self.root = master
		self.windowInit()
		self.createMenu()
		self.decorateBar()
		self.parameterSetting()
		self.reserveFunc()
		self.processDisplay()
		
	def windowInit(self):
		self.root.title('Data Processor & Calculator')
		self.root.attributes('-alpha', 0.96)
		
		# set the window size and position
		screenWidth, screenHeight = self.root.maxsize()
		self.root.winWidth = 0.5 * screenWidth
		self.root.winHeight = 0.5 * screenHeight
		self.root.geometry('%dx%d+%d+%d' % (self.root.winWidth, self.root.winHeight, (screenWidth - self.root.winWidth)/2, (screenHeight - self.root.winHeight)/2))
	
	def createMenu(self):
		# the toplevel menu
		self.menubar = tk.Menu(self.root)
		
		def func():
			print('testing...')
		
		# create the Filemenu
		filemenu = tk.Menu(self.menubar, tearoff=0)
		filemenu.add_command(label='Open...', command=func)
		filemenu.add_command(label='Save', command=func)
		filemenu.add_command(label='Save as...', command=func)
		filemenu.add_command(label='Close', command=func)
		filemenu.add_separator()
		filemenu.add_command(label='Print', command=func)
		filemenu.add_separator()
		filemenu.add_command(label='Exit', command=self.root.quit)
		self.menubar.add_cascade(label='File', menu=filemenu)
		
		# create the Editmenu
		editmenu = tk.Menu(self.menubar, tearoff=0)
		editmenu.add_command(label='Undo', command=func)
		editmenu.add_command(label='Redo', command=func)
		editmenu.add_separator()
		editmenu.add_command(label='Cut', command=func)
		editmenu.add_command(label='Copy', command=func)
		editmenu.add_command(label='Paste', command=func)
		editmenu.add_command(label='Delete', command=func)
		self.menubar.add_cascade(label='Edit', menu=editmenu)
		
		# create the Helpmenu
		helpmenu = tk.Menu(self.menubar, tearoff=0)
		helpmenu.add_command(label='Documentation', command=func)
		helpmenu.add_separator()
		helpmenu.add_command(label='About...', command=func)
		self.menubar.add_cascade(label='Help', menu=helpmenu)

		self.root.config(menu=self.menubar)
		
	def decorateBar(self):
		self.decorateArea = ttk.Frame(self.root)
		self.decorateArea.pack(fill='both')
		
		decorateStyle = ttk.Style()
		decorateStyle.configure('dS.TLabel', background='#B0E0E6')
		self.decorateArea = ttk.Label(self.decorateArea, text='\n', width=self.root.winWidth, style='dS.TLabel', state='readonly')
		# ttk 中Label的'height'属性无法使用，用'\n\n'进行换行增加区域高度

		self.decorateArea.pack(fill='both', pady=3)
		
	def parameterSetting(self):
		self.parameterArea = ttk.Frame(self.root)
		self.parameterArea.pack(anchor='w', fill='x', pady=11)
		self.parameterArea_left = ttk.Frame(self.parameterArea)
		self.parameterArea_right = ttk.Frame(self.parameterArea)
		
		self.modeTuple = ('Data arrangement', 'Data calculate', 'Others')
		
		# 数据处理模式
		self.processMode = ttk.Combobox(self.parameterArea_left, width=18, justify='center', values=self.modeTuple, font=('华文楷体'), state='readonly')
		self.processMode.current(0)
		self.processMode.pack(side='left', padx=4)
		
		#-------------------------------------------------------------------------------
		# 根据数据处理模式的不同，显示不同的参数设置
		self.processSymbol = ttk.Combobox(self.parameterArea_left, width=10, justify='center', values=self.modeTuple, font=('华文楷体'), state='readonly')
		self.processSymbol.current(1)
		self.processSymbol.pack(side='left', padx=4)
		
		self.processNumInALine = ttk.Combobox(self.parameterArea_left, width=18, justify='center', values=self.modeTuple, font=('华文楷体'))
		self.processNumInALine.current(2)
		self.processNumInALine.pack(padx=4)
		#-------------------------------------------------------------------------------
		self.parameterArea_left.pack(side='left')
		
		def func():
			print('testing...')
		
		# 数据处理启动控制
		buttonStyle = ttk.Style()
		buttonStyle.configure('BT.TButton', font=('Arial', 11), bd=0, foreground='#B8860B')
		self.processStart = ttk.Button(self.parameterArea_right, text='RUN', style='BT.TButton', command=func)
		self.processStart.pack()
		
		self.parameterArea_right.pack(side='right', padx=22)
		
	def reserveFunc(self):
		# 预留功能区
		self.reserveArea = ttk.Frame(self.root)
		self.reserveArea.pack(fill='both')
		
		labelStyle = ttk.Style()
		labelStyle.configure('lS.TLabel', background='#F5F5DC')
		self.reserveLabel = ttk.Label(self.reserveArea, text='\n\n\n', width=self.root.winWidth, style='lS.TLabel', state='readonly')
		# ttk 中Label的'height'属性无法使用，用'\n\n'进行换行增加区域高度
		# self.reserveLabel = tk.Label(self.reserveArea, width=int(self.root.winWidth), height=5,  state='disabled', bg='#D3D3D3')
		self.reserveLabel.pack(fill='both', pady=3)
		
	def processDisplay(self):
		self.processArea = ttk.Frame(self.root)
		self.processArea.pack(fill='both', pady=9)
		self.processArea_left = ttk.Frame(self.processArea)
		self.processArea_right = ttk.Frame(self.processArea)
		
		# 窗口宽度除以字体大约长度，再除以2平分
		displayWidth = int(self.root.winWidth / 10 / 2)
		
		self.dataBeforeProcess = tk.Text(self.processArea_left, width=displayWidth, height=16, bd=1, font=('Arial', 12))
		self.dataBeforeProcess.pack()
		self.processArea_left.pack(side='left')
		
		self.dataAfterProcess = tk.Text(self.processArea_right, width=displayWidth, height=16, bd=1, font=('Arial', 12), state='disabled')
		self.dataAfterProcess.pack()
		self.processArea_right.pack(side='right')
		

def main():
	root = tk.Tk()
	#version = root.tk.eval('package require Tix')
	#print(version)		# display for test
	mainWindow(root)
	root.mainloop()
		
if __name__ == '__main__':
	main()
