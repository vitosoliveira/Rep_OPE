
var gulp = require('gulp');
var sass = require('gulp-sass');
 
sass.compiler = require('node-sass');

gulp.task('default', watch);

gulp.task('sass', compilaSass);


function compilaSass(){
    return gulp
        .src("src/*.sass")
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(gulp.dest('static/css'));

    }

function watch(){
    gulp.watch('src/*.sass',compilaSass);
}


