from playwright.sync_api import sync_playwright
import sys
sys.path.append(sys.path[0] + "/..")


from elementSelectors.registrationPageSelectors import elementSelector
from testCapabilities.testCaps import testCapabilities

select = elementSelector()

capability = testCapabilities()


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
        return self.page.locator(select.firstName()).fill(data)
    def fillLastName(self, data):
        return self.page.locator(select.lastName()).fill(data)
    def fillEmail(self, data):
        return self.page.locator(select.eMail()).fill(data)
    def fillPhone(self, data):
        return self.page.locator(select.Telephone()).fill(data)
    def fillPassword(self, data):
        return self.page.locator(select.Password()).fill(data)
    def confirmPassword(self, data):
        return self.page.locator(select.confirmPassword()).fill(data)
    def subscribe(self):
        return self.page.locator(select.Subscribe()).click()
    def acceptPolicy(self):
        return self.page.locator(select.privacyPolicy()).click()
    def submit(self):
        return self.page.locator(select.Submit()).click()
    def continueToDashboard(self):
        return self.page.locator(select.goToDashboard()).click()
    def closeBrowser(self):
        return self.browser.close()
    









