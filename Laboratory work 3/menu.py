import pygame
from game_data import btn_s
import sys
from settings import screen_width


class MenuBtn(pygame.sprite.Sprite):
    def __init__(self, pos, icon_speed):
        super().__init__()
        self.image = pygame.Surface((200, 80))
        self.image.fill('grey')
        self.rect = self.image.get_rect(center=pos)

        self.detection_zone = pygame.Rect(self.rect.midtop[0] - (icon_speed / 2),
                                          self.rect.midtop[1] - (icon_speed / 2),
                                          icon_speed, icon_speed)


class MenuIcon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('/PyCharm/Ознакомление/pygame_level/graphics/overworld/hat.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.center = self.pos


class Text:
    def __init__(self, btn_content, pos):
        self.font = pygame.font.SysFont('Arial', 40)
        self.text_surf = self.font.render(btn_content, True, 'Black')
        self.text_rect = self.text_surf.get_rect(center=(pos[0], pos[1]))


class About:
    def __init__(self, surface, btn_content, create_menu):
        self.list_info = []
        self.display_surface = surface
        self.create_menu = create_menu
        self.bg = pygame.image.load(
            '/PyCharm/Ознакомление/pygame_level/graphics/menu/menu.jpg').convert_alpha()
        shift = 0
        for i in btn_content:
            shift += 50
            self.font = pygame.font.SysFont('Arial', 40)
            self.text_surf = self.font.render(i, True, 'Black')
            self.text_rect = self.text_surf.get_rect(topleft=(screen_width / 2-200, 0 + 200 + shift))
            self.list_info.append((self.text_surf, self.text_rect))

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu()

    def run(self):
        self.input()
        self.display_surface.blit(self.bg, (0, 0))
        for i in range(len(self.list_info)):
            self.display_surface.blit(self.list_info[i][0], self.list_info[i][1])


class Records:
    def __init__(self, surface, score_content, create_menu, name):
        self.list_score = []
        self.list_name = []
        self.text = []
        self.display_surface = surface
        self.create_menu = create_menu
        self.bg = pygame.image.load(
            '/PyCharm/Ознакомление/pygame_level/graphics/menu/menu.jpg').convert_alpha()
        shift = 0

        self.font = pygame.font.SysFont('Arial', 60)
        self.text_surf = self.font.render('Records', True, 'Black')
        self.text_rect = self.text_surf.get_rect(center=(screen_width / 2, 0 + 100))
        self.text.append((self.text_surf, self.text_rect))

        for i in name:
            shift += 50
            self.font = pygame.font.SysFont('Arial', 40)
            self.text_surf = self.font.render(i, True, 'Black')
            self.text_rect = self.text_surf.get_rect(center=((screen_width / 2) - 50, 0 + 200 + shift))
            self.list_name.append((self.text_surf, self.text_rect))

        shift = 0

        for i in score_content:
            shift += 50
            self.font = pygame.font.SysFont('Arial', 40)
            self.text_surf = self.font.render(i, True, 'Black')
            self.text_rect = self.text_surf.get_rect(center=(screen_width / 2 + 50, 0 + 200 + shift))
            self.list_score.append((self.text_surf, self.text_rect))

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu()

    def run(self):
        self.input()
        self.display_surface.blit(self.bg, (0, 0))
        for i in range(len(self.list_score)):
            self.display_surface.blit(self.list_score[i][0], self.list_score[i][1])
        for i in range(len(self.list_name)):
            self.display_surface.blit(self.list_name[i][0], self.list_name[i][1])
        self.display_surface.blit(self.text[0][0], self.text[0][1])


class Menu:
    def __init__(self, current_btn, max_btn, surface, create_overworld, create_about, create_records):
        # setup
        self.create_overworld = create_overworld
        self.create_records = create_records
        self.create_about = create_about
        self.display_surface = surface
        self.current_btn = current_btn
        self.max_btn = max_btn
        self.menu = pygame.image.load(
            '/PyCharm/Ознакомление/pygame_level/graphics/menu/menu.jpg').convert_alpha()

        # movement logic
        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 9

        # sprites
        self.setup_btn()
        self.setup_icon()

    def setup_btn(self):
        self.btn_s = pygame.sprite.Group()
        self.text = []

        for btn_data in btn_s.values():
            btn_sprite = MenuBtn(btn_data['node_pos'], self.speed)
            self.btn_s.add(btn_sprite)
            btn_sprite = Text(btn_data['content'], btn_data['node_pos'])
            self.text.append(btn_sprite)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = MenuIcon(self.btn_s.sprites()[self.current_btn].rect.midtop)
        self.icon.add(icon_sprite)

    def draw_paths(self):
        points = [btn['node_pos'] for btn in btn_s.values()]
        pygame.draw.lines(self.display_surface, '#a04f45', False, points, 6)

    def draw_bg(self, surface):
        surface.blit(self.menu, (0, 0))

    def input(self):
        if not self.moving:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and self.current_btn < self.max_btn:
                self.move_direction = self.get_movement_data('next')
                self.current_btn += 1
                self.moving = True
            elif keys[pygame.K_UP] and self.current_btn > 0:
                self.move_direction = self.get_movement_data('previous')
                self.current_btn -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                if self.current_btn == 0:
                    self.create_overworld(0, 0)
                if self.current_btn == 1:
                    self.create_about()
                if self.current_btn == 2:
                    self.create_records()
                if self.current_btn == 3:
                    sys.exit()

    def get_movement_data(self, target):
        start = pygame.math.Vector2(self.btn_s.sprites()[self.current_btn].rect.midtop)

        if target == 'next':
            end = pygame.math.Vector2(self.btn_s.sprites()[self.current_btn + 1].rect.midtop)
        else:
            end = pygame.math.Vector2(self.btn_s.sprites()[self.current_btn - 1].rect.midtop)

        return (end - start).normalize()

    def update_icon_pos(self):
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_btn = self.btn_s.sprites()[self.current_btn]
            if target_btn.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def run(self):
        self.input()
        self.update_icon_pos()
        self.icon.update()

        self.draw_bg(self.display_surface)
        self.draw_paths()
        self.btn_s.draw(self.display_surface)
        for i in self.text:
            self.display_surface.blit(i.text_surf, i.text_rect)
        self.icon.draw(self.display_surface)
