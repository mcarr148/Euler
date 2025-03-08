nums = [1,2,3]
nums[-1:] = [1,2]
print(nums)

nums = [1,2,3]
nums[-1:] = [11,22]
print(nums)




'''
#printing a spiral
def spiral_odd_n(n):
    # Assumes n is odd so the spiral has a unique center
    spiral = [[0] * n for _ in range(n)]
    x = y = n // 2  # Start at center
    val = 1
    spiral[y][x] = val
    step = 1

    # Fill the spiral outwards
    while val < n * n:
        # Move right 'step' times
        for _ in range(step):
            if val == n * n:
                break
            x += 1
            val += 1
            spiral[y][x] = val

        # Move up 'step' times
        for _ in range(step):
            if val == n * n:
                break
            y -= 1
            val += 1
            spiral[y][x] = val

        step += 1

        # Move left 'step' times
        for _ in range(step):
            if val == n * n:
                break
            x -= 1
            val += 1
            spiral[y][x] = val

        # Move down 'step' times
        for _ in range(step):
            if val == n * n:
                break
            y += 1
            val += 1
            spiral[y][x] = val

        step += 1

    return spiral

# Example: create a 1001 x 1001 spiral
n = 21
spiral_1001 = spiral_odd_n(n)

# Printing 1001 x 1001 lines to the console can be huge;
# this shows how you’d do it if you really want to see everything:
for row in spiral_1001:
    print(" ".join(f"{x:5}" for x in row))
'''