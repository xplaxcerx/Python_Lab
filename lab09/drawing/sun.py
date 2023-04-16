import simple_draw as sd
sd.resolution = (1024, 760)

sd.ellipse(sd.Point(-180, -250), sd.Point(2100, 250), color=sd.COLOR_GREEN)
import simple_draw as sd

def drawing_sun(center,rad):
    sd.circle(center_position=center, radius=rad,color=sd.COLOR_YELLOW,width=0)
    for angle in range(0, 360, 30):
        sd.vector(start=center,color=sd.COLOR_YELLOW, length=rad+50,angle=angle, width=10)
