
def maxWater(height):
    # start = 0
    # end = len(height) - 1
    # start_h = height[start]
    # end_h = height[end]
    # water = min(start_h, end_h) * (end - start)
    # while start < end:
    #     if start_h < end_h:
    #         move_h = True
    #     else:
    #         move_h = False
    #     if move_h:
    #         start += 1
    #         if height[start] > start_h:
    #             start_h = height[start]
    #             water = max(water, min(start_h, end_h)*(end - start))
    #     else:
    #         end -= 1
    #         if height[end] > end_h:
    #             end_h = height[end]
    #             water = max(water, min(start_h, end_h)*(end - start))
    # return water


    res = 0
    l, r = 0, len(height) - 1
    while l<r:
        print(l,r)
        area = (r-l) * min(height[l], height[r])
        print(res, area)
        res = max(area, res)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return res


print(maxWater([1,3,2,5,25,24,5]))