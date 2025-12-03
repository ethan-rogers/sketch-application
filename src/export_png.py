from PIL import Image, ImageDraw
from drawings import FreeShape, Line, Circle, Rectangle, Elipse
import numpy as np



def create_png(shapes, path):
    # have set width
    width = 600

    border = 40

    # find boundaries

    max_x = float("-inf")
    min_x = float("inf")

    max_y = float("-inf")
    min_y = float("inf")

    for s in shapes:
        min_x_check, min_y_check, max_x_check, max_y_check = s.get_limits()

        max_x = max_x_check if max_x_check > max_x else max_x
        min_x = min_x_check if min_x_check < min_x else min_x

        max_y = max_y_check if max_y_check > max_y else max_y
        min_y = min_y_check if min_y_check < min_y else min_y


    # calculate height
    size_ratio = (max_y - min_y + border*2) / (max_x - min_x + border*2)
    height = round(width * size_ratio)

    # create image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # calculate scaler
    scaler = (width - border*2)/ (max_x - min_x)
    
    # draw for each shape
    for s in shapes:
        typ, size, color, points = s.to_list()
        size = int(size/2)
        points = points.copy()
        points[:, 0] -= min_x
        points[:, 1] -= min_y

        points *= scaler

        points[:, 0] += border
        points[:, 1] += border

        count = np.size(points, axis=0)

        match typ:
            case 0:
                if count > 1:
                    for i in range(count - 1):
                        x1, y1 = points[i]
                        x2, y2 = points[i+1]
                        
                        draw.line([(x1, y1), (x2, y2)], fill=color, width=size)
            case 1:
                if count > 1:
                    x1, y1 = points[0]
                    x2, y2 = points[1]
                    draw.line([(x1, y1), (x2, y2)], fill=color, width=size)
            case 2:
                if count > 1:
                    x1, y1, x2, y2 = np.min(points[:, 0]), np.min(points[:, 1]), np.max(points[:, 0]), np.max(points[:, 1])
                    draw.rectangle((x1, y1, x2, y2), fill=None, outline=color, width=size)
            case 3:
                if count > 1:
  
                    radius = s.get_radius() * scaler

                    draw.circle(points[0], radius, fill=None, width=size, outline=color)
            case 4:
                if count > 1:
                    x0, y0, x1, y1 = s.get_limits()

                    x0 -= min_x
                    x0 *= scaler

                    x1 -= min_x
                    x1 *= scaler

                    y0 -= min_y
                    y0 *= scaler

                    y1 -= min_y
                    y1 *= scaler

                    draw.ellipse((x0, y0, x1, y1), fill = None, outline=color, width=size)
        
        image.save(path)
    




