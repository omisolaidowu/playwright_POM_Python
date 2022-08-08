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
        self.allCaps = [capability.Edge(), capability.Chrome()]
        self.browsers = [playwright.chromium.connect(i) for i in self.allCaps]
        pages = [i.new_page() for i in self.browsers]
        self.pages = pages

    def launchWeb(self):
        for page in self.pages:
            page.goto(select.webPage())
            title = page.title()
            print(title)

    def fillEmail(self, data):
        for page in self.pages:
            page.locator(select.eMail()).fill(data)
    
    def fillPassword(self, data):
        for page in self.pages:
            page.locator(select.Password()).fill(data)

    def clickLogin(self):
        for page in self.pages:
            page.locator(select.loginAccount()).click()
    
    def fillSearchBox(self, data):
        for page in self.pages:
            page.locator(select.searchProduct()).fill(data)
    
    def clickSearchButton(self):
        for page in self.pages:
            page.locator(select.searchButton()).click()

    def clickProduct(self):
        for page in self.pages:
            page.locator(select.Product()).click()

    def clickAddToCart(self):
        for page in self.pages:
            page.locator(select.addCart()).click()
    
    def clickCheckOutModal(self):
        for page in self.pages:
            page.locator(select.checkOut()).click()
    
    def hoverMenuBox(self):
        for page in self.pages:
            page.locator(select.hoverBox()).hover()
    
    def clickLogout(self):
        for page in self.pages:
            page.locator(select.logoutUser()).click()

    def getSuccessStatus(self):
        for page in self.pages:
            set_test_status(page, "passed", "Success")

    def getFailed(self):
        for page in self.pages:
            set_test_status(page, "failed", "Test failed")

    def closeBrowser(self):
        for browser in self.browsers:
            browser.close()

    