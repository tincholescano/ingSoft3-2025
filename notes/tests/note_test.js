Feature('Notas');

Scenario('Crear una nueva nota', ({ I }) => {
    // Al abrir se necesita iniciar sesion
    // Inicia sesion de test
    I.amOnPage('/accounts/login/');
    I.fillField("input#id_username", 'cuenta_test');
    I.fillField("input#id_password", 'Prueba123');
    
    I.waitForElement("button.btn.yellow.black-text", 50);
    I.click("button.btn.yellow.black-text");

    I.waitForNavigation(); // Espera a que se procese el login

    // Crea una Nota
    I.amOnPage('/notes/new');  
    I.fillField("input#id_title", "Mi primera nota");
    I.fillField("textarea#id_body", "Este es el cuerpo de la nota.");    
    I.waitForElement("button.btn.yellow.black-text", 5);
    I.click("button.btn.yellow.black-text");

    // Ver Notas
    I.amOnPage('/notes'); 
    I.wait(5); 
});
