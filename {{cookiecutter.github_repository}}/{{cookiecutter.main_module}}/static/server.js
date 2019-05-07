/*eslint no-console:0 */

'use strict';
var path = require("path")
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config');
var port = 3000

// Use webpack dev server
config.entry = [
  'webpack-dev-server/client?http://localhost:3000',
  'webpack/hot/only-dev-server',
  path.join(__dirname, '/js/main'),
],

// override django's STATIC_URL for webpack bundles
config.output.publicPath = 'http://localhost:3000/bundles/'

// Add HotModuleReplacementPlugin and BundleTracker plugins
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
])


new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    historyApiFallback: true,
    headers: { 'Access-Control-Allow-Origin': '*' }
}).listen(port, 'localhost', function (err, result) {
  if (err) {
    console.log(err)
  }

  console.log('Listening at http://localhost:' + port)
});
