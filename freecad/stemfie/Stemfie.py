import FreeCAD
import FreeCADGui

import os
import random
from freecad.stemfie import ICONPATH, Piezas, Plates

QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP


class ViewProvider:
    def __init__(self, obj):
        obj.Proxy = self

    def getIcon(self):
        return os.path.join(ICONPATH, "STEMFIE.svg")


class BaseCommand:
    """Make commands unavailable when there is no active document"""

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True


# Brazos
class STR_STD_ERR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_ERR")
        Piezas.STR_STD_ERR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD ERR_icon.png"),
            "MenuText": "STR STD ERR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_ERR", "Brace - Straight - Standard - End Round Round"
            ),
        }


class STR_STD_BRD_AZ(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_BRD_AZ")
        # myObj = FreeCAD.ActiveDocument.addObject("Part::Refine","STR_STD_BRD_AZ")
        Piezas.STR_STD_BRD_AZ(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD BRD AZ_icon.png"),
            "MenuText": "STR STD BRD AZ",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_BRD_AZ", "Brace - Straight - Standard - Barbed -  AZ"
            ),  # FIXME: What does it mean "AZ"
        }


class CRN_ERR_ASYM(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "CRN_ERR_ASYM")
        Piezas.CRN_ERR_ASYM(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace CRN ERR ASYM_icon.png"),
            "MenuText": "CRN ERR ASYM",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_CRN_ERR_ASYM", "Brace - Corner - End Round Round - Asymmetric"
            ),
        }


class STR_STD_BRM_AY(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_BRM_AY")
        Piezas.STR_STD_BRM_AY(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD BRM AY_icon.png"),
            "MenuText": "STR STD BRM_AY",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_BRM_AY", "Brace - Straight - Standard -  BRM_AY"
            ),
        }  # FIXME: BRM_AY?


class STR_SLT_BE_SYM_ERR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_SLT_BE_SYM_ERR")
        Piezas.STR_SLT_BE_SYM_ERR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR SLT BE SYM ERR_icon.png"),
            "MenuText": "STR SLT BE SYM ERR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_SLT_BE_SYM_ERR",
                "Brace - Standard - Slotted - Both Ends - Symmetric - End Round Round",
            ),
        }


class STR_SLT_CNT_ERR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_SLT_CNT_ERR")
        Piezas.STR_SLT_CNT_ERR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR SLT CNT ERR_icon.png"),
            "MenuText": "STR SLT CNT ERR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_SLT_CNT_ERR",
                "Brace - Straight - Slotted - Centered - End Round Round",
            ),
        }


class STR_SLT_FL_ERR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_SLT_FL_ERR")
        Piezas.STR_SLT_FL_ERR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR SLT FL ERR_icon.png"),
            "MenuText": "STR SLT FL ERR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_SLT_FL_ERR",
                "Brace - Straight - Slotted - Full Length - End Round Round",
            ),
        }


class STR_SLT_SE_ERR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_SLT_SE_ERR")
        Piezas.STR_SLT_SE_ERR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR SLT SE ERR_icon.png"),
            "MenuText": "STR SLT SE ERR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_SLT_SE_ERR",
                "Brace - Straight - Slotted - Single End - End Round Round",
            ),
        }


class STR_STD_BRD_AY(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_BRD_AY")
        Piezas.STR_STD_BRD_AY(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD BRD AY_icon.png"),
            "MenuText": "STR STD BRD AY",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_BRD_AY", "Brace - Straight - Standard - Barbed - AY"
            ),  # FIXME: AY?
        }


class STR_STD_BRT_AZ(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_BRT_AZ")
        Piezas.STR_STD_BRT_AZ(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD BRT AZ_icon.png"),
            "MenuText": "STR STD BRT AZ",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_BRT_AZ", "Brace Straight - Standard - BRT AZ"
            ),  # FIXME: BRT AZ?
        }


class STR_STD_BRT_AY(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_BRT_AY")
        Piezas.STR_STD_BRT_AY(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD BRT AY_icon.png"),
            "MenuText": "STR STD BRT AY",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_BRT_AY", "Brace - Straight - Standard - BRT AY"
            ),  # FIXME: RT AY?
        }


class STR_STD_CR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_STD_CR")
        Piezas.STR_STD_CR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Brace STR STD CR_icon.png"),
            "MenuText": "STR STD CR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Brace_STR_STD_CR", "Brace - Straight - Standard - CR"
            ),  # FIXME: CR? maybe CRN?
        }


# Plates
class PLT_TRI(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "PLT_TRI")
        Plates.PLT_TRI(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Plate_TRI.svg"),
            "MenuText": "PLT TRI",
            "ToolTip": QT_TRANSLATE_NOOP("STEMFIE_Plate_TRI_PLT", "Plate - Triangular"),
        }


