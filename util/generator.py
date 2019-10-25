# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

import random
rooms = [
    {"title": "entry", "description": "You are in room: entry. Enjoy!"},
    {"title": "armory", "description": "You are in room: armory. Enjoy!"},
    {"title": "assembly room", "description": "You are in room: assembly room. Enjoy!"},
    {"title": "attic", "description": "You are in room: attic. Enjoy!"},
    {"title": "cloakroom", "description": "You are in room: cloakroom. Enjoy!"},
    {"title": "backroom", "description": "You are in room: backroom. Enjoy!"},
    {"title": "ballroom", "description": "You are in room: ballroom. Enjoy!"},
    {"title": "basement", "description": "You are in room: basement. Enjoy!"},
    {"title": "bathroom", "description": "You are in room: bathroom. Enjoy!"},
    {"title": "bedroom", "description": "You are in room: bedroom. Enjoy!"},
    {"title": "boardroom", "description": "You are in room: boardroom. Enjoy!"},
    {"title": "boiler room", "description": "You are in room: boiler room. Enjoy!"},
    {"title": "boudoir", "description": "You are in room: boudoir. Enjoy!"},
    {
        "title": "breakfast nook",
        "description": "You are in room: breakfast nook. Enjoy!",
    },
    {
        "title": "breakfast room",
        "description": "You are in room: breakfast room. Enjoy!",
    },
    {"title": "cabin", "description": "You are in room: cabin. Enjoy!"},
    {"title": "cellar", "description": "You are in room: cellar. Enjoy!"},
    {"title": "chamber", "description": "You are in room: chamber. Enjoy!"},
    {"title": "cabin", "description": "You are in room: cabin. Enjoy!"},
    {"title": "classroom", "description": "You are in room: classroom. Enjoy!"},
    {"title": "control room", "description": "You are in room: control room. Enjoy!"},
    {"title": "court room", "description": "You are in room: court room. Enjoy!"},
    {"title": "conservatory", "description": "You are in room: conservatory. Enjoy!"},
    {"title": "cubby", "description": "You are in room: cubby. Enjoy!"},
    {"title": "common room", "description": "You are in room: common room. Enjoy!"},
    {"title": "darkroom", "description": "You are in room: darkroom. Enjoy!"},
    {"title": "den", "description": "You are in room: den. Enjoy!"},
    {"title": "dinning room", "description": "You are in room: dinning room. Enjoy!"},
    {"title": "dungeon", "description": "You are in room: dungeon. Enjoy!"},
    {"title": "dormitory", "description": "You are in room: dormitory. Enjoy!"},
    {"title": "dressing room", "description": "You are in room: dressing room. Enjoy!"},
    {"title": "computer room", "description": "You are in room: computer room. Enjoy!"},
    {
        "title": "emergency room",
        "description": "You are in room: emergency room. Enjoy!",
    },
    {"title": "sunroom", "description": "You are in room: sunroom. Enjoy!"},
    {"title": "anteroom", "description": "You are in room: anteroom. Enjoy!"},
    {"title": "family room", "description": "You are in room: family room. Enjoy!"},
    {"title": "foyer", "description": "You are in room: foyer. Enjoy!"},
    {"title": "front room", "description": "You are in room: front room. Enjoy!"},
    {"title": "fitting room", "description": "You are in room: fitting room. Enjoy!"},
    {"title": "game room", "description": "You are in room: game room. Enjoy!"},
    {"title": "garage", "description": "You are in room: garage. Enjoy!"},
    {"title": "garret", "description": "You are in room: garret. Enjoy!"},
    {"title": "grotto", "description": "You are in room: grotto. Enjoy!"},
    {"title": "riding hall", "description": "You are in room: riding hall. Enjoy!"},
    {"title": "guest room", "description": "You are in room: guest room. Enjoy!"},
    {"title": "green room", "description": "You are in room: green room. Enjoy!"},
    {"title": "gym", "description": "You are in room: gym. Enjoy!"},
    {"title": "hall", "description": "You are in room: hall. Enjoy!"},
    {"title": "hallway", "description": "You are in room: hallway. Enjoy!"},
    {"title": "hotel room", "description": "You are in room: hotel room. Enjoy!"},
    {"title": "inglenook", "description": "You are in room: inglenook. Enjoy!"},
    {"title": "keep", "description": "You are in room: keep. Enjoy!"},
    {"title": "kitchen", "description": "You are in room: kitchen. Enjoy!"},
    {"title": "kitchenette", "description": "You are in room: kitchenette. Enjoy!"},
    {"title": "larder", "description": "You are in room: larder. Enjoy!"},
    {"title": "great room", "description": "You are in room: great room. Enjoy!"},
    {"title": "lobby", "description": "You are in room: lobby. Enjoy!"},
    {"title": "lounge", "description": "You are in room: lounge. Enjoy!"},
    {"title": "loft", "description": "You are in room: loft. Enjoy!"},
    {"title": "living room", "description": "You are in room: living room. Enjoy!"},
    {"title": "library", "description": "You are in room: library. Enjoy!"},
    {"title": "lunchroom", "description": "You are in room: lunchroom. Enjoy!"},
    {"title": "maid's room", "description": "You are in room: maid's room. Enjoy!"},
    {"title": "ladies' room", "description": "You are in room: ladies' room. Enjoy!"},
    {"title": "clean room", "description": "You are in room: clean room. Enjoy!"},
    {"title": "rumpus room", "description": "You are in room: rumpus room. Enjoy!"},
    {"title": "study", "description": "You are in room: study. Enjoy!"},
    {"title": "stockroom", "description": "You are in room: stockroom. Enjoy!"},
    {"title": "solarium", "description": "You are in room: solarium. Enjoy!"},
    {"title": "scullery", "description": "You are in room: scullery. Enjoy!"},
    {"title": "screen porch", "description": "You are in room: screen porch. Enjoy!"},
    {"title": "washroom", "description": "You are in room: washroom. Enjoy!"},
    {"title": "weight room", "description": "You are in room: weight room. Enjoy!"},
    {
        "title": "visitors' room",
        "description": "You are in room: visitors' room. Enjoy!",
    },
    {"title": "wine cellar", "description": "You are in room: wine cellar. Enjoy!"},
    {"title": "workroom", "description": "You are in room: workroom. Enjoy!"},
    {"title": "wine room", "description": "You are in room: wine room. Enjoy!"},
    {"title": "waiting room", "description": "You are in room: waiting room. Enjoy!"},
    {"title": "ward room", "description": "You are in room: ward room. Enjoy!"},
    {"title": "vestibule", "description": "You are in room: vestibule. Enjoy!"},
    {"title": "utility room", "description": "You are in room: utility room. Enjoy!"},
    {"title": "tack room", "description": "You are in room: tack room. Enjoy!"},
    {"title": "schoolroom", "description": "You are in room: schoolroom. Enjoy!"},
    {"title": "show room", "description": "You are in room: show room. Enjoy!"},
    {"title": "state room", "description": "You are in room: state room. Enjoy!"},
    {"title": "studio", "description": "You are in room: studio. Enjoy!"},
    {"title": "staffroom", "description": "You are in room: staffroom. Enjoy!"},
    {"title": "suite", "description": "You are in room: suite. Enjoy!"},
    {"title": "saloon", "description": "You are in room: saloon. Enjoy!"},
    {"title": "restroom", "description": "You are in room: restroom. Enjoy!"},
    {"title": "playroom", "description": "You are in room: playroom. Enjoy!"},
    {"title": "pool room", "description": "You are in room: pool room. Enjoy!"},
    {"title": "pantry", "description": "You are in room: pantry. Enjoy!"},
    {"title": "parlor", "description": "You are in room: parlor. Enjoy!"},
    {
        "title": "operating room",
        "description": "You are in room: operating room. Enjoy!",
    },
    {"title": "office", "description": "You are in room: office. Enjoy!"},
    {"title": "newsroom", "description": "You are in room: newsroom. Enjoy!"},
    {"title": "nursery", "description": "You are in room: nursery. Enjoy!"},
    {"title": "mud room", "description": "You are in room: mud room. Enjoy!"},
    {"title": "motel room", "description": "You are in room: motel room. Enjoy!"},
    {"title": "mailroom", "description": "You are in room: mailroom. Enjoy!"},
]

