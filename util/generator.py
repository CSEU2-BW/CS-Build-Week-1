# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

import random
class Room:
    def __init__(self, id, name, description, objects, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.objects = [None]
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
    def get_neighbours(self, x, y, size_x, size_y):      
        '''
        Get the neighbours of a room
        '''
        neighbours = [None, None, None, None]
        if y < size_y - 1 and self.grid[y +1][x]:
            neighbours[0] = self.grid[y +1][x]
        elif y == size_y -1:
            neighbours[0] = 'wall'

        if y > 0 and self.grid[y - 1][x]:
            neighbours[1] = self.grid[y - 1][x]
        elif y == 0:
            neighbours[1] = 'wall'
    
        if x < size_x - 1 and self.grid[y][x + 1]:
            neighbours[3] = self.grid[y][x + 1]
        elif x == size_x -1:
            neighbours[3] = 'wall'

        if x > 0 and self.grid[y][x - 1]:
            neighbours[2] = self.grid[y][x - 1]
        elif x == 0:
            neighbours[2] = 'wall'
        return neighbours
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0
       

        # Start generating rooms to the east
        # direction = 1  # 1: east, -1: west


        # While there are rooms to be created...
        previous_room = None
        coordinates =['n','s','w','e']
        while room_count < num_rooms:
            
        # insert for directions for each room
            x +=1
            if(x == self.width):
               x = 0
               y+=1
            # Calculate the direction of the room to be created
            allDirections = []
            connected_rooms = None
            room = Room(room_count, "A Generic Room", "This is a generic room.",['objects'], x, y)
            neighbours = self.get_neighbours(x, y, self.width, self.height)
            # print('room_id:',room.id , 'room:', room ,'directions:',room_directions)
            # # Note that in Django, you'll need to save the room after you create it
            # #Save the room in the World grid
            self.grid[y][x] = room
            # # Connect the new room to the previous room
          
            for index, neighbour in enumerate(neighbours):
            # Update iteration variables

                if(neighbour and neighbour !='wall'):
                    if index == 1 :
                        room.connect_rooms(neighbour ,'s')
                    if index == 2 :
                        room.connect_rooms(neighbour,'w')
            room_count +=1

        for row in self.grid:
            count = 0
            for room in row:
                count += 1
                direction = random.choice(['n', 's', 'e', 'w'])
                if(room and count == 3):
                    count = 0
                    if(direction == 'n' and room.n_to ):
                        room.n_to.s_to = None
                        room.n_to = None
                    if(direction == 's' and room.s_to ):
                        room.s_to.n_to = None
                        room.s_to = None
                    if(direction == 'w' and room.w_to):
                        room.w_to.e_to = None
                        room.w_to = None
                    if(direction == 'e' and room.e_to):
                        room.e_to.w_to = None
                        room.e_to = None

         

      




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
        reverse_grid = list(self.grid) # make a copy of the list
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


w = World()
num_rooms = 86
width = 8
height = 11
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
