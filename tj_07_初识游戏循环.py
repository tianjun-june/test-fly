import pygame
#游戏初始化：
pygame.init()
#创建游戏的窗口:480*700
screen = pygame.display.set_mode((480,700))

#绘制背景图像
#1.加载图像数据
bg = pygame.image.load("./images/background.png")

#2.blit绘制图像
screen.blit(bg,(0,0))
#3.update 更新屏幕

#绘制英雄的飞机
hero = pygame.image.load("images/me1.png")
screen.blit(hero,(200,500))
pygame.display.update()

#创建始终对象
clock = pygame.time.Clock()

#游戏循环 ->意味着游戏的正式开始！
i = 0
while True:

    clock.tick(1)
    print(i)
    i  += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
pygame.quit()