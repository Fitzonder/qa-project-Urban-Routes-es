# 🚗 Urban Routes - E2E Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Automation-Selenium-green)
![Pytest](https://img.shields.io/badge/Tested%20With-Pytest-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![QA](https://img.shields.io/badge/Focus-E2E%20Testing-blueviolet)

This project implements an end-to-end (E2E) automated testing framework for the Urban Routes web application, a ride-hailing platform.

The framework validates critical user flows such as route setup, phone authentication, service selection, and payment method management, ensuring application stability and preventing regressions.

---

## 📌 Overview

The automation suite simulates real user interactions across the application, covering complete booking flows from start to finish.

Key scenarios covered:

* Route configuration (origin & destination)
* Service selection (e.g., Comfort ride)
* Phone number authentication
* Payment method management
* Additional ride preferences (notes, extras)

---

## 💼 Professional Context

This project demonstrates practical QA Automation skills aligned with real-world testing environments:

* End-to-End (E2E) test automation
* UI interaction using Selenium WebDriver
* Test design based on user behavior
* Automation of multi-step workflows
* Handling dynamic elements and authentication flows
* Maintainable and scalable test structure

---

## 🛠️ Technologies & Tools

* Python 🐍
* Selenium WebDriver 🌐
* Pytest ⚡
* Microsoft Edge
* EdgeDriver

---

## 📂 Project Structure

```bash id="3kq9ra"
qa-project-Urban-Routes-es/
│
├── data.py              # Test data and configuration values
├── CodeRetrieve.py      # Verification code retrieval logic
├── PageLocators.py      # UI locators and interaction methods
├── main.py              # Test suite (E2E scenarios)
```

---

## 🔄 Example Test Flow

### 🚕 End-to-End Ride Booking Scenario

1. User enters origin and destination
2. Selects ride type (Comfort)
3. Enters phone number
4. System retrieves and validates verification code
5. Adds payment method
6. Confirms ride preferences
7. Submits request

✔️ The test validates that each step completes successfully and the system responds correctly.

---

## ⚙️ Installation

1. Clone the repository:

```bash id="b6wqg9"
git clone https://github.com/Fitzonder/qa-project-Urban-Routes-es
cd qa-project-Urban-Routes-es
```

2. Create a virtual environment:

```bash id="9l8o6k"
python -m venv env
```

3. Activate the environment:

**Mac/Linux**

```bash id="c8bq2u"
source env/bin/activate
```

**Windows**

```bash id="9ks8jm"
env\Scripts\activate
```

4. Install dependencies:

```bash id="c9x1v3"
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run the test suite with:

```bash id="1j3o8g"
pytest main.py
```

For detailed output:

```bash id="lq2x3n"
pytest main.py -v
```

---

## 🧪 Key Testing Validations

* UI element interaction and stability
* End-to-end workflow validation
* Authentication flow handling
* Data input and validation
* Error detection and regression prevention

---

## 📈 Skills Demonstrated

* E2E Test Automation
* Selenium WebDriver usage
* Test case design and execution
* Debugging and issue identification
* Handling dynamic UI elements
* Test data management

---

## 🚧 Future Improvements

* Cross-browser testing (Chrome, Firefox)
* Integration with CI/CD (GitHub Actions)
* Test reporting (Allure Reports)
* Page Object Model (POM) refactor
* Parallel test execution

---

## 👨‍💻 Author

Carlos Lenis
QA Automation Engineer (Junior) 🚀

---

## 📬 Contact

* LinkedIn: *https://www.linkedin.com/in/carlos-lenis-812a5918/*
* GitHub: https://github.com/Fitzonder

