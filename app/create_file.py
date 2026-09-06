import argparse
import os
from datetime import datetime, timezone


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*", default=[])
    parser.add_argument("-f", default=None)
    parsed_args = parser.parse_args()

    if parsed_args.d:
        target_dir = os.path.join(*parsed_args.d)
        os.makedirs(target_dir, exist_ok=True)
    else:
        target_dir = ""

    if parsed_args.f is None and not parsed_args.d:
        file_name = "file.txt"
    else:
        file_name = parsed_args.f

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