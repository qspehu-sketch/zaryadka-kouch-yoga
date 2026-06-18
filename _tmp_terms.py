import json
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

xmind = r"D:\ДИСК Д\03_МОНЕТИЗАЦИЯ\БЛОГ\ФЗ 8 ТИМОЧКО\ЗАПУСК.xmind"
with zipfile.ZipFile(xmind) as z:
    data = json.loads(z.read("content.json"))


def children_of(node):
    return (node.get("children") or {}).get("attached") or []


def find_by_title(node, target):
    title = (node.get("title") or "").strip()
    if title == target:
        return node
    for child in children_of(node):
        found = find_by_title(child, target)
        if found:
            return found
    return None


def print_subtree(node, depth=0, max_depth=3):
    title = (node.get("title") or "").replace("\n", " ").strip()
    if title:
        print("  " * depth + "- " + (title[:250]))
    if depth >= max_depth:
        return
    for child in children_of(node):
        print_subtree(child, depth + 1, max_depth)

root = data[0]["rootTopic"]
terms = find_by_title(root, "ТЕРМИНЫ")
if terms:
    print("=== ТЕРМИНЫ ===")
    print_subtree(terms, 0, 4)

# search any node whose title is exactly short and contains numbered triggers
for child in children_of(root):
    t = (child.get("title") or "")
    if "ПРОГРЕВ" in t or "прогрев" in t.lower():
        print("\n===", t[:50], "===")
        print_subtree(child, 0, 2)
