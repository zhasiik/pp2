import os

path = "D:\pp2"

print("exists" if os.access(path, os.F_OK) else "not exist")
print("readable" if os.access(path, os.R_OK) else "not reaable")
print("writable" if os.access(path, os.W_OK) else "not writable")
print("executable" if os.access(path, os.X_OK) else "not executable")