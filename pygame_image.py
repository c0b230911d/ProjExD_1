import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_inv = pg.transform.flip(bg_img,True,False)
    koukaton = pg.image.load("fig/3.png")
    koukaton_inv = pg.transform.flip(koukaton,True,False)
    koukaton_rct = koukaton_inv.get_rect()
    koukaton_rct.center = (300, 200)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            koukaton_rct.move_ip(0, -1)
        elif key_lst[pg.K_DOWN]:
            koukaton_rct.move_ip(0, 1)
        elif key_lst[pg.K_RIGHT]:
            koukaton_rct.move_ip(1, 0)
        elif key_lst[pg.K_LEFT]:
            koukaton_rct.move_ip(-1, 0)

        x = tmr%3200

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_inv,[-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img_inv,[-x+4800, 0])
        screen.blit(koukaton_inv, koukaton_rct)
        pg.display.update()
        tmr += 1      
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()