from fltk import *
import random

class rockpaperscissors(Fl_Window):
	def __init__(self,x,y,w,h,label='Rock Paper Scissors'):
		Fl_Window.__init__(self,x,y,w,h,label)
		self.names=['rock','paper','scissors']
		self.yourscore=0
		self.compscore=0
		cbnames=[self.rock_cb,self.paper_cb,self.scissors_cb]
		self.begin()
		#buttons
		self.bl=[]
		for y in range(3):
			self.bl.append(Fl_Button(150,y*50,100,50))
			self.bl[-1].label(self.names[y])
			self.bl[-1].callback(cbnames[y])
			
		self.box=Fl_Box(0,150,400,250)
		self.box.label(f'Your choice: None \n Computer choice: None \n Your score: {self.yourscore} \n Computer score: {self.compscore}')
		self.end()
		
	def rock_cb(self,wid):
		comp=random.randrange(0,3)
		self.determinescore(wid,comp)
		self.box.label(f'Your choice: rock \n Computer choice: {self.names[comp]} \n Your score: {self.yourscore} \n Computer score: {self.compscore}')
	
	def paper_cb(self,wid):
		comp=random.randrange(0,3)
		self.determinescore(wid,comp)
		self.box.label(f'Your choice: paper \n Computer choice: {self.names[comp]} \n Your score: {self.yourscore} \n Computer score: {self.compscore}')
	
	def scissors_cb(self,wid):
		comp=random.randrange(0,3)
		self.determinescore(wid,comp)
		self.box.label(f'Your choice: scissors \n Computer choice: {self.names[comp]} \n Your score: {self.yourscore} \n Computer score: {self.compscore}')

    def hello(self):
        print("hello")
		
	def determinescore(self,wid,comp):
		playerchoice=self.bl.index(wid)
		
		if playerchoice==0 and comp==2:
			self.yourscore+=1
			
		elif playerchoice==0 and comp==1:
			self.compscore+=1
			
		elif playerchoice==1 and comp==0:
			self.yourscore+=1
			
		elif playerchoice==1 and comp==2:
			self.compscore+=1
			
		elif playerchoice==2 and comp==1:
			self.yourscore+=1
			
		elif playerchoice==2 and comp==0:
			self.compscore+=1
			
		else:
			return []
		
		
		
app=rockpaperscissors(0,0,400,400)
app.show()
Fl.run()
