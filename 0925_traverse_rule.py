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

def scan(root):
    for p in Path(root).rglob("*.png"):
        tag = classify(p.name)
        print(f"{p}|{tag}")

if __name__ == "__main__":
    scan(r"D:/TA/Assets")