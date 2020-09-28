from AutomationDemoApp.pages.drag_and_drop_page import DragAndDrop
import unittest
import pytest
import time


@pytest.mark.usefixtures("one_time_setup")
class DragDropTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def cls_obj(self):
        self.dd = DragAndDrop(self.driver)

    @pytest.mark.run(order=12)
    def test_drag_drop_button(self):
        self.dd.scroll_to_drag_option()
        self.dd.click_on_drag_button()
        result = self.dd.verify_page_title()
        assert True == result

    @pytest.mark.run(order=13)
    def test_drag_and_drop_text(self):
        src_loc = self.dd.get_drop_text_location()
        self.dd.drag_drop_text()
        time.sleep(5)
        dest_loc = self.dd.get_drop_text_location()
        if src_loc != dest_loc:
            assert True
        else:
            assert False

    @pytest.mark.run(order=14)
    def test_drag_and_drop_button(self):
        src_loc = self.dd.get_drop_button_location()
        self.dd.drag_draggable_button()
        time.sleep(5)
        dest_loc = self.dd.get_drop_button_location()
        if src_loc != dest_loc:
            assert True
        else:
            assert False

    @pytest.mark.run(order=15)
    def test_drag_and_drop_image(self):
        src_loc = self.dd.get_kw_image_location()
        self.dd.drag_kw_image()
        time.sleep(5)
        dest_loc = self.dd.get_kw_image_location()
        if src_loc != dest_loc:
            assert True
        else:
            assert False






