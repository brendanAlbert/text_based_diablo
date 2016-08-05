import random, time

CELLS = [
    (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9),
    (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9),
    (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
    (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
    (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
    (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
    (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
    (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
    (8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
    (9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9)
]

POSSIBLE_CELLS = {
    (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9),
    (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9),
    (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
    (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
    (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
    (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
    (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
    (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
    (8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
    (9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9)
}

MAP = [
    #if a location has been discovered it becomes True
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False
]

def get_locations():
    random_int = random.randint(0,100)
    start = POSSIBLE_CELLS.pop()
    exit = start
    den_monsters_set = set()

    while len(den_monsters_set) != 15:
        random_int = random.randint(0,100)
        monster = POSSIBLE_CELLS.pop()
        den_monsters_set.add(monster)
    return start, exit, den_monsters_set

def move_player(player, move):

    x, y = player

    if move == 'LEFT' or move == 'A':
        y -= 1
    elif move == 'RIGHT' or move == 'D':
        y += 1
    elif move == 'UP' or move == 'W':
        x -= 1
    elif move == 'DOWN' or move == 'S':
        x += 1

    return x, y

def get_moves(player):
    moves = ['A', 'D', 'W', 'S']
    # player = (x,y)

    if player[1] == 0:
        moves.remove('A')
    if player[1] == 9:
        moves.remove('D')
    if player[0] == 0:
        moves.remove('W')
    if player[0] == 9:
        moves.remove('S')

    return moves

def draw_map(player, exit, monster_locations):
    print(' ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^')
    #tile = '|{}'
    printed_map = ""

    for idx, cell in enumerate(CELLS):
        if idx in [0,  1,  2,  3,  4,  5,  6,  7,  8,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   20, 21, 22, 23, 24, 25, 26, 27, 28,
                   30, 31, 32, 33, 34, 35, 36, 37, 38,
                   40, 41, 42, 43, 44, 45, 46, 47, 48,
                   50, 51, 52, 53, 54, 55, 56, 57, 58,
                   60, 61, 62, 63, 64, 65, 66, 67, 68,
                   70, 71, 72, 73, 74, 75, 76, 77, 78,
                   80, 81, 82, 83, 84, 85, 86, 87, 88,
                   90, 91, 92, 93, 94, 95, 96, 97, 98
            ]:
            if cell == exit and MAP[idx]:
                printed_map += ' ()'
                MAP[idx] = True
            elif cell in monster_locations and MAP[idx]:
                printed_map += ' x '
                MAP[idx] = True
            elif cell == player:
                #print(tile.format('X'), end='')
                printed_map += ' H '
                MAP[idx] = True
            elif MAP[idx]:
                 printed_map += ' _ '
            else:
                #print(tile.format('_'), end='')
                printed_map += '   '
        else:
            if cell == exit and MAP[idx]:
                printed_map += ' ()\n'
                MAP[idx] = True
            elif cell in monster_locations and MAP[idx]:
                printed_map += ' x|\n'
                MAP[idx] = True
            elif cell == player:
                #print(tile.format('X|'))
                printed_map += " H|\n"
                MAP[idx] = True
            elif MAP[idx]:
                printed_map += " _|\n"
            else:
                #print(tile.format('_|'))
                printed_map += "   \n"
    return printed_map

def cls(numb):
    print_spaces = ""
    for i in range(0,numb):
        print_spaces += "\n"
    return print_spaces

def dungeon():

    player, exit, den_monsters_set = get_locations()
    quest_complete = False
    monsters_left = len(den_monsters_set)
    go = True
    while go:
        moves = get_moves(player)

        if monsters_left == 0 and not quest_complete:
            time.sleep(2)
            print(' .', end=' ')
            time.sleep(2)
            print(' .', end=' ')
            time.sleep(2)
            print(' . ', end=' ')
            time.sleep(2)
            print('You feel the presence of evil departing from this place')
            time.sleep(3)
            print('Return to Akhara for a reward!')
            time.sleep(2)
            quest_complete = True
        print(' ')
        #print("You're currently in room {}".format(player))
        print(cls(26))
        print(draw_map(player, exit, den_monsters_set))
        print(cls(8))

        print("\nYou can move {}. Monsters remaining[ {} ]".format(moves, monsters_left))

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            break

        if move in moves:
            player = move_player(player, move)
        else:
            print("** That's a wall! **")
            continue

        if player in den_monsters_set:
            random_enemy = random.randint(0,3)
            enemy_dict = {0:"fallen", 1:"fallen shaman", 2: "zombie", 3:"gargantuan beast"}
            time.sleep(2)
            print('You found a {}!'.format(enemy_dict[random_enemy]))
            monsters_left -= 1
            time.sleep(2)
            #go = False

        elif player == exit:
            time.sleep(2)
            print("\n*** Exiting the Den. ***\n")
            time.sleep(2)
            #go = False


def main():

    # sanity check to be sure monsters set is populating correctly
    #player, den_monsters_set = get_locations()
    #print(player, '<-- player')
    #for monster in den_monsters_set:
        #print(monster, '<-- monster')
    dungeon()

main()
