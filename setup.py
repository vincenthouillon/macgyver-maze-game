import sys
from cx_Freeze import setup, Executable

# <added>
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# </added>

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('macgyver_maze_game.py', base=base)
]

# <added>
options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "includes",
         ],
        'packages':[
            "pygame",
            "random"
        ]
    },
}
# </added>

setup(name = 'MacGyverMaze',
      version = '1.1',
      description = 'Help macgyver to escape',
      url = 'https://github.com/vincenthouillon/macgyver-maze-game',
      # <added>
      options = options,
      # </added>
      executables = executables
      )