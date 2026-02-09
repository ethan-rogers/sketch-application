from pickle import dump, load
from export_png import create_png
from drawings import FreeShape, Line, Rectangle, Circle, Elipse
import easygui
from fpdf import FPDF


# saving settings

def save_config():
    pass

# retrive shape

def create_shape(save, sp):
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

def import_file(sp):
    file_name = easygui.fileopenbox(filetypes=[["*.nts", "Notes File"], ["*.nbk", "Notebook file"]])
    if file_name == None:
        return
    
    if file_name[-4:] == ".nts":
        import_nts(sp, file_name)
    elif file_name[-4:] == ".nbk":
        import_nbk(sp, file_name)
    else:
        print(file_name[:-4], "not supported.")


# saving notes
def import_nts(sp, file_name):


    sp.clear_page()
    with open(file_name, "rb") as save:
        sp.anchored_offset = load(save)
        sp.anchored_scaler = load(save)
        sp.global_scaler = 1
        sp.global_offset = [0,0]
        while True:
            try:
                create_shape(save, sp)

            except EOFError:
                break
        sp.go_home()



def export_nts(sp):
    file_name = easygui.filesavebox(msg="Save your file", title="Choose a file name", default="notes.nts", filetypes=[["*.nts", "Notes File"]])
    if not file_name:
        return

    with open(file_name, 'wb') as save:
        dump(sp.anchored_offset, save)
        dump(sp.anchored_scaler, save)

        for shape in sp.get_shapes():
           dump(shape.to_list(), save) 


# saving notes
def import_nbk(sp, file_name):


    sp.clear_book()
    with open(file_name, "rb") as save:
        sp.anchored_offset = load(save)
        sp.anchored_scaler = load(save)
        sp.global_scaler = 1
        sp.global_offset = [0,0]

        page_list = load(save)



        for i, p in enumerate(page_list):
            for j in range(p):
                create_shape(save, sp)
            sp.next_page()
        sp.notebook.pop()
        sp.current_page = 0

            


        sp.go_home()


def export_nbk(sp):
    file_name = easygui.filesavebox(msg="Save your file", title="Choose a file name", default="notes.nbk", filetypes=[["*.nbk", "Notebook File"]])
    if not file_name:
        return
    
    with open(file_name, 'wb') as save:
        dump(sp.anchored_offset, save)
        dump(sp.anchored_scaler, save)

        page_list = [len(i) for i in sp.notebook]

        dump(page_list, save)
        for page in sp.notebook:
            for shape in page:
                dump(shape.to_list(), save) 




def export_png(sp):
    file_name = easygui.filesavebox(msg="Save your file", title="Choose a file name", default="notes.png", filetypes=[["*.png", "PNG File"]])

    if not file_name:
        return

    create_png(sp.get_shapes(), file_name)

def export_pdf(sp):
    file_name = easygui.filesavebox(msg="Save your file", title="Choose a file name", default="notes.pdf", filetypes=[["*.pdf", "PDF File"]])

    if not file_name:
        return

    pdf = FPDF()
    

    for i, shapes in enumerate(sp.get_notebook()):
        name = file_name.replace(".pdf", f"{i}.png")
        create_png(shapes, name)
        pdf.add_page()
        pdf.image(name, x=0, y=0, w=210)

    pdf.output(file_name, "F")





def export(format):
    if format == "nts":
        export_nts()
    

