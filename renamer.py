import os

folder = r"C:\Users\User\Desktop\test"
for i, name in enumerate(os.listdir(folder), 1):
    old = os.path.join(folder, name)
    new = os.path.join(folder, f"{i:03d}_{name}")
    os.rename(old, new)
    print(f"Done: {new}")