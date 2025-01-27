import gymnasium as gym
import pygame

env = gym.make('CartPole-v1', render_mode='human')
observation, info = env.reset()

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    action = 1 if keys[pygame.K_RIGHT] else 0 if keys[pygame.K_LEFT] else env.action_space.sample()
    
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()
        
    clock.tick(60)
    
pygame.quit()
env.close()
