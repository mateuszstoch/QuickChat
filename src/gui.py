import pygame
from time import sleep
import win32gui, win32con, win32api

TOGGLE_UI = pygame.USEREVENT + 1
NEXT_PAGE = pygame.USEREVENT + 2
PREV_PAGE = pygame.USEREVENT + 3

class Page:
    def __init__(self,category=None,page_number=0):
        self.category = category
        self.page_number = page_number
    
class GUI:
    def __init__(self):
        self.page = Page()
        self.window_width = 500
        self.window_height = 200
        self.window_visible = True
        self.text_lines = []
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.NOFRAME) 
        self.hwnd = pygame.display.get_wm_info()['window']
        
        styles = win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(0, 0, 0), 200, win32con.LWA_COLORKEY | win32con.LWA_ALPHA)
        
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
               

    def align_to_league(self):
        if not self.window_visible:
            return

        hwnd_league = win32gui.FindWindow(None, "League of Legends (TM) Client")
        if hwnd_league:
            rect = win32gui.GetWindowRect(hwnd_league)
            x, y = rect[0], rect[1]
            win32gui.SetWindowPos(self.hwnd, 0, x, y, 0, 0, 
                                     win32con.SWP_NOSIZE | win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE)
                

    def draw(self):
       
        pygame.draw.rect(self.screen, (50, 50, 50), (0, 0, self.window_width, self.window_height), 2)
        
        if self.page.category is None:
            items = list(self.text_lines.keys())
            header = "Select Category (6-0):"
        else:
            items = self.text_lines.get(self.page.category, [])
            header = f"[{self.page.category}] Select Message (6-0):"
            
        title = self.font.render(header, True, (255, 255, 255))
        self.screen.blit(title, (5, 5))
        
        start_idx = self.page.page_number * 5
        visible_items = items[start_idx : start_idx + 5]
        
        for i, item in enumerate(visible_items):
            text = f"{(i+6)% 10}. {item}"
            surf = self.font.render(text, True, (200, 200, 200))
            self.screen.blit(surf, (10, 30 + i * 25))

    
    def run(self):  
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == TOGGLE_UI:
                    self.toggle_visibility()
                elif event.type == NEXT_PAGE:
                    self.next_page()
                elif event.type == PREV_PAGE:
                    self.previous_page()
            if self.window_visible:
                self.screen.fill((10, 10, 10)) 
                self.draw()
                pygame.display.update()
            else:
                pygame.display.update() 

            self.clock.tick(30)
        
        pygame.quit()


    def toggle_visibility(self):
        self.window_visible = not self.window_visible
        if self.window_visible:
            win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)
            self.align_to_league()
        else:
            win32gui.ShowWindow(self.hwnd, win32con.SW_HIDE)

    def load_text_lines(self,lines):
        self.text_lines = lines

    def previous_page(self):
        if self.page.page_number > 0:
            self.page.page_number -=1

    def next_page(self):
        if self.page.category is None:
            total_items = len(self.text_lines)
        else:
            total_items = len(self.text_lines.get(self.page.category, []))
            
        if (self.page.page_number + 1) * 5 < total_items:
            self.page.page_number += 1
            
    def select_item(self, index_0_based):
        if not self.window_visible: 
            return None
        if self.page.category is None:
            items = list(self.text_lines.keys())
            real_index = self.page.page_number * 5 + index_0_based
            if real_index < len(items):
                self.page.category = items[real_index]
                self.page.page_number = 0
                return None 
        else:
            items = self.text_lines.get(self.page.category, [])
            real_index = self.page.page_number * 5 + index_0_based
            if real_index < len(items):
                return items[real_index] 
        return None
    
    def back_to_categories(self):
        self.page.category = None
        self.page.page_number = 0

    def trigger_next(self):
        pygame.event.post(pygame.event.Event(NEXT_PAGE))

    def trigger_prev(self):
        pygame.event.post(pygame.event.Event(PREV_PAGE))

    def trigger_toggle(self):
        pygame.event.post(pygame.event.Event(TOGGLE_UI))

    def trigger_exit(self):
         pygame.event.post(pygame.event.Event(pygame.QUIT)) 