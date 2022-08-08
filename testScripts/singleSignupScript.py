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
        self.browser = playwright.chromium.connect(capability.Chrome())
        page = self.browser.new_page()
        self.page = page
    def launchWeb(self):
        self.page.goto(select.webPage())
        title = self.page.title()
        print(title)

    def fillFirstName(self, data):
        self.page.locator(select.firstName()).fill(data)

    def fillLastName(self, data):
        self.page.locator(select.lastName()).fill(data)

    def fillEmail(self, data):
        self.page.locator(select.eMail()).fill(data)

    def fillPhone(self, data):
        self.page.locator(select.Telephone()).fill(data)

    def fillPassword(self, data):
        self.page.locator(select.Password()).fill(data)

    def confirmPassword(self, data):
        self.page.locator(select.confirmPassword()).fill(data)

    def subscribe(self):
        self.page.locator(select.Subscribe()).click()

    def acceptPolicy(self):
        self.page.locator(select.privacyPolicy()).click()

    def submit(self):
        self.page.locator(select.Submit()).click()

    def continueToDashboard(self):
        self.page.locator(select.goToDashboard()).click()

    def getSuccessStatus(self):
        return set_test_status(self.page, "passed", "Success")

    def getFailedStatus(self):
        return set_test_status(self.page, "failed", "Test failed")

    def closeBrowser(self):
        self.browser.close()
    









