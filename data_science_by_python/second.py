import pandas as pd

IPL_data = pd.read_csv("C:\\Users\\hunny\\Desktop\\IPL.csv")
IPL_data

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(200)
    left(200)
    left(200)
    if(abs(pos()) < 1 ):
        break
end_fill()
done()


from graphics import *
win = GraphWin()
pt.draw(win)
cir = Circle(pt, 25)
cir.draw(win)
cir.setOuline('red')
cir.setFill('blue')


