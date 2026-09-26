import pygame
import sys
import math
pygame.init()
# Ekran boyutları
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Lamba ve I Love You")
#Renk Tanımlamaları (RGB)
Siyah = (10, 10, 10)
SARI = (255, 183, 3)
Koyu_SARI = (100, 80, 20)
GRI = (80, 80, 80)
BEYAZ = (255, 255, 255)
KIRMIZI = (220, 20, 60)
font_love = pygame.font.SysFont("Arial", 64, bold=True)
font_ipucu = pygame.font.SysFont("Arial",20)
is_on=False
ip_x=200
ip_y_baslangic=120
ip_uzunluk = 100
ip_kutu = pygame.Rect(ip_x - 10, ip_y_baslangic + ip_uzunluk, 20, 30)
animasyon_basladi = False
animasyon_bitmis = False
kalp_merkez_x = GENISLIK // 2
kalp_merkez_y = YUKSEKLIK // 2
kalp_aci = 0
kalp_hiz = 0.05
ok_boyutu = 20
kalp_yuzeyi = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
kalp_yuzeyi.fill((0, 0, 0, 0))

running = True
clock = pygame.time.Clock()
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ip_kutu.collidepoint(event.pos):
                is_on = not is_on
                # Lamba açıldığında animasyonu sıfırla ve ekranı temizle
                animasyon_basladi = True
                animasyon_bitmis = False
                kalp_aci = 0
                ekran.fill(Siyah)
                kalp_yuzeyi.fill((0, 0, 0, 0)) # Kalp yüzeyini şeffaf olarak temizle
            else:
                # Lamba kapandığında animasyonu durdur
                animasyon_basladi = False
                animasyon_bitmis = False
   # Lamba Kablosu ve Duy
    pygame.draw.line(ekran, GRI, (200, 0), (200, 100), 4)
    pygame.draw.rect(ekran, GRI, (180, 100, 40, 15))

    # İp ve Tutamak
    pygame.draw.line(ekran, BEYAZ, (ip_x, ip_y_baslangic), (ip_x, ip_y_baslangic + ip_uzunluk), 2)
    ip_renk = SARI if is_on else GRI
    pygame.draw.rect(ekran, ip_renk, ip_kutu, border_radius=5)
    if is_on:
        pygame.draw.circle(ekran, SARI, (200, 140), 30)
        if animasyon_basladi and not animasyon_bitmis:
            ok_x = kalp_merkez_x + 16 * math.pow(math.sin(kalp_aci), 3) * 10
            ok_y = kalp_merkez_y - (13 * math.cos(kalp_aci) - 5 * math.cos(2 * kalp_aci) - 2 * math.cos(3 * kalp_aci) - math.cos(4 * kalp_aci)) * 10

            pygame.draw.circle(kalp_yuzeyi, KIRMIZI, (int(ok_x), int(ok_y)), 3)
            
            pygame.draw.line(ekran, BEYAZ, (int(ok_x), int(ok_y)), (int(ok_x) - ok_boyutu, int(ok_y) + ok_boyutu // 2), 4)
            pygame.draw.line(ekran, BEYAZ, (int(ok_x), int(ok_y)), (int(ok_x) - ok_boyutu, int(ok_y) - ok_boyutu // 2), 4)

            kalp_aci += kalp_hiz

            if kalp_aci >= 2 * math.pi:
                animasyon_bitmis = True
                animasyon_basladi = False
        elif animasyon_bitmis:
            yazi_surface = font_love.render("I LOVE YOU", True, SARI)
            ekran.blit(yazi_surface, (GENISLIK // 2 - yazi_surface.get_width() // 2, YUKSEKLIK // 2))

        ekran.blit(kalp_yuzeyi, (0, 0))

        ipucu_metin = "Kapatmak için sarı tutamağa tıkla"
    else:
        pygame.draw.circle(ekran, Koyu_SARI, (200, 140), 30)
        ipucu_metin = "Açmak için tutamağa tıkla"

    ipucu_surface = font_ipucu.render(ipucu_metin, True, GRI)
    ekran.blit(ipucu_surface, (20, YUKSEKLIK - 40))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit() 

