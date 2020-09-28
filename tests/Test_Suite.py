from AutomationDemoApp.tests.contact_us_form_test import ContactFormTests
from AutomationDemoApp.tests.login_test import LoginPageTest
from AutomationDemoApp.tests.enter_some_value_test import EnterSomeValueTest
from AutomationDemoApp.tests.scroll_view_page_test import ScrollViewTest
from AutomationDemoApp.tests.drag_and_drop_page_test import DragDropTest
import unittest

# Create the object of class using unittest
tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(ContactFormTests)
tc_3 = unittest.TestLoader().loadTestsFromTestCase(EnterSomeValueTest)
tc_4 = unittest.TestLoader().loadTestsFromTestCase(ScrollViewTest)
tc_5 = unittest.TestLoader().loadTestsFromTestCase(DragDropTest)

# Create the Test Suite
regression_test = unittest.TestSuite([tc_1, tc_2, tc_3, tc_4, tc_5])

# Call the test runner method
unittest.TextTestRunner(verbosity=1).run(regression_test)
