import pygame 
import sys 
from game_window_class import * 
from button_class import * 

WIDTH = HEIGHT = 800 
run = True 
BACKGROUND = (42, 21, 13)
FPS = 60


# --------------------------------------- SETTINGS STATE FUNCTION ---------------------------------
def settings_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons: 
                    button.click()

def settings_update():
    game_window.update() 
    for button in buttons: 
        button.update(mouse_pos, game_state= state)


def settings_draw():
    window.fill((BACKGROUND))
    for button in buttons: 
        button.draw()
    game_window.draw()

# --------------------------- RUNNING STATE FUNCTIONS ----------------------------------------
def running_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons: 
                    button.click()

def running_update():
    game_window.update() 
    for button in buttons: 
        button.update(mouse_pos, game_state= state)
    
    if frame_count % (FPS//10): 
        game_window.evaluate()

def running_draw():
    window.fill((BACKGROUND))
    for button in buttons: 
        button.draw()
    game_window.draw()


# ----------------------------------- PAUSED STATE FUNCTIONS -----------------------------------------------
def paused_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons: 
                    button.click()

def paused_update():
    game_window.update() 
    for button in buttons: 
        button.update(mouse_pos, game_state= state)

def paused_draw():
    window.fill((BACKGROUND))
    for button in buttons: 
        button.draw()
    game_window.draw()


def mouse_on_grid(pos): 
    if pos[0] > 100 and pos[0] < WIDTH - 100: 
        if pos[1] > 180 and pos[1] < HEIGHT - 20: 
            return True
    return False
    pass

def click_cell(pos):
    grid_pos = [pos[0] - 100, pos[1] - 180]
    grid_pos[0] = grid_pos[0] // 20
    grid_pos[1] = grid_pos[1] // 20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False 
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True


def make_buttons():
    buttons = [] 
    buttons.append(Button(window, WIDTH//2-50, 50, 100, 30, text='RUN', bg_color=(28, 111, 51), state= 'setting', hover_color= (48, 141, 81), function=run_game))
    buttons.append(Button(window, WIDTH//2-50, 50, 100, 30, text='PAUSE', bg_color=(18, 104, 135), state= 'running', hover_color= (51, 168, 212), function= pause_game))
    buttons.append(Button(window, WIDTH//4-50, 50, 100, 30, text='RESET', bg_color=(117, 14, 14), state= 'paused', hover_color= (217, 54, 54), function= reset_game))
    buttons.append(Button(window, WIDTH//1.4-50, 50, 100, 30, text='RESUME', bg_color=(28, 111, 51), state= 'paused', hover_color= (48, 141, 81), function= run_game))

    return buttons


def run_game():
    global state 
    state = 'running' 

def pause_game():
    global state 
    state = 'paused' 

def reset_game():
    global state 
    state = 'setting' 
    game_window.reset_grid()

pygame.init() 
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180) 
buttons = make_buttons() 
state = 'setting'
frame_count = 0 

while run: 
    frame_count += 1 
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        settings_get_events() 
        settings_update()
        settings_draw() 
    
    if state == 'running':
        running_get_events() 
        running_update()
        running_draw() 
         
    if state == 'paused':
        paused_get_events() 
        paused_update()
        paused_draw() 
    
         
         

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()