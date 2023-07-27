import math

exp = 0
level = 1
exp_needed = 0


def level_curve():
    exp_needed = pow(level,1.5) + (level * 100)
    print(exp_needed)

def level_up():
    global level
    level += 1
    print(level)



level_curve()
level_up()
level_curve()
