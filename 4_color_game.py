import pygame
import time
import random

pygame.init()
pygame.font.init()

white = 255, 255, 255
black = 0, 0, 0

yellow = 200, 150, 0
yellow_2 = 255, 255, 0

blue = 0, 0, 150
blue_2 = 0, 150, 255

red = 200, 0, 0
red_2 = 255, 100, 100

green = 0, 100, 0
green_2 = 50, 255, 50

score = 0
highscore = 7

game_pattern = {}
player_pattern = {}

screen = pygame.display.set_mode([450, 450])
pygame.display.set_caption('4 Color Game')


class Button:
    def __init__(self, color, color_clicked, x, y):
        self.color = color
        self.color_clicked = color_clicked
        self.x = x
        self.y = y
        self.width = 200
        self.height = 200

    def __repr__(self):
        if self.color == yellow:
            return 'yellow'
        elif self.color == blue:
            return 'blue'
        elif self.color == red:
            return 'red'
        elif self.color == green:
            return 'green'

    def draw(self, clicked):
        if clicked:
            pygame.draw.rect(screen, self.color_clicked, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_clicked(self):
        pygame.draw.rect(screen, self.color_clicked, (self.x, self.y, self.width, self.height))


class Screen:
    def __init__(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4

    def draw_screen(self, b1_clicked, b2_clicked, b3_clicked, b4_clicked):
        score_font = pygame.font.SysFont('Comic Sans MS', 37)
        score_image = score_font.render(str(score), False, white)

        screen.fill(black)

        self.b1.draw(b1_clicked)
        self.b2.draw(b2_clicked)
        self.b3.draw(b3_clicked)
        self.b4.draw(b4_clicked)

        screen.blit(score_image, (213, 200))

        pygame.display.flip()

        if b1_clicked:
            time.sleep(0.5)
            self.b1.draw(False)
        elif b2_clicked:
            time.sleep(0.5)
            self.b2.draw(False)
        elif b3_clicked:
            time.sleep(0.5)
            self.b3.draw(False)
        elif b4_clicked:
            time.sleep(0.5)
            self.b4.draw(False)

    def get_clicked(self, btn):
        score_font = pygame.font.SysFont('Comic Sans MS', 37)
        score_image = score_font.render(str(score), False, white)

        screen.fill(black)

        btn.get_clicked()

        if btn == yellow_button:
            blue_button.draw(False)
            red_button.draw(False)
            green_button.draw(False)
        elif btn == blue_button:
            yellow_button.draw(False)
            red_button.draw(False)
            green_button.draw(False)
        elif btn == red_button:
            yellow_button.draw(False)
            blue_button.draw(False)
            green_button.draw(False)
        elif btn == green_button:
            yellow_button.draw(False)
            blue_button.draw(False)
            red_button.draw(False)

        screen.blit(score_image, (213, 200))

        pygame.display.flip()


yellow_button = Button(yellow, yellow_2, 0, 0)
blue_button = Button(blue, blue_2, 250, 0)
red_button = Button(red, red_2, 0, 250)
green_button = Button(green, green_2, 250, 250)

screen_with_buttons = Screen(yellow_button, blue_button, red_button, green_button)

running = True
turn = 'game'

while running:
    round_won = False

    yellow_clicked = False
    blue_clicked = False
    red_clicked = False
    green_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if turn == 'game':
        random_number = random.randint(1, 4)
        if random_number == 1:
            random_button = yellow_button
            game_pattern[len(game_pattern) + 1] = 'yellow'
        elif random_number == 2:
            random_button = blue_button
            game_pattern[len(game_pattern) + 1] = 'blue'
        elif random_number == 3:
            random_button = red_button
            game_pattern[len(game_pattern) + 1] = 'red'
        elif random_number == 4:
            random_button = green_button
            game_pattern[len(game_pattern) + 1] = 'green'

        for key in game_pattern.keys():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            if game_pattern[key] == 'yellow':
                screen_with_buttons.get_clicked(yellow_button)
            elif game_pattern[key] == 'blue':
                screen_with_buttons.get_clicked(blue_button)
            elif game_pattern[key] == 'red':
                screen_with_buttons.get_clicked(red_button)
            elif game_pattern[key] == 'green':
                screen_with_buttons.get_clicked(green_button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            time.sleep(0.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            screen_with_buttons.draw_screen(False, False, False, False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            time.sleep(1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

        turn = 'player'
        player_pattern = {}

    print(turn)
    if turn == 'player':
        while len(player_pattern) < len(game_pattern):
            countdown = 30
            while countdown > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        countdown = 0
                    elif event.type == pygame.MOUSEBUTTONUP:
                        position = pygame.mouse.get_pos()
                        position = list(position)
                        countdown = 0
                countdown -= 0.5
                time.sleep(0.5)

            if position[0] < 200 and position[1] < 200:
                screen_with_buttons.get_clicked(yellow_button)
                time.sleep(0.5)
                screen_with_buttons.draw_screen(False, False, False, False)

                player_pattern[len(player_pattern) + 1] = 'yellow'

            elif position[0] < 200 and position[1] > 250:
                screen_with_buttons.get_clicked(red_button)
                time.sleep(0.5)
                screen_with_buttons.draw_screen(False, False, False, False)

                player_pattern[len(player_pattern) + 1] = 'red'

            elif position[0] > 250 and position[1] < 200:
                screen_with_buttons.get_clicked(blue_button)
                time.sleep(0.5)
                screen_with_buttons.draw_screen(False, False, False, False)

                player_pattern[len(player_pattern) + 1] = 'blue'

            elif position[0] > 250 and position[1] > 250:
                screen_with_buttons.get_clicked(green_button)
                time.sleep(0.5)
                screen_with_buttons.draw_screen(False, False, False, False)

                player_pattern[len(player_pattern) + 1] = 'green'

            if player_pattern[len(player_pattern)] == game_pattern[len(player_pattern)]:
                continue
            else:
                break
                round_won = False
        turn = 'game'

    if len(game_pattern) == len(player_pattern):
        for index in range(1, len(game_pattern) + 1):
            if game_pattern[index] == player_pattern[index]:
                round_won = True
            else:
                round_won = False
                break

    if round_won:
        score += 1
        time.sleep(0.75)
    elif not round_won:
        print('you lost the game with a score of ' + str(score))
        if score > highscore:
            print('you beated the old highscore of ' + str(highscore))
            highscore = score
        else:
            print("unfortunately, you couldn't beat the highscore of " + str(highscore))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        running = False
        break

pygame.quit()
