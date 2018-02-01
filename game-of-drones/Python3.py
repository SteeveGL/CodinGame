import sys
import math

class Zone:
    def __init__(self, id, x, y):
        self._id = id
        self._x = x
        self._y = y

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, id):
        self._owner = id

    @property
    def position(self):
        return "{} {}".format(self._x, self._y)

class Team:
    def __init__(self, id):
        self._id = id

    @property
    def drones(self):
        return self._drones

    @drones.setter
    def drones(self, value):
        self._drones = value

class Drone:
    def __init__(self, id, x, y):
        self._id = id
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = y

# p: number of players in the game (2 to 4 players)
# id: ID of your player (0, 1, 2, or 3)
# d: number of drones in each team (3 to 11)
# z: number of zones on the map (4 to 8)
p, id, d, z = [int(i) for i in input().split()]

teams = {}
for i in range(p):
    teams[i] = Team(i)
    drones = {}
    for j in range(d):
        drones[j] = Drone(j, 0, 0)
    teams[i].drones = drones

zones = {}
for i in range(z):
    # x: corresponds to the position of the center of a zone. A zone is a circle with a radius of 100 units.
    x, y = [int(j) for j in input().split()]
    zones[i] = Zone(i, x, y)

# game loop
while True:
    for zoneId, zone in zones.items():
        tid = int(input())  # ID of the team controlling the zone (0, 1, 2, or 3) or -1 if it is not controlled. The zones are given in the same order as in the initialization.
        zone.owner = tid

    for teamId, team in teams.items():
        for droneId, drone in team.drones.items():
            # dx: The first D lines contain the coordinates of drones of a player with the ID 0, the following D lines those of the drones of player 1, and thus it continues until the last player.
            dx, dy = [int(k) for k in input().split()]
            drone.x = dx
            drone.y = dy

    count = 0
    for droneId, drone in team.drones.items():
        print(zones[count].position)
        count += 1
        if (count >= len(zones)):
            count = 0
 