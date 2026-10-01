from pathlib import Path

def classify(name):
    if name.startswith("T_"):
        return "BaseColor"
    elif name.startswith("N_"):
        return "Normal"
    elif name.startswith("R_"):
        return "Roughness"
    elif name.startswith("M_"):
        return "Metallic"
    else:
        return "未知"

def new_name_for(old_name,tag):
    return f"{tag}_{old_name}"

def rename_file(root):
    for p in Path(root).rglob("*.png"):
        new = new_name_for(p.name,classify(p.name))
        target = p.parent / new
        if target.exists() and target != p:
            target = p.parent / (new.split(".")[0] + "_1.png")
        p.rename(target)
        print(f"{p}->{target}")

if __name__ == "__main__":
    rename_file(f"D:/TA/Assets")