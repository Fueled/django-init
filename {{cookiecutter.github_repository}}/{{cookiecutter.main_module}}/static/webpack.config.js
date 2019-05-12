var path = require("path");
var webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

const devMode = process.env.NODE_ENV !== 'production'

module.exports = {
  context: __dirname,
  mode: devMode? 'development': 'production',

  entry: path.join(__dirname, '/js/main'), // entry point of our app. assets/js/main.js should require other js modules and dependencies it needs

  output: {
    path: __dirname + '/dist',
    filename: devMode ? '[name].js' : '[name]-[contenthash].js',
  },

  // https://webpack.js.org/configuration/optimization/
  optimization: {
    minimizer: [new TerserPlugin(), new OptimizeCSSAssetsPlugin({})],
    minimize: !devMode,
    noEmitOnErrors: devMode
  },

  plugins: [
    // new webpack.ProvidePlugin({$: 'jquery', jQuery: 'jquery'}),
    new MiniCssExtractPlugin({
      // Options similar to the same options in webpackOptions.output
      // both options are optional
      filename: devMode ? '[name].css' : '[name]-[contenthash].css',
      chunkFilename: "[id].css"
    }),
    // Creates manifest file to be used by Djnago Server
    new BundleTracker({filename: './webpack-stats.json'})
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
          test: /\.css$/,
          use: [
            devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
            'css-loader'
          ]
      },
      {
          test: /\.sass/,
          use: [
            devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
            'css-loader',
            { loader: 'sass-loader', options: { sourceMap: devMode } }
          ]
      },
      {
          test: /\.scss/,
          use: [
            devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
            { loader: 'css-loader', options: { sourceMap: devMode } },
            { loader: 'sass-loader', options: { sourceMap: devMode } }
          ]
      },
      {
          test: /\.(png|jpg|gif|woff|woff2|eot|ttf|svg)$/,
          use: [
            {loader: 'url-loader', options: {limit: 8192 }}
          ]
      },
      {
          test: /\.(mp4|ogg|svg)$/,
          use: [{
            loader: 'file-loader'
          }]
      },
    ] // add all common loaders here
  },

  resolve: {
    modules: ['node_modules']
  },
}
