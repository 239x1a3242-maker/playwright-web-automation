# task.py - YOUR EXACT SEND BUTTON SE
TASK = [
    # === STEPS 1-3 (ALREADY WORKING) ===
    {"action": "open", "url": "https://www.perplexity.ai"},
    {"action": "wait_seconds", "seconds": 4},
    {"action": "type", "selector": "#ask-input", "value": "youtube official site"},
    {"action": "wait_seconds", "seconds": 2},
    
    # === YOUR EXACT SEND BUTTON ===
    {"action": "click", "selector": 'button[aria-label="Submit"]'},
    {"action": "wait_seconds", "seconds": 6},
    
    # === YOUTUBE FREE FIRE (UNCHANGED) ===
    {"action": "wait_for", "selector": "a[href*='youtube.com']", "timeout": 20},
    {"action": "click", "selector": "a[href*='youtube.com']"},
    {"action": "wait_seconds", "seconds": 5},
    {"action": "type", "selector": "input#search", "value": "free fire"},
    {"action": "click", "selector": "button[aria-label*='Search']"},
    {"action": "wait_seconds", "seconds": 5},
    {"action": "click", "selector": "ytd-video-renderer a#thumbnail"},
    {"action": "wait_seconds", "seconds": 6},
    
    # === EVIDENCE ===
    {"action": "screenshot", "filename": "submit_button_success.png"},
    {"action": "get_text", "selector": "yt-formatted-string#title"}
]
