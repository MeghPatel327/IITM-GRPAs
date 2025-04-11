def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    return (a**2 + b**2 == c**2) and (a%2 ==0 and b%2==0)
