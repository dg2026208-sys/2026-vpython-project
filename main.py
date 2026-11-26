Web VPython 3.2
import random
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

background = box(texture = "https://media.istockphoto.com/id/641972700/ko/%EC%82%AC%EC%A7%84/%EB%B0%A4-%EC%B4%88%EC%9B%90-%EB%B0%B0%EA%B2%BD%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%B0%A4-%EB%B3%84%EC%9D%B4-%EB%B9%9B%EB%82%98%EB%8A%94-%ED%95%98%EB%8A%98-%EB%B0%A4%ED%95%98%EB%8A%98%EA%B3%BC-%EB%B3%84.jpg?s=170667a&w=0&k=20&c=10iNd70_cF0x-akP7xuAq-ugqdrtuYw3P7zF4mtoLIg=", pos = vec(0, -30, -45), size=vec(250,170,1))

play = compound(make_trail=True, [a, b, c, d, e, f, oo, h, i, j, k, l, m])
yyyy = local_light(pos=vec(0,play.pos.y,0))
scene.camera.follow(play)
scene.camera.axis = vec(0, -6, -8)
label(pos=vec(0, 0.5, 0), text='스페이스를 눌러 시작하세요!', xoffset=0, yoffset=50, space=30, height=30, border=4, font='sans')

for i in range(300) :
    rate(1000)
    mm = box(size=vec(0.5,3,0.5),pos = vec(random.uniform(-50,50), -8*i-8, random.uniform(-40,40)), color = vec(0.1, random.uniform(0.3,1), random.uniform(0.5,1)))
    po = box(size=vec(0.5,3,0.5),pos = vec(random.uniform(-50,50), -8*i-11, random.uniform(-40,40)), color = vec(random.uniform(0,0.3), random.uniform(0.6,1), 1))
    bo = box(size=vec(0.5,3,0.5),pos = vec(random.uniform(-50,50), -8*i-9, random.uniform(-40,40)), color = vec(0.1, random.uniform(0.4,0.8), 1))
    Aw = box(size=vec(0.5,3,0.5),pos = vec(random.uniform(-50,50), -8*i-10, random.uniform(-40,40)), color = vec(0.1, random.uniform(0.3,0.5), 1))
    ge = box(size=vec(0.5,3,0.5),pos = vec(random.uniform(-50,50), -8*i-7, random.uniform(-40,40)), color = vec(0.71, random.uniform(0,0.5), 1))

g = vec(0, -9.8, 0)
play.v = vec(0,0,0)
dt = 0.01
TT=0

while True : 
    rate(100)
    K = keysdown()
    if ' ' in K :
        while play.pos.y >= -1600:
            rate(100)
            play.pos = play.pos + play.v*dt
            play.v = play.v + g*dt
            play.trail_color = vec(random.uniform(0,1),random.uniform(0,1),1)
    if 'up' in K :
        play.pos.z = play.pos.z - 0.1
    if 'left' in K :
        play.pos.x = play.pos.x - 0.1
    if 'right' in K :
        play.pos.x = play.pos.x + 0.1
    if 'down' in K :
        play.pos.z = play.pos.z + 0.1
