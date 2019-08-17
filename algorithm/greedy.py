import math

def solve_set_cover(tocover, sets):
    final_sets = set()
    while tocover:
        best_set = None
        has_covered = set()
        for key, values in sets.items():
            covered = tocover & values
            if len(covered) > len(has_covered):
                has_covered = covered
                best_set = key
        tocover -= has_covered
        final_sets.add(best_set)
    return final_sets

def third(hypotenuse, edge):
    return math.sqrt(hypotenuse*hypotenuse - edge*edge)

def solve_radar_installation(islands, radius):
    intersection = []
    # 初始化与海岸线交点
    for x,y in islands:
        edge = third(radius, y)
        intersection.append((x-edge, x+edge))
    intersection.sort(key=lambda k:k[1])

    first = intersection[0]
    num = 1
    for item in intersection:
        if first == item:
            continue
        if item[0] <= first[1]:
            continue
        else:
            num += 1
            first = item
    return num


islands_1 = [(1,2), (-3,1), (2,1)]
islands_2 = [(0,2)]

num = solve_radar_installation(islands_1, 2)
print("radar count is: ", num)

num = solve_radar_installation(islands_2, 2)
print("radar count is: ", num)

tocover = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
sets = {}
sets['kone'] = set(["id", "nv", "ut"])
sets["ktwo"] = set(["wa", "id", "mt"])
sets["kthree"] = set(["or", "nv", "ca"])
sets["kfour"] = set(["nv", "ut"])
sets["kfive"] = set(["ca", "az"])

final = solve_set_cover(tocover, sets)
print(final)