import argparse
import os



def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "-d",
        nargs="*",
        default=[]
    )
    p.add_argument(
        "-f",
        default=None
    )
    a = p.parse_args()

    if a.d:
        d = os.path.sep.join(
            a.d
        )
        os.makedirs(
            d,
            exist_ok=True
        )
    else:
        d = ""

    fn = (
        "file.txt"
        if a.f is None
        else a.f
    )

    tf = (
        os.path.join(
            d,
            fn
        )
        if d
        else fn
    )

    lines = []
    while True:
        try:
            l = input(
                "Enter content line: "
            )
            if (
                l.lower()
                == "stop"
            ):
                break
            lines.append(l)
        except EOFError:
            break

    if tf and (
        a.f is not None
        or not a.d
        or lines
    ):
        with open(
            tf,
            "w",
            encoding="utf-8",
        ) as f:
            for l in lines:
                f.write(
                    l + "\n"
                )


if __name__ == "__main__":
    main()
