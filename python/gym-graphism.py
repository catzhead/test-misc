import gymnasium as gym
import pygame
import numpy as np

env = gym.make('CartPole-v1', render_mode='rgb_array')
observation, info = env.reset()

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        action = 0
    elif keys[pygame.K_RIGHT]:
        action = 1
    else:
        action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

    rgb_array = env.render()
    surface = pygame.surfarray.make_surface(rgb_array.swapaxes(0,1))
    screen.blit(surface, (0,0))
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
env.close()
