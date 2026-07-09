from einkdriver import EPD
import utime

epd = EPD()

epd.init(1)
epd.image_Landscape.fill(0xFF)
epd.display_Landscape(epd.buffer_Landscape)

epd.image_Landscape.fill(0x00)


epd.display_Landscape(epd.buffer_Landscape)

utime.sleep_ms(2000)
