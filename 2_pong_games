import pygame
import random
import sys

Choice = input(f"Enter Your Choice  , TO choose game: Paddle POP select 'a' , else select 'b' :")
if Choice == 'a':

    def ball_animation():
        global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1

        if ball.left <= 0:
            player_score += 1

            score_time = pygame.time.get_ticks()

        if ball.right >= screen_width:
            opponent_score += 1

            score_time = pygame.time.get_ticks()

        if ball.colliderect(player) and ball_speed_x > 0:
            if abs(ball.right - player.left) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - player.bottom) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1

        if ball.colliderect(opponent):
            if abs(ball.left - opponent.right) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1


    def player_collide():
        player.y += player_speed
        if player.top <= 0:
            player.top = 0

        if player.bottom >= screen_height:
            player.bottom = screen_height


    def opponent_Automation():
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height


    def ball_start():
        global ball_speed_x, ball_speed_y, score_time

        current_time = pygame.time.get_ticks()
        ball.center = (screen_width/2, screen_height/2)

        if current_time - score_time < 700:
            number_three = game_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))

        if 700 < current_time - score_time < 1400:
            number_two = game_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))

        if 1400 < current_time - score_time < 2100:
            number_one = game_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

        if current_time - score_time < 2100:
            ball_speed_x, ball_speed_y = 0, 0
        else:
            ball_speed_y = 1 * random.choice((1, -1))
            ball_speed_x = 1 * random.choice((1, -1))
            score_time = None


    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("PONG")

    ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
    player = pygame.Rect(screen_width - 10, screen_height/2 - 70, 8, 140)
    opponent = pygame.Rect(2, screen_height/2 - 70, 8, 140)

    ball_speed_x = 1 * random.choice((1, -1))
    ball_speed_y = 1 * random.choice((1, -1))
    player_speed = 0
    opponent_speed = 6


    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font("freesansbold.ttf", 24)

    score_time = None

    bg_color = pygame.Color("grey12")
    light_grey = (245, 123, 66)


    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 1

                if event.key == pygame.K_UP:
                    player_speed -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 1

                if event.key == pygame.K_UP:
                    player_speed += 1

        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,
                        0), (screen_width/2, screen_height))

        player_text = game_font.render(f"{player_score}", False, light_grey)
        screen.blit(player_text, (420, 295))

        opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
        screen.blit(opponent_text, (370, 295))

        ball_animation()
        player_collide()
        opponent_Automation()
        if score_time:
            ball_start()

        pygame.display.update()


elif Choice == 'b':


    import pygame
    import sys

    from pygame.constants import KEYDOWN, KEYUP, K_LEFT, K_RIGHT


    def ball_animation():
        global ball_speed_x, ball_speed_y
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1

        if ball.left <= 0 or ball.right >= screen_width:
            ball_speed_x *= -1

        if ball.colliderect(player):
            ball_speed_y *= -1


    def player_animation():
        player.x += player_speed
        if player.left <= 0:
            player.left = 0

        if player.right >= screen_width:
            player.right = screen_width

        # if ball.left < screen_width:
        #     player.left = ball.left
        # if ball.right >= screen_width:
        #     player.right = screen_width


    pygame.init()


    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("paddle and pop")

    ball = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
    player = pygame.Rect(screen_width / 2 - 60, screen_height / 2 + 225, 140, 8)

    bg_color = "grey12"
    light_grey = (200, 200, 200)

    ball_speed_x = 2
    ball_speed_y = 2
    player_speed = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player_speed -= 2

                if event.key == K_RIGHT:
                    player_speed += 2

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    player_speed += 2

                if event.key == K_RIGHT:
                    player_speed -= 2

        screen.fill(bg_color)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.rect(screen, light_grey, player)
        ball_animation()
        player_animation()

        pygame.display.update()

else:
    print("Invaild Choice")
