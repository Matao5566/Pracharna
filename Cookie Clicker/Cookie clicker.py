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

#Background Music
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

#Colors
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

def Money(values):
    m = 6
    j = 0
    while money >= 10 ** m:
        if m >= 66:
            break
        m += 3
        j += 1

    if money < 10**6:
        money_value = font.render("Cookies : " + str(round(money)), True, (150, 75, 0))
        screen.blit(money_value, (moneyX, moneyY))
    elif money >= 10**6:
        money_value = font.render("Cookies : " + str(round(money/10**(m-3), 2)) + values[j-1], True, (150, 75, 0))
        screen.blit(money_value, (moneyX, moneyY))
    # print(m, j)

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
    if moneyadd >= 10**6:
        moneyadd_value = font.render("Cookies per click: " + str(round((moneyadd * multiplier)/10**n, 2)) + values[i], True,
                                         (255, 255, 255))
        screen.blit(moneyadd_value, (0, 700))
    elif moneyadd < 10**6:
        moneyadd_value = font.render("Cookies per click: " + str(round(moneyadd * multiplier)), True,
                                     (255, 255, 255))
        screen.blit(moneyadd_value, (0, 700))
    # print(n, i)

def Backtobakery():
    bakery_value = font.render("To get back to bakery press <-", True, (255, 255, 255))
    screen.blit(bakery_value, (0, 400))

#Upgrades

class Upgrades:
    def __init__(self, x, y, sx, sy, text, detail, background_color, hover_color):
        self.rect = pygame.Rect(x, y, sx, sy)
        self.text = text
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
        display.blit(upgrade1_value, (10, 100))


    def button_detail(self, display):
        if self.current:
            mouse_pos = pygame.mouse.get_pos()
            display.blit(self.detail_surface, (mouse_pos[0] + 16, mouse_pos[1]))

    def focus_check(self, mouse_pos, mouse_click):
        self.current = self.rect.collidepoint(mouse_pos)
        return mouse_click if self.current else True

def n_counter(upgrade_x):
    n = 0
    i = 0
    if upgrade_x > 10**3:
        while upgrade_x >= 10 ** n:
            n += 3
            i += 1
    else:
        n = 0
    return n, i

# def n_counter(upgrade_x):
#     n = 63
#     i = 19
#     while upgrade_x <= 10 ** n:
#         n -= 3
#         i -= 1
#     return n




def Upgrade1(values):
    n = 63
    i = 19
    while upgrade1 <= 10**n:
        n -= 3
        i -= 1

    pygame.draw.rect(screen, color_light, [0, 95, 1000, 40])

    if upgrade1 >= 10**6:
        upgrade1_value = font.render("<1> Babiččina volba (+1 Cookie per click) Price :" + str(round(upgrade1/10**n, 2))
                                     + values[i], True, (0, 255, 0))
        screen.blit(upgrade1_value, (10, 100))
    elif upgrade1 < 10**6:
        upgrade1_value = font.render("<1> Babiččina volba (+1 Cookie per click) Price :" + str(round(upgrade1)), True,
                                     (0, 255, 0))
        screen.blit(upgrade1_value, (10, 100))



def Upgrade2(values):
    n = 63
    i = 19
    while upgrade2 <= 10**n:
        n -= 3
        i -= 1
    if upgrade2 >= 10**6:
        upgrade2_value = font.render("<2> Sušenkové Mlsání (+10 Cookies per click) Price :" + str(round(upgrade2/10**n, 2))
                                     + values[i], True, (0, 255, 0))
        screen.blit(upgrade2_value, (0, 150))
    elif upgrade2 < 10**6:
        upgrade2_value = font.render("<2> Sušenkové Mlsání (+10 Cookies per click) Price :" + str(round(upgrade2)), True,
                                     (0, 255, 0))
        screen.blit(upgrade2_value, (0, 150))


def Upgrade3(values):
    n = 63
    i = 19
    while upgrade3 <= 10**n:
        n -= 3
        i -= 1
    if upgrade3 >= 10**6:
        upgrade3_value = font.render("<3> Mlsný jazýček (+1% Cookies per click) Price :" + str(round(upgrade3/10**n, 2))
                                     + values[i], True, (0, 255, 0))
        screen.blit(upgrade3_value, (0, 200))
    elif upgrade3 < 10**6:
        upgrade3_value = font.render("<3> Mlsný jazýček (+1% Cookies per click) Price :" + str(round(upgrade3)), True,
                                     (0, 255, 0))
        screen.blit(upgrade3_value, (0, 200))


def Upgrade4(values):
    m = 6
    j = 0
    while upgrade4 >= 10 ** m:
        if m >= 66:
            break
        m += 3
        j += 1
    if upgrade4 >= 10**6:
        upgrade4_value = font.render("<4> Dvojité sušenkové krabice (+50% Cookies per click) Price :" + str(round(upgrade4/10**(m-3), 2))
                                     + values[j-1], True, (0, 255, 0))
        screen.blit(upgrade4_value, (0, 250))
    elif upgrade4 < 10**6:
        upgrade4_value = font.render("<4> Dvojité sušenkové krabice (+50% Cookies per click) Price :" + str(round(upgrade4)),
                                     True, (0, 255, 0))
        screen.blit(upgrade4_value, (0, 250))


