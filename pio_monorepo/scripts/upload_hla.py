Import("env")

hla_serial = env.GetProjectOption("custom_hla_serial", None)

env.Append(
    UPLOADERFLAGS=["-c", f"hla_serial {hla_serial}"]
)