
var gulp = require('gulp');
var sass = require('gulp-sass');
 
sass.compiler = require('node-sass');

gulp.task('sass', compilaSass);
 
function compilaSass(){
    return gulp
        .src('src/*.sass')
        .pipe(sass())
        .pipe(gulp.dest('static/css'));
}