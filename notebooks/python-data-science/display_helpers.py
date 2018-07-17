#!/usr/bin/env python

from IPython.display import display, Markdown, Math, Latex
from cycler import cycler
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import string

def head(exp):
    display(Markdown("### " + exp))

def subhead(exp):
    display(Markdown("#### " + exp))

def desc(exp):
    display(Markdown("*" + exp + "*"))

def pycode(exp, description=None):
    display(Markdown("```python\n" + exp + "```"))
    if description is not None:
        display(Markdown("*" + description + "*"))
    #display( eval(exp) )
    print("")
    print("")

def print_matrix(nd, format_str="{:.2f}", max_vertex_row=6, font_size="small"):
    s = "{\\" + font_size + "  \n\\begin{bmatrix}\n" 
    for ir, r in enumerate(nd):
        try:
            for ic, c in enumerate(r):
                s += str(c) if nd.dtype.name[0:3]=='int' else format_str.format(c)
                if ic < len(r)-1:
                    s += "& "
            s += "\\\\\n"
        except TypeError:
            if ir>0 and ir % max_vertex_row == 0:
                 s += "	…\\\\\n" 
            s += str(r) if nd.dtype.name[0:3]=='int' else format_str.format(r)
            if ir < len(nd)-1:
                s += "& "
    s += "\n\\end{bmatrix}\n}"
    display(Math( s ))
    
def print_table(array):

    """ Input: Python list with rows of table as lists
               First element as header. 
        Output: String to put into a .md file 
        
    Ex Input: 
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]] 
    """


    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"

    display( Markdown( markdown + "\n" ))

def ndarray_props(a, typename=None):
    descriptions = {
        'base': 'Base class',
        'data': 'Mem location',
        'dtype': 'Element datatype',
        'itemsize': 'Item size',
        'ndim': '# Dimensions',
        'nbytes': '# Bytes',
        'newbyteorder': 'New byte order',
        'shape': 'Shape',
        'size': 'Size',
        'strides': 'Strides'
    }
    if typename == None:
        typename = a.dtype

    subhead(f'NDArray properties for {typename}')
    table = [[v, f'arr.{k}', f'{ getattr(a, k) }'] for k,v in descriptions.items()]
    table.insert(0, ['Description', 'Property', 'Value'])
    print_table(table)

def ndarray_flags(a):
    subhead('NDArray flags')
    flag_Table = [r.split(':') for r in str(a.flags).split('\n')]
    flag_Table.insert(0, ['Flag', 'Value'])
    print_table( flag_Table )
    
def lb():
    display(Markdown("----"))

def configure_plot(xlim, ylim, figsize=(12, 8), subplots=1, colors=['teal', 'seagreen', 'blue', 'limegreen', 'royalblue', 'deepskyblue', 'slateblue'] ):
    fig = plt.figure(figsize=figsize)
    plt.rc('axes', prop_cycle=(cycler('color', colors)))
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    if (subplots==1):
        return plt
    elif (subplots==2):
        p1 = configure_subplot(fig.add_subplot(1,2,1))
        p2 = configure_subplot(fig.add_subplot(1,2,2))
        return p1, p2

def configure_subplot(sp):
    sp.grid(True, which='both', color='lavender')
    sp.axhline(y=0, color='lightsteelblue')
    sp.axvline(x=0, color='lightsteelblue')
    return sp

def print_eq(*args):
    formated_lines = [l[0].format(*[sp.latex(a) for a in l[1:]]) for l in args]
    s = '\\begin{equation}\n'
    s += '\\begin{split}\n'
    s += ' \\\\\n'.join(formated_lines) + ' \\\\\n'
    s += '\\end{split}\n'
    s += '\\end{equation}'
    display(Math(s))