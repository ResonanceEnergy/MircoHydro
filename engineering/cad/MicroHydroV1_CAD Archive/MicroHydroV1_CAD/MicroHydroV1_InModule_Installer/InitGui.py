# MicroHydroV1 Add-on GUI — in-module resources (QA/Drawings/CFD inside MicroHydroV1)
import os, sys

def _find_module_base():
    try:
        origin = __spec__.origin  # type: ignore
        if origin and os.path.exists(origin):
            return os.path.dirname(os.path.abspath(origin))
    except Exception:
        pass
    mod = sys.modules.get(__name__)
    if mod:
        f = getattr(mod, '__file__', None)
        if f and os.path.exists(f):
            return os.path.dirname(os.path.abspath(f))
    guess = "/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1"
    if os.path.exists(guess):
        return guess
    return os.getcwd()

_BASE  = _find_module_base()
_ICONS = os.path.join(_BASE, 'icons')
_MACROS= os.path.join(_BASE, 'macros')
_QA    = os.path.join(_BASE, 'QA')
_DRAW  = os.path.join(_BASE, 'Drawings')
_CFD   = os.path.join(_BASE, 'CFD')

# --- Startup self-test ---
print('[MHV1][InitGui] Base:', _BASE)
for label, path in (
    ('ICONS', _ICONS),
    ('MACROS', _MACROS),
    ('QA', _QA),
    ('DRAWINGS', _DRAW),
    ('CFD', _CFD),
):
    print(f"[MHV1][SELF-TEST] {label}: {'OK' if os.path.exists(path) else 'FAIL'} — {path}")


def _exec_macro(relpath):
    path = os.path.normpath(os.path.join(_MACROS, relpath))
    if not os.path.exists(path):
        print('[MHV1][ERROR] Macro missing:', path)
        return
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    exec(compile(code, path, 'exec'), {})

class _MHV1_Cmd_GenerateAll:
    def GetResources(self):
        return {'Pixmap': os.path.join(_ICONS,'mhv1_generate.svg'),'MenuText':'Generate All Parts','ToolTip':'Run MicroHydroV1 build_all macro'}
    def IsActive(self): return True
    def Activated(self): _exec_macro('build_all.FCMacro')

class _MHV1_Cmd_ExportAll:
    def GetResources(self):
        return {'Pixmap': os.path.join(_ICONS,'mhv1_export.svg'),'MenuText':'Export ALL CAD','ToolTip':'Export STEP/STL/IGES/BREP for all parts'}
    def IsActive(self): return True
    def Activated(self): _exec_macro(os.path.join('scripts','export_all_formats.FCMacro'))

class _MHV1_Cmd_RunQA:
    def GetResources(self):
        return {'Pixmap': os.path.join(_ICONS,'mhv1_qa.svg'),'MenuText':'Run QA Suite','ToolTip':'Geometry QA checks'}
    def IsActive(self): return True
    def Activated(self):
        qa = os.path.join(_QA,'run_qa_suite.FCMacro')
        if not os.path.exists(qa):
            print('[MHV1][ERROR] QA macro not found:', qa); return
        with open(qa,'r',encoding='utf-8') as f: code=f.read()
        exec(compile(code, qa, 'exec'), {})

class _MHV1_Cmd_GenDrawings:
    def GetResources(self):
        return {'Pixmap': os.path.join(_ICONS,'mhv1_drawings.svg'),'MenuText':'Generate Drawings','ToolTip':'TechDraw → PDF/SVG'}
    def IsActive(self): return True
    def Activated(self):
        dm = os.path.join(_DRAW,'generate_drawings.FCMacro')
        if not os.path.exists(dm):
            print('[MHV1][ERROR] Drawings macro not found:', dm); return
        with open(dm,'r',encoding='utf-8') as f: code=f.read()
        exec(compile(code, dm, 'exec'), {})

class _MHV1_Cmd_ExportCFD:
    def GetResources(self):
        return {'Pixmap': os.path.join(_ICONS,'mhv1_cfd.svg'),'MenuText':'Export CFD Mesh','ToolTip':'Export STL + STEP for UNV/MED'}
    def IsActive(self): return True
    def Activated(self):
        cm = os.path.join(_CFD,'export_cfd_mesh.FCMacro')
        if not os.path.exists(cm):
            print('[MHV1][ERROR] CFD macro not found:', cm); return
        with open(cm,'r',encoding='utf-8') as f: code=f.read()
        exec(compile(code, cm, 'exec'), {})


def Initialize():
    print('[MHV1] Registering GUI commands ...')
    import FreeCADGui as Gui
    Gui.addCommand('MHV1_GenerateAll', _MHV1_Cmd_GenerateAll())
    Gui.addCommand('MHV1_ExportAll',   _MHV1_Cmd_ExportAll())
    Gui.addCommand('MHV1_RunQA',       _MHV1_Cmd_RunQA())
    Gui.addCommand('MHV1_GenDrawings', _MHV1_Cmd_GenDrawings())
    Gui.addCommand('MHV1_ExportCFD',   _MHV1_Cmd_ExportCFD())
    print('[MHV1] Commands registered.')

def Activated(): pass

def Deactivated(): pass
