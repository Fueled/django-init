var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: path.join(__dirname, '/js/main'), // entry point of our app. assets/js/main.js should require other js modules and dependencies it needs

  output: {
    path: path.resolve(path.join(__dirname, './dist/assets/')),
    filename: '[name]-[hash].js',
  },

  plugins: [
  ], // add all common plugins here

  module: {
    loaders: [
      {
          test: /\.css$/,
          loader: 'style-loader!css-loader!postcss-loader'
      },
      {
          test: /\.sass/,
          loader: 'style-loader!css-loader!postcss-loader!sass-loader?outputStyle=expanded&indentedSyntax'
      },
      {
          test: /\.scss/,
          loader: 'style-loader!css-loader!postcss-loader!sass-loader?outputStyle=expanded'
      }
      {
          test: /\.(png|jpg|gif|woff|woff2|eot|ttf|svg)$/,
          loader: 'url-loader?limit=8192'
      },
      {
          test: /\.(mp4|ogg|svg)$/,
          loader: 'file-loader'
      },
    ] // add all common loaders here
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}
