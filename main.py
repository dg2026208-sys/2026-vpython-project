a = box(size = vec(0.1, 1, 0.1), pos = vec(0.5,0,0.5))
b = box(size = vec(0.1, 1, 0.1), pos = vec(-0.5,0,0.5))
c = box(size = vec(0.1, 1, 0.1), pos = vec(-0.5,0,-0.5))
d = box(size = vec(0.1, 1, 0.1), pos = vec(0.5,0,-0.5))
e = box(size = vec(0.1, 0.1, 1), pos = vec(0.5 ,0.45,0))
f = box(size = vec(0.1, 0.1, 1), pos = vec(0.5 ,-0.45,0))
g = box(size = vec(0.1, 0.1, 1), pos = vec(-0.5 ,0.45,0))
h = box(size = vec(0.1, 0.1, 1), pos = vec(-0.5 ,-0.45,0))
i = box(size = vec(1, 0.1, 0.1), pos = vec(0,-0.45,0.5))
j = box(size = vec(1, 0.1, 0.1), pos = vec(0,0.45,0.5))
k = box(size = vec(1, 0.1, 0.1), pos = vec(0,-0.45,-0.5))
l = box(size = vec(1, 0.1, 0.1), pos = vec(0,0.45,-0.5))
m = box(size=vec(0.95,0.95,0.95), opacity=0.3)
play = compound( [a, b, c, d, e, f, g, h, i, j, k, l, m])

gra = vec(0, -9.8,0) #중력가속도

play.v = vec(0,0,0)
dt= 0.01

while ball.pos.y >= 0
