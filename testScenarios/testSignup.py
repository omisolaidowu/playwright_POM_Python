import sys
sys.path.append(sys.path[0] + "/..")

from testScripts.signup import Register
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    playwright = Register(playwright)
    playwright.launchWeb()
    playwright.fillFirstName("Idowu")
    playwright.fillLastName("Omisola")
    playwright.fillEmail("somegmai@gmail.com")
    playwright.fillPhone("08122334433")
    playwright.fillPassword("mypassword")
    playwright.confirmPassword("mypassword")
    playwright.subscribe()
    playwright.acceptPolicy()
    playwright.submit()
    playwright.continueToDashboard()
    playwright.closeBrowser()