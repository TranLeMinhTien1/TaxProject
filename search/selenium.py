from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class Test(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.chrome('search/chromedriver.exe')

    