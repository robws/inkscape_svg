# inkscape_svg
Inkscape SVG-focused extensions to add arbitrary classes to selected objects, and to "clean up" SVG files as you prepare them for animation.


## Manifest/index

| Filename | Description |
| --- | --- |
| applyclasstoselected.inx |Apply CSS class to selected items in Layers and Objects panel| 
| applyclasstoselected.py || 
| applytransform.inx |Apply Transform plugin (available for cleanup plugin to import)| 
| applytransform.py || 
| cleanup_svg_animation.inx |Run File->Clean Up Document, Path->Object to Path, Apply Transform, and Remove Empty Groups| 
| cleanup_svg_animation.py || 
| LICENSE.txt || 
| meta.json |part of the Remove Empty Groups Plugin| 
| README.md || 
| remove_empty_groups.inx |Remove Empty Groups Plugin, whose functionlity is reproduced in the cleanup_svg_animation.* extension| 
| remove_empty_groups.py || 

## How to install

### Mac, etc
Not yet determined.

### Windows
On Windows, I copied these files to the **User extensions** folder (Preferences->System->User extensions:), which on my machine is `C:\Users\Rob\AppData\Roaming\inkscape\extensions`.

## Attributions

These extensions include and extend both [Mark Riedesel's Apply Transforms](https://github.com/Klowner/inkscape-applytransforms) extension and [FabLab_Chemntiz's remove_empty_groups](https://gitea.fablabchemnitz.de/FabLab_Chemnitz/mightyscape-1.2/src/branch/master/extensions/fablabchemnitz/remove_empty_groups) extensions.



