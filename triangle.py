def print_triangle(num):
    for up in range(num-1):
        for j in range(num-up-1):
            print(" ", end="")
        for j in range(up*2+1):
            if j == 0 or j == up*2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for down in range(num):
        print("* ", end="")
    print()

print_triangle(3)
