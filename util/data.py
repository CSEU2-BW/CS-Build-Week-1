

# Seed the database
from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.generator import World

Room.objects.all().delete()


w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)

allRooms = []

for row in w.grid:
    for room in row:
        roomN = room.n_to.id if room.n_to != None else 0
        roomS = room.s_to.id if room.s_to != None else 0
        roomE = room.e_to.id if room.e_to != None else 0
        roomW = room.w_to.id if room.w_to != None else 0
        r = Room(title=room.name, description=room.description,
                 n_to=roomN, s_to=roomS, e_to=roomE, w_to=roomW)
        allRooms.append(room)
        r.save()


players = Player.objects.all()
for p in players:
    p.currentRoom = allRooms[0].id
    p.save()
