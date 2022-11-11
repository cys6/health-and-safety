from pygame.locals import *
import pygame
import time

STEP = 44

class Food():
    def __init__(self, x, y, surface):
        self.x = x*STEP
        self.y = y*STEP
        self.surface = surface
        self.image = pygame.image.load(r'C:Users\yongshun.cao.ext\Desktop\image.png').convert()

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))


class SnakeGame():
    def __init__(self):
        self.width = 800
        self.height = 600
        self._running = False

    def init(self):
        pygame.init()  #初始化所有导入的pygame模块
        # 初始化一个准备显示的窗口或屏幕
        self._display_surf = pygame.display.set_mode((self.width,self.height), pygame.HWSURFACE)
        self._running = True
        self.food = Food(5, 5, self._display_surf)

    def run(self):
        self.init()
        while self._running:
            pygame.event.pump()    # 内部处理pygame事件处理程序
            self.render()
            time.sleep(0.05)

    def render(self):
        self._display_surf.fill((0, 0, 0))    # 游戏界面填充为黑色
        self.food.draw()        # 画出食物
        pygame.display.flip()   # 刷新屏幕


if __name__ == '__main__':
    snake = SnakeGame()
    snake.run()