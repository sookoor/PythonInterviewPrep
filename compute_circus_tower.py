# Given the heights and weights of people, computes the largest possible number of people in a tower such that each peron is both shorter and lighter than the person below him or her.
# Input: [(ht_0, wt_0), (ht_1, wt_1), ... (ht_n, wt_n)]


def compute_circus_tower(people):
    sorted_people = sorted(people, key=lambda x : x[0])
    max_towers = []
    for p, person in enumerate(sorted_people):
        max_towers.append([person])
        for tower in max_towers[:p]:
            if tower[-1][0] < person[0] and tower[-1][1] < person[1] and len(tower) + 1 > len(max_towers[p]):
                max_towers.insert(p, tower + [person])

    max_tower = []
    for tower in max_towers:
        tower_height = len(tower)
        if tower_height > len(max_tower):
            max_tower = tower
    return max_tower

if __name__ == "__main__":
    people = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    assert compute_circus_tower(people) == [(56, 90), (60, 95), (65, 100), (68, 110), (70, 150), (75, 190)]
