from machine import Pin, SoftSPI, PWM, unique_id
import utime
import framebuf
import struct


# spi pins

spi = SoftSPI(
    baudrate=40000000, 
    polarity=0, 
    phase=0, 
    sck=Pin(10),
    mosi=Pin(9),
    miso=Pin(16))


badge_data = {
    "Name": "Taran the Idiot",
    "Github": "https://github.com/taran-the-idiot",
    "Pronouns": "He/Him",
}



def bmp_to_framebuf_at(path, fb, x0, y0, max_w=80, max_h=80):
    with open(path, "rb") as f:
        if f.read(2) != b"BM":
            raise ValueError("Not a BMP")

        f.seek(10)
        data_offset = struct.unpack("<I", f.read(4))[0]

        f.seek(18)
        w, h = struct.unpack("<ii", f.read(8))
        h = abs(h)

        f.seek(28)
        bpp = struct.unpack("<H", f.read(2))[0]
        if bpp not in (1, 24):
            raise ValueError("Unsupported BMP depth")

        f.seek(data_offset)
        row_bytes = ((w * bpp + 31) // 32) * 4

        draw_w = min(w, max_w)
        draw_h = min(h, max_h)

        for y in range(draw_h):
            row = f.read(row_bytes)
            py = h - 1 - y  # BMP bottom-up

            for x in range(draw_w):
                if bpp == 1:
                    bit = row[x >> 3] & (0x80 >> (x & 7))
                    color = 0 if bit else 1
                else:
                    b, g, r = row[x * 3 : x * 3 + 3]
                    color = 0 if (r + g + b) > 384 else 1

                fb.pixel(x0 + x, y0 + py, color)

# display bullshitery

from einkdriver import EPD

disp_cs = Pin(8, Pin.OUT)
disp_dc = Pin(4, Pin.OUT)
disp_rst = Pin(6, Pin.OUT)
disp_busy = Pin(5, Pin.IN)

epd = EPD()

epd.image_Landscape.fill(0xFF)

bmp_to_framebuf_at(badge_data["Logo"], epd.image_Landscape, 0, 0)

if configured:
    epd.image_Landscape.text(badge_data["Name"], 0, 80, 0)
    epd.image_Landscape.text(badge_data["Github"], 0, 100, 0)
    epd.image_Landscape.text(badge_data["Pronouns"], 0, 120, 0)

else:
    epd.image_Landscape.text("Not Configured", 0, 80, 0)
    epd.image_Landscape.text("ERROR", 0, 100, 0)


epd.display_frame(epd.image_Landscape)

# kill itself

utime.sleep(2000)
epd.init(0)
utime.sleep(2000)
epd.sleep()

