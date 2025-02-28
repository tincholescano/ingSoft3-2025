Feature('notas');

Scenario('test Account',  ({ I }) => {
    I.amOnPage('http://127.0.0.1:8000/accounts/login/?next=/notes/');
		I.saveScreenshot('1-SesionSinIniciar.png');
		I.pressKey('Enter');
		I.saveScreenshot('2-ErrorSinDatos.png');
	
		I.login('admin', 'Cont1234');
		I.saveScreenshot('3-SesionIniciada.png');
});

Scenario('test Notas',  ({ I }) => {
    I.amOnPage('http://127.0.0.1:8000/accounts/login/?next=/notes/');	
		I.login('admin', 'Cont1234');	

	I.amOnPage('http://127.0.0.1:8000/notes/');
		I.saveScreenshot('4-Notas.png');
		I.click('note_add'); // Botón para agregar nota
		I.waitForElement('#id_title', 5);
		I.fillField('#id_title', 'Mi primera nota');
		I.fillField('#id_body', 'Este es el contenido de la nota');
		I.wait(2);  // Verifica que los campos se llenan
		I.saveScreenshot('5-CompletoForm.png');
		I.click('note_add');
		
	I.amOnPage('http://127.0.0.1:8000/notes/');
		I.saveScreenshot('6-NuevaNota.png');
		I.see('Mi primera nota'); // Verifica que la nota aparece en el listado
		I.click('Ver nota');
		I.see('Este es el contenido de la nota');
		I.saveScreenshot('7-NotaCompleta.png');
});
