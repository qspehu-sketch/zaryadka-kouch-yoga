import json
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

xmind = r"D:\ДИСК Д\03_МОНЕТИЗАЦИЯ\БЛОГ\ФЗ 8 ТИМОЧКО\ЗАПУСК.xmind"
with zipfile.ZipFile(xmind) as z:
    data = json.loads(z.read("content.json"))


def children_of(node):
    ch = node.get("children") or {}
    return ch.get("attached") or []


def walk(node, depth=0, path=None):
    path = path or []
    title = (node.get("title") or "").replace("\n", " ").strip()
    cur = path + [title] if title else path
    yield depth, cur, title
    for child in children_of(node):
        yield from walk(child, depth + 1, cur)


for sheet in data:
    root = sheet["rootTopic"]
    print("\n=== SHEET:", root.get("title"), "===")
    for depth, path, title in walk(root):
        tl = title.lower()
        if "тригг" in tl or "тригер" in tl:
            print("FOUND:", " > ".join(path))
            # print children of this node
            # find node again - skip for now
        if title in ("ТРИГГЕРЫ", "Триггеры", "триггеры"):
            print("EXACT:", path)

# dump top-level branches of ZAPUSK sheet
root = data[0]["rootTopic"]
print("\nTOP BRANCHES:")
for c in children_of(root):
    print("-", c.get("title"))

# find branch containing триггер in any descendant title
def find_branch(node, needle):
    title = (node.get("title") or "").lower()
    if needle in title:
        return node
    for child in children_of(node):
        found = find_branch(child, needle)
        if found:
            return found
    return None

for needle in ["тригг", "тригер"]:
    n = find_branch(root, needle)
    if n:
        print("\nNODE for", needle, ":", n.get("title"))
        for ch in children_of(n):
            t = (ch.get("title") or "").replace("\n", " ")
            print("  *", t[:300])
