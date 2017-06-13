/* global require */

var gulp = require("gulp");
var util = require("gulp-util");
var sourcemaps = require("gulp-sourcemaps");

// CSS processors
var less = require("gulp-less");

// Post CSS transformations
var postcss = require("gulp-postcss");
var atImport = require("postcss-import");
var autoprefixer = require("autoprefixer");
var cssnano = require("cssnano");


gulp.task("less", function() {
    "use strict";

    var processors = [
        atImport(),
        autoprefixer(),
    ];

    if (util.env.production === true) {
        processors.push(cssnano());
    }

    return gulp.src(["./blanc_admin_theme/static/admin/css/*.less"])
        .pipe(sourcemaps.init())
        .pipe(less())
        .pipe(postcss(processors))
        .pipe(sourcemaps.write("."))
        .pipe(gulp.dest("./blanc_admin_theme/static/admin/css"));
});

gulp.task("default", ["less"]);

gulp.task("serve", ["default"], function() {
    "use strict";

    gulp.watch("./static/less/**/*", ["less"]);
});
