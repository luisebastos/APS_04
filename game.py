import pygame
import numpy as np
import math

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cubo 3D")

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

# definição dos vértices de um cubo 3D
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
    (0, 1), (1, 2), (2, 3), (3, 0), # base inferior
    (4, 5), (5, 6), (6, 7), (7, 4), # base superior
    (0, 4), (1, 5), (2, 6), (3, 7)  # verticais conectando as bases
]

# translação para o centro da tela
def translate_to_center(vertices):
    translated = []
    for vertex in vertices:
        translated.append([vertex[0] * 100 + screen_width // 2, vertex[1] * 100 + screen_height // 2])
    return np.array(translated)

clock = pygame.time.Clock()
theta_x, theta_y, theta_z = 0, 0, 0
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    theta_y -= 0.05  # Rotaciona ao redor do eixo Y para a esquerda
if keys[pygame.K_RIGHT]:
    theta_y += 0.05  # Rotaciona ao redor do eixo Y para a direita
if keys[pygame.K_UP]:
    theta_x -= 0.05  # Rotaciona ao redor do eixo X para cima
if keys[pygame.K_DOWN]:
    theta_x += 0.05  # Rotaciona ao redor do eixo X para baixo
if keys[pygame.K_w]:
    cube_vertices[:, 2] += 0.1  # Movimenta o cubo para "frente" ao longo do eixo Z
if keys[pygame.K_s]:
    cube_vertices[:, 2] -= 0.1  # Movimenta o cubo para "trás" ao longo do eixo Z

running = True
while running:
    screen.fill((0, 0, 0))
    
    # rotação do cubo
    rotated_vertices = rotate_x(cube_vertices, theta_x)
    rotated_vertices = rotate_y(rotated_vertices, theta_y)
    rotated_vertices = rotate_z(rotated_vertices, theta_z)
    
    # projeção dos vértices para 2D
    projected_vertices = project(rotated_vertices)
    
    # transladar para o centro da tela
    projected_vertices = translate_to_center(projected_vertices)
    
    # desenhar as arestas do cubo
    for edge in cube_edges:
        pygame.draw.line(screen, (255, 255, 255), projected_vertices[edge[0]], projected_vertices[edge[1]], 2)
    
    # atualizar as rotações
    theta_x += 0.01
    theta_y += 0.01
    theta_z += 0.01
    
    # atualizar a tela
    pygame.display.flip()
    clock.tick(60)
    
    # eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
