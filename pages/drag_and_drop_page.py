from AutomationDemoApp.base.base_page import BasePage
import AutomationDemoApp.utilities.custom_logger as cl


class DragAndDrop(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    drag_drop_button = "com.code2lead.kwad:id/drag"
    draggable_text = "com.code2lead.kwad:id/lbl"
    kw_image = "com.code2lead.kwad:id/ingvw"
    draggable_button = "com.code2lead.kwad:id/btnDrag"
    layout_2 = "com.code2lead.kwad:id/layout2"
    layout_3 = "com.code2lead.kwad:id/layout3"
    page_title = "KWADemo"

    def scroll_to_drag_option(self):
        self.scroll_screen(1)

    def click_on_drag_button(self):
        self.click_element(self.drag_drop_button)

    def drag_drop_text(self):
        self.drag_and_drop_element(locator_value=self.draggable_text,drop_locator_value=self.layout_2)

    def verify_page_title(self):
        return self.is_element_displayed(self.page_title, "text")

    def get_drop_text_location(self):
        loc = self.get_location(self.draggable_text)
        print(loc)
        return loc

    def drag_draggable_button(self):
        self.drag_and_drop_element(locator_value=self.draggable_button, drop_locator_value=self.layout_2)

    def get_drop_button_location(self):
        loc = self.get_location(self.draggable_button)
        print(loc)
        return loc

    def drag_kw_image(self):
        self.drag_and_drop_element(locator_value=self.kw_image, drop_locator_value=self.layout_3)

    def get_kw_image_location(self):
        loc = self.get_location(self.kw_image)
        print(loc)
        return loc

