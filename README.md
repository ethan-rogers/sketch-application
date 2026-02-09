# PenGuin

![](images/logo.png)

PenGuin is an opensource Python drawing application designed for STEM note taking and problem solving. This application is meant to be light weight, simple to use and easily modifiable. 

The main reason I started work on PenGuin was because I found most notetaking software that is based on digital drawing is either a notebook with fixed page sizes or individual infinite whiteboards. PenGuin combines these ideas, allowing you to create notebooks with pages of inifite and differing sizes. 

PeGuin's main goal is to give users the freedom of a whiteboard while still maintaining the organization benefits of a traditional notebook. 

## How to run

A windows executable is aviable for download through [itch](https://ethanrogers.itch.io/penguin). 

To run from the source code, ensure python is downloaded on your machine. This project uses 3.13.7, but should be compadible with most versions. After this, also run the following commands to isntall the dependencies. 
```console
pip install pygame
pip install numpy
pip install pickle5
pip install easygui
pip install Pillow
pip install fpdf
```

Then, run the `main.py` file. If there are any issues running, it is most likely because the `path` variables in the `constants.py` file is incorrect. If you are not using VSCode or another IDE that sets the working directory to the root folder, change the path variables to `../`.   

If you wish to compile on windows you can run  `bash compile.bat`. This first requires you to install `pyinstaller`.

## How to use

![](images/example.png)

### Scaling and Offseting

You can scale the view window with the scroll wheel on your mouse. Scaling is automatically done based around the center. You can also move the viewport by right clicking and dragging. 

### Basic Drawing

The pen tool allows you to create new freehand shapes. Pressing the pen icon also allows you to change the color and pen size. 

By pressing the shape icon you can view the menu of shapes you can create. Currently, the program supports lines, rectangles, circles and elipses. 

### Select the tool

The select tool is the top icon. This allows you to select one shape by clicking it, or select a block of shapes by pressing an empty area then making a select region. Once you have shapes selected, you can move them around by clicking the blue box and dragging. You can also delete selected shapes with the `del` key. 

### Anchor Functionality

The anchor allows you to return to a certain offset and scaler and determines how the page is viewed when imported. To set an anchor, press the anchor icon and then the target icon. To return to the anchor you have set, or the default position if you have not yet set an anchor, press the anchor button then the home icon. 

### Exporting

Currently the program supports exporting to `.nts` format. `.nts` files allow you to reimport your work inside the program. The program also has `.png` and `.pdf` buttons, which allow you to export to formats that can be viewed independently of the PenGuin application. Exporting to a `.png` will only export the current page, while exporting to pdf creates a document with each page inside your notebook. It also generates the pdf for each page, numbered with 0 based indexing. 

### Shortcuts

Below are the shortcuts currently implemented. 

* `s` use select tool.
* `p` use pen tool.
* `l` use line tool.
* `r` use rectangle tool.
* `c` use circle tool.
* `e` use elipse tool.
* `a` set anchor.
* `g` go to set anchor.
* `h` hide / show tool bar. 
*  `ctrl` + `z` undo your last edit.
* `ctrl` + `y` redo your last edit.

## Roadmap

Below are the planned additional features, in the order they will most likely be implemented
1. __Copy Paste for selected shape group__. Self explanatory. Should be added in the near future.
1. __Improved grdlines.__ I feel like the gridlines are far from perfect and the algorithm controlling them needs work.
2. __Pen Cursor.__ Adding an icon instead of the default cursor would help it standout on the black background.  
3. __Point snapping.__ When creating lines or other shapes, it would be helpful if the cursor snapped in place on other line end points, circle centers and rectangle edges, similar to in most CAD software. 
4. __Fulling complete settings__. This would include export file margins, point snapping sensitivity and zoom sensitivity. 
6. __Page index.__ This would provide a menu listing each page, along with the option to move the order of the pages. I would also add the ability to name pages, and the titles would be displayed at the top of each page in the PDF exported. 


## Contributions

If you are interested in contributing to the projet, email Ethan Roger at eholtrogers@gmail.com. Forks are also welcome. Feel free to remix, edit or even copy this code in any way shape or form. If you do something cool or improve the program, reach out!
  
