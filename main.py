import pygame
import random
import sys


def draw_current_spell(path, screen):
    current_img = pygame.image.load(path)
    current_img = pygame.transform.scale(current_img, (300, 300))
    screen.blit(current_img, (50, 180))


def fill_values(vector):
    vector.append(random.randint(1, 5))
    vector.append(random.randint(6, 10))
    for i in range(200):
        value = random.randint(1, 10)
        while vector[i - 1] == value:
            value = random.randint(1, 10)
        vector.append(value)
    return vector


def generate_random_powers(vector, vector_path):
    combinations = {
        1: 'Images/COLD SNAP.png', 2: 'Images/Ghost Walk.png', 3: 'Images/Ice Wall.png',
        4: 'Images/Tornado.png', 5: 'Images/Alacrity.png', 6: 'Images/Forge Spirit.png',
        7: 'Images/CHAOS METEOR.png', 8: 'Images/Deafening Blast.png', 9: 'Images/EMP.png',
        10: 'Images/Sun Strike.png'
    }

    for value in vector:
        vector_path.append(combinations[value])

    return vector_path


def draw_current(array, screen):
    combinations = {
        'QQQ': 'Images/COLD SNAP.png', 'WWW': 'Images/EMP.png', 'EEE': 'Images/Sun Strike.png',
        'QQW': 'Images/Ghost Walk.png', 'QWQ': 'Images/Ghost Walk.png', 'WQQ': 'Images/Ghost Walk.png',
        'QQE': 'Images/Ice Wall.png', 'QEQ': 'Images/Ice Wall.png', 'EQQ': 'Images/Ice Wall.png',
        'WWQ': 'Images/Tornado.png', 'WQW': 'Images/Tornado.png', 'QWW': 'Images/Tornado.png',
        'WWE': 'Images/Alacrity.png', 'WEW': 'Images/Alacrity.png', 'EWW': 'Images/Alacrity.png',
        'EEQ': 'Images/Forge Spirit.png', 'EQE': 'Images/Forge Spirit.png', 'QEE': 'Images/Forge Spirit.png',
        'EEW': 'Images/CHAOS METEOR.png', 'EWE': 'Images/CHAOS METEOR.png', 'WEE': 'Images/CHAOS METEOR.png',
        'QWE': 'Images/Deafening Blast.png', 'QEW': 'Images/Deafening Blast.png', 'WQE': 'Images/Deafening Blast.png',
        'WEQ': 'Images/Deafening Blast.png', 'EQW': 'Images/Deafening Blast.png', 'EWQ': 'Images/Deafening Blast.png'
    }
    key_str = array[0]+array[1]+array[2]
    if key_str in combinations:
        current = pygame.image.load(combinations[key_str])
        screen.blit(current, (304, 530))
    else:
        current = pygame.image.load('Images/EMPTY.png')
        screen.blit(current, (304, 530))
    return combinations[key_str]


def draw_powers(array, screen):
    pos1 = pygame.image.load(array[2])
    pos2 = pygame.image.load(array[1])
    pos3 = pygame.image.load(array[0])
    screen.blit(pos1, (4, 530))
    screen.blit(pos2, (104, 530))
    screen.blit(pos3, (204, 530))


def assign_path(value, array):
    if value == 'q':
        powers_list(array, "Images/QUAS.png")
    elif value == 'w':
        powers_list(array, "Images/WEX.png")
    else:
        powers_list(array, "Images/EXORT.png")


def powers_list(array, new_value):
    array[2] = array[1]
    array[1] = array[0]
    array[0] = new_value


def draw_board(screen, score):
    quas = pygame.image.load("Images/QUAS.png")
    wex = pygame.image.load("Images/WEX.png")
    exort = pygame.image.load("Images/EXORT.png")
    invoke = pygame.image.load("Images/INVOKE.png")
    screen.blit(quas, (4, 34))
    screen.blit(wex, (104, 34))
    screen.blit(exort, (204, 34))
    screen.blit(invoke, (304, 34))


def show_game(p_array, k_array, computer_arr, cnt, t_time):
    pygame.init()
    bg_color = (32, 32, 32)
    screen = pygame.display.set_mode((404, 660))
    screen.fill(bg_color)
    pygame.display.set_caption("Invoker Trainer")

    font = pygame.font.Font(None, 32)

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if pygame.key.name(event.key) == 'q' or pygame.key.name(event.key) == 'w' or pygame.key.name(
                        event.key) == 'e':
                    new_value = pygame.key.name(event.key)
                    powers_list(k_array, new_value.upper())
                    assign_path(new_value, p_array)
                if pygame.key.name(event.key) == 'r':
                    str_curr = draw_current(k_array, screen)
                    if computer_arr[cnt] == str_curr:
                        cnt += 1
                        screen.fill((0, 0, 0))
                        screen.fill(bg_color)
                        draw_current(k_array, screen)

        draw_board(screen, cnt)
        draw_powers(p_array, screen)
        draw_current_spell(computer_arr[cnt], screen)

        score_text = font.render(f'Score: {cnt}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(total_time - elapsed_time, 0)

        if remaining_time == 0:
            pygame.display.set_mode((404, 660))
            pop_up_message = font.render("Dire Victory!", True, (255, 0, 0))
            pop_up_message = pygame.transform.scale(pop_up_message, (200, 80))  # Change the size here
            screen.blit(pop_up_message, (104, 290))
            pygame.display.flip()
        if cnt == len(computer_arr)-1:
            pygame.display.set_mode((404, 660))
            pop_up_message = font.render("Radiant Victory!", True, (0, 255, 0))
            pop_up_message = pygame.transform.scale(pop_up_message, (200, 80))  # Change the size here
            screen.blit(pop_up_message, (104, 290))
            pygame.display.flip()

        pygame.display.flip()

        clock.tick(30)

    # Quit Pygame
    pygame.quit()
    sys.exit()


# Main function to run the program
if __name__ == "__main__":
    counter = 0
    path_array = ["Images/EMPTY.png", "Images/EMPTY.png", "Images/EMPTY.png"]
    key_array = ["", "", ""]
    random_array = []
    random_path_array = []
    total_time = 210
    r_arr = generate_random_powers(fill_values(random_array), random_path_array)
    show_game(path_array, key_array, r_arr, counter, total_time)
