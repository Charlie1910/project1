#main.py
test = 5 * 5
if test == 25:
    print('true')
else:
    print('false')

gold coins = 3
silver coins = 6
brass coins = 9
print'gold coins + silver coins + brass coins'
18
#bounce game 
#creating game canvis

from tinker import *
import random
import time
tk = Tk()
tk.title("game")
tk.resizable(0, 0)
tk.wm_attrubutes("-tompost", 1)
canvas = Canvas(tk, with=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
#creating the ball class
class Ball:
    def_init_(self, canvis, color):
        self.canvas = canvis
        self.id = canvis.creata-oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id,245, 100)

    def draw(self):
        pass

ball = ball(canvis, 'red')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
#making the ball move/adding some action
def draw(self):
    self.canvis.move(self.id, 0, -1)
#the game code should look now like this
from tinker import *
import random
import time

class Ball:
    def_init_(self, canvis, color):
        self.canvis = canvis
        self.id = canvis.create_oval(10, 10, 25, 25, fill=color)
         self.canvis.move(self.id, 245, 100)
    
   def draw(self):
       self.canvis.move(self.id, 0, 1)
            
tk = Tk()
tk.title("game")
tk.resizable(0, 0)
tk.wm_attributes("-tampost", 1)
canvis = Canvis(tk, with=500, hight=400, bd=0, highlightthickness=0)
#to be continued
#making the ball bounce
