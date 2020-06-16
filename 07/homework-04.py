with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\20k1026-06-turtle.txt") as file:
    import turtle
    t = turtle.Pen()
    for line in file:
        data = line.split(":")
        if data[0] == "FORWARD":
            t.forward(float(data[1]))
        if data[0] == "LEFT":
            t.left(float(data[1]))
        if data[0] == "RIGHT":
            t.right(float(data[1]))
        if data[0] == "UP":
            t.up()
        if data[0] == "DOWN":
            t.down()
        if data[0] == "GOTO":
            t.goto(float(data[1]),float(data[2]))