def Upgrade5(values):
    m = 6
    j = 0
    while upgrade5 >= 10 ** m:
        if m >= 66:
            break
        m += 3
        j += 1
    if upgrade5 >= 10**6:
        upgrade5_value = font.render("<5> Babka (+1 Cookies per second) Price :" + str(round(upgrade5/10**(m-3), 2))
                                     + values[j-1], True, (0, 255, 0))
        screen.blit(upgrade5_value, (0, 300))
    elif upgrade5 < 10**6:
        upgrade5_value = font.render("<5> Babka (+1 Cookies per second) Price :" + str(round(upgrade5)),
                                     True, (0, 255, 0))
        screen.blit(upgrade5_value, (0, 300))


shop = False


def toggle_shop(shop):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        shop = True
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        shop = False
    return shop


def redraw():
    screen.blit(store, (0, 0))
    Money(values)
    Moneyadd(values)
    Score()
    CPS()


def update():
    Upgrade_1.button_show(screen)
    Upgrade_1.button_detail(screen)
    Upgrade2(values)
    Upgrade3(values)
    Upgrade4(values)
    Upgrade5(values)
    Backtobakery()
    pygame.display.update()

Upgrade_1 = Upgrades(0, 95, 1000, 40, "Babiččin váleček Price :" + str(round(upgrade1 / 10 ** n_counter(upgrade1)[0], 2)) + values[n_counter(upgrade1)[1]], "+1 Cookie per click", color_dark, color_light)

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

    if shop:
        update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True

            if event.key == pygame.K_SPACE and not shop:
                CookieY = 145
                money += moneyadd * multiplier
                celkem += moneyadd * multiplier
                score += 1
                data.append([score, money])
                data2.append([score, celkem])
                Moneyadd(values)
                Money(values)

            if event.key == pygame.K_RIGHT:
                shop = True

            if event.key == pygame.K_LEFT:
                shop = False

            if event.key == pygame.K_1 and shop:
                if money - upgrade1 >= 0:
                    money -= upgrade1
                    upgrade1 += 15
                    moneyadd += 100
                    Upgrade_1 = Upgrades(0, 95, 1000, 40, "Babiččin váleček Price :" + str(
                        round(upgrade1 / 10 ** n_counter(upgrade1)[0], 2)) + values[n_counter(upgrade1)[1]],
                                         "+1 Cookie per click", color_dark, color_light)

            if event.key == pygame.K_2 and shop:
                if money - upgrade2 >= 0:
                    money -= upgrade2
                    upgrade2 += 200
                    moneyadd += 10
                    Upgrade_1 = Upgrades(0, 95, 1000, 40, "Babiččin váleček Price :" + str(
                        round(upgrade1 / 10 ** n_counter(upgrade1)[0], 2)) + values[n_counter(upgrade1)[1]],
                                         "+1 Cookie per click", color_dark, color_light)

            if event.key == pygame.K_3 and shop:
                if money - upgrade3 >= 0:
                    money -= upgrade3
                    upgrade3 += 1.25 * upgrade3
                    multiplier += 0.01
                    Upgrade_1 = Upgrades(0, 95, 1000, 40, "Babiččin váleček Price :" + str(
                        round(upgrade1 / 10 ** n_counter(upgrade1)[0], 2)) + values[n_counter(upgrade1)[1]],
                                         "+1 Cookie per click", color_dark, color_light)

            if event.key == pygame.K_4 and shop:
                if money - upgrade4 >= 0:
                    money -= upgrade4
                    upgrade4 += upgrade4 * 1.5
                    multiplier += 0.5
                    Upgrade_1 = Upgrades(0, 95, 1000, 40, "Babiččin váleček Price :" + str(
                        round(upgrade1 / 10 ** n_counter(upgrade1)[0], 2)) + values[n_counter(upgrade1)[1]],
                                         "+1 Cookie per click", color_dark, color_light)

            if event.key == pygame.K_5 and shop:
                if money - upgrade5 >= 0:
                    money -= upgrade5
                    upgrade5 += 300 * 1.2
                    cps += 1
                    Upgrade_1 = Upgrades(0, 95, 1000, 40, "Babiččin váleček Price :" + str(
                        round(upgrade1 / 10 ** n_counter(upgrade1)[0], 2)) + values[n_counter(upgrade1)[1]],
                                         "+1 Cookie per click", color_dark, color_light)

            # sušenka nahoru
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                CookieY = 150

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False
    screen2button = Upgrade_1.focus_check(mouse_pos, mouse_click)

    pygame.display.update()
