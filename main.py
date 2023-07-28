import math

exp = 0
level = 1
exp_needed = 0
total_exp = 0

def level_curve(level):
    exp_needed = pow(level,1.5) + (level * 100)
    print(exp_needed)
    return exp_needed

def level_up(many_levels):
    global level

    level += many_levels
    print(level)
    return level


def total_exp_needed():
    global total_exp
    global level
    levelstart = 1
    for levelstart in range(level+1):
        total_exp = total_exp + level_curve(levelstart)
        levelstart = levelstart + 1
    print(total_exp)


#level_curve(level)
level_up(3)
total_exp_needed()
