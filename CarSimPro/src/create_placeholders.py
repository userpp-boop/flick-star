import pygame
import os
import wave
import struct

def create_placeholders():
    pygame.init()
    # Relative to project root
    img_path = os.path.join('assets', 'images', 'najaf_street.png')
    snd_path = os.path.join('assets', 'sounds', 'engine_v8.wav')

    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    os.makedirs(os.path.dirname(snd_path), exist_ok=True)

    # Simple landscape for Najaf
    bg = pygame.Surface((800, 400))
    bg.fill((210, 180, 140)) # Sand
    pygame.draw.rect(bg, (50, 50, 50), (0, 200, 800, 200)) # Road
    pygame.draw.rect(bg, (255, 255, 255), (0, 300, 800, 10)) # Line
    pygame.image.save(bg, img_path)

    with wave.open(snd_path, 'w') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(44100)
        for i in range(44100):
            # Rough engine sound
            v = int(16000 * (2 * (i * 100 / 44100 % 1) - 1))
            f.writeframes(struct.pack('h', v))
    print("Assets created in assets/")

if __name__ == "__main__":
    # Ensure we are in project root when running this from src/
    if os.path.basename(os.getcwd()) == 'src':
        os.chdir('..')
    create_placeholders()
