import inkex
from applytransform import ApplyTransform  # Assuming ApplyTransform is in a file named applytransform.py

class CleanupSVGAnimation(inkex.Effect):
    def __init__(self):
        super().__init__()

    def effect(self):
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
        apply_transform = ApplyTransform()
        apply_transform.svg = self.svg
        apply_transform.document = self.document
        apply_transform.effect()
        inkex.utils.debug("ApplyTransform executed successfully")

    def remove_empty_groups(self):
        groups = self.document.xpath('//svg:g', namespaces=inkex.NSS)
        if len(groups) == 0:
            return

        for group in groups:
            while len(group.getchildren()) == 0:
                parent = group.getparent()
                parent.remove(group)
                group = parent

    def call_inkscape_command(self, action):
        # Apply the action to the current document
        inkex.command.inkscape(self.svg_file, actions=action)

if __name__ == '__main__':
    CleanupSVGAnimation().run()
