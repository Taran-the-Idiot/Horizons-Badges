from einkdriver import EPD
import utime

epd = EPD()

epd.image_Landscape.fill(0xFF)
epd.image_Landscape.rect(8, 8, 136, 136, 0x00)
epd.text_scaled("Horizons", 22, 30, 2, 0x00)
epd.text_scaled("Badge display test", 22, 62, 1, 0x00)
epd.text_scaled("main2.py", 22, 82, 1, 0x00)

epd.display_Landscape(epd.buffer_Landscape)

utime.sleep_ms(2000)