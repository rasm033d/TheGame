#https://codereview.stackexchange.com/questions/209922/simple-text-escape-room-game
#This can be used to generate a visual represntation of where the player is
room_wall = "|"
spot_template = "[ ]"
position_indicator = "^"

def room_template(width, height):
    row = [room_wall + spot_template * width + room_wall]

    return "\n".join(row * height)

def generate_room(width, height, pos_x, pos_y):
    template = room_template(width, height)

    spot_width = len(spot_template)
    wall_width = len(room_wall)
    row_width = spot_width * width + wall_width * 2 + 1 # + 1 to account for newline
    replace_index = 1 + wall_width + pos_y * row_width + pos_x * spot_width

    return template[:replace_index] \
               + position_indicator \
               + template[replace_index + 1:] 

def generate_rooms(room_width, room_height):
    return [generate_room(room_width, room_height, x, y)
            for x in range(room_width)
            for y in range(room_height - 1, -1, -1)]

for r in generate_rooms(3, 3):
        print(r + "\n")