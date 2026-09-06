import argparse
import os


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="*",
        default=[]
    )
    parser.add_argument(
        "-f",
        default=None
    )
    parsed_args = parser.parse_args()

    if parsed_args.d:
        target_dir = os.path.sep.join(
            parsed_args.d
        )
        os.makedirs(
            target_dir,
            exist_ok=True
        )
    else:
        target_dir = ""

    if parsed_args.f is None:
        file_name = "file.txt"
    else:
        file_name = parsed_args.f

    if target_dir:
        target_file = os.path.join(
            target_dir,
            file_name
        )
    else:
        target_file = file_name

    lines = []
    while True:
        try:
            content_line = input(
                "Enter content line: "
            )
            if (
                content_line.lower()
                == "stop"
            ):
                break
            lines.append(content_line)
        except EOFError:
            break

    should_write = (
        parsed_args.f is not None
        or not parsed_args.d
        or lines
    )

    if target_file and should_write:
        with open(
            target_file,
            "w",
            encoding="utf-8"
        ) as file_handle:
            for content_line in lines:
                file_handle.write(
                    content_line + "\n"
                )


if __name__ == "__main__":
    main()
