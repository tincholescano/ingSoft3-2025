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
      url: 'http://localhost:8000/notes/',
      show: false
    }
  },
  include: {
    I: './steps_file.js'
  },
  name: 'ingSoft3-2025'
}