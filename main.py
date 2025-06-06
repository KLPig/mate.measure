import os.path

import pygame as pg
from tkinter import filedialog as fd
from tkinter import messagebox as mb

pg.init()

font = pg.font.SysFont("Arial", 32)

stage = 0
pts = []
tip = ['Start point of measured pipe', 'End point of measured pipe',
       'Start point of the unknown pipe', 'End point of the unknown pipe',
       '']

image = pg.transform.scale_by(pg.image.load(fd.askopenfilename(defaultextension='.png',
                                                               filetypes=[('PNG', '*.png'), ('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('All Files', '*.*')],
                                                               initialdir=os.path.dirname(__file__))), 1.5)
window = pg.display.set_mode(image.get_size())

t = tip[0]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pts.append(event.pos)
            if stage < 3:
                stage += 1
                t = tip[stage]
            elif stage == 3:
                stage = 4
                kn = ((pts[0][0] - pts[1][0]) ** 2 + (pts[0][1] - pts[1][1]) ** 2) ** .5
                un = ((pts[2][0] - pts[3][0]) ** 2 + (pts[2][1] - pts[3][1]) ** 2) ** .5
                unknown = 30 / kn * un
                pg.draw.line(window, (0, 100, 0), pts[2], pts[3], 5)
                pg.display.update()
                known = 46.6
                mb.showinfo('Results', f'Known pipe: {kn:.2f}pxl., 30cm.\n'
                                       f'Unknown pipe: {un:.2f}pxl., {30 / kn * un:.2f}cm.\n'
                                       f'Whole pipe: {kn / 30 * (30 / kn * un + kn + known):.2f}pxl., {30 / kn * un + kn + known:.2f}cm.')

            else:
                stage = 0
                pts = []
                t = tip[0]
    window.blit(image, (0, 0))
    if len(pts) >= 2:
        pg.draw.line(window, (100, 0, 0), pts[0], pts[1], 5)
    if len(pts) >= 4:
        pg.draw.line(window, (0, 100, 0), pts[2], pts[3], 5)
    tx = font.render(t, True, (0, 0, 0))
    window.blit(tx, (10, 10))
    pg.display.update()
