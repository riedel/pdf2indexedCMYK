# pdf2indexedCMYK
Conversion of a RGB pdf into an indexed CMYK pdf

Requires PDFtk and ghostscript

Works for common PDFs and allows control of output color space (3 dimensions to 4 dimensions). Replaces RGB colors with a CMYK value based on its nearest neighbour in the RGB color space.

Uses a dictionary to translate RGB values in order to allow manually "specify" a simple color profile.

Useful for keeping common CMYK values for printing while having only RGB capable vector graphics tools (like Powerpoint, Inkscape, ...). 


BUGS/IMPROVEMENTS:
* Also does not yet replace complex lineart correctly (TODO:correct regexp)
* Break PDF Stream a bit
* Does not work with Images (WONT-FIX)
