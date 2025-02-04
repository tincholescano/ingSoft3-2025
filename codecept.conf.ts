import { setHeadlessWhen, setCommonPlugins } from '@codeceptjs/configure';
// turn on headless mode when running with HEADLESS=true environment variable
// export HEADLESS=true && npx codeceptjs run
setHeadlessWhen(process.env.HEADLESS);

// enable all common plugins https://github.com/codeceptjs/configure#setcommonplugins
setCommonPlugins();

export const config: CodeceptJS.MainConfig = {
  tests: './notes/tests/*_test.js',  // Ruta donde están los tests
  output: './notes/tests/',
  helpers: {
    Puppeteer: {
      url: 'http://localhost:8000',
      show: true,
      windowSize: '1920x1080'
    }
  },
  include: {
    I: './steps_file'
  },
  name: 'Ingenieria de Software 3 - Final 2025'
}