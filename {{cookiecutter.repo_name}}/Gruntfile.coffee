module.exports = (grunt) ->
  appConfig = grunt.file.readJSON("package.json")

  # Load grunt tasks automatically
  # see: https://github.com/sindresorhus/load-grunt-tasks
  require("load-grunt-tasks") grunt

  # Time how long tasks take. Can help when optimizing build times
  # see: https://npmjs.org/package/time-grunt
  require("time-grunt") grunt
  pathsConfig = (appName) ->
    @app = appName or appConfig.name
    app: @app
    templates: @app + "/templates"
    css: @app + "/static/css"
    sass: @app + "/static/sass"
    coffee: @app + "/static/coffee"
    fonts: @app + "/static/fonts"
    images: @app + "/static/images"
    js: @app + "/static/js"
    docs: "docs/"
    manageScript: @app + "/manage.py"

  grunt.initConfig
    paths: pathsConfig()
    pkg: appConfig

    # see: https://github.com/gruntjs/grunt-contrib-watch
    watch:
      gruntfile:
        files: ["Gruntfile.coffee"]

      coffee:
        files: ["<%= paths.coffee %>{,*/}*.{coffee,litcoffee,coffee.md}"]
        tasks: ["coffee"]

      compass:
        files: ["<%= paths.sass %>/**/*.{scss,sass}"]
        tasks: ["compass:server"]

      livereload:
        files: [
          "<%= paths.js %>/**/*.js"
          "<%= paths.sass %>/**/*.{scss,sass}"
          "<%= paths.app %>/**/*.html"
          "<%= paths.app %>/**/*.html"
          "<%= paths.docs %>/**/*.md"
        ]
        options:
          spawn: false
          livereload: true


    # Compiles CoffeeScript to JavaScript
    coffee:
      options:
        sourceMap: false
        sourceRoot: ""

      dist:
        files: [
          expand: true
          cwd: "<%= paths.coffee %>"
          src: "{,*/}*.coffee"
          dest: "<%= paths.js %>"
          ext: ".js"
        ]


    # see: https://github.com/gruntjs/grunt-contrib-compass
    compass:
      options:
        sassDir: "<%= paths.sass %>"
        cssDir: "<%= paths.css %>"
        fontsDir: "<%= paths.fonts %>"
        imagesDir: "<%= paths.images %>"
        relativeAssets: false
        assetCacheBuster: false
        raw: "Sass::Script::Number.precision = 10\n"

      dist:
        options:
          environment: "production"

      server:
        options: {}

    # see: https://npmjs.org/package/grunt-bg-shell
    bgShell:
      _defaults:
        bg: true

      runDjango:
        cmd: "fab webserver"

      runDocsServer:
        cmd: "fab serve_docs"

  grunt.registerTask "serve", [
    "bgShell:runDjango"
    "bgShell:runDocsServer"
    "compass"
    "coffee"
    "watch"
  ]
  grunt.registerTask "build", [
    "compass:dist"
    "coffee:dist"
  ]
  grunt.registerTask "default", ["build"]
  return
