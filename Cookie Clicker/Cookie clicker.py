import pygame
import pandas as pd
import plotly.graph_objects as go

# Values
values = ["Mil", "Bil", "Tril", "Quadrill", "Quintill", "Sextill", "Septill", "Octill", "Nonill", "Decill", "Undecill",
          "Duodecill", "Tredecill", "Quattuordecill", "Quindecill", "Sexdecill", "Septendecill",
          "Octodecill", "Novemdecill", "Vigintill"]
i = 19

# Graf
data = [[0, 0]]
data2 = [[0, 0]]

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1250, 800))


# Big cookie
CookieImg = pygame.image.load('bigcookie.png')
CookieX = 600
CookieY = 150
CookieY_change = 0
# zabí se
# Background
background = pygame.image.load('oven.png')
# Store
store = pygame.image.load('oven.png')

# Caption and Icon
pygame.display.set_caption("Cookie Clicker")
icon = pygame.image.load('cookie.png')
pygame.display.set_icon(icon)

# upgrade1
upgrade1 = 10
# upgrade2
upgrade2 = 150
# upgrade3
upgrade3 = 1000
# upgrade4
upgrade4 = 100000
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


def Money(i, values):
    n = 63
    while moneyadd <= 10 ** n:
        n -= 3
        i -= 1
    if money < 1000000:
        money_value = font.render("Cookies : " + str(round(money)), True, (150, 75, 0))
        screen.blit(money_value, (moneyX, moneyY))
    elif money >= 1000000:
        money_value = font.render("Cookies : " + str(round(money/10**n, 2)) + values[i], True, (150, 75, 0))
        screen.blit(money_value, (moneyX, moneyY))


def Score():
    if score < 1000000:
        score_value = font.render("Score : " + str(score), True, (255, 255, 255))
        screen.blit(score_value, (scoreX, scoreY))
    elif score >= 1000000:
        score_value = font.render("Score : " + str(score/10**6) + "Mil", True, (255, 255, 255))
        screen.blit(score_value, (scoreX, scoreY))


def Cookie():
    screen.blit(CookieImg, (CookieX, CookieY))


def Shop():
    shop_value = font.render("To open shop press ->", True, (255, 255, 255))
    screen.blit(shop_value, (shopX, shopY))


def Moneyadd(i, values):
    n = 63
    while moneyadd <= 10**n:
        n -= 3
        i -= 1
    if moneyadd >= 1000000:
        moneyadd_value = font.render("Cookies per click: " + str(round(moneyadd/10**n, 2)) + values[i], True,
                                         (255, 255, 255))
        screen.blit(moneyadd_value, (0, 700))
    else:
        moneyadd_value = font.render("Cookies per click: " + str(round(moneyadd)), True,
                                     (255, 255, 255))
        screen.blit(moneyadd_value, (0, 700))


def Backtobakery():
    bakery_value = font.render("To get back to bakery press <-", True, (255, 255, 255))
    screen.blit(bakery_value, (0, 400))


def Upgrade1():
    upgrade1_value = font.render("<1> Babiččina volba (+1 Cookie per click) Price :" + str(round(upgrade1)), True,
                                 (0, 255, 0))
    screen.blit(upgrade1_value, (0, 100))


def Upgrade2():
    upgrade2_value = font.render("<2> Sušenkové Mlsání (1.5x Cookies per click) Price :" + str(round(upgrade2)), True,
                                 (0, 255, 0))
    screen.blit(upgrade2_value, (0, 150))


def Upgrade3():
    upgrade3_value = font.render("<3> Mlsný jazýček (+100 Cookies per click) Price :" + str(round(upgrade3)), True,
                                 (0, 255, 0))
    screen.blit(upgrade3_value, (0, 200))

def Upgrade4():
    upgrade4_value = font.render("<4> Dvojité sušenkové krabice (2x vaše cookies) Price :" + str(round(upgrade4)),
                                 True, (0, 255, 0))
    screen.blit(upgrade4_value, (0, 250))


def update():
    screen.blit(store, (0, 0))
    Money(i, values)
    Upgrade1()
    Upgrade2()
    Upgrade3()
    Upgrade4()
    Moneyadd(i, values)
    Score()
    Backtobakery()
    pygame.display.update()

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(shop_icon, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                CookieY = 145
                money += moneyadd
                celkem += moneyadd
                score += 1
                data.append([score, money])
                data2.append([score, celkem])
                Moneyadd(i, values)
            if event.key == pygame.K_RIGHT:
                screen.blit(store, (0, 0))
                update()
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        break
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                        if money - upgrade1 >= 0:
                            money -= upgrade1
                            upgrade1 += 10
                            moneyadd += 1
                            update()
                        else:
                            continue
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        if money - upgrade2 >= 0:
                            money -= upgrade2
                            upgrade2 += (upgrade2/2)
                            moneyadd += moneyadd
                            update()
                        else:
                            continue
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                        if money - upgrade3 >= 0:
                            money -= upgrade3
                            upgrade3 += upgrade3
                            moneyadd += 100
                            update()
                        else:
                            continue
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                        if money - upgrade4 >= 0:
                            money -= upgrade4
                            upgrade4 += upgrade4 * 2
                            moneyadd += money
                            update()
                        else:
                            continue
                    else:
                        continue

            if event.key == pygame.K_ESCAPE:
                print(data)
                print(data2)
                df = pd.DataFrame(data, columns=["x", "y"])  # převedu data na formát DataFrame

                fig = go.Figure()  # do prom. si uložíme "obejkt" graf

                fig.add_trace(go.Scatter(  # do grafu přidáme grafovou čáru a upřesníme její vlastnosti
                    x=df["x"],
                    y=df["y"],
                    name="na druhou",
                    mode="lines+markers",
                    marker=dict({"symbol": "arrow-bar-left", "size": 6}),
                    line=dict({"width": 2, "shape": "linear", "dash": "dashdot"}),
                    fill="tozeroy",
                ))
                df2 = pd.DataFrame(data2, columns=["x", "y"])  # převedu data na formát DataFrame

                fig2 = go.Figure()  # do prom. si uložíme "obejkt" graf

                fig2.add_trace(go.Scatter(  # do grafu přidáme grafovou čáru a upřesníme její vlastnosti
                    x=df2["x"],
                    y=df2["y"],
                    name="na druhou",
                    mode="lines+markers",
                    marker=dict({"symbol": "arrow-bar-left", "size": 6}),
                    line=dict({"width": 2, "shape": "linear", "dash": "dashdot"}),
                    fill="tozeroy",
                ))
                fig2.show()
                fig.show()
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                CookieY = 150
    Cookie()
    Shop()
    Money(i, values)
    Score()
    Moneyadd(i, values)
    pygame.display.update()
