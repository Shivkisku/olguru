from sketchpy import canvas
from sklearn.preprocessing import scale

obj = canvas.sketch_from_svg('your image path',scale = 250)

obj.draw()