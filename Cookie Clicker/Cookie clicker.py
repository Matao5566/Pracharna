import pygame
import pandas as pd
import plotly.graph_objects as go
from pygame import mixer



# Values
values = [" ", "K", "Mil", "Bil", "Tril", "Quadrill", "Quintill", "Sextill", "Septill", "Octill", "Nonill", "Decill", "Undecill",
          "Duodecill", "Tredecill", "Quattuordecill", "Quindecill", "Sexdecill", "Septendecill",
          "Octodecill", "Novemdecill", "Vigintill"]
i = 19

# Graf
data = [[0, 0]]
data2 = [[0, 0]]

# Intialize the pygame
pygame.init()

# Background Music
mixer.music.load('OST3.wav')
Sound1 = mixer.Sound('OST3.wav')
Sound1.set_volume(0.1)
Sound1.play(-1)

# create the screen
screen = pygame.display.set_mode((1250, 800))

# Big cookie
CookieImg = pygame.image.load('bigcookie.png')
CookieX = 600
CookieY = 150
CookieY_change = 0

# Background
background = pygame.image.load('oven.png')
# Store
store = pygame.image.load('oven.png')

# Caption and Icon
pygame.display.set_caption("Cookie Clicker")
icon = pygame.image.load('cookie.png')
pygame.display.set_icon(icon)
# multiplier
multiplier = 1
# upgrade1
upgrade1 = 10
# upgrade2
upgrade2 = 100
# upgrade3
upgrade3 = 1000
# upgrade4
upgrade4 = 10**6
# upgrade5
upgrade5 = 300
# Money
money = 0
font = pygame.font.Font('freesansbold.ttf', 32)
moneyX = moneyY = 0
moneyadd = 1

# Celkem prachy
celkem = 0

# Score
score = 0
scoreX = 625
scoreY = 0

# Shop
shopX = 70
shopY = 80

# Shop icon
shop_icon = pygame.image.load('Shop.png')

# Timer
timer = 0
clock = pygame.time.Clock()
cps = 0

# Colors
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

# Toggle_shop
shop = False

def n_counter(upgrade_x):
    n = 0
    i = 0
    if upgrade_x >= 10**3:
        while upgrade_x >= 10 ** (3 + n):
            n += 3
            i += 1
    else:
        n = 0
    return n, i


def Money(values):
    if money < 10**3:
        money_value = font.render("Cookies : " + str(round(money)), True, (150, 75, 0))
        screen.blit(money_value, (moneyX, moneyY))
    elif money >= 10**3:
        money_value = font.render("Cookies : " + str(round(money/10**(n_counter(money)[0]), 2)) + values[n_counter(money)[1]], True, (150, 75, 0))
        screen.blit(money_value, (moneyX, moneyY))


def Score():
    if score < 1000000:
        score_value = font.render("Score : " + str(score) + "             " + str(round(multiplier*100)) + "%", True, (255, 255, 255))
        screen.blit(score_value, (scoreX, scoreY))
    elif score >= 1000000:
        score_value = font.render("Score : " + str(score/10**6) + "Mil"+ "             " + str(round(multiplier*100)) + "%", True, (255, 255, 255))
        screen.blit(score_value, (scoreX, scoreY))


def Cookie():
    screen.blit(CookieImg, (CookieX, CookieY))


def Shop():
    shop_value = font.render("To open shop press ->", True, (255, 255, 255))
    screen.blit(shop_value, (shopX, shopY))


def CPS():
    cps_value = font.render("Cookies per second:" + str(cps), True, (255, 255, 255))
    screen.blit(cps_value, (0, 750))


def Moneyadd(values):
    n = 63
    i = 19
    while moneyadd <= 10**n:
        n -= 3
        i -= 1
    if moneyadd >= 10**3:
        moneyadd_value = font.render("Cookies per click: " + str(round((moneyadd * multiplier)/10**n_counter(moneyadd)[0], 2)) + values[n_counter(moneyadd)[1]], True,
                                         (255, 255, 255))
        screen.blit(moneyadd_value, (0, 700))
    elif moneyadd < 10**6:
        moneyadd_value = font.render("Cookies per click: " + str(round(moneyadd * multiplier)), True,
                                     (255, 255, 255))
        screen.blit(moneyadd_value, (0, 700))


