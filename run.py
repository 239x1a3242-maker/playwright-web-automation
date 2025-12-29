from playwright_engine import PlaywrightEngine  # ← CHANGED
from action_runner import run_actions
from task import TASK

engine = PlaywrightEngine(max_retries=3)

try:
    run_actions(engine, TASK)
finally:
    engine.quit()