class PLT_SQR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "PLT_SQR")
        Plates.PLT_SQR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Plate_SQR.svg"),
            "MenuText": "PLT SQR",
            "ToolTip": QT_TRANSLATE_NOOP("STEMFIE_Plate_SQR", "Plate - Square"),
        }


class PLT_HEX(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "PLT_HEX")
        Plates.PLT_HEX(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Plate_HEX.svg"),
            "MenuText": "PLT HEX",
            "ToolTip": QT_TRANSLATE_NOOP("STEMFIE_Plate_HEX", "Plate - Hexagonal"),
        }


# Vigas
class STR_ESS(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_ESS")
        Piezas.STR_ESS(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR ESS_icon.png"),
            "MenuText": "STR ESS",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_STR_ESS", "Beam - Straight - Ending Square Square"
            ),
        }


class STR_ERR(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_ERR")
        Piezas.STR_ERR(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR ERR_icon.png"),
            "MenuText": "STR ERR",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_STR_ERR", "Beam - Straight - End Round Round"
            ),
        }


class STR_BEM(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_BEM")
        Piezas.STR_BEM(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR BEM_icon.png"),
            "MenuText": "STR BEM",
            "ToolTip": QT_TRANSLATE_NOOP("STEMFIE_Beam_STR_BEM", "Beam - Straight"),
        }


class AGD_ESS_USH_SYM(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "AGD_ESS_USH_SYM")
        Piezas.AGD_ESS_USH_SYM(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam AGD ESS USH SYM_icon.png"),
            "MenuText": "AGD ESS USH SYM",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_AGD_ESS_USH_SYM",
                "Beam - Angled - End Square Aquare - U-shaped - Symmetric",
            ),
        }


class STR_BED(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_BED")
        Piezas.STR_BED(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR BED_icon.png"),
            "MenuText": "STR BED",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_STR_BED", "Beam - Straight - BED"
            ),  # FIXME: BED?
        }


class STR_BET(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_BET")
        Piezas.STR_BET(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR BET_icon.png"),
            "MenuText": "STR BET",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_STR_BET", "Beam - Straight - BET"
            ),  # FIXME: BET?
        }


class STR_BXS_ESS_H(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_BXS_ESS_H")
        Piezas.STR_BXS_ESS_H(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR BXS ESS H_icon.png"),
            "MenuText": "STR BXS ESS H",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_STR_BXS_ESS_H",
                "Beam - Straight - Box-section - End Square Square - H",
            ),  # FIXME: H?
        }


class STR_BXS_ESS_C(BaseCommand):
    def Activated(self):
        myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "STR_BXS_ESS_C")
        Piezas.STR_BXS_ESS_C(myObj)
        ViewProvider(myObj.ViewObject)
        myObj.ViewObject.ShapeColor = tuple(random.random() for _ in range(3))

        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Beam STR BXS ESS C_icon.png"),
            "MenuText": "STR BXS ESS C",
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Beam_STR_BXS_ESS_C",
                "Beam - Straight - Box-section - End Square Square - C",
            ),  # FIXME: C?
        }


#  Conectores
class TRH_H_BEM_SFT_1W(BaseCommand):
    NAME = "TRH_H_BEM_SFT_1W"
    FUNCTION = Piezas.TRH_H_BEM_SFT_1W
    pixmap = os.path.join(ICONPATH, "Conector THR H BEM SFT 1W_icon.png")
    menutext = "THR-H BEM SFT 1W"
    tooltip = QT_TRANSLATE_NOOP(
        "STEMFIE_Connector_TRH_H_BEM_SFT_1W",
        "Connector - Throught-Hole - Beam - Shaft - One-way",
    )


class TRH_H_BEM_SFT_2W_180(BaseCommand):
    NAME = "TRH_H_BEM_SFT_2W_180"
    FUNCTION = Piezas.TRH_H_BEM_SFT_2W_180
    pixmap = os.path.join(ICONPATH, "Conector THR H BEM SFT 2W 180_icon.png")
    menutext = "THR-H BEM SFT 2W 180º"
    tooltip = QT_TRANSLATE_NOOP(
        "STEMFIE_Connector_TRH_H_BEM_SFT_2W_180",
        "Connector - Throught-Hole - Beam - Shaft - Two-way - 180º",
    )


class TRH_H_BEM_SFT_2W_90(BaseCommand):
    NAME = "TRH_H_BEM_SFT_2W_90"
    FUNCTION = Piezas.TRH_H_BEM_SFT_2W_90
    pixmap = os.path.join(ICONPATH, "Conector THR H BEM SFT 2W 90_icon.png")
    menutext = "THR-H BEM SFT 2W 90º"
    tooltip = QT_TRANSLATE_NOOP(
        "STEMFIE_Connector_TRH_H_BEM_SFT_2W_90",
        "Connector - Throught-Hole - Beam - Shaft - Two-way - 90º",
    )


