import random
import numpy as np
import pygame
import sys

SIZE = 6
START_X = 0
START_Y = 0
SCREEN_SIZE = 800
SPACING = SCREEN_SIZE / SIZE

board = np.zeros((SIZE, SIZE))
screen = None

def updateWindow(visited_fields):
    screen.fill((0, 0, 0))
    coordinates = []
    for field in visited_fields:
        offset = int(SPACING / 2)
        coordinates.append((field[0] * SPACING + offset, field[1] * SPACING + offset))
    
    if len(coordinates) >= 2:
        pygame.draw.lines(screen, (255, 255, 255), False, coordinates, int(SPACING / 2))
    pygame.display.flip()

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        return False
    return True

def getPossibleMoves(x, y):
    possible_moves = []
    if x > 0 and board[x-1][y] == 0:
        possible_moves.append([-1, 0])
    if x < SIZE - 1 and board[x+1][y] == 0:
        possible_moves.append([1, 0])
    if y > 0 and board[x][y-1] == 0:
        possible_moves.append([0, -1])
    if y < SIZE - 1 and board[x][y+1] == 0:
        possible_moves.append([0, 1])
    return possible_moves

def isBoardFilled():
    for row in board:
        for field in row:
            if field == 0:
                return False
    return True

def walk(visited_fields, x, y):
    updateWindow(visited_fields)
    if handleEvents() == False:
        return False
    board[x][y] = 1
    possible_moves = getPossibleMoves(x, y)
    # End condition: if actor can't move check if board is filled
    if len(possible_moves) == 0:
        if isBoardFilled():
            return True
        board[x][y] = 0
        return False
    random.shuffle(possible_moves)
    for move in possible_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        visited_fields.append([new_x, new_y])
        if walk(visited_fields, new_x, new_y):
            return True
        visited_fields.pop()
    board[x][y] = 0
    return False

if __name__ == "__main__":
    sys.setrecursionlimit(max(SIZE * SIZE, 1000))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    visited_fields = [[START_X, START_Y]]
    updateWindow(visited_fields)
    if walk(visited_fields, START_X, START_Y):
        print(visited_fields)

        updateWindow(visited_fields)

        running = True

        while running:
            running = handleEvents()
    else:
        print("Unable to fill board completley")

