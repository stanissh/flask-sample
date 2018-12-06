var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, 'public');
var APP_DIR = path.resolve(__dirname, 'src/js');

var config = {
  entry: APP_DIR + '/index.jsx',
  output: {
    path: BUILD_DIR,
    filename: 'app.js'
  },
  module: {
  	rules: [{
  		test : /\.jsx?/,
      exclude: /node_modules/,
      loader: 'babel-loader'
  	}]
  }
};

module.exports = config;