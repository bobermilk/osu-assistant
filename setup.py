import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI"
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="osu! assistant",
    version="0.1",
    description="beatmap aggregator",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
