import pygame
import numpy as np
import math
import random

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cubo e Pirâmide 3D")

# rotação nos eixos X, Y, Z
def rotate_x(vertices, theta):
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta)]
    ])
    return np.dot(vertices, rotation_matrix)

def rotate_y(vertices, theta):
    rotation_matrix = np.array([
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ])
    return np.dot(vertices, rotation_matrix)

def rotate_z(vertices, theta):
    rotation_matrix = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ])
    return np.dot(vertices, rotation_matrix)

# projeção 3D para 2D
def project(vertices):
    projection_matrix = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ])
    projected_points = np.dot(vertices, projection_matrix.T)
    return projected_points

# vértices de um cubo 3D
cube_vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])

# arestas do cubo (conectando os vértices)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # base inferior
    (4, 5), (5, 6), (6, 7), (7, 4),  # base superior
    (0, 4), (1, 5), (2, 6), (3, 7)   # verticais conectando as bases
]

# vértices de uma pirâmide 3D
pyramid_vertices = np.array([
    [-1, -1, -1],  # inferior esquerda
    [1, -1, -1],   # inferior direita
    [1, 1, -1],    # superior direita
    [-1, 1, -1],   # superior esquerda
    [0, 0, 1]      # superior
])

# conectando os vértices
pyramid_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # arestas da base
    (0, 4), (1, 4), (2, 4), (3, 4)   # arestas conectando a base ao vértice
]

# transladar os pontos para o centro da tela
def translate_to_center(vertices):
    translated = []
    for vertex in vertices:
        translated.append([vertex[0] * 100 + screen_width // 2, vertex[1] * 100 + screen_height // 2])
    return np.array(translated)

# gerar uma cor aleatória
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# armazena a cor atual das formas
shape_color = (255, 255, 255)  

# controla se o cubo ou a pirâmide será desenhado
draw_cube = True

clock = pygame.time.Clock()
theta_x, theta_y, theta_z = 0, 0, 0

running = True
while running:
    screen.fill((0, 0, 0))
    
    # teclas pressionadas para mudar a forma
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:  # Se a tecla 'C' for pressionada, muda a cor
        shape_color = random_color()  # Gera uma cor aleatória
    if keys[pygame.K_s]:  # Se a tecla 'S' for pressionada, alterna entre cubo e pirâmide
        draw_cube = not draw_cube
    
    # rotação das formas
    if draw_cube:
        rotated_vertices = rotate_x(cube_vertices, theta_x)
        rotated_vertices = rotate_y(rotated_vertices, theta_y)
        rotated_vertices = rotate_z(rotated_vertices, theta_z)
        projected_vertices = project(rotated_vertices)
        projected_vertices = translate_to_center(projected_vertices)
        
        # desenhar o cubo
        for edge in cube_edges:
            pygame.draw.line(screen, shape_color, projected_vertices[edge[0]], projected_vertices[edge[1]], 2)
    else:
        rotated_vertices = rotate_x(pyramid_vertices, theta_x)
        rotated_vertices = rotate_y(rotated_vertices, theta_y)
        rotated_vertices = rotate_z(rotated_vertices, theta_z)
        projected_vertices = project(rotated_vertices)
        projected_vertices = translate_to_center(projected_vertices)
        
        # Ddsenhar a pirâmide
        for edge in pyramid_edges:
            pygame.draw.line(screen, shape_color, projected_vertices[edge[0]], projected_vertices[edge[1]], 2)
    
    # atualizar as rotações
    theta_x += 0.01
    theta_y += 0.01
    theta_z += 0.01
    
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
