/*eslint no-console:0 */
'use strict';
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.dev.config');

var port = 3000

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

  console.log('Listening at http://localhost:${port}')
});
