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
    def disconnect_rooms(self , disconnected_room , direction):
        pass
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
        count = 0
        toBeRemoved = []
        value = None
        while room_count < num_rooms:
            coordinates =['n','w','e','s']
        # insert for directions for each room
            x +=1
            if(x == self.width):
               x = 0
               y+=1
            # Calculate the direction of the room to be created
            allDirections = []
            connected_room = None
            room = Room(room_count, "A Generic Room", "This is a generic room.",['objects'], x, y)
            for i in coordinates:
                if i == 'w':
                    connected_room = Room(room_count-1 ,None,None,[None],x-1 , y )
                if i == 'e':
                    connected_room = Room(room_count+1 ,None,None,[None],x+1 , y )
                if i == 'n':
                    connected_room = Room(room_count+self.width ,None,None,[None],x , y+1)
                if i == 's':
                    connected_room = Room(room_count-self.width,None,None,[None],x , y-1)
                  
                next_movement = i
                if (next_movement== 'w' and x == 0) or (next_movement== 'e' and x == self.width - 1) or(next_movement == 'e' and room_count == num_rooms -1) or(next_movement == 'n' and (room_count + self.width) > num_rooms - 1 ) or ( next_movement== 'n' and y == self.height -1) or (next_movement== 's' and y == 0):
                    next_movement =  None
                    allDirections.append(next_movement)
                elif count == 3:
                    if next_movement =='n':
                        pass
                        # print('here' ,room.n_to)
                    if next_movement == 's':
                        pass
                        # room.get_room_in_direction('s').n_to = None
                    if next_movement == 'e':
                       pass
                        # room.get_room_in_direction('e').w_to = None
                    if next_movement == 'w':
                        pass
                        # room.get_room_in_direction('w').e_to = None
                    next_movement = None
                    allDirections.append(next_movement)
                    count = 0
                else:
                    allDirections.append(next_movement)
            count +=1
            room_directions=list(filter(None ,allDirections))
         

            # print('room_id:',room.id , 'room:', room ,'directions:',room_directions)
            # # Note that in Django, you'll need to save the room after you create it
            # #Save the room in the World grid
            self.grid[y][x] = room
            # # Connect the new room to the previous room
            
            for i in room_directions:
            # Update iteration variables
                previous_room = connected_room
                room.connect_rooms(previous_room, i) 
            room_count +=1
        # print('\n',toBeRemoved)

            

      




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
num_rooms = 20
width = 5
height = 4
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
