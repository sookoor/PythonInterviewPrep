class TowersOfHanoi(object):
    '''Implementation of Towers of Hanoi using lists as stacks.'''

    def __init__(self, num_disks):

        # Declare three stacks to represent the three rods
        self.towers = [[], [], []] 

        # Initialize first rod with disks. Numbers represent disk size
        # with larger numbers signifying larger disks. append == push
        for disk in range(num_disks, 0, -1):
            self.towers[0].append(disk)

    def move(self, n, src=0, aux=1, dest=2):
        if n > 0:
            self.move(n - 1, src, dest, aux)
            self.towers[dest].append(self.towers[src].pop())
            self.move(n - 1, aux, src, dest)

if __name__ == "__main__":
    num_disks = 5
    towers = TowersOfHanoi(5)

    print towers.towers

    towers.move(num_disks)

    print towers.towers
