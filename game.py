import pygame
import numpy as np
import math
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cubo 3D")

# Funções para rotação nos eixos X, Y, Z
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

# Função de projeção 3D para 2D
def project(vertices):
    projection_matrix = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ])
    projected_points = np.dot(vertices, projection_matrix.T)
    return projected_points

# Definição dos vértices de um cubo 3D
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

# Arestas do cubo (conectando os vértices)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0), # Arestas da base inferior
    (4, 5), (5, 6), (6, 7), (7, 4), # Arestas da base superior
    (0, 4), (1, 5), (2, 6), (3, 7)  # Arestas verticais conectando as bases
]

# Função para transladar os pontos para o centro da tela
def translate_to_center(vertices):
    translated = []
    for vertex in vertices:
        translated.append([vertex[0] * 100 + screen_width // 2, vertex[1] * 100 + screen_height // 2])
    return np.array(translated)

# Função para gerar uma cor aleatória
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Variável que armazena a cor atual do cubo
cube_color = (255, 255, 255)  # Branco inicial

# Loop principal
clock = pygame.time.Clock()
theta_x, theta_y, theta_z = 0, 0, 0

running = True
while running:
    screen.fill((0, 0, 0))
    
    # Rotação do cubo
    rotated_vertices = rotate_x(cube_vertices, theta_x)
    rotated_vertices = rotate_y(rotated_vertices, theta_y)
    rotated_vertices = rotate_z(rotated_vertices, theta_z)
    
    # Projeção dos vértices para 2D
    projected_vertices = project(rotated_vertices)
    
    # Transladar para o centro da tela
    projected_vertices = translate_to_center(projected_vertices)
    
    # Desenhar as arestas do cubo com a cor atual
    for edge in cube_edges:
        pygame.draw.line(screen, cube_color, projected_vertices[edge[0]], projected_vertices[edge[1]], 2)
    
    # Verificar teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:  # Se a tecla 'C' for pressionada, muda a cor
        cube_color = random_color()  # Gera uma cor aleatória
    
    # Atualizar as rotações
    theta_x += 0.01
    theta_y += 0.01
    theta_z += 0.01
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)
    
    # Eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
