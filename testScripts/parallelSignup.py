from playwright.sync_api import sync_playwright
import sys
sys.path.append(sys.path[0] + "/..")


from elementSelectors.registrationPageSelectors import elementSelector
from testCapabilities.testCaps import testCapabilities

select = elementSelector()

capability = testCapabilities()

def set_test_status(page, status, remark):
        page.evaluate("_ => {}",
        "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")



class Register:
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
    def fillFirstName(self, data):
        for page in self.pages:
            page.locator(select.firstName()).fill(data)
    def fillLastName(self, data):
        for page in self.pages:
            page.locator(select.lastName()).fill(data)
    def fillEmail(self, data):
        for page in self.pages:
            page.locator(select.eMail()).fill(data)
    def fillPhone(self, data):
        for page in self.pages:
            page.locator(select.Telephone()).fill(data)
    def fillPassword(self, data):
        for page in self.pages:
            page.locator(select.Password()).fill(data)
    def confirmPassword(self, data):
        for page in self.pages:
            page.locator(select.confirmPassword()).fill(data)
    def subscribe(self):
        for page in self.pages:
            page.locator(select.Subscribe()).click()
    def acceptPolicy(self):
        for page in self.pages:
            page.locator(select.privacyPolicy()).click()
    def submit(self):
        for page in self.pages:
            page.locator(select.Submit()).click()
    def continueToDashboard(self):
        for page in self.pages:
            page.locator(select.goToDashboard()).click()
    def getSuccessStatus(self):
        for page in self.pages:
            set_test_status(page, "passed", "Success")

    def getFailedStatus(self):
        for page in self.pages:
            set_test_status(page, "failed", "Test failed")

    def closeBrowser(self):
        for browser in self.browsers:
            browser.close()
    









