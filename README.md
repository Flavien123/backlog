
# Daily Backlog CLI

A simple command-line tool to log daily notes with timestamps.

## Features

- Save notes to a default backlog file
- Optionally save to a custom file
- Automatic timestamp formatting (YYYY-MM-DD HH:MM:SS)

## Installation

```bash
python main.py "Your note text here"
```

## Usage

### Basic usage
```bash
python main.py "Task completed"
```

### Save to custom file
```bash
python main.py "Task completed" -f /path/to/custom/file.txt
```

## Arguments

- `text` (required): The note text to save
- `-f, --file` (optional): Path to custom file (defaults to `backlog.txt`)


## Output Format

Each note is saved as:
```
YYYY-MM-DD HH:MM:SS | Note content
```
