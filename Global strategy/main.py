import pygame
import sys
from game import Game
from GUI import Button
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("cambria", 60)
play_img = pygame.image.load("assets/Play Rect.png").convert_alpha()
quit_img = pygame.image.load("assets/Quit Rect.png").convert_alpha()
play_button = Button("Play", (640, 300), font, "white", "blue", image=play_img)
quit_button = Button("Quit", (640, 450), font, "white", "red", image=quit_img)
continue_button = Button("Continue", (640, 300), font, "white", "blue", image=play_img)
newgame_button = Button("New Game", (640, 420), font, "white", "blue", image=play_img)
return_button = Button("Return", (640, 540), font, "white", "red", image=quit_img)
menu_buttons = [play_button, quit_button]
option_buttons = [continue_button,newgame_button,return_button]
def draw_menu():
    screen.fill("black")
    text = font.render("MAIN MENU", True, "white")
    screen.blit(text, text.get_rect(center=(640, 150)))
    for button in menu_buttons:
        button.update(screen)

def draw_pause():
    screen.fill("black")
    text = font.render("PAUSED", True, "white")
    screen.blit(text, text.get_rect(center=(640, 150)))
    for button in option_buttons:
        button.update(screen)

def main():
    state = "menu"
    game = None 
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if state == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.rect.collidepoint(mouse_pos):
                        game = Game(screen, clock, 1280, 720)
                        state = "game"
                    elif quit_button.rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
            elif state == "game":   
                result = game.handle_event(event)
                if result == "pause":
                    state = "paused"
                if result == "menu":
                    state = "menu"
            elif state == "paused":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if continue_button.rect.collidepoint(mouse_pos):
                        state = "game"
                    elif newgame_button.rect.collidepoint(mouse_pos):
                        game = Game(screen, clock, 1280, 720)
                        state = "game"
                    elif return_button.rect.collidepoint(mouse_pos):
                        state = "menu"
        if state == "menu":
            draw_menu()
        elif state == "game":
            game.update()
            game.draw()
        elif state == "paused":
            game.draw()
            draw_pause()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()