import pygame
import win32gui, win32con, win32api


class GUI:
    def __init__(self):
        self.windowWidth = 500
        self.windowHeigh = 200
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 30)
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeigh), pygame.NOFRAME) 
        self.hwnd = pygame.display.get_wm_info()['window']
        

        styles = win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(10, 10, 10), 0, win32con.LWA_COLORKEY)
        win32gui.SetLayeredWindowAttributes(self.hwnd, 0, 50, win32con.LWA_ALPHA)

        self.run()
               

    def align_to_league(self,hwnd):
        hwnd_league = win32gui.FindWindow(None, "League of Legends (TM) Client")
        
        if hwnd_league:
            rect = win32gui.GetWindowRect(hwnd_league)
            x = rect[0]
            y = rect[1]
            
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, self.windowWidth, self.windowHeigh, 0)
        else:
            print("Nie znaleziono okna League of Legends")

    def draw(self):
        pygame.draw.rect(self.screen, (50, 50, 50), (0, 0, self.windowWidth, self.windowHeigh), 2)
    
    def run(self):
        running = True
        while running:
            self.align_to_league(self.hwnd)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False

            self.screen.fill((0, 0, 0)) 
            self.draw()

            pygame.display.update()
        self.exit_gui() 

    def exit_gui():
        pygame.quit()