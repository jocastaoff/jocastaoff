import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre du jeu
largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pacman Chasse Fantômes")

# Couleurs
BLANC = (255, 255, 255)
JAUNE = (255, 255, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

# Classe pour le Pacman
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pacman.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)
        self.vitesse = 5

    def update(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            self.rect.x -= self.vitesse
        if touches[pygame.K_RIGHT]:
            self.rect.x += self.vitesse
        if touches[pygame.K_UP]:
            self.rect.y -= self.vitesse
        if touches[pygame.K_DOWN]:
            self.rect.y += self.vitesse

        # Vérifier les collisions avec les fantômes
        collisions = pygame.sprite.spritecollide(self, fantomes, False)
        if collisions:
            pygame.quit()

# Classe pour les Fantômes
class Fantome(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ROUGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largeur - self.rect.width)
        self.rect.y = random.randint(0, hauteur - self.rect.height)
        self.vitesse = random.randint(1, 3)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.vitesse * self.direction_x
        self.rect.y += self.vitesse * self.direction_y

        # Faire rebondir les fantômes sur les bords de l'écran
        if self.rect.right >= largeur or self.rect.left <= 0:
            self.direction_x *= -1
        if self.rect.bottom >= hauteur or self.rect.top <= 0:
            self.direction_y *= -1

# Création des groupes de sprites
pacman = pygame.sprite.GroupSingle(Pacman())
fantomes = pygame.sprite.Group()
for _ in range(5):
    fantome = Fantome()
    fantomes.add(fantome)

# Boucle de jeu
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pacman.update()
    fantomes.update()

    # Dessiner le fond de la fenêtre
    fenetre.fill(BLANC)

    # Dessiner les sprites
    pacman.draw(fenetre)
    fantomes.draw(fenetre)

    # Rafraîchir l'écran
    pygame.display.flip()

    # Limiter la vitesse de rafraîchissement
    clock.tick(60)

# Quitter Pygame
pygame.quit()