class TRH_H_BEM_SFT_3W(BaseCommand):
    NAME = "TRH_H_BEM_SFT_3W"
    FUNCTION = Piezas.TRH_H_BEM_SFT_3W
    pixmap = os.path.join(ICONPATH, "Conector THR H BEM SFT 3W_icon.png")
    menutext = "THR-H BEM SFT 3W"
    tooltip = QT_TRANSLATE_NOOP(
        "STEMFIE_Connector_TRH_H_BEM_SFT_3W",
        "Connector - Throught-Hole - Beam - Shaft - Three-way",
    )  # FIXME: H?


class TRH_H_BEM_SFT_4W(BaseCommand):
    NAME = "TRH_H_BEM_SFT_4W"
    FUNCTION = Piezas.TRH_H_BEM_SFT_4W
    pixmap = os.path.join(ICONPATH, "Conector THR H BEM SFT 4W_icon.png")
    menutext = "THR-H BEM SFT 4W"
    tooltip = QT_TRANSLATE_NOOP(
        "STEMFIE_Connector_TRH_H_BEM_SFT_4W",
        "Connector - Throught-Hole - Beam - Shaft - Four-way",
    )


#  Comandos
class Cmd_Listado(BaseCommand):
    def Activated(self):
        from freecad.stemfie import Comandos

        Comandos.ListadoPiezas()

    def GetResources(self):
        return {
            "Pixmap": os.path.join(ICONPATH, "Cmd_Listado_icon.png"),
            "MenuText": QT_TRANSLATE_NOOP("STEMFIE_Cmd_Listado", "Part list"),
            "ToolTip": QT_TRANSLATE_NOOP(
                "STEMFIE_Cmd_Listado", "Print a list of the STEMFIE parts on the tree"
            ),
        }


# Brazos
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_ERR", STR_STD_ERR())
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_BRD_AZ", STR_STD_BRD_AZ())
FreeCADGui.addCommand("STEMFIE_Brace_CRN_ERR_ASYM", CRN_ERR_ASYM())
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_BRM_AY", STR_STD_BRM_AY())
FreeCADGui.addCommand("STEMFIE_Brace_STR_SLT_BE_SYM_ERR", STR_SLT_BE_SYM_ERR())
FreeCADGui.addCommand("STEMFIE_Brace_STR_SLT_CNT_ERR", STR_SLT_CNT_ERR())
FreeCADGui.addCommand("STEMFIE_Brace_STR_SLT_FL_ERR", STR_SLT_FL_ERR())
FreeCADGui.addCommand("STEMFIE_Brace_STR_SLT_SE_ERR", STR_SLT_SE_ERR())
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_BRD_AY", STR_STD_BRD_AY())
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_BRT_AZ", STR_STD_BRT_AZ())
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_BRT_AY", STR_STD_BRT_AY())
FreeCADGui.addCommand("STEMFIE_Brace_STR_STD_CR", STR_STD_CR())
# Vigas
FreeCADGui.addCommand("STEMFIE_Beam_STR_ESS", STR_ESS())
FreeCADGui.addCommand("STEMFIE_Beam_STR_ERR", STR_ERR())
FreeCADGui.addCommand("STEMFIE_Beam_STR_BEM", STR_BEM())
FreeCADGui.addCommand("STEMFIE_Beam_AGD_ESS_USH_SYM", AGD_ESS_USH_SYM())
FreeCADGui.addCommand("STEMFIE_Beam_STR_BED", STR_BED())
FreeCADGui.addCommand("STEMFIE_Beam_STR_BET", STR_BET())
FreeCADGui.addCommand("STEMFIE_Beam_STR_BXS_ESS_H", STR_BXS_ESS_H())
FreeCADGui.addCommand("STEMFIE_Beam_STR_BXS_ESS_C", STR_BXS_ESS_C())
# Plates
FreeCADGui.addCommand("STEMFIE_Plate_TRI", PLT_TRI())
FreeCADGui.addCommand("STEMFIE_Plate_SQR", PLT_SQR())
FreeCADGui.addCommand("STEMFIE_Plate_HEX", PLT_HEX())
# Conectores
FreeCADGui.addCommand("STEMFIE_Connector_TRH-H_BEM_SFT_1W", TRH_H_BEM_SFT_1W())
FreeCADGui.addCommand("STEMFIE_Connector_TRH-H_BEM_SFT_2W_180", TRH_H_BEM_SFT_2W_180())
FreeCADGui.addCommand("STEMFIE_Connector_TRH-H_BEM_SFT_2W_90", TRH_H_BEM_SFT_2W_90())
FreeCADGui.addCommand("STEMFIE_Connector_TRH-H_BEM_SFT_3W", TRH_H_BEM_SFT_3W())
FreeCADGui.addCommand("STEMFIE_Connector_TRH-H_BEM_SFT_4W", TRH_H_BEM_SFT_4W())
# Comandos
FreeCADGui.addCommand("STEMFIE_Cmd_Listado", Cmd_Listado())


Icon = os.path.join(ICONPATH, "STEMFIE.svg")
