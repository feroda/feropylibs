# -*- encoding: utf-8 -*-

# Copyright (C) 2011 Luca Ferroni <https://github.com/feroda>
#
# This file is part of feropylibs: "Luca Ferroni Python libs"
# feropylibs is free software: you can redistribute it and/or modify
# it under the terms of the MIT License
#
# feropylibs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.

import re

class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()


def load_symbol(path):

    # Split path in 'module' and 'class'
    path = str(path) # avoid unicode
    i = path.rfind('.')
    module, attr = path[:i], path[i + 1:]

    #print ("loading " + module + " attr: " + attr)
    # Load module (dlopen())
    try:
        mod = __import__(module, {}, {}, [attr])
    except ImportError, e:
        raise Exception('Error importing handler %s: "%s"' % (module, e))
    except ValueError, e:
        raise Exception('Error importing handler! Invalid Value')

    # get symbol (dlsym())
    try:
        symbol = getattr(mod, attr)
    except AttributeError:
        raise Exception('Module "%s" does not define a "%s" table! ' % (module, attr))

    return symbol

#------------------------------------------------------------------------------
# Uniq functions from http://www.peterbe.com/plog/uniqifiers-benchmark
#

def unordered_uniq(seq): #Peter Bengtsson
    # Not order preserving
    return list(set(seq))

def ordered_uniq(seq): # Dave Kirby
    # Order preserving
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]


#Is it provided by default python lib?
# def mkpath(path):
#    current_dir = ''
#    for dir_name in path.split('/'):
#        current_dir = current_dir + "/" + dir_name
#        if not os.path.exists(current_dir):
#            os.mkdir(current_dir, 0755)

def get_params_from_template(tmpl):

    # split python template
    expr = r"%\((.*?)\)"
    r = re.compile(expr)
    # find attributes
    attr_names = r.findall(tmpl)
    return attr_names

