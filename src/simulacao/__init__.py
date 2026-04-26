import pygame

nextSceane = pygame.USEREVENT + 2
NEXT_SCEANE = pygame.event.Event(nextSceane)

priorSceane = pygame.USEREVENT + 3
PRIOR_SCEANE = pygame.event.Event(priorSceane)
