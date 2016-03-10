#!/usr/bin/env python
#-*-coding:utf-8-*-

from jinja2 import Environment,FileSystemLoader
from glob import glob
import sys
import os 
import re
import pdb
import argparse

def recur_include(directory,extension,load_files):
        files = [factor for factor in glob(directory+'/*'+ extension) ]
        directories = [os.path.join(directory,factor) for factor in os.listdir(directory) if os.path.isdir(os.path.join(directory,factor)) ]
        #pdb.set_trace()
        load_files.extend(files)
        if len(directories) > 0 :
            for x in directories:
                recur_include(x,extension,load_files)
        return load_files
        
#def priority_sort(file_path,priorty_target) :
#    file_path


def main():
        #parser = argparse.ArgumentParser(description='Template generator for html with all include js and css you want to choose.')
        #parser.add_argument('-j','--javascript',action='append', nargs='+',help='an integer for the accumulator')
        #parser.add_argument('-c','--css', dest='accumulate', action='store_const',nargs ='?',help='sum the integers (default: find the max)')
        #args = parser.parse_args()
        #print args.accumulate(args.integers)
        js_path = 'js/controls'
        css_path = 'styles'
    
        js_files = recur_include(js_path,'.min.js',[])
        css_files = recur_include(css_path,'.min.css',[])

        env = Environment(loader = FileSystemLoader('./',encoding='utf-8') )
        v = {"js_path" : js_files,"css_path":css_files}
        tmpl = env.get_template('for_js_test.html')
        html = tmpl.render(v).encode('utf-8')
        print html

if __name__ =='__main__':
    main()
