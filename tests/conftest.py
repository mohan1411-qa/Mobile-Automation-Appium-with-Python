import pytest
from AutomationDemoApp.base.DriverClass import Driver
import time


@pytest.yield_fixture(scope='class')
def one_time_setup(request):
    print("Before Class")
    obj = Driver()
    driver = obj.get_driver_method()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    time.sleep(5)
    print("Test Execution Completed")
    driver.quit()
