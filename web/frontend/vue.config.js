const path = require('path');

module.exports = {
    publicPath: 'static/dist/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, '../static/dist/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true,
    devServer: {
      devMiddleware: {
        // see https://github.com/webpack/webpack-dev-server/issues/2958
        writeToDisk: true, 
      }
    },
}
/* 
const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
}); */
