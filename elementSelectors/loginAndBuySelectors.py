webElements = {
    'webpage': "https://ecommerce-playground.lambdatest.io/index.php?route=account/login",
    'E-Mail': 'input[placeholder="E-Mail Address"]',
    'Password': 'input[placeholder="Password"]',
    'Login': 'input:has-text("Login")',
    'Search': 'input[name="search"] >> nth = 0',
    'searchbutton': 'div[class="search-button"]:has-text("Search")',
    'product': 'h4[class="title"]:has-text("Nikon D300") >> nth = 0',
    'addcart': 'div[id="entry_216842"]:has-text("Add to Cart")',
    'checkoutmodal': 'div[role="alert"]:has-text("Checkout")',
    'Hoverable': 'a[role="button"]:has-text("My account")',
    'Logout': 'span:has-text("Logout")'
}
class elementSelector:
    def __init__(self) -> None:
        self.webpage = webElements['webpage']
        self.email = webElements['E-Mail']
        self.password = webElements['Password']
        self.login = webElements['Login']
        self.hover = webElements['Hoverable']
        self.searchproduct = webElements['Search']
        self.product = webElements['product']
        self.addcart = webElements['addcart']
        self.checkout = webElements['checkoutmodal']
        self.searchbutton = webElements['searchbutton']
        self.logout = webElements['Logout']
    def webPage(self):
        return self.webpage
    def eMail(self):
        return self.email
    def Password(self):
        return self.password
    def loginAccount(self):
        return self.login
    def hoverBox(self):
        return self.hover
    def searchProduct(self):
        return self.searchproduct
    def Product(self):
        return self.product
    def addCart(self):
        return self.addcart
    def checkOut(self):
        return self.checkout
    def searchButton(self):
        return self.searchbutton
    def logoutUser(self):
        return self.logout