
Import("env")

PIOENV = env.subst("$PIOENV")
#print("Starting extra_script.py from env: ", PIOENV)

PROJECT_INCLUDE_DIR = env.subst("$PROJECT_INCLUDE_DIR")
#print(PROJECT_INCLUDE_DIR)
env.Append(
    CPPPATH=[PROJECT_INCLUDE_DIR]
)