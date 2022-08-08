webElements = {
    'webpage': "https://ecommerce-playground.lambdatest.io/index.php?route=account/register",
    'First_Name': 'input[placeholder="First Name"]',
    'Last_Name': 'input[placeholder="Last Name"]',
    'E-Mail': 'input[placeholder="E-Mail"]',
    'Telephone': 'input[placeholder="Telephone"]',
    'Password': 'input[placeholder="Password"]',
    'Confirm_Password': 'input[placeholder="Password Confirm"]',
    'Subscribe': 'label:has-text("No")',
    'Privacy_Policy': 'label:has-text("I have read and agree to the Privacy Policy")',
    'Submit': 'input[value="Continue"]',
    'Continue': "text=Continue"
}


class elementSelector:
    def __init__(self) -> None:
        self.webpage = webElements["webpage"]
        self.firstname = webElements["First_Name"]
        self.lastname = webElements["Last_Name"]
        self.email = webElements["E-Mail"]
        self.telephone = webElements["Telephone"]
        self.password = webElements["Password"]
        self.confirmpassword = webElements["Confirm_Password"]
        self.subscribe = webElements["Subscribe"]
        self.privacypolicy = webElements["Privacy_Policy"]
        self.submit = webElements["Submit"]
        self.todashboard = webElements["Continue"]
    
    def webPage(self):
        return self.webpage
    def firstName(self):
        return self.firstname
    def lastName(self):
        return self.lastname
    def eMail(self):
        return self.email
    def Telephone(self):
        return self.telephone
    def Password(self):
        return self.password
    def confirmPassword(self):
        return self.confirmpassword
    def Subscribe(self):
        return self.subscribe   
    def privacyPolicy(self):
        return self.privacypolicy
    def Submit(self):
        return self.submit
    def goToDashboard(self):
        return self.todashboard