from turtle import*

a = int(input('Сторона першого квадрата = '))
b = a - 30
wn = Screen()
wn.setup(width=0.5, height=0.5, startx=100, starty=100) # встановлюємо розмір і положення вікна
wn.title("Hello, turtle!") # встановлюємо заголовок вікна
color('black', 'blue')
begin_fill()

for i in range(4):
    fd(a)
    right(90)

end_fill()

up()
goto(15, -15)
down()
color('orange', 'yellow')
begin_fill()

for i in range(4):
    fd(b)
    right(90)

end_fill()


done()