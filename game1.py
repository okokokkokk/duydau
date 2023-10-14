#Thư viện pygame
import pygame
pygame.init()

#tiêu đề và icon:
pygame.display.set_caption('Game Duy Đậu')
icon = pygame.image.load(r'assets\duy.png')
pygame.display.set_icon(icon)

#thêm background:
bg = pygame.image.load(r'assets\background-night.png')
bg = pygame.transform.scale2x(bg)

#thêm floor:
fl = pygame.image.load(r'assets\floor.png')
fl = pygame.transform.scale2x(fl)
fl_x = 0

p = 0.2 #hằng trọng lực
score = 0 #khởi tạo điểm

bird_y = 0 #tọa độ y của con chim

#score:
game_font=pygame.font.Font('04B_19.TTF',40)
def score_view():
    score_f =game_font.render(str(int(score)),True,(225,225,225))
    score_hcn = score_f.get_rect(center = (200,100))
    screen.blit(score_f,score_hcn)

#Cửa sổ game
screen = pygame.display.set_mode((432,768))

#Đưa bird vào xd:
bird = pygame.image.load(r'assets\duy.png')
bird = pygame.transform.scale2x(bird)
bird_hcn = bird.get_rect(center = (100,386))

#vòng lặp xử lý game
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y = -5
    screen.blit(bg,(0,0))
    fl_x -=1
    screen.blit(fl,(fl_x,600))
    screen.blit(fl,(fl_x+432,600))
    if fl_x == -432:
        fl_x = 0
    #Đưa bird vô game:
    screen.blit(bird,bird_hcn)
    bird_y+=p
    bird_hcn.centery+=bird_y
    score+=0.01
    score_view()
    pygame.display.update()
