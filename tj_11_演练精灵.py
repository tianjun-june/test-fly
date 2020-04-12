import pygame
from plane_sprites import GameSprite

# 游戏初始化：
pygame.init()
# 创建游戏的窗口:480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")

# 2.blit绘制图像
screen.blit(bg, (0, 0))
# 3.update 更新屏幕

# 绘制英雄的飞机
hero = pygame.image.load("images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建始终对象
clock = pygame.time.Clock()
# 1.记录飞机初识位置
hero_rect = pygame.Rect(150, 300, 102, 126)

#创建低级的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

#创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

# 游戏循环 ->意味着游戏的正式开始！
while True:

    clock.tick(60)
    #监听事件
    for event in pygame.event.get():

        #判断是否是退出事件
        if event.type == pygame.QUIT:

            print("退出游戏...")
            #quit 卸载所有的模块
            pygame.quit()
            #退出python程序
            exit()

    # 2.修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的Y值
    if hero_rect.y + hero_rect.h <= 0:
        hero_rect.y = 700

    # 3.调用blit方法
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    #让精灵组调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)
# 4.重新绘制图像
    pygame.display.update()

pygame.quit()