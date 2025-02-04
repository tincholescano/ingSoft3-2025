Feature('Notas');

Scenario('Crear una nueva nota', ({ I }) => {
    I.amOnPage('/accounts/login/');
    I.fillField("input#id_username", 'cuenta_test');
    I.fillField("input#id_password", 'Prueba123');
    
    I.waitForElement("button.btn.white.black-text", 50);
    I.click("button.btn.white.black-text");

    I.waitForNavigation(); // Espera a que se procese el login

    I.amOnPage('/notes/new');  
    I.fillField("input#id_title", "Mi primera nota");
    I.fillField("textarea#id_body", "Este es el cuerpo de la nota.");    
    I.waitForElement("button.btn.white.black-text", 5);
    I.click("button.btn.white.black-text");
});
