from konwerter.KonwerterMagazynSklepSalus import KonwerterMagazynSklepSalus

class ExportButtonFN:
    #def __init__(self, export_path):

    def pushed_released(self,export_path, paths):
        KonwerterMagazynSklepSalus(export_path, paths).konwertuj()



