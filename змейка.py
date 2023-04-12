# Импортируем библиотеки
import pygame
import time
import random
 
# Инициализируем Pygame
pygame.init()
 
# Устанавливаем ширину и высоту экрана
width = 600
height = 400
display = pygame.display.set_mode((width, height))
 
# Устанавливаем заголовок окна
pygame.display.set_caption('Змейка')
 
# Устанавливаем цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
yellow = (255, 255, 102)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# Устанавливаем размер блока
block_size = 10
 
# Устанавливаем задержку
clock = pygame.time.Clock()
 
# Устанавливаем стандартный шрифт и размер
font_style = pygame.font.SysFont(None, 30)
 
 
def our_snake(block_size, snake_List):
    """
    Функция отрисовки змейки
    """
    for x in snake_List:
        pygame.draw.rect(display, green, [x[0], x[1], block_size, block_size])
 
 
def message(msg, color):
    """
    Функция вывода текстового сообщения на экран
    """
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])
 
 
def gameLoop():
    """
    Главная функция игры
    """
    game_over = False
    game_close = False
    
    # Устанавливаем координаты головы змейки
    x1 = width / 2
    y1 = height / 2
     
    # Устанавливаем скорость перемещения змейки по осям x и y
    x1_change = 0
    y1_change = 0
    
    # Создаем список для змейки
    snake_List = []
    Length_of_snake = 1
     
    # Устанавливаем координаты еды
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
     
    # Главный цикл игры
    while not game_over:
       
        while game_close == True:
            # Отрисовываем сообщение, что игра окончена
            display.fill(blue)
            message("Вы проиграли! Нажмите C-играть или Q-выйти", red)
            pygame.display.update()
             
            # Обрабатываем нажатия кнопок
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
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
 
        # Проверяем, если голова достигает края экрана - игра заканчивается
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        
        # Обновляем координаты головы
        x1 += x1_change
        y1 += y1_change
        
        # Отрисовываем белый цвет фона окна
        display.fill(blue)
        
        # Отрисовываем красный кружок - ее пропитания
        pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])
        
        # Добавляем голову змейки в начало списка координат
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        # Обновляем положение змейки
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(block_size, snake_List)
        
        # Обновляем длину змейки
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1
         
        clock.tick(20)
 
    # Завершаем Pygame
    pygame.quit()
    quit()
 
# Вызываем главную функцию игры
gameLoop()
