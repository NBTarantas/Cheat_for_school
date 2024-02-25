v_boat = int(input('Швидкість човна = '))
v_stream = int(input('Швидкість течії = '))

t_river = 3
t_lake = 2

l = v_boat*t_lake + (v_boat+v_stream)*t_river

print('Човен проплив ', l, 'км')