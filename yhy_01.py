from yhy_plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./yhy_images/bg_银河(1).png")
screen.blit(bg, (0, 0))
hero = pygame.image.load("./yhy_images/aline_145_160.png")
screen.blit(hero, (180, 700))
hero_rect = pygame.Rect(180, 560, 145, 160)
# 创建精灵
enemy = GameSprite("./yhy_images/敌机(1).png")
enemy1 = GameSprite("./yhy_images/敌机(1).png", 2)
# 通过精灵创建精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

pygame.display.update()

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()

            exit()
    #  移动hero（动画）
    hero_rect.y -= 1
    if hero_rect.y <= -100:
        hero_rect.y = 700

    # 用pygame的bilt方法必须指定位置和大小
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 用Sorite精灵中的update方法可以让精灵组自动更新位置
    enemy_group.update()
    # draw-在screen上绘制所有的精灵
    enemy_group.draw(screen)

    pygame.display.update()

    pass