def backtobakery():
    bakery_value = font.render("To get back to bakery press <-", True, (255, 255, 255))
    screen.blit(bakery_value, (0, 400))


# Upgrades
class Upgrades:
    def __init__(self, x, y, sx, sy, text, detail, background_color, hover_color, upgrade):
        self.rect = pygame.Rect(x, y, sx, sy)
        self.text = f"{text} Price: {str(round(upgrade / 10 ** n_counter(upgrade)[0], 2)) + values[n_counter(upgrade)[1]]}"
        self.detail = detail
        self.background_color = background_color
        self.hover_color = hover_color
        self.current = False
        self.x = x
        self.y = y
        self.detail_surface = font.render(detail, False, (0, 0, 0), (255, 255, 0))

    def button_show(self, display):
        colour = self.hover_color if self.current else self.background_color
        pygame.draw.rect(display, colour, self.rect)

        upgrade1_value = font.render(self.text, True, (0, 255, 0))
        display.blit(upgrade1_value, upgrade1_value.get_rect(center=self.rect.center))

    def button_detail(self, display):
        if self.current:
            mouse_position = pygame.mouse.get_pos()
            display.blit(self.detail_surface, (mouse_position[0] + 16, mouse_position[1]))

    def focus_check(self, mouse_position, mouse_click):
        self.current = self.rect.collidepoint(mouse_position)
        return mouse_click if self.current else True

    def mouse_clicking(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            sus = True
        else:
            sus = False
        return sus


pressing = False
class Xbutton:
    def __init__(self, x, y, sx, sy, text, upgrade, prachy, background_color, press_color):
        self.rect = pygame.Rect(x, y, sx, sy)
        self.background_color = background_color
        self.current = False
        self.text = text
        self.prachy = prachy
        self.upgrade = upgrade
        self.press_color = press_color

    def button_show(self, display):
        color = self.press_color if self.current else self.background_color
        pygame.draw.rect(display, color, self.rect)
        text = font.render(self.text, True, (0, 255, 0))
        display.blit(text, text.get_rect(center=self.rect.center))
        
    def press_check(self, mouse_position):
        self.current = self.rect.collidepoint(mouse_position)
        return mouse_click if self.current else True

    def mouse_clicking(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            sus = True
        else:
            sus = False
        return sus

    def X10(self, upgrade, x, add, prachy, prachyadd):
        celkem = 0
        for i in range(10):
            celkem += upgrade
            upgrade *= x
        if prachy - celkem >= 0:
            prachy -= celkem
            prachyadd += 10*add
            sus = True
            return upgrade, prachy, prachyadd, sus
        else:
            sus = False
            return sus

    def sus(self,sus):
        if
Upgrade_1 = Upgrades(0, 90, 650, 40, "Babiččin váleček", "+1 Cookie per click", color_dark, color_light, upgrade1)

Upgrade_2 = Upgrades(0, 150, 650, 40, "Babiččina vařečka", "+10 Cookies per click", color_dark, color_light, upgrade2)

Upgrade_3 = Upgrades(0, 210, 650, 40, "Sušenková planetka", "+1% Cookies per click", color_dark, color_light, upgrade3)

Upgrade_4 = Upgrades(0, 270, 650, 40, "Sušenkový božík", "+50% Cookies per click", color_dark, color_light, upgrade4)

Upgrade_5 = Upgrades(0, 330, 650, 40, "Bába", "+1 Cookie per second", color_dark, color_light, upgrade5)

X10 = Xbutton(800, 90, 40, 40, "10x", upgrade1, money, color_dark, color_light)


def redraw():
    screen.blit(store, (0, 0))
    Money(values)
    Moneyadd(values)
    Score()
    CPS()


def update():
    Upgrade_1.button_show(screen)
    Upgrade_1.button_detail(screen)
    Upgrade_1.focus_check(mouse_pos, mouse_click)
    Upgrade_2.button_show(screen)
    Upgrade_2.button_detail(screen)
    Upgrade_2.focus_check(mouse_pos, mouse_click)
    Upgrade_3.button_show(screen)
    Upgrade_3.button_detail(screen)
    Upgrade_3.focus_check(mouse_pos, mouse_click)
    Upgrade_4.button_show(screen)
    Upgrade_4.button_detail(screen)
    Upgrade_4.focus_check(mouse_pos, mouse_click)
    Upgrade_5.button_show(screen)
    Upgrade_5.button_detail(screen)
    Upgrade_5.focus_check(mouse_pos, mouse_click)
    backtobakery()
    X10.button_show(screen)
    X10.press_check(mouse_pos)
    pygame.display.update()

# Game Loop
running = True
while running:

    redraw()
    if not shop:
        Cookie()
        Shop()
        screen.blit(shop_icon, (0, 50))

    # timer
    dt = clock.tick()
    timer += dt
    if timer >= 1000:
        timer_diff = timer % 1000
        money += cps
        timer = 0
        timer += timer_diff
        timer_diff = 0
    mouse_pos = pygame.mouse.get_pos()
    if shop:
        update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
            print(money)

            if X10.mouse_clicking(mouse_pos) and (X10.X10(upgrade1, 1.2, 100, money, moneyadd)[3], bool):
                upgrade1 = X10.X10(upgrade1, 1.2, 100, money, moneyadd)[0]
                money = X10.X10(upgrade1, 1.2, 100, money, moneyadd)[1]
                moneyadd = X10.X10(upgrade1, 1.2, 100, money, moneyadd)[2]
                Upgrade_1 = Upgrades(0, 90, 650, 40, "Babiččin váleček", "+1 Cookie per click", color_dark,
                                     color_light, upgrade1)

            if Upgrade_1.mouse_clicking(mouse_pos):
                if money - upgrade1 >= 0:
                    money -= upgrade1
                    upgrade1 *= 1.2
                    moneyadd += 100
                    Upgrade_1 = Upgrades(0, 90, 650, 40, "Babiččin váleček", "+1 Cookie per click", color_dark,
                                         color_light, upgrade1)
                    
            elif Upgrade_2.mouse_clicking(mouse_pos):
                if money - upgrade2 >= 0:
                    money -= upgrade2
                    upgrade2 *= 2
                    moneyadd += 10
                    Upgrade_2 = Upgrades(0, 150, 650, 40, "Babiččina vařečka", "+10 Cookies per click", color_dark,
                                         color_light, upgrade2)

            elif Upgrade_3.mouse_clicking(mouse_pos):
                if money - upgrade3 >= 0:
                    money -= upgrade3
                    upgrade3 *= 2
                    multiplier += 0.01
                    Upgrade_3 = Upgrades(0, 210, 650, 40, "Sušenková planetka", "+1% Cookies per click", color_dark,
                                         color_light, upgrade3)

            elif Upgrade_4.mouse_clicking(mouse_pos):
                if money - upgrade4 >= 0:
                    money -= upgrade4
                    upgrade4 *= 2
                    multiplier += 0.5
                    Upgrade_4 = Upgrades(0, 270, 650, 40, "Sušenkový božík", "+50% Cookies per click", color_dark,
                                         color_light, upgrade4)
            elif Upgrade_5.mouse_clicking(mouse_pos):
                if money - upgrade5 >= 0:
                    money -= upgrade5
                    upgrade5 *= 2
                    cps += 1
                    Upgrade_5 = Upgrades(0, 330, 650, 40, "Bába", "+1 Cookie per second", color_dark, color_light,
                                         upgrade5)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not shop:
                CookieY = 145
                money += moneyadd * multiplier
                celkem += moneyadd * multiplier
                score += 1
                data.append([score, money])
                data2.append([score, celkem])
                Moneyadd(values)
                Money(values)

            elif event.key == pygame.K_RIGHT:
                shop = True

            elif event.key == pygame.K_LEFT:
                shop = False


            # sušenka nahoru
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                CookieY = 150


    mouse_click = False
    Upgrade_1.focus_check(mouse_pos, mouse_click)
    pygame.display.update()
