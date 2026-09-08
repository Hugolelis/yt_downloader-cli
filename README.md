# YT Downloader CLI

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.11-1a1a2e?style=for-the-badge&logo=python&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Active-1a1a2e?style=for-the-badge&logoColor=white)]()

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
- [License](#license)
- [Author](#author)

</details>

---

## About

`yt-dlp` already does the heavy lifting for YouTube downloads, but its CLI surface is built for every option under the sun. This wraps just the two things actually needed day to day — grab a video at a given quality, or pull the audio as MP3 — behind a small Typer CLI with duplicate protection and clean colored output, instead of remembering `yt-dlp` flags every time.

<!-- Adjust to your actual motivation — draft based on the feature list. -->

---

## Demo

```bash
yt https://youtube.com/watch?v=example
```

<!-- Replace with a real captured terminal output or GIF (Rich-styled progress/success message) — strengthens this section a lot more than a bare command. -->

---

## Features

| Capability | Description |
|---|---|
| **Video Download** | Download YouTube videos in MP4 format with selectable quality (720p, 1080p, 1440p) |
| **Audio Extraction** | Extract and convert audio to MP3 at 192 kbps via FFmpeg |
| **Duplicate Protection** | Skips downloads if the file already exists |
| **URL Validation** | Validates URLs before attempting to download |
| **Clean Output** | Colored terminal feedback powered by Rich |
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
| [FFmpeg](https://ffmpeg.org) | Audio transcoding (MP3) |

---

## Architecture & Design Decisions

```
yt-downloader/
├── src/
│   ├── cli/
│   │   └── commands.py      # Typer CLI commands
│   ├── helpers/
│   │   └── errors.py        # Custom exceptions and validation
│   ├── services/
│   │   └── downloader.py    # Core download logic (yt-dlp)
│   └── main.py              # Application entry point
├── downloads/
│   ├── videos/
│   └── audios/
├── pyproject.toml           # Project metadata & dependencies
└── README.md
```

**Why this shape:** `downloader.py` isolates all `yt-dlp` calls behind one service, so the CLI layer only deals with user input/output, not download internals. Typer was chosen for type-hint-driven commands and automatic `--help`; Rich keeps terminal styling out of the download logic entirely.

**Known limitations:**
- No playlist support — one URL per invocation.
- No resume for interrupted downloads; a partial file is treated as incomplete and re-downloaded.
- Quality selection (`720`/`1080`/`1440`) depends on what YouTube actually offers for a given video — no fallback message if the requested quality isn't available.

<!-- Adjust "Why this shape" and "Known limitations" to match your actual reasoning — draft based on the code structure. -->

---

## Getting Started

### Prerequisites

- **Python** >= 3.11
- **FFmpeg** installed and available on your PATH (required for audio extraction)

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
git clone https://github.com/Hugolelis/YT-Downloader-CLI.git
cd YT-Downloader-CLI
pip install -e .
```

> **Note:** This registers the `yt` command globally in your environment.

---

## Usage

### Download a video (defaults to 720p)

```bash
yt <youtube-url>
```

### Download at a specific quality

```bash
yt <youtube-url> --quality 1080
yt <youtube-url> -q 1440
```

### Download audio only (MP3)

```bash
yt <youtube-url> --audio
yt <youtube-url> -a
```

### Check the version

```bash
yt version
```

---

## Commands

| Command | Description |
|---|---|
| `yt <url>` | Download video at 720p (default) |
| `yt <url> -q <quality>` | Download video at specified quality (720, 1080, 1440) |
| `yt <url> -a` | Download audio only as MP3 |
| `yt version` | Show the installed version |

### Options

| Flag | Shorthand | Description | Default |
|---|---|---|---|
| `--quality` | `-q` | Video quality (720, 1080, 1440) | `720` |
| `--audio` | `-a` | Download audio only | `false` |

---

## Output Structure

```
yt-downloader/
└── downloads/
    ├── videos/       # MP4 files
    └── audios/       # MP3 files
```

Files are named after the YouTube video title.

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

## Author

**Hugo** — [GitHub](https://github.com/Hugolelis)
