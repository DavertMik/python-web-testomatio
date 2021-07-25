# pytest-web-ui-demo
Project to demonstrate Pytest + Selenium usage for Web UI test automation
---

:computer: Application used in this project: [Swag Labs Demo](https://www.saucedemo.com/)

:red_circle: To build the project you must have [Python](https://www.python.org/) installed.
It is recommended that you create a new [virtualenv](https://virtualenv.pypa.io/en/latest/) to install the dependencies. 

:large_orange_diamond: To install virtualenv run:
- `pip3 install virtualenv`

:large_orange_diamond: Create a new virtualenv at the project root:
- `python3 -m venv venv`

:large_orange_diamond: Install dependencies. **Make sure your virtualenv is activated** if you don't know how to do it please read this [guide](https://docs.python-guide.org/dev/virtualenvs/) Basic Usage section.
- `pip -r install requirements.txt`

:large_blue_diamond: To execute tests simply run:
- `pytest`
---
### This project have the following structure:
- **config**
  - General test data, composed by constants like chrome executable path, base url, default selenium timeout
- **drivers**
  - Should contain desired drivers, i'm using just chrome
- **lib**
  - element :arrow_right: Model representation of a web element, contains elements related actions like click(), send_keys(), get_text()
  - page :arrow_right: Model representation of a page object, contains page related actions like open()
  - selenium_utils :arrow_right: Implements selenium specific funcionality like find_elements and explicit waits
- **page_objects**
  - Implements different application pages with their locators and actions
- **tests**
  - Implements the actual tests, using actions that should be implemented at the page objects level
- **conftest**
  - pytest fixtures implementations, contains driver and page objects initialization
