def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    x1, y1 = pos
    vx, vy = vel
    xf = x1 + vx * time
    yf = y1 + vy * time

    return (xf, yf)
