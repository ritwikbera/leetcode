houses = [1,2,3,4]
heaters = [1,4]

def findRadius(houses,heaters):
    maxRadius = 0

    for house in houses:
        start = 0
        end = len(heaters)-1

        nearRad = 100
        while start <= end:

            mid = (start+end)//2 

            nearRad = min(nearRad, abs(house - heaters[mid]))
            if house < heaters[mid]:
                end = mid - 1
            elif house > heaters[mid]:
                start = mid + 1
            else:
                nearRad = 0
                break

        maxRadius = max(maxRadius, nearRad)

    return maxRadius


print(findRadius(houses,heaters))