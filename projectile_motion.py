#!/usr/bin/env python
# https://phys221.wordpress.com/2015/02/26/glowscript-tutorial-2-projectile-motion/
# https://www.glowscript.org/#/user/rhettallain/folder/phys221/program/glowscripttutorialprojectilemotion/edit

from vpython import box, vec, sphere, color, cos, sin, pi, rate, gcurve

floor=box(pos=vec(0,-.02,0), size=vec(2,.02,.4))
ball=sphere(pos=vec(-1,0,0), radius=0.02, color=color.red, make_trail=True)

g=vec(0,-9.8,0)
ball.m=0.1
v0=4.0
theta=60 #degrees

ball.p=ball.m*v0*vec(cos(theta*pi/180),sin(theta*pi/180),0)

t=0
dt=0.01

f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.red)

while ball.pos.y>=0:
    rate(100)
    Fnet = ball.m * g + vec(0, 0, 0) * ball.pos.y
    ball.p = ball.p + Fnet * dt
    ball.pos = ball.pos + (ball.p / ball.m) * dt
    f1.plot(pos=(t, ball.pos.y))
    f2.plot(pos=(t, ball.pos.x))
    t=t+dt

print(f"y pos {ball.pos.y}")
print(f"x pos {ball.pos.x}")
print(f"time of flight {t} s")

final_velocity = ball.p / ball.m
print(f"final velocity {final_velocity}")
print(f"final velocity magnitude {final_velocity.mag}")

