# PenGuin

![](images/logo.png)

PenGuin is an opensource Python drawing application designed for STEM note taking and problem solving. This application is meant to be light weight, easy to use and easily modifiable. 

## How to run

The project is still development so there is not a compiled executable. To run the demo, ensure python is downloaded on your machine. This project uses 3.13.7, but should be compadible with mose versions. After this, also run the following commands to isntall the dependencies. 
```
pip install pygame
pip install numpy
pip install pickle5
pip install easygui
```

Then, run the `main.py` file. If there are any issues running, it is most likely because the `path` variables in the `constants.py` file is incorrect. If you are not using VSCode or another IDE that sets the working directory to the root folder, change the path variables to `../`.   

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

Currently the program supports exporting to `.nts` format. `.nts` files allow you to reimport your work inside the program. In the future, we plan on adding functionality to the `.png` and `.pdf` buttons, which will allow you to export to formats that can be viewed independently of the PenGuin application. 

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

## Contributions

If you are interested in contributing to the projet, email Ethan Roger at bay2uu@virginia.edu
  
