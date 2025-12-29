def run_actions(engine, task):
    """
    Execute ALL 37 Playwright operations with comprehensive error handling.
    """
    for step_idx, step in enumerate(task, 1):
        try:
            action = step.get("action")
            if not action:
                print(f"\n[Step {step_idx}] Missing 'action' key: {step}")
                continue
                
            handlers = {
                # === CORE 22 OPERATIONS ===
                "open": handle_open,
                "click": handle_click,
                "type": handle_type,
                "wait": handle_wait,
                "wait_seconds": handle_wait_seconds,
                "wait_for": handle_wait_for,
                "scroll_to": handle_scroll_to,
                "scroll_pixels": handle_scroll_pixels,
                "hover": handle_hover,
                "double_click": handle_double_click,
                "right_click": handle_right_click,
                "drag_drop": handle_drag_drop,
                "select_option": handle_select_option,
                "clear": handle_clear,
                "screenshot": handle_screenshot,
                "switch_window": handle_switch_window,
                "back": handle_back,
                "forward": handle_forward,
                "refresh": handle_refresh,
                "close": handle_close,
                "get_text": handle_get_text,
                "get_attribute": handle_get_attribute,
                "assert_visible": handle_assert_visible,
                "assert_text": handle_assert_text,
                
                # === PLAYWRIGHT SUPERPOWERS (15 NEW) ===
                "mock_api": handle_mock_api,
                "emulate_mobile": handle_emulate_mobile,
                "expect_download": handle_expect_download,
                "pdf": handle_pdf,
                "start_tracing": handle_start_tracing,
                "stop_tracing": handle_stop_tracing,
                "set_geolocation": handle_set_geolocation,
                "grant_permissions": handle_grant_permissions,
                "clear_cookies": handle_clear_cookies,
                "record_video": handle_record_video,
                "expect_screenshot": handle_expect_screenshot,
                "intercept_request": handle_intercept_request,
                "wait_for_response": handle_wait_for_response,
                "wait_for_request": handle_wait_for_request,
                "set_download_path": handle_set_download_path
            }
            
            if action in handlers:
                handlers[action](engine, step, step_idx)
            else:
                print(f"\n[Step {step_idx}] Unknown action '{action}': {step}")
                
        except Exception as e:
            print(f"\n❌ Automation failed at step {step_idx}:")
            print(f"   Action: {step}")
            print(f"   Error: {str(e)}")
            print(f"   Type: {type(e).__name__}")
            break
    
    print("\n✅ Automation sequence completed!")

# === CORE 22 HANDLERS ===
def handle_open(engine, step, step_idx):
    url = step.get("url")
    if not url: raise ValueError("Missing 'url'")
    print(f"[Step {step_idx}] 🌐 Opening: {url}")
    engine.open(url)

def handle_click(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] 🖱️ Clicking: {selector}")
    engine.click(selector)

def handle_type(engine, step, step_idx):
    selector = step.get("selector")
    value = step.get("value", "")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] ⌨️ Typing '{value[:20]}...' into: {selector}")
    engine.type(selector, value)

def handle_wait(engine, step, step_idx):
    seconds = step.get("seconds", 1)
    print(f"[Step {step_idx}] ⏳ Waiting {seconds}s...")
    engine.wait_seconds(seconds)

def handle_wait_seconds(engine, step, step_idx):
    seconds = step.get("seconds", 1)
    print(f"[Step {step_idx}] ⏳ Waiting {seconds}s...")
    engine.wait_seconds(seconds)

def handle_wait_for(engine, step, step_idx):
    selector = step.get("selector")
    timeout = step.get("timeout", 10)
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] ⌛ Waiting for: {selector}")
    engine.wait_for_selector(selector, timeout)

