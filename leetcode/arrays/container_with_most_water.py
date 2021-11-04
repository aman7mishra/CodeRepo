
def maxWater(height):
    start = 0
    end = len(height) - 1
    start_h = height[start]
    end_h = height[end]
    water = min(start_h, end_h) * (end - start)
    while start < end:
        if start_h < end_h:
            move_h = True
        else:
            move_h = False
        if move_h:
            start += 1
            if height[start] > start_h:
                start_h = height[start]
                water = max(water, min(start_h, end_h)*(end - start))
        else:
            end -= 1
            if height[end] > end_h:
                end_h = height[end]
                water = max(water, min(start_h, end_h)*(end - start))
    return water


print(maxWater([2,3,10,5,7,8,9]))