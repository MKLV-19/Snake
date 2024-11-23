import pygame
import time
import random

# 初始化pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (250,100,0)

# 定义屏幕大小
dis_width = 1200
dis_height = 600

# 定义贪吃蛇大小和速度, 生长速度
snake_block = 30
snake_speed = 10
snake_growth = 2

# 创建屏幕对象
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃曹')

# 加载蛇头图片
snake_head_image = pygame.image.load(r'D:\python_EX\Snake\head2.jpg')
snake_head_image = pygame.transform.scale(snake_head_image, (snake_block, snake_block))

# 加载食物图片
food_image = pygame.image.load(r"D:\python_EX\Snake\head.jpg")
food_image = pygame.transform.scale(food_image, (snake_block, snake_block))

# 定义时钟
clock = pygame.time.Clock()

# 定义字体
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list)-1:
            # 绘制蛇头
            rotated_head = pygame.transform.rotate(snake_head_image, snake_direction_angle)
            dis.blit(rotated_head, [x[0], x[1]])
        else:
            # 绘制蛇身
            pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 7, dis_height *2 / 5])


def gameLoop():
    global snake_direction_angle

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = -snake_block  # 默认向上移动
    snake_direction_angle = 0  # 蛇头初始方向角度为0度（向上）

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                    snake_direction_angle = 90  # 左转
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                    snake_direction_angle = 270  # 右转
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                    snake_direction_angle = 0  # 上转
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0
                    snake_direction_angle = 180  # 下转

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        # pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        dis.blit(food_image, [foodx, foody])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # 每次循环向change的方向添加一格像素，同时删除最开始的一格像素，从而达到前进的效果
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 自我碰撞判定
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += snake_growth

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()


