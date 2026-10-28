class AppiumGestures:
    @staticmethod
    def swipe(driver, start_x, start_y, end_x, end_y, duration=800):
        try:
            driver.swipe(start_x, start_y, end_x, end_y, duration)
        except Exception:
            pass

    @staticmethod
    def scroll_down(driver):
        try:
            size = driver.get_window_size()
            x = size['width'] // 2
            start_y = int(size['height'] * 0.8)
            end_y = int(size['height'] * 0.2)
            driver.swipe(x, start_y, x, end_y, 800)
        except Exception:
            pass

    @staticmethod
    def scroll_up(driver):
        try:
            size = driver.get_window_size()
            x = size['width'] // 2
            start_y = int(size['height'] * 0.2)
            end_y = int(size['height'] * 0.8)
            driver.swipe(x, start_y, x, end_y, 800)
        except Exception:
            pass

    @staticmethod
    def pull_to_refresh(driver):
        AppiumGestures.scroll_up(driver)
