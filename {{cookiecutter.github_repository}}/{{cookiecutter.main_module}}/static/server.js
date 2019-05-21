const path = require("path");
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config');

const host = 'localhost'
const port = 3000

// Use webpack dev server
config.entry = [
  `webpack-dev-server/client?http://${host}:${port}`,
  'webpack/hot/only-dev-server',
  path.join(__dirname, '/js/main'),
],

// override django's STATIC_URL for webpack bundles
config.output.publicPath = `http://${host}:${port}/bundles/`

// Add HotModuleReplacementPlugin and BundleTracker plugins
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
])


new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    host: host,
    port: port,
    headers: { 'Access-Control-Allow-Origin': '*' }
}).listen(port, host, function (err, result) {
  if (err) {
    console.log(err)
  }
  console.log(`Listening at http://${host}:${port}`)
});
