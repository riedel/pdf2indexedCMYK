# pdf2indexedCMYK
Simple conversion of a RGB pdf into an indexed CMYK pdf

      ./pdf2indexedCMYK input.pdf colors.yaml output.pdf

Currently requires PDFtk, ghostscript, pyYAML, numpy 

Works for common PDFs and allows control of output color space (3 dimensions to 4 dimensions). Replaces RGB colors with a CMYK value based on its nearest neighbour in the RGB color space.

Uses a dictionary to translate RGB values in order to allow manually "specify" a simple color profile.

Useful for keeping common CMYK values for printing while having only RGB capable vector graphics tools (like Powerpoint, Inkscape, ...). 

NOTES:
* Does not work with Images
* The YAML Syntax for the colors is not correct but functional

BUGS/IMPROVEMENTS:
* Does not yet replace complex lineart correctly (TODO:correct regexp)
* Break PDF Stream a bit

Copyright Till Riedel 2017, licenced under MIT Licence
