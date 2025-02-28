const { setHeadlessWhen, setCommonPlugins } = require('@codeceptjs/configure');
// turn on headless mode when running with HEADLESS=true environment variable
// export HEADLESS=true && npx codeceptjs run
setHeadlessWhen(process.env.HEADLESS);

// enable all common plugins https://github.com/codeceptjs/configure#setcommonplugins
setCommonPlugins();

/** @type {CodeceptJS.MainConfig} */
exports.config = {
  tests: './test/*.js',
  output: './test/output',
  helpers: {
    Playwright: {
      browser: 'chromium',
      url: 'https://gc-django-app-340020449796.us-central1.run.app/notes/',
      show: true
    }
  },
  include: {
    I: './steps_file.js'
  },
  name: 'ingSoft3-2025'
}