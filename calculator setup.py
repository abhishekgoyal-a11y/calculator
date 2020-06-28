import cx_Freeze
executables = [cx_Freeze.Executable("calculator.py")]

cx_Freeze.setup(
    name="CALCULATOR",
    options={"build_exe": {"packages":["tkinter"],
                            "include_files": ["calculator.ico"]}},
    executables = executables
    )
