from django.contrib.auth.models import User
from django.test import TransactionTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SeleniumBaseTest(TransactionTestCase):
    """Clase base para configurar Selenium y evitar código repetido."""
    reset_sequences = True  # Resetea ID de autoincremento en MySQL

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

        cls.browser = webdriver.Chrome(options=options)
        cls.base_url = "https://gc-ingsoft3-2025-320310590859.southamerica-east1.run.app/"  # Cambia por tu URL real

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()


class LoginTest(SeleniumBaseTest):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_login(self):
        self.browser.get(f"{self.base_url}/accounts/login/")
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password").send_keys("testpassword", Keys.RETURN)

        # Verificamos si el login fue exitoso
        self.assertIn("NOTEPAD", self.browser.page_source)


class RegisterTest(SeleniumBaseTest):
    def test_register_user(self):
        self.browser.get(f"{self.base_url}/notes/accounts/signup/")

        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password1").send_keys("TestPass123!")
        self.browser.find_element(By.NAME, "password2").send_keys("TestPass123!", Keys.RETURN)

        self.assertIn("NOTEPAD", self.browser.page_source)
        self.assertTrue(User.objects.filter(username="testuser").exists())


class AddNoteTest(SeleniumBaseTest):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="TestPass123!")

    def test_create_note(self):
        self.browser.get(f"{self.base_url}/accounts/login/")
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password").send_keys("TestPass123!", Keys.RETURN)

        self.browser.get(f"{self.base_url}/notes/new/")
        self.browser.find_element(By.NAME, "title").send_keys("Nota de prueba")
        self.browser.find_element(By.NAME, "body").send_keys("Contenido de la nota de prueba.")
        self.browser.find_element(By.NAME, "submit").click()

        self.assertIn("Nota de prueba", self.browser.page_source)
