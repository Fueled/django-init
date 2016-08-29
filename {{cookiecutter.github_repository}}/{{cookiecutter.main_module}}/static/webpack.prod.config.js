var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

var config = require('./webpack.base.config.js')

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats.json'}),

  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    'process.env': {
    'NODE_ENV': JSON.stringify('production')
  }}),

  // keeps hashes consistent between compilations
  new webpack.optimize.OccurenceOrderPlugin(),

  // minifies your code
  new webpack.optimize.UglifyJsPlugin({compressor: {warnings: false }}),

  new ExtractTextPlugin('[name]-[hash].css', {allChunks: true})
])

// Add a loader for JS files
config.module.loaders.push(
  { test: /\.css$/,  loader: ExtractTextPlugin.extract('style-loader', 'css-loader!postcss-loader')},
  { test: /\.scss$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader!postcss-loader!sass-loader") },
  { test: /\.js?$/, exclude: /node_modules/, loader: 'babel-loader'}
)

module.exports = config
