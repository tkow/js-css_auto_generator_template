# js-css_auto_generator_template
This script genarates html template simply and speedy
If you want to test trivial code of js/css/html application,
but not so much as to make framework environment,
with no framework except jinja2 and standard python modules,
it enable you to make a trial easiliy with browser only or with  
SimpleHTTPServer(python2) or http.server(python3) modules.

##Usage

Make your directory includes for_js_test.html and template.py ,
your js-files in js/control directory,your css-files in styles,
and run 

python template.py > your_index.html

js and css files are searched for hierarchical directories' path recursivey

and  to watch page for mac,for example with browser application,

open -a "/Applications/Safari.app" your_index.html
open -a "/Applications/Firefox.app" your_index.html
open -a "/Applications/Google Chrome.app" your_index.html

or other way like localhost web server starting.


#future work

・select js and css files included or excluded with flags and argument options with options --include and --exclude
・choose directory or files for js and css with options -j and -c
・add priority check with arguments as dependency between files with option -p.
・add rendering partial template html and choise of template with option -t. 
・genarete many templates sample code like rails' scaffolding with option -g.
・set configuration files like manifest.json to constructure above options and targetfiles automatically.

#License 
FREE.You can use and modify this code freely to fork this to your repository.
