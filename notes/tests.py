# Test unitarios con Django Test

from django.test import TestCase
from django.contrib.auth.models import User
from notes.models import Note

class RegistroTest(TestCase):
    def test_crear_usuario(self):
        print("\nCreamos un usuario")
        user = User.objects.create_user(username="usuario_test2", password="MiClaveSegura123")
        self.assertEqual(user.username, "usuario_test")
        print("\nUsuarios en la BD:", User.objects.all())  # Ver que usuarios hay

    def test_login_usuario(self):
        print("\nIniciamos sesion con ese usuario")
        User.objects.create_user(username="usuario_test", password="MiClaveSegura123")
        login = self.client.login(username="usuario_test", password="MiClaveSegura123")
        
        # Verificamos que el login fue exitoso
        self.assertTrue(login)

        # Verificamos que la sesión tiene el usuario autenticado
        self.assertTrue("_auth_user_id" in self.client.session)

        print("\nLogIn Exitoso.")

class NoteTest(TestCase):
    def setUp(self):
        """Crear un usuario para las pruebas"""
        self.user = User.objects.create_user(username="usuario_test", password="MiClaveSegura123")

    def test_crear_nota(self):
        """Verifica que se pueda crear una nota y que se almacene correctamente"""
        self.client.login(username="usuario_test", password="MiClaveSegura123")

        # Crear una nota
        note = Note.objects.create(title="Mi primera nota", body="Este es el contenido de la nota", user=self.user)

        # Verificar que la nota fue creada
        self.assertEqual(note.title, "Mi primera nota")
        self.assertEqual(note.body, "Este es el contenido de la nota")
        self.assertEqual(note.user.username, "usuario_test")

        # Mostrar la nota en la consola
        print(f"\nTítulo: {note.title}\nContenido: {note.body}\nAutor: {note.user.username}\n")