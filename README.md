# playwright_POM_Python

## Ensure that you:
1. Fork the repo.
2. Install dependencies using pip or pip3 depending on Python version (pip install Playwright dotenv).

## To run the test:
To run the **single signup test** for Chrome and go to dashboard for the first time:

`python singleSignupRun.py`

To run **parallel signup tests** for Chrome and Edge and go to dashboard for the first time:

`python parallelSignupRun.py`

To run **single login and buy test** for Chrome, buy a product, and checkout:

`python singleLoginBuyRun.py`

To run **parallel login and buy test** for Chrome and Edge, buy a product, and checkout:

`python parallelLoginBuyRun.py`

## Test Structure

```
Project Directory
        |-----------elementSelectors
        |                 |----------------loginAndBuySelectors.py
        |                 |----------------registrationPageSelectors.py
        |
        |------------testCapabilities
        |                 |-----------------testCaps.py
        |
        |
        |-------------testScenarios
        |                 |-----------------.env
                          |-----------------parallelLoginBuyRun.py
        |                 |-----------------parallelSignupRun.py
        |                 |-----------------singleLoginBuyRun.py
        |                 |-----------------singleSignupRun.py
        |
        |
        |
        |---------------testScripts
                          |-----------------parallelLoginBuyScript
                          |-----------------parallelSignup.py
                          |-----------------singleLoginBuyScript.py
                          |-----------------singleSignupScript.py
```

