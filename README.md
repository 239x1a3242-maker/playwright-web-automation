# Playwright Web Automation

A Python-based web automation framework built using Playwright.
This project provides a task-driven structure for automating browser actions.

## Project Overview

This repository demonstrates:
- Browser automation using Playwright (Python)
- Task-based execution model
- Custom automation engine structure

## Project Structure

playwright-web-automation/
|
|-- action_runner.py        Executes automation actions
|-- playwright_engine.py    Playwright wrapper and browser logic
|-- run.py                  Main entry point
|-- task.py                 Task definitions
|-- README.md               Project documentation

## Requirements

- Python 3.8 or higher
- Playwright for Python

## Installation

Clone the repository:

git clone https://github.com/239x1a3242-maker/playwright-web-automation.git
cd playwright-web-automation

Install Playwright:

pip install playwright

Install Playwright browsers:

playwright install

## Usage

Run the automation script:

python run.py

This will execute the tasks defined in task.py using the Playwright engine.

## Customization

To add a new task:
1. Define task logic in task.py
2. Implement browser actions in playwright_engine.py
3. Execute tasks via action_runner.py

Example usage:

from task import MyTask

task = MyTask()
task.run()

## Features

- Task-based automation design
- Lightweight Playwright wrapper
- Easy to extend and modify
- Simple Python structure

## Future Improvements

- Configuration file support
- Headless and headed mode switching
- Logging and reporting
- Better error handling

## License

No license specified.
Add a license file if you plan to distribute this project.
