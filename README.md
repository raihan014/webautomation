# Automation Exercise - Web Login Automation

A web automation project developed as part of the **SQA Engineer Intern Assessment** for RoBenDevs.

The project automates the login scenario of the [Automation Exercise](https://www.automationexercise.com/) website using **Python, Playwright, and Pytest**.

---

##  Project Objective

The objective of this project is to automate the following login scenario:

1. Launch the Automation Exercise website.
2. Navigate to the Login page.
3. Enter the registered email address.
4. Enter the registered password.
5. Submit the login form.
6. Verify that the login was successful.

The user account used for automation was manually created before starting the automation project, as required by the assessment.

---

##  Technologies Used

- Python 3.14.7
- Playwright 1.63.0
- Pytest 9.1.1
- python-dotenv 1.2.3
- Google Chrome
- VS Code

---

##  Project Structure

```text
automationexercise-sqa/
│
├── tests/
│   └── test_login.py
│
├── .env
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

### File Description

| File / Folder | Description |
|---|---|
| `tests/test_login.py` | Contains the automated login test |
| `.env` | Stores login credentials locally |
| `.gitignore` | Prevents sensitive and unnecessary files from being committed |
| `pytest.ini` | Pytest configuration |
| `requirements.txt` | Python project dependencies |
| `README.md` | Project documentation |



---

##  Test Account

A new user account was manually created on Automation Exercise before starting the automation project.

The automated test uses the credentials of that manually created account.

Credentials are stored locally in the `.env` file:

```env
EMAIL=registered_email
PASSWORD=registered_password
```

The actual credentials are intentionally not included in this repository.

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone <GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd automationexercise-sqa
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

### 4. Configure credentials

Create a `.env` file in the project root:

```text
automationexercise-sqa/
└── .env
```

Add the credentials of the Automation Exercise account that was manually created before automation:

```env
EMAIL=registered_email
PASSWORD=registered_password
```


---

##  Browser Configuration

The automation uses the Google Chrome installation available on the local Windows machine.


If Chrome is installed in a different location, update the `executable_path` in `tests/test_login.py` accordingly.

---

##  Automated Test Scenario

### Test Case: Successful User Login

| Step | Action | Expected Result |
|---|---|---|
| 1 | Launch Automation Exercise | Website loads successfully |
| 2 | Click `Signup / Login` | Login page is displayed |
| 3 | Enter registered email | Email is entered successfully |
| 4 | Enter registered password | Password is entered successfully |
| 5 | Click `Login` | User is authenticated |
| 6 | Verify `Logged in as` | Successful login is confirmed |

---

##  Running the Test

Make sure the virtual environment is activated.

Run:

```powershell
pytest
```

Pytest will automatically discover the test inside the `tests` directory.

---

##  Test Result

The automated login test was executed successfully.

### Result

**Status: PASSED**

The test successfully:

- Launched Automation Exercise
- Navigated to the Login page
- Entered the registered email
- Entered the registered password
- Submitted the login form
- Verified successful authentication

---

##  Security

Sensitive credentials are not stored directly in the test source code.

The project uses `python-dotenv` to load credentials from the local `.env` file.

The `.gitignore` file excludes:

```text
.env
.venv/
__pycache__/
.pytest_cache/
```

---

##  Assessment Coverage

This project covers the requested Web Automation bonus scenario:

- Manually create a new user account
- Use the newly created credentials
- Set up a complete automation project
- Use a popular automation framework
- Launch the website
- Navigate to the Login page
- Enter registered email address
- Enter registered password
- Submit the login form
- Verify successful login
- Provide complete automation source code

---

##  Author

**Marfi Hasan Raihan**

SQA / Software Testing Candidate

---

##  Assessment

This project was created as the **Web Automation Bonus Question** for the SQA Engineer Intern Assessment.

**Application under test:**  
[Automation Exercise](https://www.automationexercise.com/)

**Automation Framework:**  
Playwright

**Programming Language:**  
Python