import sys
sys.path.append(sys.path[0] + "/..")

from testScripts.singleSignupScript import Register
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    try:
        playwright = Register(playwright)
        playwright.launchWeb()
        playwright.fillFirstName("Idowu")
        playwright.fillLastName("Omisola")
        playwright.fillEmail("anEmailgmai@gmail.com")
        playwright.fillPhone("08122334433")
        playwright.fillPassword("mypassword")
        playwright.confirmPassword("mypassword")
        playwright.subscribe()
        playwright.acceptPolicy()
        playwright.submit()
        playwright.continueToDashboard()
        playwright.getSuccessStatus()
    except:
        playwright.getFailedStatus()

    playwright.closeBrowser()