class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __repr__(self):
        # if self.e_to is not None:
            # return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"


    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.rooms = []

    def get_neighbours(self, x, y, size_x, size_y):
        '''
        Get the neighbours of a room
        '''
        neighbours = [None, None, None, None]
        if y < size_y - 1 and self.grid[y + 1][x]:
            neighbours[0] = self.grid[y + 1][x]
        elif y == size_y - 1:
            neighbours[0] = 'wall'

        if y > 0 and self.grid[y - 1][x]:
            neighbours[1] = self.grid[y - 1][x]
        elif y == 0:
            neighbours[1] = 'wall'

        if x < size_x - 1 and self.grid[y][x + 1]:
            neighbours[3] = self.grid[y][x + 1]
        elif x == size_x - 1:
            neighbours[3] = 'wall'

        if x > 0 and self.grid[y][x - 1]:
            neighbours[2] = self.grid[y][x - 1]
        elif x == 0:
            neighbours[2] = 'wall'
        print(neighbours)
        return neighbours

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        # direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        # previous_room = None
        # coordinates = ['n', 's', 'w', 'e']
        while room_count < num_rooms:

            # insert for directions for each room
            x += 1
            if(x == self.width):
                x = 0
                y += 1
            # Calculate the direction of the room to be created
            # allDirections = []
            # connected_rooms = None
            room = Room(room_count + 1, rooms[room_count]['title'],
                        rooms[room_count]['description'], x, y)

            neighbours = self.get_neighbours(x, y, self.width, self.height)
            # print('room_id:',room.id , 'room:', room ,'directions:',room_directions)
            # # Note that in Django, you'll need to save the room after you create it
            # #Save the room in the World grid
            self.grid[y][x] = room
            # # Connect the new room to the previous room

            for index, neighbour in enumerate(neighbours):
                # Update iteration variables

                if(neighbour and neighbour != 'wall'):
                    if index == 1:
                        room.connect_rooms(neighbour, 's')
                    if index == 2:
                        room.connect_rooms(neighbour, 'w')
            room_count += 1

        for row in self.grid:
            count = 0
            for room in row:
                # if room.n_to == 'None' or room.s_to == 'None' or room.w_to == 'None' or room.e_to == 'None':
                #     room.n_to.id = None
                

                count += 1
                direction = random.choice(['n', 's', 'e', 'w'])
                if(room and count == 2):
                    count = 0
                    if(direction == 'n' and room.n_to):
                        room.n_to.s_to = None
                        room.n_to = None
                    if(direction == 's' and room.s_to):
                        room.s_to.n_to = None
                        room.s_to = None
                    if(direction == 'w' and room.w_to):
                        room.w_to.e_to = None
                        room.w_to = None
                    if(direction == 'e' and room.e_to):
                        room.e_to.w_to = None
                        room.e_to = None

        def get_opposite(direction):
            if direction == 'n_to':
                return 's_to'
            if direction == 's_to':
                return 'n_to'
            if direction == 'e_to':
                return 'w_to'
            if direction == 'w_to':
                return 'e_to'

        def get_opposite_x(direction, x):
            if direction == 'e_to':
                return x + 1
            if direction == 'w_to':
                return x - 1
            return x           

        def get_opposite_y(direction, y):
            if direction == 'n_to':
                return y + 1
            if direction == 's_to':
                return y - 1
            return y

        for row in self.grid:
            for room in row:
                if room.n_to and room.s_to and room.e_to and room.w_to:
                    direction = random.choice(['n_to', 's_to', 'e_to', 'w_to'])
                    opposite = get_opposite(direction)
                    # room.n_to = None
                    setattr(room, direction, None)
                    # x = room.x
                    # y = room.y+1
                    x = get_opposite_x(direction, room.x)
                    y = get_opposite_y(direction, room.y)
                    # .s_to = None
                    setattr(self.grid[y][x], opposite, None)
                    # print('four walls')


    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)

                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)

    def print_json(self):
        for i in self.grid:
            print(i)


w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")


