// in this file you can append custom step methods to 'I' object

module.exports = function() {
  return actor({

    // Define custom steps here, use 'this' to access default methods of I.
    // It is recommended to place a general 'login' function here.
    // in this file you can append custom step methods to 'I' object

    login(username, password) {
      this.amOnPage('http://127.0.0.1:8000/accounts/login/');
        this.fillField('#id_username', username);
        this.fillField('#id_password', password);
        this.pressKey('Enter');
      this.waitForNavigation();
    },
    
  });
}
