# WIN_WIDTH = 640
# WIN_HEIGHT = 480
WIN_WIDTH = 1280
WIN_HEIGHT = 960
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_RED = (150, 0, 0)
GOLD = (255, 215, 0)

#the code above us signifies the RGB color of the self.image.fill function
#RED = (#REDamount, #GREENamount, #BLUEamount) you can adjust it however you want it scales from 0 to 255

# tilemap = [
#     'BBBBBBBBBBBBBBBBBBBB',
#     'B.....BBBBBBB......B',
#     'B.....B..P..B......B',
#     'B.....B.....B......B',
#     'B.....B.....B......B',
#     'B.....B.....B......B',
#     'B....B.......B.....B',
#     'B...B.........B....B',
#     'B..B...........B...B',
#     'B.......BBB.....B..B',
#     'B..................B',
#     'B..E...........E...B',
#     'B..................B',
#     'B..................B',
#     'BBBBBBBBBBBBBBBBBBBB',

# ]

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B......................................B',
    'B.............................B........B',
    'B....B.....E..................B........B',
    'B....B..........BBBBBBBBBBBBBBB........B',
    'B....BBBBBBB....B......................B',
    'B..........B....B...E..................B',
    'B..........B....B.............B........B',
    'B..........B....B.........E...B...E....B',
    'B.....BBBBBB....BBBBBBBBBBBBBBBBBBBBBBBB',
    'B.....B................................B',
    'B.....B................................B',
    'B..E..B......BBBBBBB........B..........B',
    'B.....B............B...E....B....E.....B',
    'B.....B.......E....B........B..........B',
    'B.....B............B...E....B..........B',
    'B.....BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B............B..............B....E.....B',
    'B......................................B',
    'B....B.................................B',
    'B....B.......B....BBBBBBBBBBB.....B....B',
    'B....B.......B....B..E...BE.......B....B',
    'B.E..B.......BBBBBB......BBBBBBBBBBBBBBB',
    'B....B.................................B',
    'BBBBBB...........................BBBBBBB',
    'B.E.....BBBBB...BBBBBBBBBBBB.....B..E..B',
    'B.......B.......E................B.....B',
    'BBBBBB..B..............................B',
    'B.P.....B...................E..........B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',

]

    # def win_screen(selfd):
    #     totalE = 0
    #     for i, row in enumerate(tilemap):
    #         for j, column in enumerate(row):
    #             if column == "E":
    #                 totalE += 1
    #                 print(totalE)

    #     if totalE == 17:
    #         print('You won') 