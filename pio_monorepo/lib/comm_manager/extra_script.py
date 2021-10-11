
Import("env")
env.Append(
    CPPPATH=[env.subst("$PROJECT_INCLUDE_DIR")]
)