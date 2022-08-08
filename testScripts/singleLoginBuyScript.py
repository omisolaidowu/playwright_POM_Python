from playwright.sync_api import sync_playwright
import sys
sys.path.append(sys.path[0] + "/..")


from elementSelectors.loginAndBuySelectors import elementSelector
from testCapabilities.testCaps import testCapabilities

select = elementSelector()

capability = testCapabilities()

# Setting grid status to failed or passed
def set_test_status(page, status, remark):
        page.evaluate("_ => {}",
        "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")

class LoginAndBuy:
    
    def __init__(self, playwright) -> None:
        self.browser = playwright.chromium.connect(capability.Chrome())
        page = self.browser.new_page()
        self.page = page

    def launchWeb(self):
        self.page.goto(select.webPage())
        title = self.page.title()
        print(title)

    def fillEmail(self, data):
        return self.page.locator(select.eMail()).fill(data)
    
    def fillPassword(self, data):
        return self.page.locator(select.Password()).fill(data)

    def clickLogin(self):
        return self.page.locator(select.loginAccount()).click()
    
    def fillSearchBox(self, data):
        return self.page.locator(select.searchProduct()).fill(data)
    
    def clickSearchButton(self):
        return self.page.locator(select.searchButton()).click()

    def clickProduct(self):
        return self.page.locator(select.Product()).click()

    def clickAddToCart(self):
        return self.page.locator(select.addCart()).click()
    
    def clickCheckOutModal(self):
        return self.page.locator(select.checkOut()).click()
    

    def hoverMenuBox(self):
        return self.page.locator(select.hoverBox()).hover()
    
    def clickLogout(self):
        return self.page.locator(select.logoutUser()).click()

    def getSuccessStatus(self):
        return set_test_status(self.page, "passed", "Success")

    def getFailedStatus(self):
        return set_test_status(self.page, "failed", "Test failed")

    def closeBrowser(self):
        return self.browser.close()

    