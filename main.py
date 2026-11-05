a = box(size = vec(0.1, 1, 0.1), pos = vec(0.5,0,0.5))
b = box(size = vec(0.1, 1, 0.1), pos = vec(-0.5,0,0.5))
c = box(size = vec(0.1, 1, 0.1), pos = vec(-0.5,0,-0.5))
d = box(size = vec(0.1, 1, 0.1), pos = vec(0.5,0,-0.5))
e = box(size = vec(0.1, 0.1, 1), pos = vec(0.5 ,0.45,0))
f = box(size = vec(0.1, 0.1, 1), pos = vec(0.5 ,-0.45,0))
oo = box(size = vec(0.1, 0.1, 1), pos = vec(-0.5 ,0.45,0))
h = box(size = vec(0.1, 0.1, 1), pos = vec(-0.5 ,-0.45,0))
i = box(size = vec(1, 0.1, 0.1), pos = vec(0,-0.45,0.5))
j = box(size = vec(1, 0.1, 0.1), pos = vec(0,0.45,0.5))
k = box(size = vec(1, 0.1, 0.1), pos = vec(0,-0.45,-0.5))
l = box(size = vec(1, 0.1, 0.1), pos = vec(0,0.45,-0.5))
m = box(size=vec(0.95,0.95,0.95), opacity=0.3)

play = compound(make_trail=True, [a, b, c, d, e, f, oo, h, i, j, k, l, m])
g = vec(0, -9.8, 0)
play.v = vec(0,0,0)
dt = 0.01

while True : 
    rate(100)
    K = keysdown()
    if ' ' in K :
        while play.pos.y >= -100:
            rate(100)

            play.pos = play.pos + play.v*dt
            play.v = play.v + g*dt
