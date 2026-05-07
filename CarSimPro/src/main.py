import pygame
import sys
import os

# Set working directory to project root for correct path resolution
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.getcwd(), 'src'))

from car import Car
from background import Background
from sound_manager import SoundManager

def main():
    pygame.init()
    sw, sh = 800, 400
    try: screen = pygame.display.set_mode((sw, sh))
    except:
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        screen = pygame.display.set_mode((sw, sh))

    clock = pygame.time.Clock()
    car = Car(sw // 4, sh // 2 + 100)
    bg = Background(sw, sh)
    sm = SoundManager()

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for e in pygame.event.get():
            if e.type == pygame.QUIT: running = False

        keys = pygame.key.get_pressed()
        thr = 1.0 if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) else (-0.5 if (keys[pygame.K_LEFT] or keys[pygame.K_a]) else 0)

        car.update(dt, thr)
        bg.update(car.velocity, dt)
        sm.update(car.velocity)

        bg.draw(screen)
        car.draw(screen)

        # Display Speed
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Najaf Streets - Speed: {abs(car.velocity)*3.6:.1f} km/h", True, (255, 255, 255))
        screen.blit(text, (20, 20))

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__": main()
