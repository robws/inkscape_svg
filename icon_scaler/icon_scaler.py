#!/usr/bin/env python3
#
# License: GPL2
# Copyright Robert Hudson
#
import inkex
from applytransform import ApplyTransform  # Assuming ApplyTransform is in a file named applytransform.py

class CleanupSVGAnimation(inkex.Effect):
    def __init__(self):
        super().__init__()

    def effect(self):
        """ Run a series of actions and custom functions to clean up this document
    
    
        Execute built-in vacuum-defs (remove unused defs) and object-to-path actions
        along with the custom actions defined here (apply all transforms and remove empty groups)
    
        """
        actions = [
            'vacuum-defs',
            'object-to-path'
        ]
        for action in actions:
            try:
                self.call_inkscape_command(action)
                inkex.utils.debug(f"Successfully executed: {action}")
            except Exception as e:
                inkex.utils.debug(f"Failed to execute: {action} with error: {e}")
                break
        
        self.apply_transform()
        self.remove_empty_groups()

    def apply_transform(self):
        """
        Applies transformations to the current SVG document using the ApplyTransform extension.
        """

        apply_transform = ApplyTransform()
        apply_transform.svg = self.svg
        apply_transform.document = self.document
        apply_transform.effect()
        inkex.utils.debug("ApplyTransform executed successfully")

    def remove_empty_groups(self):
        """
        Removes empty group <g> elements from the SVG Document
        """
        groups = self.document.xpath('//svg:g', namespaces=inkex.NSS)
        if len(groups) == 0:
            return

        for group in groups:
            while len(group.getchildren()) == 0:
                parent = group.getparent()
                parent.remove(group)
                group = parent

    def call_inkscape_command(self, action):
        """Calls built-in Inkscape commands to manipulate the current document.

        Args:
            action (str): The action to apply to the current document (e.g., 'vacuum-defs', 'object-to-path').
        """
        inkex.command.inkscape(self.svg_file, actions=action)

if __name__ == '__main__':
    """
      Runs the CleanupSVGAnimation effect on the current SVG document 
      by invoking the inherited run() method from inkex.Effect.
    """
    CleanupSVGAnimation().run()
