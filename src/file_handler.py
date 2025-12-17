from pickle import dump, load
from export_png import create_png
from drawings import FreeShape, Line, Rectangle, Circle, Elipse
import easygui


# saving settings

def save_config():
    pass

# saving notes
def import_nts(sp):
    file_name = easygui.fileopenbox(filetypes=[["*.nts", "Notes File"]])
    if file_name == None:
        return

    clear(sp)
    with open(file_name, "rb") as save:
        sp.anchored_offset = load(save)
        sp.anchored_scaler = load(save)
        sp.global_scaler = 1
        sp.global_offset = [0,0]
        while True:
            try:
                type_shape, size, color, points = load(save)
                shape = None

                if type_shape == 0:
                    shape = FreeShape(sp, size, color)
                elif type_shape == 1:
                    shape = Line(sp, size, color)
                elif type_shape == 2:
                    shape = Rectangle(sp, size, color)
                elif type_shape == 3:
                    shape = Circle(sp, size, color)
                elif type_shape == 4:
                    shape = Elipse(sp, size, color)
                for p in points:
                    shape.add_point(p)

            except EOFError:
                break
        sp.go_home()

def clear(sp):
    sp.clear_page()


def export_nts(sp):
    file_name = easygui.filesavebox(msg="Save your file", title="Choose a file name", default="notes.nts", filetypes=[["*.nts", "Notes File"]])
    if not file_name:
        return

    with open(file_name, 'wb') as save:
        dump(sp.anchored_offset, save)
        dump(sp.anchored_scaler, save)

        for shape in sp.get_shapes():
           dump(shape.to_list(), save) 

def export_png(sp):
    file_name = easygui.filesavebox(msg="Save your file", title="Choose a file name", default="notes.png", filetypes=[["*.png", "PNG File"]])

    if not file_name:
        return

    create_png(sp.get_shapes(), file_name)

def export(format):
    if format == "nts":
        export_nts()
    