def handle_scroll_to(engine, step, step_idx):
    selector = step.get("selector")
    pixels = step.get("pixels")
    if selector:
        print(f"[Step {step_idx}] 📜 Scrolling to: {selector}")
        engine.scroll_to_selector(selector)
    elif pixels:
        print(f"[Step {step_idx}] 📜 Scrolling {pixels}px")
        engine.scroll_pixels(pixels)
    else:
        raise ValueError("Provide 'selector' or 'pixels'")

def handle_scroll_pixels(engine, step, step_idx):
    pixels = step.get("pixels")
    if pixels is None: raise ValueError("Missing 'pixels'")
    print(f"[Step {step_idx}] 📜 Scrolling {pixels}px")
    engine.scroll_pixels(pixels)

def handle_hover(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] 🖱️ Hovering: {selector}")
    engine.hover(selector)

def handle_double_click(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] 🖱️ Double clicking: {selector}")
    engine.double_click(selector)

def handle_right_click(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] 🖱️ Right clicking: {selector}")
    engine.right_click(selector)

def handle_drag_drop(engine, step, step_idx):
    source = step.get("source")
    target = step.get("target")
    if not source or not target: raise ValueError("Missing 'source' or 'target'")
    print(f"[Step {step_idx}] 🖱️ Dragging {source} → {target}")
    engine.drag_drop(source, target)

def handle_select_option(engine, step, step_idx):
    selector = step.get("selector")
    option = step.get("option")
    method = step.get("method", "text")
    if not selector or not option: raise ValueError("Missing 'selector' or 'option'")
    print(f"[Step {step_idx}] 📋 Selecting '{option}' ({method}): {selector}")
    engine.select_option(selector, option, method)

def handle_clear(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] 🗑️ Clearing: {selector}")
    engine.clear(selector)

def handle_screenshot(engine, step, step_idx):
    filename = step.get("filename", f"screenshot_step_{step_idx}.png")
    print(f"[Step {step_idx}] 📸 Screenshot: {filename}")
    path = engine.screenshot(filename)
    print(f"📁 Saved: {path}")

def handle_switch_window(engine, step, step_idx):
    window = step.get("window", "next")
    print(f"[Step {step_idx}] 🔄 Switching window: {window}")
    engine.switch_window(window)

def handle_back(engine, step, step_idx):
    print(f"[Step {step_idx}] ⬅️ Going back")
    engine.back()

def handle_forward(engine, step, step_idx):
    print(f"[Step {step_idx}] ➡️ Going forward")
    engine.forward()

def handle_refresh(engine, step, step_idx):
    print(f"[Step {step_idx}] 🔄 Refreshing page")
    engine.refresh()

def handle_close(engine, step, step_idx):
    print(f"[Step {step_idx}] ❌ Closing window")
    engine.close()

