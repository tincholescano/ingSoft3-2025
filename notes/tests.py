# Create your tests here.

from django.contrib.auth.models import User
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # Abrir la página de login
        self.browser.get(f"{self.live_server_url}/accounts/login/")
        time.sleep(1)  # Esperar un momento para la carga

        # Buscar campos de usuario y contraseña
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")

        # Ingresar datos
        username_input.send_keys("testuser")
        password_input.send_keys("testpassword")
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Esperar para ver el resultado

        # Verificar que el usuario fue autenticado
        self.assertIn("NOTEPAD", self.browser.page_source)  # Ajusta según la redirección de tu aplicación

class RegisterTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_register_user(self):
        self.browser.get(f"{self.live_server_url}/notes/accounts/signup/")  # Ajustá la URL si es distinta
        time.sleep(1)

        # Llenamos el formulario de registro
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password1").send_keys("TestPass123!")
        self.browser.find_element(By.NAME, "password2").send_keys("TestPass123!")
        self.browser.find_element(By.NAME, "password2").send_keys(Keys.RETURN)  # Ajustá el botón si es diferente

        time.sleep(2)  # Esperamos a que cargue la página

        # Verificamos si se redirige correctamente después del registro
        self.assertIn("NOTEPAD", self.browser.page_source)

        # Verificamos que el usuario se haya creado en la base de datos
        self.assertTrue(User.objects.filter(username="testuser").exists())


class AddnoteTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()  # Asegurate de tener Chromedriver instalado

    def tearDown(self):
        self.browser.quit()

    def test_create_note(self):
        # Creamos un usuario en la base de datos
        user = User.objects.create_user(username="testuser", password="TestPass123!")

        # Iniciamos sesión con el usuario creado
        self.browser.get(f"{self.live_server_url}/accounts/login/")
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password").send_keys("TestPass123!")
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        time.sleep(2)  # Esperamos a que cargue la página

        # Vamos a la página de creación de notas
        self.browser.get(self.live_server_url + "/notes/new/")
        self.browser.find_element(By.NAME, "title").send_keys("Nota de prueba")
        self.browser.find_element(By.NAME, "body").send_keys("Contenido de la nota de prueba.")
        self.browser.find_element(By.NAME, "submit").click()

        time.sleep(2)  # Esperamos a que cargue la página

        # Verificamos que la nota aparece en la lista de notas
        self.assertIn("Nota de prueba", self.browser.page_source)