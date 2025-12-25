


import pygame as pg
from modules import statics as st
from modules.statics import *
from modules.checker_board import *
from modules.checker import *

socials = """https://discord.gg/X6zXjC2vdA
https://cuty.sellhub.cx/product/CUTY-AIO-3/"""

test = """<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <script>
            window.KPSDK = {};
            KPSDK.now = typeof performance !== 'undefined' && performance.now ? performance.now.bind(performance) : Date.now.bind(Date);
            KPSDK.start = KPSDK.now();
            window.parent.postMessage('KPSDK:MC:-::::', '*');
        </script>
        <script src="/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/ips.js?ga__15_abel=&amp;x-kpsdk-v=j-1.2.94&amp;x-kpsdk-im=-"></script>
    </body>
</html>"""

"https://cuty.sellhub.cx/product/CUTY-AIO-3/"
"https://discord.gg/X6zXjC2vdA"
"x-kpsdk-v"
"x-kpsdk-dt"
"x-kpsdk-im"
"x-kpsdk-ct"



fps = 60

WIN = pg.display.set_mode((st.width, st.height))
pg.display.set_caption("Checkers")


# get row and col for mouse
def get_row_col_mouse(pos):
    x, y = pos
    row = y // sq_size
    col = x // sq_size
    return row, col


# main function
if __name__ == "__main__":
    # represents the game
    run = True

    # certain clock value default because it is varries from diff pc to pc
    clock = pg.time.Clock()

    # create board
    board = checker_board()
    game = checker(WIN)

    # main loop
    while run:
        clock.tick(fps)

        if board.winner() != None:
            print(board.winner())

        # check if any events is running or not
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                row, col = get_row_col_mouse(pos)
                game.selectrc(row, col)
                # piece = board.get_piece(row, col)
                # board.move(piece, 4, 3)

        game.update()
    pg.quit()
