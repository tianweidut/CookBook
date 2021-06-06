#coding: utf-8

def draw_line(tick, label=""):
    line = '-' * tick
    if label != "":
        line += label
    print(line)

def draw_interval(tick):
    if tick > 0:
        draw_interval(tick-1)
        draw_line(tick)
        draw_interval(tick-1)

def draw_ruler(inches, major_tick):
    draw_line(major_tick, '0')

    for i in range(1, inches):
        draw_interval(major_tick - 1)
        draw_line(major_tick, str(i))

if __name__ == "__main__":
    print("a, 4,3")
    draw_ruler(3, 4)
    print("b, 5,2")
    draw_ruler(2, 5)
    print("c, 3,4")
    draw_ruler(4, 3)