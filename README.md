# inkscape_svg

Inkscape SVG-focused extensions to add arbitrary classes to selected objects, and to "clean up" SVG files as you prepare them for animation.

## Manifest/index

| Filename                  | Description                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------ |
| applyclasstoselected.inx  | Apply CSS class to selected items in Layers and Objects panel                                          |
| applyclasstoselected.py   |                                                                                                        |
| applytransform.inx        | Apply Transform plugin (available for cleanup plugin to import)                                        |
| applytransform.py         |                                                                                                        |
| cleanup_svg_animation.inx | Run File->Clean Up Document, Path->Object to Path, Apply Transform, and Remove Empty Groups            |
| cleanup_svg_animation.py  |                                                                                                        |
| LICENSE.txt               |                                                                                                        |
| meta.json                 | part of the Remove Empty Groups Plugin                                                                 |
| README.md                 |                                                                                                        |
| remove_empty_groups.inx   | Remove Empty Groups Plugin, whose functionlity is reproduced in the cleanup_svg_animation extension    |
| remove_empty_groups.py    |                                                                                                        |

## How to install

### Mac, etc

Copy cleanup_svg/ folder to your Inkscape user extensions folder.

You can find the location of this folder by going to Inkscape->Settings, and choosing System.
Then, look for the User extensions folder name.


If my Mac username is rhudson20, my folder is at
`/Users/rhudson20/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions`

### Windows

Copy cleanup_svg/ folder to your Inkscape User Extensions folder.

**Note** You may have to create this folder if it doesn't exist.

Check **Preferences->System->User extensions** to confirm the location of this folder.
If my Windows username is Rob, then my folder is at :
`C:\Users\Rob\AppData\Roaming\inkscape\extensions`

## Attributions

These extensions include and extend both [Mark Riedesel's Apply Transforms](https://github.com/Klowner/inkscape-applytransforms) extension and [FabLab_Chemntiz's remove_empty_groups](https://gitea.fablabchemnitz.de/FabLab_Chemnitz/mightyscape-1.2/src/branch/master/extensions/fablabchemnitz/remove_empty_groups) extensions.

Per their respective GP2 licenses, their source has been included in the /compliance folder for your reference.

