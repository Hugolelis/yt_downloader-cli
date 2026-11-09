# YT Downloader CLI

<div align="left">

[![Status](https://img.shields.io/badge/Status-Active-407a50?style=for-the-badge&labelColor=1a1a1a&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-0f766e?style=for-the-badge&labelColor=1a1a1a&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-0f766e?style=for-the-badge&labelColor=1a1a1a&logoColor=white)](LICENSE)

</div>

> **YT Downloader CLI** is a fast, single-purpose command-line tool to download YouTube videos and audio, built on top of `yt-dlp` and wrapped in a clean Typer CLI.

<details>
<summary><strong>Table of Contents</strong></summary>

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [Output Structure](#output-structure)
- [Author](#author)
- [License](#license)

</details>

---

## About

`yt-dlp` already does the heavy lifting for YouTube downloads, but its CLI surface is built for every option under the sun. This wraps just the two things actually needed day to day (grab a video at a given quality, or pull the audio as MP3) behind a small Typer CLI with duplicate protection and clean colored output, instead of remembering `yt-dlp` flags every time.

---

## Demo

```bash
yt download https://www.youtube.com/watch?v=<video-id> --quality 1080
```

The command shows a panel with the URL, downloads through `yt-dlp` and ends with a green confirmation (messages are in Portuguese). The full set of options is always one flag away:

```
$ yt download --help

 Usage: yt download [OPTIONS] {url}

 Download vídeo or audio in YouTube.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    url      <str>  URL do vídeo do YouTube [required]                      │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --audio    -a      <bool>  Baixar apenas o áudio                             │
│ --quality  -q      <int>   Qualidade do vídeo (ex: 720, 1080) [default: 720] │
│ --help             <bool>  Show this message and exit.                       │
╰──────────────────────────────────────────────────────────────────────────────╯
```

---

## Features

| Capability | Description |
|---|---|
| **Video Download** | Download YouTube videos as MP4 with a selectable maximum quality (720p, 1080p, 1440p). Prefers H.264 video with AAC audio for wide player compatibility |
| **Audio Extraction** | Extract and convert audio to MP3 at 192 kbps via FFmpeg |
| **Duplicate Protection** | Stops with an error instead of downloading again when the file already exists |
| **URL Validation** | Validates the URL before attempting to download |
| **Clean Output** | Colored terminal feedback powered by Rich, and a non-zero exit code on errors |
| **Lightweight** | Minimal dependencies, focused on one job |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Python](https://python.org) >= 3.11 | Core language |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | YouTube download engine |
| [Typer](https://typer.tiangolo.com) | CLI interface builder |
| [Rich](https://rich.readthedocs.io) | Terminal styling and output |
| [validators](https://validators.readthedocs.io) | URL validation |
| [FFmpeg](https://ffmpeg.org) | Merging video and audio streams, and MP3 transcoding |

---

## Architecture & Design Decisions

```
.
├── src/
│   ├── cli/
│   │   └── commands.py      # Typer commands (download, version)
│   ├── helpers/
│   │   └── errors.py        # DownloaderError and input checks (URL, quality, duplicates)
│   ├── services/
│   │   └── downloader.py    # Core download logic (yt-dlp)
│   └── main.py              # Application entry point
├── pyproject.toml           # Project metadata, dependencies and the `yt` script
├── LICENSE
└── README.md
```

At runtime the tool creates `downloads/videos/` and `downloads/audios/` in the folder you run it from (git-ignored here).

**Why this shape:** `downloader.py` isolates all `yt-dlp` calls behind one service, so the CLI layer only deals with user input/output, not download internals. Every expected failure is raised as a `DownloaderError`, so the CLI catches one exception type, prints a clean message and exits with code 1. Typer was chosen for type-hint-driven commands and automatic `--help`; Rich keeps terminal styling out of the download logic entirely.

**Known limitations:**
- No playlist support: one URL per invocation.
- Quality is a maximum (`height <= quality`), so if YouTube does not offer the requested resolution the best one below it is downloaded, with no message saying so.
- The duplicate check looks for `<video title>.mp4` / `.mp3`, but `yt-dlp` replaces characters that are invalid in file names, so a title with such characters may not be recognized as already downloaded.
- Only 720, 1080 and 1440 are accepted as quality values.
- User-facing messages are in Portuguese.
- No automated tests yet.

---

## Getting Started

### Prerequisites

- **Python** >= 3.11
- **FFmpeg** installed and available on your PATH (required to merge video and audio into MP4, and to extract MP3)

  ```bash
  # Debian / Ubuntu
  sudo apt install ffmpeg

  # macOS (Homebrew)
  brew install ffmpeg

  # Windows (Chocolatey)
  choco install ffmpeg
  ```

### Installation

```bash
git clone https://github.com/Hugolelis/yt_downloader-cli.git
cd yt_downloader-cli
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

> **Note:** This registers the `yt` command inside the virtual environment, so activate it (`source .venv/bin/activate`) before using it in a new terminal.

---

## Usage

The download is the `download` command, so the URL always comes after it.

### Download a video (defaults to 720p)

```bash
yt download <youtube-url>
```

### Download at a specific quality

```bash
yt download <youtube-url> --quality 1080
yt download <youtube-url> -q 1440
```

### Download audio only (MP3)

```bash
yt download <youtube-url> --audio
yt download <youtube-url> -a
```

### Check the version

```bash
yt version
```

---

## Commands

| Command | Description |
|---|---|
| `yt download <url>` | Download video at 720p (default) |
| `yt download <url> -q <quality>` | Download video at the given maximum quality (720, 1080, 1440) |
| `yt download <url> -a` | Download audio only as MP3 |
| `yt version` | Show the installed version |

### Options (`yt download`)

| Flag | Shorthand | Description | Default |
|---|---|---|---|
| `--quality` | `-q` | Maximum video height: 720, 1080 or 1440 | `720` |
| `--audio` | `-a` | Download audio only (the quality is ignored) | `false` |

---

## Output Structure

Files go to a `downloads/` folder inside the directory where you run the command:

```
downloads/
├── videos/       # MP4 files
└── audios/       # MP3 files
```

Files are named after the YouTube video title.

---

## Author

[Hugolelis](https://github.com/Hugolelis)

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.
