from playwright.sync_api import sync_playwright
import time
import os
import random
from pathlib import Path

class PlaywrightEngine:
    def __init__(self, timeout=15000, max_retries=3):
        self.max_retries = max_retries
        self.timeout = timeout
        
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(viewport=None)
        self.page = self.context.new_page()
        
        Path("screenshots").mkdir(exist_ok=True)
        Path("downloads").mkdir(exist_ok=True)
        Path("traces").mkdir(exist_ok=True)

    def _retry_operation(self, func, *args, **kwargs):
        """Universal retry - CORRECT ARGUMENT PASSING"""
        for attempt in range(self.max_retries):
            try:
                result = func(*args, **kwargs)
                print(f"✅ SUCCESS on attempt {attempt + 1}")
                return result
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1}/{self.max_retries} failed: {str(e)[:50]}")
                if attempt < self.max_retries - 1:
                    wait_time = (attempt + 1) * random.uniform(0.5, 1.5)
                    print(f"⏳ Retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ FINAL FAILURE after {self.max_retries} attempts")
                    raise e

    def open(self, url):
        self._retry_operation(self._open_impl, url)

    def _open_impl(self, url):
        self.page.goto(url, wait_until="networkidle")

    def click(self, selector):
        self._retry_operation(self._click_impl, selector)

    def _click_impl(self, selector):
        self.page.click(selector, timeout=self.timeout)

    def type(self, selector, value):
        self._retry_operation(self._type_impl, selector, value)

    def _type_impl(self, selector, value):
        self.page.wait_for_selector(selector, timeout=5000)
        self.page.click(selector)
        self.page.fill(selector, value)

    def wait_seconds(self, seconds):
        time.sleep(seconds)

    def wait_for_selector(self, selector, timeout=10000):
        self._retry_operation(self._wait_selector_impl, selector, timeout)

    def _wait_selector_impl(self, selector, timeout):
        self.page.wait_for_selector(selector, timeout=timeout)

    def scroll_to_selector(self, selector):
        self._retry_operation(self._scroll_selector_impl, selector)

    def _scroll_selector_impl(self, selector):
        self.page.eval_on_selector(selector, "el => el.scrollIntoView({block: 'center'})")

    def scroll_pixels(self, pixels):
        self._retry_operation(self._scroll_pixels_impl, pixels)

    def _scroll_pixels_impl(self, pixels):
        self.page.evaluate(f"window.scrollBy(0, {pixels})")

    def hover(self, selector):
        self._retry_operation(self._hover_impl, selector)

    def _hover_impl(self, selector):
        self.page.hover(selector)

    def double_click(self, selector):
        self._retry_operation(self._dblclick_impl, selector)

    def _dblclick_impl(self, selector):
        self.page.dblclick(selector)

    def right_click(self, selector):
        self._retry_operation(self._rightclick_impl, selector)

    def _rightclick_impl(self, selector):
        self.page.click(selector, button="right")

    def drag_drop(self, source_selector, target_selector):
        self._retry_operation(self._dragdrop_impl, source_selector, target_selector)

    def _dragdrop_impl(self, source_selector, target_selector):
        self.page.drag_and_drop(source_selector, target_selector)

    def select_option(self, selector, option, method="text"):
        self._retry_operation(self._select_impl, selector, option, method)

    def _select_impl(self, selector, option, method):
        if method == "text":
            self.page.select_option(selector, label=option)
        elif method == "value":
            self.page.select_option(selector, value=option)
        else:
            self.page.select_option(selector, index=int(option))

    def clear(self, selector):
        self._retry_operation(self._clear_impl, selector)

    def _clear_impl(self, selector):
        self.page.fill(selector, "")

    def screenshot(self, filename=None):
        return self._retry_operation(self._screenshot_impl, filename)

    def _screenshot_impl(self, filename):
        if not filename:
            filename = f"screenshot_{int(time.time())}.png"
        self.page.screenshot(path=f"screenshots/{filename}")
        return f"screenshots/{filename}"

    def switch_window(self, window):
        self._retry_operation(self._switch_impl, window)

    def _switch_impl(self, window):
        if window == "next":
            self.context.pages[-1].bring_to_front()

    def back(self):
        self._retry_operation(self._back_impl)

    def _back_impl(self):
        self.page.go_back()

    def forward(self):
        self._retry_operation(self._forward_impl)

    def _forward_impl(self):
        self.page.go_forward()

    def refresh(self):
        self._retry_operation(self._refresh_impl)

    def _refresh_impl(self):
        self.page.reload()

    def close(self):
        self._retry_operation(self._close_impl)

    def _close_impl(self):
        self.page.close()

    def get_text(self, selector):
        return self._retry_operation(self._get_text_impl, selector)

    def _get_text_impl(self, selector):
        return self.page.inner_text(selector)

    def get_attribute(self, selector, attr):
        return self._retry_operation(self._get_attr_impl, selector, attr)

    def _get_attr_impl(self, selector, attr):
        return self.page.get_attribute(selector, attr)

    def is_visible(self, selector):
        return self._retry_operation(self._is_visible_impl, selector)

    def _is_visible_impl(self, selector):
        return self.page.is_visible(selector)

    def quit(self):
        try:
            self.browser.close()
            self.playwright.stop()
        except:
            pass
