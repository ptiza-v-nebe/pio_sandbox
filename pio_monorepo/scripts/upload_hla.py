Import("env")

PIOENV = env.subst("$PIOENV")
print("Starting upload_hla.py from env: ", PIOENV)

#hla_serial = env.GetProjectOption("custom_hla_serial", None)
#print("hla_serial: ", hla_serial)
#env.Append(
#    UPLOADERFLAGS=["-c", f"hla_serial {hla_serial}"]
#)

f_index = env.get("UPLOADERFLAGS", []).index("-c")
hla_serial = env.GetProjectOption("custom_hla_serial", None)
print("hla_serial: ", hla_serial)
if f_index > 0 and hla_serial:
    env["UPLOADERFLAGS"].insert(f_index, ["-c", f"hla_serial {hla_serial}"])