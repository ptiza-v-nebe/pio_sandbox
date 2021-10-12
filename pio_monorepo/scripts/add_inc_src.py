Import("env")
from os import path

PIOENV = env.subst("$PIOENV")
#print("Starting add_inc_src.py from env: ", PIOENV)

PROJECT_SRC_DIR = env.subst("$PROJECT_SRC_DIR")

#add include path
env.Append(
    CPPPATH=[path.join(PROJECT_SRC_DIR, PIOENV, "inc")]
)

#add src path
env.Append(
    SRC_FILTER=["+<"+ PIOENV +">"]
)