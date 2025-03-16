# JKUAT Session Report Automation

Welcome to the JKUAT Session Report Automation project! This Python script uses Selenium to automate navigating through a web portal, logging in with credentials from a `.env` file and session reporting. JKUAT Comrades can understand the hustle of trying to get registered for the semester after you accidentally forgot this time. The down side is that I haven't figured out a way to prevent the "I'm not a robot" captchas... Help me fix this if you know how. As the script runs after it searches via the search engine you'll most likely get a captcha which you have to solve before an exception is thrown and the program terminates. After that, it continues up to the end without any more human intervention

## What Does It Do?

- **Starts with Google:** The script opens Google and searches for "JKUAT students portal". After this you have to accurately finish a "I'm not a robot" captcha
- **Navigates Like a Pro:** It clicks on the first search result to open the portal. 
- **Signs You In:** It finds the username and password fields on the sign-in page, fills them in from your secure `.env` file, and clicks the sign-in button.
- **Opens the Dropdown:** The script simulates a human by opening a dropdown menu (Admission) to reveal additional options.
- **Clicks Reporting:** It then clicks the "Reporting" link from the dropdown.
- **Takes a Screenshot:** Once on the reporting page, the script takes a screenshot so you know everything worked as expected.

## Installation

Before you run the script, make sure you have the following installed:

1. **Python 3.7+** – [Download Python](https://www.python.org/downloads/)
2. **Selenium:**  
   ```bash
   pip install selenium
   ```
3. **Webdriver Manager:**  
   ```bash
   pip install webdriver-manager
   ```
4. **python-dotenv:**  
   ```bash
   pip install python-dotenv
   ```
5. **Google Chrome:** Ensure you have Google Chrome installed on your machine.

## Setup

1. **Create a `.env` file:**  
   In the project directory, create a `.env` file with your credentials:
   ```env
   USERNAME=your_student-reg
   PASSWORD=your_password_here
   ```
## How to Run

Simply run the script using your Python interpreter. For example, on Windows:
```bash
python session-report.py
```
*Note: The script uses human-like delays, but if a CAPTCHA appears (as sometimes happens), you have a few seconds to solve it before continuing.*

## Limitations & What To Do

- **CAPTCHA Challenges:**  
  The website might ask you to prove you're not a bot, you'll need to solve the CAPTCHA manually.  
  **Tip:** Increase the wait time or add a manual prompt (using `input("Solve the CAPTCHA and press Enter...")`) if needed.

- **Dynamic Web Elements:**  
  Websites change their layout often. If the script stops working, check if the HTML structure (like element IDs, classes, or XPath) has changed and update the selectors accordingly.

- **Manual Intervention:**  
  Some elements (like CAPTCHAs) might require human interaction. While the script simulates human behavior, there's no perfect solution to completely avoid manual steps.

- **Browser & Driver Updates:**  
  This script uses `webdriver-manager` to automatically manage ChromeDriver. However, if your Chrome version is updated, ensure `webdriver-manager` is up-to-date with:
  ```bash
  pip install --upgrade webdriver-manager
  ```

## Future Improvements

- **CAPTCHA Bypass Options:**  
  Explore using test keys for CAPTCHA if you're in a controlled test environment.
- **Error Handling:**  
  Improve error messages and logging to better understand issues if elements are not found.
- **Configuration Options:**  
  Consider using command-line arguments or a configuration file for customizing wait times, selectors, and other parameters.

Enjoy