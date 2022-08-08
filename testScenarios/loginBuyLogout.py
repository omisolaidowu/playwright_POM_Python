import sys
sys.path.append(sys.path[0] + "/..")

from testScripts.loginBuyLogoutScript import LoginAndBuy
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    try:
        playwright = LoginAndBuy(playwright)
        playwright.launchWeb()
        playwright.fillEmail("somegmai@gmail.com")
        playwright.fillPassword("mypassword")
        playwright.clickLogin()
        playwright.fillSearchBox("Nikon")
        playwright.clickSearchButton()
        playwright.clickProduct()
        playwright.clickAddToCart()
        playwright.clickCheckOutModal()

        playwright.hoverMenuBox()
        playwright.clickLogout()
        playwright.getStatus()
    except Exception as err:
        playwright.getFailedStatus()
    playwright.closeBrowser()