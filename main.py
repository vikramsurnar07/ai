import os
import shutil

practicals = [
    ("1A", "Simple Reflex Agent (Vacuum Cleaner World)", "prac1a"),
    ("1B", "BFS Robot Path Planning with Obstacles", "prac1b"),
    ("2A", "Model-Based Intelligent Agent (Grid Navigation & Obstacles)", "prac2a"),
    ("2B", "DFS for Missionaries and Cannibals Problem", "prac2b"),
    ("3A", "A* Search Algorithm for 8-Puzzle Problem", "prac3a"),
    ("3B", "Backtracking Search for 8-Queens Problem", "prac3b"),
    ("4A", "Adversarial Search with Alpha-Beta Pruning", "prac4a"),
    ("4B", "Rule-Based Chatbot with Pattern Matching", "prac4b"),
]

def main():
    print("=" * 65)
    print("            AI PRACTICAL SELECTION MENU")
    print("=" * 65)
    for idx, (pid, topic, short_name) in enumerate(practicals, start=1):
        print(f"[{idx}] {pid:<3} - {topic} ({short_name})")
    print("=" * 65)

    choice = input("\nEnter practical choice (e.g., 1A or 1-8): ").strip().upper()

    selected = None
    for idx, (pid, topic, short_name) in enumerate(practicals, start=1):
        if choice == pid or choice == str(idx):
            selected = (pid, topic, short_name)
            break

    if not selected:
        print("Invalid choice! Exiting.")
        return

    pid, topic, short_name = selected
    print(f"\nSelected: {pid} - {topic}")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(base_dir, short_name)
    os.makedirs(target_dir, exist_ok=True)

    src_code = os.path.join(base_dir, "code", f"{short_name}.py")
    src_txt = os.path.join(base_dir, "txt", f"{short_name}.txt")

    if os.path.exists(src_code):
        shutil.copy(src_code, os.path.join(target_dir, f"{short_name}.py"))
    if os.path.exists(src_txt):
        shutil.copy(src_txt, os.path.join(target_dir, f"{short_name}.txt"))

    code_dir = os.path.join(base_dir, "code")
    txt_dir = os.path.join(base_dir, "txt")

    if os.path.exists(code_dir):
        shutil.rmtree(code_dir)
    if os.path.exists(txt_dir):
        shutil.rmtree(txt_dir)

    main_file = os.path.abspath(__file__)
    if os.path.exists(main_file):
        os.remove(main_file)

    print(f"Created folder '{short_name}' with {short_name}.py and {short_name}.txt.")
    print("Deleted 'code', 'txt', and 'main.py'.")

if __name__ == "__main__":
    main()
