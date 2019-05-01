import tkinter as tk
from tkinter import ttk
from tkinter import *
import tempfile
import sys
import os

cdl = os.getcwd()

def main():
	root = tk.Tk()

	root.geometry("550x385+700+300")
	root.iconbitmap("{}\\img\\Icon.ico".format(cdl))
	root.title("Lib-Farm")
	root.configure(bg="white")
	root.wm_attributes('-alpha',0.9)
	ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
	        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
	        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64
	_, ICON_PATH = tempfile.mkstemp()
	with open(ICON_PATH, 'wb') as icon_file:icon_file.write(ICON)
	root.iconbitmap(default=ICON_PATH)
	#------------------------------------------------------------------------------------
	def Packages_module():
		large_font = ('Calibri',19)
		large_font1 = ('Bahnschrift',19)
		large_font2 = ('Bahnschrift',15)
		large_font3 = ('Bahnschrift',12)
		bg1install = "gray18"
		bg2unistall = "gray35"
		bg1 = "White"
		bg2 = "gray88"
		fg1 = "gray1"
		text = tk.Text(root, width="66", selectbackground="white")
		text.configure(bg="White")
		scrollbar = tk.Scrollbar(root, command=text.yview)
		text.configure(yscrollcommand=scrollbar.set)
		scrollbar.grid(row=0,column=1,sticky=tk.NS+tk.W)
		text.grid(row=0,column=0)
		Install = tk.PhotoImage(file= "{}\\img\\I6.gif".format(cdl))
		Uninstall = tk.PhotoImage(file="{}\\img\\I7.png".format(cdl))
		Back = tk.PhotoImage(file="{}\\img\\I8.png".format(cdl))
		Packagelogo = tk.PhotoImage(file="{}\\img\\I3.png".format(cdl))
		P1 = tk.PhotoImage(file="{}\\img\\numpy.png".format(cdl))
		P2 = tk.PhotoImage(file="{}\\img\\pandas.png".format(cdl))
		P3 = tk.PhotoImage(file="{}\\img\\keras.png".format(cdl))
		P4 = tk.PhotoImage(file="{}\\img\\matplotlib.png".format(cdl))
		P5 = tk.PhotoImage(file="{}\\img\\django.png".format(cdl))
		P6 = tk.PhotoImage(file="{}\\img\\flask.png".format(cdl))
		P7 = tk.PhotoImage(file="{}\\img\\pypi.png".format(cdl))	
		P8 = tk.PhotoImage(file="{}\\img\\OpenCV.png".format(cdl))	
		P9 = tk.PhotoImage(file="{}\\img\\Tensorflow.png".format(cdl))	
		P10 = tk.PhotoImage(file="{}\\img\\theano.png".format(cdl))
		P11 = tk.PhotoImage(file="{}\\img\\requests.png".format(cdl))
		P12 = tk.PhotoImage(file="{}\\img\\pyinstaller.png".format(cdl))
		P13 = tk.PhotoImage(file="{}\\img\\pillow.png".format(cdl))
		P14 = tk.PhotoImage(file="{}\\img\\scipy.png".format(cdl))
		P15 = tk.PhotoImage(file="{}\\img\\pygame.png".format(cdl))
		P16 = tk.PhotoImage(file="{}\\img\\sympy.png".format(cdl))
		P17 = tk.PhotoImage(file="{}\\img\\pyglet.png".format(cdl))
		P18 = tk.PhotoImage(file="{}\\img\\pywin32.png".format(cdl))
		P19 = tk.PhotoImage(file="{}\\img\\twisted.png".format(cdl))
		P20 = tk.PhotoImage(file="{}\\img\\WxPython.png".format(cdl))
		P21 = tk.PhotoImage(file="{}\\img\\statsmodels.png".format(cdl))
		P22 = tk.PhotoImage(file="{}\\img\\Bokeh.png".format(cdl))
		P23 = tk.PhotoImage(file="{}\\img\\scikit learn.png".format(cdl))
		P24 = tk.PhotoImage(file="{}\\img\\pytorch.png".format(cdl))
		P25 = tk.PhotoImage(file="{}\\img\\NLTK.png".format(cdl))
		P26 = tk.PhotoImage(file="{}\\img\\Scapy.png".format(cdl))
		P27 = tk.PhotoImage(file="{}\\img\\kivy.png".format(cdl))
		P28 = tk.PhotoImage(file="{}\\img\\lightgbm.png".format(cdl))
		P29 = tk.PhotoImage(file="{}\\img\\eli5.png".format(cdl))
		P30 = tk.PhotoImage(file="{}\\img\\sqlalchemy.png".format(cdl))
		P31 = tk.PhotoImage(file="{}\\img\\apachespark.png".format(cdl))
		P32 = tk.PhotoImage(file="{}\\img\\selenium.png".format(cdl))
		P33 = tk.PhotoImage(file="{}\\img\\networkx.png".format(cdl))
		P34 = tk.PhotoImage(file="{}\\img\\pendulum.png".format(cdl))
		P35 = tk.PhotoImage(file="{}\\img\\ipython.png".format(cdl))
		P36 = tk.PhotoImage(file="{}\\img\\zappa.png".format(cdl))
		def scroll_enter(x):
			text.window_create("end", window=x)
			text.insert("end", "\n")

		def scroll_pass(x):
			text.window_create("end", window=x)

		#--------------------------------------------------------------------------------------------------------------
		def back():
			root.destroy()
			main()
		back = tk.Button(root, image=Back,command=back,borderwidth=0,highlightthickness=0)
		back.grid(column=4)
		scroll_pass(back)
		Blank = tk.Label(root, width="2",bg=bg2, height="1", font=large_font, anchor=W)
		Blank.grid(column=1)
		scroll_pass(Blank)
		L = tk.Label(root, width="3",bg=bg2, height="1", font=large_font, anchor=E)
		L.grid(row=0,sticky=tk.NS+tk.EW)
		scroll_pass(L)
		Blank = tk.Label(root, text=" PYTHON", width="7",bg=bg2, height="1", font=large_font, anchor=W)
		Blank.grid(column=1)
		scroll_pass(Blank)
		blank = tk.Label(root, text="LIBRARY", width="23",bg=bg2, height="1", font=large_font, anchor=W)
		blank.grid(column=2)
		scroll_enter(blank)
		#------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)

		logo = tk.Label(root, borderwidth=0,image=P1)
		logo.grid(column=0)
		scroll_pass(logo)

		numpy = tk.Label(root, text="  NumPy", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		numpy.grid(column=1)
		scroll_pass(numpy)

		def numpy():
			os.system("start /wait cmd /c (pip install numpy)")
		button = tk.Button(root, image=Install, command=numpy,borderwidth=0,highlightthickness=0,)
		button.grid(column=2)
		scroll_pass(button)

		def numpy():
			os.system("start /wait cmd /c (pip uninstall numpy)")
		button = tk.Button(root, image=Uninstall, command=numpy,borderwidth=0,highlightthickness=0,)
		button.grid(column=3)
		scroll_enter(button)

		#-------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)

		logo = tk.Label(root, borderwidth=0, image=P2)
		logo.grid(column=0)
		scroll_pass(logo)

		Pandas = tk.Label(root, text="  Pandas", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Pandas.grid(column=1)
		scroll_pass(Pandas)

		def pandas():
			os.system("start /wait cmd /c (pip install pandas)")
		button = tk.Button(root,  image=Install,command=pandas,borderwidth=0,highlightthickness=0,)
		button.grid(column=2)
		scroll_pass(button)
		def pandas():
			os.system("start /wait cmd /c (pip uninstall pandas)")
		button = tk.Button(root, image=Uninstall, command=pandas,borderwidth=0,highlightthickness=0,)
		button.grid(column=3)
		scroll_enter(button)
		#------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P3)
		logo.grid(column=0)
		scroll_pass(logo)
		Keras = tk.Label(root, text="  Keras", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Keras.grid(column=1)
		scroll_pass(Keras)
		def keras():
			os.system("start /wait cmd /c (pip install keras)")

		button = tk.Button(root,  image=Install, command=keras,borderwidth=0,highlightthickness=0,)
		button.grid(column=2)
		scroll_pass(button)
		def keras():
			os.system("start /wait cmd /c (pip uninstall keras)")

		button = tk.Button(root, image=Uninstall, command=keras,borderwidth=0,highlightthickness=0,)
		button.grid(column=3)
		scroll_enter(button)
		#---------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P4)
		logo.grid(column=0)
		scroll_pass(logo)
		Matplotlib = tk.Label(root, text="  Matplotlib", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Matplotlib.grid(row=7)
		scroll_pass(Matplotlib)
		def matplotlib():
			os.system("start /wait cmd /c (pip install matplotlib)")

		button = tk.Button(root,  image=Install, command=matplotlib,borderwidth=0,highlightthickness=0,)
		button.grid(row=7,column=1)
		scroll_pass(button)
		def matplotlib():
			os.system("start /wait cmd /c (pip uninstall matplotlib)")

		button = tk.Button(root, image=Uninstall, command=matplotlib,borderwidth=0,highlightthickness=0,)
		button.grid(row=7,column=2)
		scroll_enter(button)
		#-------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P5)
		logo.grid(column=0)
		scroll_pass(logo)
		Django = tk.Label(root, text="  Django", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Django.grid(row=9)
		scroll_pass(Django)
		def django():
			os.system("start /wait cmd /c (pip install django)")

		button = tk.Button(root, image=Install, command=django,borderwidth=0,highlightthickness=0,)
		button.grid(row=9,column=1)
		scroll_pass(button)
		def django():
			os.system("start /wait cmd /c (pip uninstall django)")

		button = tk.Button(root, image=Uninstall, command=django,borderwidth=0,highlightthickness=0,)
		button.grid(row=9,column=2)
		scroll_enter(button)
		#------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P6)
		logo.grid(column=0)
		scroll_pass(logo)
		flask = tk.Label(root, text="  Flask", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		flask.grid(row=11)
		scroll_pass(flask)
		def flask():
			os.system("start /wait cmd /c (pip install flask)")

		button = tk.Button(root, image=Install, command=flask,borderwidth=0,highlightthickness=0,)
		button.grid(row=11,column=1)
		scroll_pass(button)
		def flask():
			os.system("start /wait cmd /c (pip uninstall flask)")

		button = tk.Button(root,image=Uninstall, command=flask,borderwidth=0,highlightthickness=0,)
		button.grid(row=11,column=2)
		scroll_enter(button)

		#---------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P7)
		logo.grid(column=0)
		scroll_pass(logo)
		PyPi = tk.Label(root, text="  PyPI", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		PyPi.grid(row=13)
		scroll_pass(PyPi)

		def pypi():
			os.system("start /wait cmd /c (pip install pypi)")

		button = tk.Button(root,  image=Install, command=pypi,borderwidth=0,highlightthickness=0,)
		button.grid(row=13,column=1)
		scroll_pass(button)

		def pypi():
			os.system("start /wait cmd /c (pip uninstall pypi)")

		button = tk.Button(root,image=Uninstall,command=pypi,borderwidth=0,highlightthickness=0,)
		button.grid(row=13,column=2)
		scroll_enter(button)
		#---------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P8)
		logo.grid(column=0)
		scroll_pass(logo)
		opencv = tk.Label(root, text="  OpenCV", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		opencv.grid(row=15)
		scroll_pass(opencv)

		def opencv():
			os.system("start /wait cmd /c (pip install opencv-python)")

		button = tk.Button(root, image=Install, command=opencv,borderwidth=0,highlightthickness=0,)
		button.grid(row=15,column=1)
		scroll_pass(button)

		def opencv():
			os.system("start /wait cmd /c (pip uninstall opencv-python)")

		button = tk.Button(root,image=Uninstall, command=opencv,borderwidth=0,highlightthickness=0,)
		button.grid(row=15,column=2)
		scroll_enter(button)

		#---------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P9)
		logo.grid(column=0)
		scroll_pass(logo)
		TensorFlow = tk.Label(root, text="  TensorFlow", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		TensorFlow.grid(row=17)
		scroll_pass(TensorFlow)

		def tensorflow():
			os.system("start /wait cmd /c (pip install --upgrade tensorflow)")

		button = tk.Button(root, image=Install, command=tensorflow,borderwidth=0,highlightthickness=0,)
		button.grid(row=17,column=1)
		scroll_pass(button)

		def tensorflow():
			os.system("start /wait cmd /c (pip uninstall --upgrade tensorflow)")

		button = tk.Button(root, image=Uninstall, command=tensorflow,borderwidth=0,highlightthickness=0,)
		button.grid(row=17,column=2)
		scroll_enter(button)

		#---------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P10)
		logo.grid(column=0)
		scroll_pass(logo)
		Theano = tk.Label(root, text="  Theano", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Theano.grid(row=19)
		scroll_pass(Theano)

		def theano():
			os.system("start /wait cmd /c (pip install theano)")

		button = tk.Button(root, image=Install, command=theano,borderwidth=0,highlightthickness=0,)
		button.grid(row=19,column=1)
		scroll_pass(button)

		def theano():
			os.system("start /wait cmd /c (pip uninstall theano)")

		button = tk.Button(root, image=Uninstall, command=theano,borderwidth=0,highlightthickness=0,)
		button.grid(row=19,column=2)
		scroll_enter(button)

		#---------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P11)
		logo.grid(column=0)
		scroll_pass(logo)
		Requests = tk.Label(root, text="  Requests", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Requests.grid(row=21)
		scroll_pass(Requests)

		def requests():
			os.system("start /wait cmd /c (pip install requests)")

		button = tk.Button(root, image=Install, command=requests,borderwidth=0,highlightthickness=0,)
		button.grid(row=21,column=1)
		scroll_pass(button)

		def requests():
			os.system("start /wait cmd /c (pip uninstall requests)")

		button = tk.Button(root, image=Uninstall, command=requests,borderwidth=0,highlightthickness=0,)
		button.grid(row=21,column=2)
		scroll_enter(button)

		#---------------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P12)
		logo.grid(column=0)
		scroll_pass(logo)
		PyInstaller = tk.Label(root, text="  PyInstaller", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		PyInstaller.grid(row=23)
		scroll_pass(PyInstaller)

		def pyinstaller():
			os.system("start /wait cmd /c (pip install pyinstaller)")

		button = tk.Button(root, image=Install, command=pyinstaller,borderwidth=0,highlightthickness=0,)
		button.grid(row=23,column=1)
		scroll_pass(button)

		def pyinstaller():
			os.system("start /wait cmd /c (pip uninstall pyinstaller)")

		button = tk.Button(root, image=Uninstall, command=pyinstaller,borderwidth=0,highlightthickness=0,)
		button.grid(row=23,column=1)
		scroll_enter(button)

		#------------------------------------install-library-2------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P13)
		logo.grid(column=0)
		scroll_pass(logo)
		Pillow = tk.Label(root, text="  Pillow", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Pillow.grid(row=0)
		scroll_pass(Pillow)

		def pillow():
			os.system("start /wait cmd /c (pip install pillow)")

		button = tk.Button(root, image=Install, command=pillow,borderwidth=0,highlightthickness=0,)
		button.grid(column=1)
		scroll_pass(button)

		def pillow():
			os.system("start /wait cmd /c (pip uninstall pillow)")

		button = tk.Button(root, image=Uninstall, command=pillow,borderwidth=0,highlightthickness=0,)
		button.grid(column=2)
		scroll_enter(button)

		#----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P14)
		logo.grid(column=0)
		scroll_pass(logo)
		SciPy = tk.Label(root, text="  SciPy", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		SciPy.grid(row=0)
		scroll_pass(SciPy)

		def scipy():
			os.system("start /wait cmd /c (pip install scipy)")

		button = tk.Button(root, image=Install, command=scipy,borderwidth=0,highlightthickness=0,)
		button.grid(column=1)
		scroll_pass(button)

		def scipy():
			os.system("start /wait cmd /c (pip uninstall scipy)")

		button = tk.Button(root, image=Uninstall, command=scipy,borderwidth=0,highlightthickness=0,)
		button.grid(column=2)
		scroll_enter(button)

		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P15)
		logo.grid(column=0)
		scroll_pass(logo)
		PyGame = tk.Label(root, text="  PyGame", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		PyGame.grid(row=4,column=3)
		scroll_pass(PyGame)
		def pygame():
			os.system("start /wait cmd /c (pip install pygame)")

		button = tk.Button(root, image=Install, command=pygame,borderwidth=0,highlightthickness=0,)
		button.grid(row=5,column=3)
		scroll_pass(button)
		def pygame():
			os.system("start /wait cmd /c (pip uninstall pygame)")

		button = tk.Button(root, image=Uninstall, command=pygame,borderwidth=0,highlightthickness=0,)
		button.grid(row=5,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P16)
		logo.grid(column=0)
		scroll_pass(logo)
		SymPy = tk.Label(root, text="  SymPy", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		SymPy.grid(row=6,column=3)
		scroll_pass(SymPy)
		def sympy():
			os.system("start /wait cmd /c (pip install sympy)")

		button = tk.Button(root, image=Install, command=sympy,borderwidth=0,highlightthickness=0,)
		button.grid(row=7,column=3)
		scroll_pass(button)
		def sympy():
			os.system("start /wait cmd /c (pip uninstall sympy)")

		button = tk.Button(root, image=Uninstall, command=sympy,borderwidth=0,highlightthickness=0,)
		button.grid(row=7,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P17)
		logo.grid(column=0)
		scroll_pass(logo)
		PyGlet = tk.Label(root, text="  PyGlet", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		PyGlet.grid(row=8,column=3)
		scroll_pass(PyGlet)
		def pyglet():
			os.system("start /wait cmd /c (pip install pyglet)")

		button = tk.Button(root, image=Install, command=pyglet,borderwidth=0,highlightthickness=0,)
		button.grid(row=9,column=3)
		scroll_pass(button)
		def pyglet():
			os.system("start /wait cmd /c (pip uninstall pyglet)")

		button = tk.Button(root, image=Uninstall, command=pyglet,borderwidth=0,highlightthickness=0,)
		button.grid(row=9,column=4)
		scroll_enter(button)
		#----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P18)
		logo.grid(column=0)
		scroll_pass(logo)
		pywin32 = tk.Label(root, text="  pywin32", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		pywin32.grid(row=10,column=3)
		scroll_pass(pywin32)
		def pywin32():
			os.system("start /wait cmd /c (pip install pywin32)")

		button = tk.Button(root, image=Install, command=pywin32,borderwidth=0,highlightthickness=0,)
		button.grid(row=11,column=3)
		scroll_pass(button)
		def pywin32():
			os.system("start /wait cmd /c (pip uninstall pywin32)")

		button = tk.Button(root, image=Uninstall, command=pywin32,borderwidth=0,highlightthickness=0,)
		button.grid(row=11,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P19)
		logo.grid(column=0)
		scroll_pass(logo)
		Twisted = tk.Label(root, text="  Twisted", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Twisted.grid(row=12,column=3)
		scroll_pass(Twisted)
		def twisted():
			os.system("start /wait cmd /c (pip install twisted)")

		button = tk.Button(root, image=Install, command=twisted,borderwidth=0,highlightthickness=0,)
		button.grid(row=13,column=3)
		scroll_pass(button)
		def twisted():
			os.system("start /wait cmd /c (pip uninstall twisted)")

		button = tk.Button(root, image=Uninstall, command=twisted,borderwidth=0,highlightthickness=0,)
		button.grid(row=13,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P20)
		logo.grid(column=0)
		scroll_pass(logo)
		WXPython = tk.Label(root, text="  WXPython", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		WXPython.grid(row=14,column=3)
		scroll_pass(WXPython)
		def wxpython():
			os.system("start /wait cmd /c (pip install wxpython)")

		button = tk.Button(root, image=Install, command=wxpython,borderwidth=0,highlightthickness=0,)
		button.grid(row=15,column=3)
		scroll_pass(button)
		def wxpython():
			os.system("start /wait cmd /c (pip uninstall wxpython)")

		button = tk.Button(root, image=Uninstall, command=wxpython,borderwidth=0,highlightthickness=0,)
		button.grid(row=15,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P21)
		logo.grid(column=0)
		scroll_pass(logo)
		StatsModels = tk.Label(root, text="  StatsModels", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		StatsModels.grid(row=16,column=3)
		scroll_pass(StatsModels)
		def statsmodels():
			os.system("start /wait cmd /c (pip install statsmodels)")

		button = tk.Button(root, image=Install, command=statsmodels,borderwidth=0,highlightthickness=0,)
		button.grid(row=17,column=3)
		scroll_pass(button)
		def statsmodels():
			os.system("start /wait cmd /c (pip uninstall statsmodels)")

		button = tk.Button(root, image=Uninstall, command=statsmodels,borderwidth=0,highlightthickness=0,)
		button.grid(row=17,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P22)
		logo.grid(column=0)
		scroll_pass(logo)
		Bokeh = tk.Label(root, text="  Bokeh", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Bokeh.grid(row=18,column=3)
		scroll_pass(Bokeh)
		def bokeh():
			os.system("start /wait cmd /c (pip install bokeh)")

		button = tk.Button(root, image=Install, command=bokeh,borderwidth=0,highlightthickness=0,)
		button.grid(row=19,column=3)
		scroll_pass(button)
		def bokeh():
			os.system("start /wait cmd /c (pip uninstall bokeh)")

		button = tk.Button(root, image=Uninstall, command=bokeh,borderwidth=0,highlightthickness=0,)
		button.grid(row=19,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P23)
		logo.grid(column=0)
		scroll_pass(logo)
		ScikitLearn = tk.Label(root, text="  ScikitLearn", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		ScikitLearn.grid(row=20,column=3)
		scroll_pass(ScikitLearn)
		def scikitlearn():
			os.system("start /wait cmd /c (pip install scikit-learn)")

		button = tk.Button(root, image=Install, command=scikitlearn,borderwidth=0,highlightthickness=0,)
		button.grid(row=21,column=3)
		scroll_pass(button)
		def scikitlearn():
			os.system("start /wait cmd /c (pip uninstall scikit-learn)")

		button = tk.Button(root, image=Uninstall, command=scikitlearn,borderwidth=0,highlightthickness=0,)
		button.grid(row=21,column=4)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P24)
		logo.grid(column=0)
		scroll_pass(logo)
		PyTorch = tk.Label(root, text="  PyTorch", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		PyTorch.grid(row=22,column=3)
		scroll_pass(PyTorch)
		def pytorch():
			os.system("start /wait cmd /c (pip install torchvision)")

		button = tk.Button(root, image=Install, command=pytorch,borderwidth=0,highlightthickness=0,)
		button.grid(row=23,column=3)
		scroll_pass(button)
		def pytorch():
			os.system("start /wait cmd /c (pip uninstall torchvision)")

		button = tk.Button(root, image=Uninstall, command=pytorch,borderwidth=0,highlightthickness=0,)
		button.grid(row=23,column=4)
		scroll_enter(button)
		#----------------------------------install-library-3------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P25)
		logo.grid(column=0)
		scroll_pass(logo)
		NLTK = tk.Label(root, text="  NLTK", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		NLTK.grid(row=0,column=5)
		scroll_pass(NLTK)
		def nltk():
			os.system("start /wait cmd /c (pip install nltk)")

		button = tk.Button(root, image=Install, command=nltk,borderwidth=0,highlightthickness=0,)
		button.grid(row=1,column=5)
		scroll_pass(button)
		def nltk():
			os.system("start /wait cmd /c (pip uninstall nltk)")

		button = tk.Button(root, image=Uninstall, command=nltk,borderwidth=0,highlightthickness=0,)
		button.grid(row=1,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P26)
		logo.grid(column=0)
		scroll_pass(logo)
		ScaPy = tk.Label(root, text="  ScaPy", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		ScaPy.grid(row=2,column=5)
		scroll_pass(ScaPy)
		def scapy():
			os.system("start /wait cmd /c (pip install scapy)")

		button = tk.Button(root, image=Install, command=scapy,borderwidth=0,highlightthickness=0,)
		button.grid(row=3,column=5)
		scroll_pass(button)
		def scapy():
			os.system("start /wait cmd /c (pip uninstall scapy)")

		button = tk.Button(root, image=Uninstall, command=scapy,borderwidth=0,highlightthickness=0,)
		button.grid(row=3,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P27)
		logo.grid(column=0)
		scroll_pass(logo)
		Kivy = tk.Label(root, text="  Kivy", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Kivy.grid(row=4,column=5)
		scroll_pass(Kivy)
		def kivy():
			os.system("start /wait cmd /c (pip install kivy)")

		button = tk.Button(root, image=Install, command=kivy,borderwidth=0,highlightthickness=0,)
		button.grid(row=5,column=5)
		scroll_pass(button)
		def kivy():
			os.system("start /wait cmd /c (pip uninstall kivy)")

		button = tk.Button(root, image=Uninstall, command=kivy,borderwidth=0,highlightthickness=0,)
		button.grid(row=5,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P28)
		logo.grid(column=0)
		scroll_pass(logo)
		LightGBM = tk.Label(root, text="  LightGBM", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		LightGBM.grid(row=6,column=5)
		scroll_pass(LightGBM)
		def lightgbm():
			os.system("start /wait cmd /c (pip install lightgbm)")

		button = tk.Button(root, image=Install, command=lightgbm,borderwidth=0,highlightthickness=0,)
		button.grid(row=7,column=5)
		scroll_pass(button)
		def lightgbm():
			os.system("start /wait cmd /c (pip uninstall lightgbm)")

		button = tk.Button(root, image=Uninstall, command=lightgbm,borderwidth=0,highlightthickness=0,)
		button.grid(row=7,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P29)
		logo.grid(column=0)
		scroll_pass(logo)
		Eli5 = tk.Label(root, text="  Eli5", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Eli5.grid(row=8,column=5)
		scroll_pass(Eli5)
		def eli5():
			os.system("start /wait cmd /c (pip install eli5)")

		button = tk.Button(root, image=Install, command=eli5,borderwidth=0,highlightthickness=0,)
		button.grid(row=9,column=5)
		scroll_pass(button)
		def eli5():
			os.system("start /wait cmd /c (pip uninstall eli5)")

		button = tk.Button(root, image=Uninstall, command=eli5,borderwidth=0,highlightthickness=0,)
		button.grid(row=9,column=6)
		scroll_enter(button)
		#-----------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P30)
		logo.grid(column=0)
		scroll_pass(logo)
		SQLAlchemy = tk.Label(root, text="  SQLAlchemy", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		SQLAlchemy.grid(row=10,column=5)
		scroll_pass(SQLAlchemy)
		def sqlalchemy():
			os.system("start /wait cmd /c (pip install sqlalchemy)")

		button = tk.Button(root, image=Install, command=sqlalchemy,borderwidth=0,highlightthickness=0,)
		button.grid(row=11,column=5)
		scroll_pass(button)
		def sqlalchemy():
			os.system("start /wait cmd /c (pip uninstall sqlalchemy)")

		button = tk.Button(root, image=Uninstall, command=sqlalchemy,borderwidth=0,highlightthickness=0,)
		button.grid(row=11,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P31)
		logo.grid(column=0)
		scroll_pass(logo)
		ApacheSpark = tk.Label(root, text="  ApacheSpark", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		ApacheSpark.grid(row=12,column=5)
		scroll_pass(ApacheSpark)
		def apachespark():
			os.system("start /wait cmd /c (pip install pyspark)")
		button = tk.Button(root, image=Install, command=apachespark,borderwidth=0,highlightthickness=0,)
		button.grid(row=13,column=5)
		scroll_pass(button)
		def apachespark():
			os.system("start /wait cmd /c (pip uninstall pyspark)")
		button = tk.Button(root, image=Uninstall, command=apachespark,borderwidth=0,highlightthickness=0,)
		button.grid(row=13,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P32)
		logo.grid(column=0)
		scroll_pass(logo)
		Selenium = tk.Label(root, text="  Selenium", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Selenium.grid(row=14,column=5)
		scroll_pass(Selenium)
		def selenium():
			os.system("start /wait cmd /c (pip install selenium)")
		button = tk.Button(root, image=Install, command=selenium,borderwidth=0,highlightthickness=0,)
		button.grid(row=15,column=5)
		scroll_pass(button)
		def selenium():
			os.system("start /wait cmd /c (pip uninstall selenium)")
		button = tk.Button(root, image=Uninstall, command=selenium,borderwidth=0,highlightthickness=0,)
		button.grid(row=15,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P33)
		logo.grid(column=0)
		scroll_pass(logo)
		NetworkX = tk.Label(root, text="  NetworkX", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		NetworkX.grid(row=16,column=5)
		scroll_pass(NetworkX)
		def networkx():
			os.system("start /wait cmd /c (pip install networkx)")
		button = tk.Button(root, image=Install, command=networkx,borderwidth=0,highlightthickness=0,)
		button.grid(row=17,column=5)
		scroll_pass(button)
		def networkx():
			os.system("start /wait cmd /c (pip uninstall networkx)")
		button = tk.Button(root, image=Uninstall, command=networkx,borderwidth=0,highlightthickness=0,)
		button.grid(row=17,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P34)
		logo.grid(column=0)
		scroll_pass(logo)
		Pendulum = tk.Label(root, text="  Pendulum", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Pendulum.grid(row=18,column=5)
		scroll_pass(Pendulum)
		def pendulum():
			os.system("start /wait cmd /c (pip install pendulum)")
		button = tk.Button(root, image=Install, command=pendulum,borderwidth=0,highlightthickness=0,)
		button.grid(row=19,column=5)
		scroll_pass(button)
		def pendulum():
			os.system("start /wait cmd /c (pip uninstall pendulum)")
		button = tk.Button(root, image=Uninstall, command=pendulum,borderwidth=0,highlightthickness=0,)
		button.grid(row=19,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P35)
		logo.grid(column=0)
		scroll_pass(logo)
		IPython = tk.Label(root, text="  IPython", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		IPython.grid(row=20,column=5)
		scroll_pass(IPython)
		def ipython():
			os.system("start /wait cmd /c (pip install ipython)")
		button = tk.Button(root, image=Install, command=ipython,borderwidth=0,highlightthickness=0,)
		button.grid(row=21,column=5)
		scroll_pass(button)
		def ipython():
			os.system("start /wait cmd /c (pip uninstall ipython)")
		button = tk.Button(root, image=Uninstall, command=ipython,borderwidth=0,highlightthickness=0,)
		button.grid(row=21,column=6)
		scroll_enter(button)
		#------------------------------------------------------------------------------------
		label = tk.Label(root,width="11", bg="white",height="2")
		label.grid(column=0)
		scroll_pass(label)
		logo = tk.Label(root, borderwidth=0, image=P36)
		logo.grid(column=0)
		scroll_pass(logo)
		Zappa = tk.Label(root, text="  Zappa", bg=bg1, fg=fg1, height="2", width="15", font=large_font1, anchor=W)
		Zappa.grid(row=22,column=5)
		scroll_pass(Zappa)
		def zappa():
			os.system("start /wait cmd /c (pip install zappa)")
		button = tk.Button(root, image=Install, command=zappa,borderwidth=0,highlightthickness=0,)
		button.grid(row=23,column=5)
		scroll_pass(button)
		def zappa():
			os.system("start /wait cmd /c (pip uninstall zappa)")
		button = tk.Button(root, image=Uninstall, command=zappa,borderwidth=0,highlightthickness=0,)
		button.grid(row=23,column=6)
		scroll_enter(button)

		text.config(state="disabled")
		root.resizable(width=0,height=0)
		root.mainloop()
		#---------------------------------------------------------------------------------------------
		
	def Lib_FARM_MAINFRAME():
		large_font1 = ('Bahnschrift',15)
		large_font2 = ('Bahnschrift',22)
		bg1 = ("White")
		fg1 = ("gray1")
		label = tk.Label(root, text="   Lib-Farm", bg = "gray88", width="20", height="2", fg=fg1, font=large_font2,anchor=W)
		label.grid(row=0,column=2,sticky=tk.EW)
		label = tk.Label(root, bg = "gray88", width="7", fg=fg1, font=large_font2)
		label.grid(row=0,column=3,sticky=tk.NS+tk.EW)
		label = tk.Label(root, bg = "gray88", width="7", height="2", fg=fg1, font=large_font2)
		label.grid(row=0,column=1)
		label = tk.Label(root, bg = "gray88", fg = fg1,height="4",)
		label.grid(row=0,column=0)
		label = tk.Label(root, bg = bg1, fg = fg1)
		label.grid(row=1,column=0)
		#-------------------------------------------------------------------------------------------------------------------------------------------------
		def Python_v():
			os.startfile("https://www.python.org/downloads")
		Button = tk.Button(root, text="   Download Python", bg = bg1, width="7", height="1", fg=fg1, font=large_font1, borderwidth=0, anchor=W,command=Python_v)
		Button.grid(row=2,column=2,sticky=tk.EW)
		Image01 = tk.PhotoImage(file="{}\\img\\I6.gif".format(cdl))
		label = tk.Button(root, image=Image01, borderwidth=0,highlightthickness=0, command=Python_v)
		label.grid(row=2,column=3)
		Image1 = tk.PhotoImage(file="{}\\img\\I1.png".format(cdl))
		label = tk.Label(root, image=Image1 , borderwidth=0, anchor=W)
		label.grid(row=2,column=1)
		#-------------------------------------------------------------------------------------------------------------------------------------------------
		def PIP_download():
			os.system("start /wait cmd /c (explorer https://bootstrap.pypa.io/get-pip.py)")
		Button = tk.Button(root, text="   Download PiP", width="7", height="1", bg=bg1, fg=fg1, font=large_font1,borderwidth=0,command=PIP_download,anchor=W)
		Button.grid(row=4,column=2,sticky=tk.EW)
		Image02 = tk.PhotoImage(file="{}\\img\\I6.gif".format(cdl))
		label = tk.Button(root, image=Image01, borderwidth=0,highlightthickness=0, command=PIP_download)
		label.grid(row=4,column=3)
		Image2 = tk.PhotoImage(file="{}\\img\\I2.png".format(cdl))
		label = tk.Label(root, image=Image2, borderwidth=0)
		label.grid(row=4,column=1)
		#-------------------------------------------------------------------------------------------------------------------------------------------------
		def Python_Libraries():
			Packages_module()
		Button = tk.Button(root, text="   Python Libraries", width="7", height="1", bg=bg1, fg=fg1, font=large_font1, borderwidth=0, command=Python_Libraries,anchor=W)
		Button.grid(row=6,column=2,sticky=tk.EW)
		Image03 = tk.PhotoImage(file="{}\\img\\I6.gif".format(cdl))
		label = tk.Button(root, image=Image01, borderwidth=0,highlightthickness=0, command=Python_Libraries)
		label.grid(row=6,column=3)
		Image3 = tk.PhotoImage(file="{}\\img\\I3.png".format(cdl))
		label = tk.Label(root, borderwidth=0, image=Image3)
		label.grid(row=6,column=1)
		#-------------------------------------------------------------------------------------------------------------------------------------------------
		def HOW_TO_INSTALL_PIP():
			os.startfile("https://packaging.python.org/guides/installing-using-pip-and-virtualenv/")
		Button = tk.Button(root, text="   How To Install PiP  ?", width="7", height="1", bg=bg1, fg=fg1, font=large_font1, borderwidth=0, command=HOW_TO_INSTALL_PIP,anchor=W)
		Button.grid(row=8,column=2,sticky=tk.EW)
		Image04 = tk.PhotoImage(file="{}\\img\\I6.gif".format(cdl))
		label = tk.Button(root, image=Image01, borderwidth=0,highlightthickness=0, command=HOW_TO_INSTALL_PIP)
		label.grid(row=8,column=3)
		Image4 = tk.PhotoImage(file="{}\\img\\I4.png".format(cdl))
		label = tk.Label(root, borderwidth=0, image=Image4)
		label.grid(row=8,column=1)
		#--------------------------------------------------------------------------------------------------------------------------------------------------
		def PIP_UPGRADE():
			os.system("start /wait cmd /c (pip install --upgrade pip)")
		Button = tk.Button(root, text="   PiP Upgrade", bg = bg1, width="7", height="1", fg=fg1, font=large_font1, borderwidth=0, command=PIP_UPGRADE,anchor=W)
		Button.grid(row=10,column=2,sticky=tk.EW)
		Image05 = tk.PhotoImage(file="{}\\img\\I6.gif".format(cdl))
		label = tk.Button(root, image=Image01, borderwidth=0,highlightthickness=0, command=PIP_UPGRADE)
		label.grid(row=10,column=3)
		Image5 = tk.PhotoImage(file="{}\\img\\I5.png".format(cdl))
		label = tk.Label(root, borderwidth=0, image=Image5)
		label.grid(row=10,column=1)
		#---------------------------------------------------------------------------------------------------------------------------------------------------------
		def About_LIBFARM():
			os.startfile("https://github.com/roshanpoduval1998/LIBFARM")
		Button = tk.Button(root, text="i",command=About_LIBFARM,width="1",anchor=W,
			bg="gray88",borderwidth=0,highlightthickness=0,font=("Bahnschrift",15))
		Button.place(x=280,y=10)
		#---------------------------------------------------------------------------------------------------------------------------------------------------------
		root.resizable(width=0, height=0)
		root.mainloop()

	Lib_FARM_MAINFRAME()

main()

if __name__=="__main__":
	try:
		root.destroy()
		main()
	except:
		pass
