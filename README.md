# 🚗 Urban Routes Automated Testing Project
 
## 📌 Description

This project focuses on building an end-to-end (E2E) automated testing framework for the Urban Routes web application, a ride-hailing platform.

The tests are developed using Python and Selenium WebDriver to validate critical user flows such as route setup, phone authentication, service requests, and payment method management.

This approach ensures systematic validation of the application's functionality and early detection of regressions.

## 🎯 Project Objectives
* Automate end-to-end testing of critical user flows
* Validate route configuration and service selection
* Verify phone number authentication process
* Ensure correct handling of payment methods
* Detect functional issues and prevent regressions

## 🛠️ Technologies & Tools
* Programming Language: Python
* Automation Framework: Selenium WebDriver
* Testing Framework: Pytest
* Browser: Microsoft Edge
* Driver: EdgeDriver

## 📁 Project Structure
qa-project-Urban-Routes-es/
│
├── data.py              # Test data and configuration values
├── CodeRetrieve.py      # Helper function to retrieve verification codes
├── PageLocators.py      # UI locators and interaction methods
├── main.py              # Automated test cases

## 📄 File Overview

🔹 data.py

Contains test data such as:
* Base URL
* Origin and destination addresses
* Phone numbers
* Payment details

🔹 CodeRetrieve.py
* Implements a helper method to retrieve verification codes from network logs
* Supports automation of phone authentication flows
  
🔹 PageLocators.py
* Defines UI elements and locators
* Contains methods to interact with the application
* Covers actions such as:
* Selecting routes
* Adding payment methods
* Interacting with UI components
  
🔹 main.py

Contains the TestUrbanRoutes test suite, including scenarios such as:

* Route configuration
* Taxi selection (Comfort option)
* Phone number input and verification
* Payment method addition
* Adding notes for the driver
* Selecting additional requirements (e.g., blankets, ice cream)

## 🚀 How to Run the Tests
1. Clone the repository
   
git clone https://github.com/Fitzonder/qa-project-Urban-Routes-es

2. Create a virtual environment
   
python -m venv env

3. Activate the environment
   
# Mac/Linux
source env/bin/activate

# Windows
env\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

Example requirements.txt
selenium==4.x.x
pytest==x.x.x

6. Run the tests
pytest main.py

## ✅ Key Skills Demonstrated
End-to-End (E2E) Testing
Test Automation with Selenium
Test Case Design
UI Testing
Debugging and Issue Detection
Test Data Management

## 🤝 Contributions

Contributions are welcome. To propose improvements:

Fork the repository
Create a new branch
Implement your changes
Submit a pull request

👤 Author

Carlos Lenis
