def draw_line(length,label=""):
    line="-"*length
    if label:
        line+=" "+label
    print(line)


def draw_interval(length):
    if length>0:
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)


def draw_ruler(inches,maj_length):
    draw_line(maj_length,"0")
    for i in range(1,1+inches):
        draw_interval(maj_length-1)
        draw_line(maj_length,str(i))
draw_ruler(3,4)