def handle_get_text(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    text = engine.get_text(selector)
    print(f"[Step {step_idx}] 📄 Text: '{text[:50]}...' ({selector})")

def handle_get_attribute(engine, step, step_idx):
    selector = step.get("selector")
    attr = step.get("attribute", "value")
    if not selector: raise ValueError("Missing 'selector'")
    value = engine.get_attribute(selector, attr)
    print(f"[Step {step_idx}] 🔍 '{attr}': {value} ({selector})")

def handle_assert_visible(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    visible = engine.is_visible(selector)
    print(f"[Step {step_idx}] 👁️ '{selector}' = {'✅ VISIBLE' if visible else '❌ HIDDEN'}")
    if not visible: raise AssertionError(f"Element not visible: {selector}")

def handle_assert_text(engine, step, step_idx):
    selector = step.get("selector")
    expected = step.get("expected")
    if not selector or not expected: raise ValueError("Missing 'selector' or 'expected'")
    actual = engine.get_text(selector)
    print(f"[Step {step_idx}] ✅ Text: '{actual[:30]}...' == '{expected}'")
    if expected not in actual: raise AssertionError(f"Expected '{expected}', got '{actual}'")

# === PLAYWRIGHT SUPERPOWERS HANDLERS (15 NEW) ===
def handle_mock_api(engine, step, step_idx):
    url_pattern = step.get("url_pattern")
    response_data = step.get("response_data", {})
    if not url_pattern: raise ValueError("Missing 'url_pattern'")
    print(f"[Step {step_idx}] 🌐 Mocking API: {url_pattern}")
    engine.mock_api(url_pattern, response_data)

def handle_emulate_mobile(engine, step, step_idx):
    device = step.get("device_name", "iPhone 12")
    print(f"[Step {step_idx}] 📱 Emulating: {device}")
    engine.emulate_mobile(device)

def handle_expect_download(engine, step, step_idx):
    selector = step.get("selector")
    if not selector: raise ValueError("Missing 'selector'")
    print(f"[Step {step_idx}] 📥 Expecting download from: {selector}")
    filename = engine.expect_download(selector)
    print(f"📁 Downloaded: {filename}")

def handle_pdf(engine, step, step_idx):
    filename = step.get("filename")
    print(f"[Step {step_idx}] 📄 Generating PDF: {filename or 'auto'}")
    path = engine.pdf(filename)
    print(f"📁 PDF saved: {path}")

def handle_start_tracing(engine, step, step_idx):
    name = step.get("name", "trace")
    print(f"[Step {step_idx}] 📹 Starting trace: {name}")
    engine.start_tracing(name)

def handle_stop_tracing(engine, step, step_idx):
    filename = step.get("filename")
    print(f"[Step {step_idx}] ⏹️ Stopping trace: {filename or 'auto'}")
    path = engine.stop_tracing(filename)
    print(f"📁 Trace saved: {path}")

def handle_set_geolocation(engine, step, step_idx):
    lat = step.get("latitude")
    lon = step.get("longitude")
    if lat is None or lon is None: raise ValueError("Missing 'latitude' or 'longitude'")
    print(f"[Step {step_idx}] 🌍 Setting GPS: {lat}, {lon}")
    engine.set_geolocation(lat, lon)

def handle_grant_permissions(engine, step, step_idx):
    perms = step.get("permissions", ["geolocation"])
    print(f"[Step {step_idx}] 🔓 Granting permissions: {perms}")
    engine.grant_permissions(perms)

def handle_clear_cookies(engine, step, step_idx):
    print(f"[Step {step_idx}] 🍪 Clearing cookies")
    engine.clear_cookies()

def handle_record_video(engine, step, step_idx):
    output_dir = step.get("output_dir", "videos")
    print(f"[Step {step_idx}] 🎥 Recording video: {output_dir}")
    engine.record_video(output_dir)

def handle_expect_screenshot(engine, step, step_idx):
    selector = step.get("selector")
    filename = step.get("filename")
    if not selector or not filename: raise ValueError("Missing 'selector' or 'filename'")
    print(f"[Step {step_idx}] 👁️ Visual test: {selector}")
    engine.expect_screenshot(selector, filename)

def handle_intercept_request(engine, step, step_idx):
    url_pattern = step.get("url_pattern")
    action = step.get("action", "abort")
    if not url_pattern: raise ValueError("Missing 'url_pattern'")
    print(f"[Step {step_idx}] 🚫 Intercepting: {url_pattern} ({action})")
    engine.intercept_request(url_pattern, action)

def handle_wait_for_response(engine, step, step_idx):
    url_predicate = step.get("url")
    if not url_predicate: raise ValueError("Missing 'url'")
    print(f"[Step {step_idx}] 🌐 Waiting response: {url_predicate}")
    engine.wait_for_response(url_predicate)

def handle_wait_for_request(engine, step, step_idx):
    url_predicate = step.get("url")
    if not url_predicate: raise ValueError("Missing 'url'")
    print(f"[Step {step_idx}] 🌐 Waiting request: {url_predicate}")
    engine.wait_for_request(url_predicate)

def handle_set_download_path(engine, step, step_idx):
    path = step.get("path", "downloads")
    print(f"[Step {step_idx}] 📁 Download path: {path}")
    engine.set_download_path(path)
