import os
import sys
from datetime import datetime, timezone


def main():
    args = sys.argv[1:]
    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                file_name = args[i]
                i += 1
        else:
            i += 1

    if dir_parts:
        target_dir = os.path.join(*dir_parts)
        os.makedirs(target_dir, exist_ok=True)
    else:
        target_dir = ""

    if file_name is None and not dir_parts:
        file_name = "file.txt"

    if file_name:
        target_file = (
            os.path.join(target_dir, file_name)
            if target_dir
            else file_name
        )

        lines = []
        while True:
            try:
                line = input("Enter content line: ")
            except EOFError:
                break
            if line == "stop":
                break
            lines.append(line)

        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_exists = os.path.exists(target_file)

        mode = "a" if file_exists else "w"
        with open(target_file, mode, encoding="utf-8") as f:
            if file_exists:
                f.write("\n" + timestamp + "\n")
            else:
                f.write(timestamp + "\n")

            content = [
                f"{idx} {l}\n"
                for idx, l in enumerate(lines, 1)
            ]
            f.writelines(content)

if __name__ == "__main__":
    main()