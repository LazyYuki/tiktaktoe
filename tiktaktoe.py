import pygame, settings, math

class ai:
    def __init__(self, _game) -> None:
        self.game = _game

    def move(self):

        return -1, -1

class tiktaktoe:
    size = 3
    currentPlayer = 0
    clicked = False

    def __init__(self, _screen) -> None:
        self.screen = _screen
        self.reset()
        self.setupDraw()
        self.ai = ai(self.game)

    def reset(self):
        self.game = [[0 for _ in range(self.size)] for __ in range(self.size)]
    
    def winCheck(self, x: int, y: int):
        size_x = self.size
        size_y = self.size
        winLen = self.size

        start_UpDown = y - winLen + 1
        count_UpDown = 0

        start_Side = x - winLen + 1
        count_Side = 0

        count_diag_li = 0

        start_diag_re = x + winLen - 1
        count_diag_re = 0

        for i in range(winLen*2 - 1):
            if not(start_UpDown + i < 0) and not(start_UpDown + i >= size_y):
                count_UpDown = count_UpDown + 1 if self.game[start_UpDown + i][x] == self.currentPlayer + 1 else 0
            if not(start_Side + i < 0) and not(start_Side + i >= size_x):
                count_Side = count_Side + 1 if self.game[y][start_Side + i] == self.currentPlayer + 1 else 0
            if not(start_UpDown + i < 0) and not(start_UpDown + i >= size_y) and not(start_Side + i < 0) and not(start_Side + i >= size_x):
                count_diag_li = count_diag_li + 1 if self.game[start_UpDown + i][start_Side + i] == self.currentPlayer + 1 else 0
            if not(start_UpDown + i < 0) and not(start_UpDown + i >= size_y) and not(start_diag_re - i < 0) and not(start_diag_re - i >= size_x):
                count_diag_re = count_diag_re + 1 if self.game[start_UpDown + i][start_diag_re - i] == self.currentPlayer + 1 else 0
            if count_UpDown == winLen or count_Side == winLen or count_diag_li == winLen or count_diag_re == winLen:
                return True

        return False

    def update(self, dt, keys, mouse):
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True

            i, j = self.getMouseFieldIndex(mouse)

            if i != -1 and j != -1:
                if not self.game[i][j]:
                    self.game[i][j] = self.currentPlayer + 1

                    if self.winCheck(j, i):
                        print("Player", self.currentPlayer + 1, "has won!")
                    else:
                        self.currentPlayer = not self.currentPlayer

        if self.clicked and not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def updateAgainstAi(self, dt, keys, mouse):
        aiMove = False
        i, j = -1, -1

        if self.currentPlayer:
            i, j = self.ai.move()
            aiMove = True

        if pygame.mouse.get_pressed()[0] and not self.clicked or aiMove:
            if not aiMove:
                self.clicked = True
                i, j = self.getMouseFieldIndex(mouse)

            if i != -1 and j != -1:
                if not self.game[i][j]:
                    self.game[i][j] = self.currentPlayer + 1

                    if self.winCheck(j, i):
                        print("Player", self.currentPlayer + 1, "has won!")
                    else:
                        self.currentPlayer = not self.currentPlayer

            if self.clicked and not pygame.mouse.get_pressed()[0]:
                self.clicked = False



    def getMouseFieldIndex(self, pos):
        x = pos[0] - self.startX
        y = pos[1] - self.startY

        if x >= 0 and y >= 0 and x <= settings.CUBESIZE * 3 and y <= settings.CUBESIZE * 3:
            i = math.floor(x / settings.CUBESIZE)
            j = math.floor(y / settings.CUBESIZE)

            return i, j

        return -1, -1

    def setupDraw(self):
        self.startX = settings.WIDTH / 2 - settings.CUBESIZE / 2 - settings.CUBESIZE
        self.startY = settings.HEIGHT/ 2 - settings.CUBESIZE / 2 - settings.CUBESIZE

    def drawCircle(self, pos):
        pygame.draw.circle(self.screen, settings.WHITE, pos, settings.CUBESIZE / 2 * 0.8, 3)

    def drawCross(self, pos):
        pygame.draw.line(self.screen, settings.WHITE, (pos[0] - (settings.CUBESIZE / 2 * 0.8), pos[1] - (settings.CUBESIZE / 2 * 0.8)), (pos[0] + (settings.CUBESIZE / 2 * 0.8), pos[1] + (settings.CUBESIZE / 2 * 0.8)), 3)
        pygame.draw.line(self.screen, settings.WHITE, (pos[0] - (settings.CUBESIZE / 2 * 0.8), pos[1] + (settings.CUBESIZE / 2 * 0.8)), (pos[0] + (settings.CUBESIZE / 2 * 0.8), pos[1] - (settings.CUBESIZE / 2 * 0.8)), 3)

    def draw(self):
        for i in range(self.size + 1):
            pygame.draw.line(self.screen, settings.WHITE, (self.startX, self.startY + settings.CUBESIZE * i), (self.startX + settings.CUBESIZE * 3, self.startY + settings.CUBESIZE * i), 3)
            pygame.draw.line(self.screen, settings.WHITE, (self.startX + settings.CUBESIZE * i, self.startY), (self.startX + settings.CUBESIZE * i, self.startY + settings.CUBESIZE * 3), 3)

        for i in range(self.size):
            for j in range(self.size):
                if self.game[i][j]:
                    posX = self.startX + settings.CUBESIZE * i + settings.CUBESIZE / 2
                    posY = self.startY + settings.CUBESIZE * j + settings.CUBESIZE / 2
                    
                    if self.game[i][j] == 1:
                        self.drawCross((posX, posY))
                    else:
                        self.drawCircle((posX, posY))
