#!/usr/bin/env python3
from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

BASE_DIR: Path = Path(__file__).parent.parent
file: Path = BASE_DIR / "backlog.txt"

now: datetime = datetime.now()
time: str = now.strftime("%Y-%m-%d %H:%M:%S")

parser = ArgumentParser(description="CLI для ежедневных записей")
parser.add_argument("text", type=str, help="Текст который сохранится в файле")
parser.add_argument("-f", "--file", type=str, help="Путь до файла")
args = parser.parse_args()


@dataclass
class Note:
    datetime: str
    content: str


def main() -> None:
    save_text(text=args.text, path=file)
    if args.file:
        save_text(text=args.text, path=args.file)


def save_text(text: str, path: Path) -> None:
    note: Note = Note(datetime=time, content=text)

    with open(path, "a", encoding="UTF-8") as f:
        f.write(f"{note.datetime} | {note.content} \n")


if __name__ == "__main__":
    main()
