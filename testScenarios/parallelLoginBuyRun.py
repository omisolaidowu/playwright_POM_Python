import sys
sys.path.append(sys.path[0] + "/..")

from testScripts.parallelLoginBuyScript import LoginAndBuy
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    try:
        playwright = LoginAndBuy(playwright)
        playwright.launchWeb()
        playwright.fillEmail("some3gmail@gmail.com")
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
        playwright.getFailed()
    playwright.closeBrowser()