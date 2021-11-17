import pygame 
vec = pygame.math.Vector2


class Button: 
    def __init__(self, window, x, y, width, height, bg_color, state='', border_color=(0, 0, 0), hover_color=None, function=None, text=None): 
        self.game = window
        self.x = x 
        self.y = y
        self.width = width
        self.height = height 
        self.bg_color = bg_color
        self.state = state
        self.border_color = border_color
        self.hover_color = hover_color
        self.hovored = False 
        self.function = function
        self.text = text 
        self.font = pygame.font.SysFont('arial', 20, bold= True)
        self.showing = True
        pass 

    def update(self, pos, game_state= ''):
        
        if self.mouse_hovering(pos): 
            self.hovored = True 
        else:
            self.hovored = False 

        if self.state == '' or game_state == '': 
            self.showing = True 
        else: 
            if self.state == game_state: 
                self.showing = True 
            else: 
                self.showing = False 

    def draw(self):
        if self.showing:
            if not self.hovored: 
                pygame.draw.rect(self.game, self.bg_color, (self.x, self.y, self.width, self.height))
            else:
                pygame.draw.rect(self.game, self.hover_color, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(self.game, self.border_color, (self.x, self.y, self.width, self.height), 2)

            self.show_text()
            pass

    def click(self):
        if self.function != None and self.hovored: 
            self.function()
        else:
            pass 

    def show_text(self): 
        if self.text != None: 
            text = self.font.render(self.text, True, (0, 0, 0))
            text_size = text.get_size()
            text_x = self.x + (self.width / 2) - (text_size[0]/2) 
            text_y = self.y + (self.height / 2) - (text_size[1]/2) 
            pos = vec(text_x, text_y)
            self.game.blit(text, pos)

    def mouse_hovering(self, cursor):
        if self.showing: 
            if self.x + self.width > cursor[0] > self.x and self.y + self.height > cursor[1] > self.y:
                return True
            else:
                return False
        else:
            return False