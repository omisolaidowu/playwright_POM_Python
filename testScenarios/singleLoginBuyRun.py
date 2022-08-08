import sys
sys.path.append(sys.path[0] + "/..")

from testScripts.singleLoginBuyScript import LoginAndBuy
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    try:
        playwright = LoginAndBuy(playwright)
        playwright.launchWeb()
        playwright.fillEmail("anEmailgmai@gmail.com")
        playwright.fillPassword("mypassword")
        playwright.clickLogin()
        playwright.fillSearchBox("Nikon")
        playwright.clickSearchButton()
        playwright.clickProduct()
        playwright.clickAddToCart()
        playwright.clickCheckOutModal()

        playwright.hoverMenuBox()
        playwright.clickLogout()
        playwright.getSuccessStatus()
    except:
        playwright.getFailedStatus()
    playwright.closeBrowser()