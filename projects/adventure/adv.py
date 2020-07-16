from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited_rooms = {}

#place to store the reversed path for backtracking
back_track_path = []
#establish the directions of the backward traversal
backwards_traversal = {"n":"s", "e":"w", "s":"n", "w":"e"}

#get that first room with it's exits into 'visited'
visited_rooms[player.current_room.id] = player.current_room.get_exits()

#figure out loop for visited list vs list of 500 rooms
while len(visited_rooms) < len(room_graph):
    if player.current_room.id not in visited_rooms:  #if not in the visited, add to visited_rooms
        #use the get_exits() from the Room class (n,s,e,w)
        visited_rooms[player.current_room.id] = player.current_room.get_exits() #get the exit information
        route_to_current_room = back_track_path[-1]
        #take the route_to_current_room and remove (using the built-in .remove() )
        visited_rooms[player.current_room.id].remove(route_to_current_room)

    #When all paths have been explored, we need to backtrack to a room with unexplored exits
    if len(visited_rooms[player.current_room.id]) == 0:  #deadend
        #engage backtracking :)
        route_to_current_room = back_track_path[-1]
        back_track_path.pop()
        traversal_path.append(route_to_current_room)
        #by using the .travel() method on the player class, move the player
        player.travel(route_to_current_room)

    else:
        #grab a direction
        cardinal_dir = visited_rooms[player.current_room.id][-1]
        visited_rooms[player.current_room.id].pop()
        #add this direction/path to the traversal_path
        traversal_path.append(cardinal_dir)
        #add the backwards traversal
        back_track_path.append(backwards_traversal[cardinal_dir])
        #move the player again using the .travel() from the player class
        player.travel(cardinal_dir)

#figure out what to do when you hit a deadend. a room where all paths have been discovered.
#backtrack until you encounter a room with paths that have not been discovered


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# get the first room and exits added to the visited
#

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
