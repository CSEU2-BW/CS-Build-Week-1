
from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.generator import World

Room.objects.all().delete()


w = World()
num_rooms = 100
width = 10
height = 10
rooms = w.generate_rooms(width, height, num_rooms)

for i in rooms:
    r = Room(title=i['name'], description=i['description'], n_to=i['roomN'], s_to=i['roomS'], e_to=i['roomE'], w_to=i['roomW'])
    r.save()
players=Player.objects.all()
for p in players:
  p.currentRoom=rooms[0].id
  p.save()