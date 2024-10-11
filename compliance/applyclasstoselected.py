import inkex

class ApplyClassToSelected(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--class_name", type=str, dest="class_name", default="")

    def effect(self):
        if not self.svg.selected:
            inkex.errormsg("No objects selected.")
            return
        
        for elem in self.svg.selected.values():
            elem.set('class', self.options.class_name)

if __name__ == '__main__':
    ApplyClassToSelected().run()
