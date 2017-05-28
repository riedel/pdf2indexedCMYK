#!/usr/bin/python3
import sys
import yaml
import os
import subprocess
import numpy as np
import re

with open(sys.argv[2], 'r') as f:
    file_lines = ''.join([''.join(['!!python/tuple ',x, '\n']) for x in f.readlines()])

try:
      colors=yaml.load(file_lines)
except yaml.YAMLError as exc:
        print(exc)

def get_closest_color(c):
    d=[np.linalg.norm(np.asarray(x)-np.asarray(c)) for x in colors.keys()]
    return list(colors.values())[d.index(min(d))]


class Pdf:
    def __init__(self, fin, fout):
        self.f=f
        self.input = subprocess.Popen(["pdftk",fin,"output","-","uncompress"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        self.output = subprocess.Popen(["gs", "-o", fout, "-sDEVICE=pdfwrite", "-sProcessColorModel=DeviceCMYK", "-sColorConversionStrategy=None", "-sColorConversionStrategyForImages=CMYK", "-sDownsampleMonoImages=false ", "-sDownsampleGrayImages=false ", "-sDownsampleColorImages=false ", "-sAutoFilterColorImages=false ", "-sAutoFilterGrayImages=false ", "-sColorImageFilter=/FlateEncode ", "-sGrayImageFilter=/FlateEncode ", "-dAutoRotatePages=/None ", "-"],stdin=subprocess.PIPE)

    def __enter__(self):
        return self

    def read(self):
        return self.input.stdout.readlines()

    def write(self,line):
        return self.output.stdin.write(line)

    def __exit__(self, exc_type, exc_value, traceback):
        self.output.stdin.close()
        return self.output.wait()

replaced_colors={}
with Pdf(sys.argv[1],sys.argv[3]) as pdf:
    for line in pdf.read():
        rgb=re.compile(b'(.* )?([01]\.?[0-9]*) ([01].?[0-9]*) ([01].?[0-9]*) (RG|rg)(\r\n)$')
        match=re.match(rgb,line)
        if match:
            #sys.stderr.buffer.write(line)
            old=(float(match.group(2)),float(match.group(3)),float(match.group(4)))
            c=get_closest_color(old)
            replaced_colors[old]=c
            newcolor=(match.group(1) if match.group(1) else b'') +'{0[0]} {0[1]} {0[2]} {0[3]}'.format(c).encode('UTF-8')
            newcolor+=b' k' if match.group(5)==b'rg' else b' K'
            newcolor+=match.group(6)
            #sys.stderr.buffer.write(newcolor)
            line=re.sub(rgb,newcolor,line)
        pdf.write(line)

print('replaced colors:', file=sys.stderr)

for c in replaced_colors:
        print('{} with {}'.format(c,replaced_colors[c]), file=sys.stderr)
