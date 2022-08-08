import json
import os
import urllib.parse
import subprocess
from dotenv import load_dotenv

load_dotenv('.env')
username = os.getenv("my_username")
gridAcessKey = os.getenv("access_key")

playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]



capabilities =[{
        'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
        'browserVersion': 'latest',
        'platform': 'Windows 10',
        'build': 'E2E Tesing POM',
        'name': 'Playwright Test',
        'user': username,
        'accessKey': gridAcessKey,
        'console': True,
        'playwrightversion': playwrightVersion
    }]

class testCapabilities:
    def __init__(self) -> None:
        self.lambdatestGridURL = 'wss://cdp.lambdatest.com/playwright?capabilities='
        

    def Chrome(self):
        self.stringifiedCaps = urllib.parse.quote(json.dumps(capabilities[0]))
        return self.lambdatestGridURL+self.stringifiedCaps