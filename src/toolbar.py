from ui_elements import Panel, Button, Text
import pygame
from constants import path, hovered_grey, button_select
import file_handler as fh


# Main UI for the application
class Toolbar:

    # insanely shitty constructor, should be doing all that
    def __init__(self, scrn, sketchpad):
        self.scrn = scrn
        self.sketchpad = sketchpad

        self.scrn_width, self.scrn_height = scrn.get_size()
    
    
        side_border = 2
        top_border = 10
        button_padding = 40
        button_count = 10
        

        self.height = top_border*2 + button_padding*(button_count-1) + 28
        self.width = 32

        self.pos_x = 4
        self.pos_y = abs((self.scrn_height - self.height) / 2)

        self.main_menu = Panel(scrn, (self.pos_x,self.pos_y), (self.width, self.height))

        self.select_image = button_select
        self.black = (0,0,0)

        self.hovered_grey = hovered_grey

        self.keys = {}

        self.hidden = False

    

        select_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border], [28, 28])
        select_button.add_graphic(path + "icons/cursor.png")
        select_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        select_button.add_action(self.select_select)
        self.main_menu.add_button(select_button)

        pen_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding], [28, 28])
        pen_button.add_graphic(path + "icons/pen.png")
        pen_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        pen_button.add_action(self.pen_button)
        self.main_menu.add_button(pen_button)

        shapes_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*2], [28, 28])
        shapes_button.add_graphic(path + "icons/shapes.png")
        shapes_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        shapes_button.add_action(self.shape_select)
        self.main_menu.add_button(shapes_button)

        anchor_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*3], [28, 28])
        anchor_button.add_graphic(path + "icons/anchor.png")
        anchor_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        anchor_button.add_action(self.anchor_select)
        self.main_menu.add_button(anchor_button)

        file_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*4], [28, 28])
        file_button.add_graphic(path + "icons/file.png")
        file_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        file_button.add_action(self.file_select)
        self.main_menu.add_button(file_button)

        setting_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*5], [28, 28])
        setting_button.add_graphic(path + "icons/settings.png")
        setting_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        setting_button.add_action(self.settings_select)
        self.main_menu.add_button(setting_button)

        undo_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*6], [28, 28])
        undo_button.add_graphic(path + "icons/undo.png")
        undo_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        undo_button.add_action(self.sketchpad.undo_action)
        self.main_menu.add_button(undo_button)

        redo_button = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*7], [28, 28])
        redo_button.add_graphic(path + "icons/redo.png")
        redo_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        redo_button.add_action(self.sketchpad.redo_action)
        self.main_menu.add_button(redo_button)

        previous_page = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*8], [28, 28])
        previous_page.add_graphic(path + "icons/previous_page.png")
        previous_page.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        previous_page.add_action(self.sketchpad.previous_page)
        self.main_menu.add_button(previous_page)

        next_page = Button(scrn, [self.pos_x + side_border, self.pos_y + top_border + button_padding*9], [28, 28])
        next_page.add_graphic(path + "icons/next_page.png")
        next_page.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        next_page.add_action(self.sketchpad.next_page)
        self.main_menu.add_button(next_page)

        # other menu panels
        side_padding = 10
        self.side_panels = []
        
        sub_menu_x = self.pos_x + self.width + side_padding


        # create  tool panel
        tool_y = self.pos_y + button_padding*2
        self.shape_selection = Panel(scrn, (sub_menu_x,tool_y), (self.width, top_border + button_padding*4))
        self.side_panels.append(self.shape_selection)

        line_button = Button(scrn, [sub_menu_x + side_border, tool_y + top_border], [28, 28])
        line_button.add_graphic(path + "icons/line.png")
        line_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        line_button.add_action(self.line_select)
        self.shape_selection.add_button(line_button)

        rect_button = Button(scrn, [sub_menu_x + side_border, tool_y + top_border + button_padding], [28, 28])
        rect_button.add_graphic(path + "icons/rect.png")
        rect_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        rect_button.add_action(self.rect_select)
        self.shape_selection.add_button(rect_button)


        circle_button = Button(scrn, [sub_menu_x + side_border, tool_y + top_border + button_padding*2], [28, 28])
        circle_button.add_graphic(path + "icons/circle.png")
        circle_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        circle_button.add_action(self.circle_select)
        self.shape_selection.add_button(circle_button)

        elipse_button = Button(scrn, [sub_menu_x + side_border, tool_y + top_border + button_padding*3], [28, 28])
        elipse_button.add_graphic(path + "icons/elipse.png")
        elipse_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        elipse_button.add_action(self.elipse_select)
        self.shape_selection.add_button(elipse_button)

        self.shape_selection.hide()

        # anchor options
        anchor_y = self.pos_y + button_padding*3
        self.anchor_buttons = Panel(scrn, (sub_menu_x,anchor_y), (self.width, top_border + button_padding*2))
        self.side_panels.append(self.anchor_buttons)


        home_button = Button(scrn, [sub_menu_x + side_border, anchor_y + top_border], [28, 28])
        home_button.add_graphic(path + "icons/home.png")
        home_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        home_button.add_action(self.go_home)
        self.anchor_buttons.add_button(home_button)

        set_home_button = Button(scrn, [sub_menu_x + side_border, anchor_y + top_border + button_padding], [28, 28])
        set_home_button.add_graphic(path + "icons/crossairs.png")
        set_home_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        set_home_button.add_action(self.set_home)
        self.anchor_buttons.add_button(set_home_button)

        self.anchor_buttons.hide()

        # export / import

        
        file_button_width = 40
        file_button_height = 22

        file_button_padding = 26


        file_y = self.pos_y + button_padding*4
        file_button_count = 5
        self.file_buttons = Panel(scrn, (sub_menu_x,file_y), (file_button_width + side_border*2, top_border*2 + file_button_padding*file_button_count))
        self.side_panels.append(self.file_buttons)


        import_button = Button(scrn, [sub_menu_x + side_border, file_y + top_border], [file_button_width, file_button_height])
        import_button.add_text("Import", 16)
        import_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        import_button.add_action(self.import_file)
        self.file_buttons.add_button(import_button)

        export_button = Button(scrn, [sub_menu_x + side_border, file_y + top_border + file_button_padding], [file_button_width, file_button_height])
        export_button.add_text(".nts", 16)
        export_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        export_button.add_action(self.export_nts)
        self.file_buttons.add_button(export_button)

        export_nbk_button = Button(scrn, [sub_menu_x + side_border, file_y + top_border + file_button_padding*2], [file_button_width, file_button_height])
        export_nbk_button.add_text(".nbk", 16)
        export_nbk_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        export_nbk_button.add_action(self.export_nbk)
        self.file_buttons.add_button(export_nbk_button)

        png_button = Button(scrn, [sub_menu_x + side_border, file_y + top_border + file_button_padding*3], [file_button_width, file_button_height])
        png_button.add_text(".png", 16)
        png_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        png_button.add_action(self.export_png)
        self.file_buttons.add_button(png_button)

        pdf_button = Button(scrn, [sub_menu_x + side_border, file_y + top_border + file_button_padding*4], [file_button_width, file_button_height])
        pdf_button.add_text(".pdf", 16)
        pdf_button.add_hovered_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))
        #export_button.add_action(self.go_home)
        self.file_buttons.add_button(pdf_button)

        self.file_buttons.hide()

        
        color_y = self.pos_y + button_padding
        color_button_count_x = 2
        color_button_count_y = 4

        color_button_width = 16
        color_button_padding = 8

        color_width = color_button_width * color_button_count_x + color_button_padding * (color_button_count_x + 1)
        color_height = color_button_width * color_button_count_y + color_button_padding * (color_button_count_y + 1)

        self.color_panel = Panel(scrn, (sub_menu_x,color_y), (color_width, color_height))
        self.side_panels.append(self.color_panel)

        self.color_panel.hide()

        col = 0
        for r in range(2):
            for g in range(2):
                for b in range(2):
                    row = b

                    
                    color_button = Button(scrn, [sub_menu_x + row * (color_button_width + color_button_padding) + color_button_padding, color_y + col * (color_button_width + color_button_padding) + color_button_padding], [color_button_width, color_button_width])
                    color_button.add_background((r*255, g*255, b*255))
                    color_button.add_hovered_background((abs(r*255 - 30), abs(g*255 - 30), abs(b*255 - 30)))
                    color_button.add_action(self.change_col)
                    color_button.add_parameter((r*255, g*255, b*255))
                    self.color_panel.add_button(color_button)
                col += 1



        # shortcuts
        self.old_keys = pygame.key.get_pressed()
        self.shortcuts = [
            [[pygame.K_s], self.select_select],
            [[pygame.K_p], self.pen_select],
            [[pygame.K_LCTRL, pygame.K_z], self.sketchpad.undo_action],
            [[pygame.K_LCTRL, pygame.K_y], self.sketchpad.redo_action],
            [[pygame.K_l], self.line_select],
            [[pygame.K_r], self.rect_select],
            [[pygame.K_c], self.circle_select],
            [[pygame.K_e], self.elipse_select],
            [[pygame.K_h], self.hide],
            [[pygame.K_a], self.set_home],
            [[pygame.K_g], self.go_home]
        ]


    def update(self):
        new_width, new_height = self.scrn.get_size()
        if new_height != self.scrn_height:
            self.scrn_height = new_height
            pos_y = abs((self.scrn_height - self.height) / 2)
            diff = pos_y-self.pos_y
            self.pos_y = pos_y

            
            self.main_menu.add_height(diff)

            for panel in self.side_panels:
                panel.add_height(diff)


        if not self.hidden:
            self.main_menu.update()
            for panel in self.side_panels:
                panel.update()
        
        self.check_shortcuts()

    def check_shortcuts(self):
        keys = self.keys
        # shortcuts
        for s in self.shortcuts:
            buttons, action = s

            pushed_down = False
            shortcut_fufilled = True
            for b in buttons:
                if not keys[b]:
                    shortcut_fufilled = False
                    break

                if keys[b] and not self.old_keys[b]:
                    pushed_down = True
            
            if pushed_down and shortcut_fufilled:
                # dont allow one key shortcut if the ctrl key is pressed
                if (not len(s[0]) == 1) or (not keys[pygame.K_LCTRL]):
                    action()
        

        self.old_keys = keys 


    def update_input(self, keys):
        self.keys = keys

    def select_tool(self, tool):
        for panel in self.side_panels:
            panel.hide()

        if self.sketchpad.tool == tool:
            return
        
        if self.sketchpad.tool != None:
            self.main_menu.buttons[self.sketchpad.tool].replace_image_color(self.select_image, self.black)
            self.main_menu.buttons[self.sketchpad.tool].add_background(None)

        self.main_menu.buttons[tool].replace_image_color(self.black, self.select_image)
        self.main_menu.buttons[tool].add_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))


        self.sketchpad.change_tool(tool)
    
    def select_shape(self, shape):
        if self.sketchpad.shape == shape:
            return
        
        if self.sketchpad.shape != None:
            self.shape_selection.buttons[self.sketchpad.shape].replace_image_color(self.select_image, self.black)
            self.shape_selection.buttons[self.sketchpad.shape].add_background(None)

        self.shape_selection.buttons[shape].replace_image_color(self.black, self.select_image)
        self.shape_selection.buttons[shape].add_background((self.hovered_grey, self.hovered_grey, self.hovered_grey))


        self.sketchpad.change_shape(shape)




    def select_select(self):
        self.select_tool(0)

    def pen_select(self):
        self.select_tool(1)

    def pen_button(self):
        shown = self.color_panel.shown()
        self.select_tool(1)

        self.color_panel.hide(shown)


    def shape_select(self):
        shown = self.shape_selection.shown()
        self.select_tool(2)

        self.shape_selection.hide(shown)

    def anchor_select(self):
        self.select_tool(3)
        shown= self.anchor_buttons.shown()



        self.anchor_buttons.hide(shown)

    def go_home(self):
        self.anchor_buttons.hide()
        self.sketchpad.go_home()

    def set_home(self):
        self.anchor_buttons.hide()
        self.sketchpad.set_home()


    def file_select(self):
        self.select_tool(4)
        shown = self.file_buttons.shown()
        self.file_buttons.hide(shown)

    def settings_select(self):
        self.select_tool(5)
    
    def line_select(self):
        self.select_tool(2)
        self.select_shape(0)

    def rect_select(self):
        self.select_tool(2)
        self.select_shape(1)

    def circle_select(self):
        self.select_tool(2)
        self.select_shape(2)

    def elipse_select(self):
        self.select_tool(2)
        self.select_shape(3)


    def mouse_in_toolbar(self):
        if self.hidden:
            return False

        for p in self.side_panels:
            if p.mouse_in_panel():
                return True
        
        return self.main_menu.mouse_in_panel()


    def hide(self):
        self.hidden = not self.hidden
    
    def import_file(self):
        self.file_buttons.hide()

        fh.import_file(self.sketchpad)

    def export_nts(self):
        self.file_buttons.hide()

        fh.export_nts(self.sketchpad)

    def export_nbk(self):
        self.file_buttons.hide()

        fh.export_nbk(self.sketchpad)

    def export_png(self):
        self.file_buttons.hide()

        fh.export_png(self.sketchpad)
    
    def change_col(self, col):
        self.sketchpad.change_col(col)
        self.color_panel.hide()

    

