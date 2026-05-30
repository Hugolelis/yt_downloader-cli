# YT Downloader CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-%3E%3D3.11-1a1a2e?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-1a1a2e?style=for-the-badge&logoColor=white" alt="Status">
</p>

<p align="center">
  A fast and simple command-line tool to download YouTube videos and audio.<br>
  Built with Python, powered by <strong>yt-dlp</strong>, wrapped in a clean <strong>Typer</strong> CLI.
</p>

---

## Features

- **Video Download** — Download YouTube videos in MP4 format with selectable quality (720p, 1080p, 1440p).
- **Audio Extraction** — Extract and convert audio to MP3 at 192 kbps via FFmpeg.
- **Duplicate Protection** — Skips downloads if the file already exists.
- **URL Validation** — Validates URLs before attempting to download.
- **Clean Output** — Colored terminal feedback powered by Rich.
- **Lightweight** — Minimal dependencies, focused on one job.

---

## Prerequisites

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

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Hugolelis/YT-Downloader-CLI.git
cd YT-Downloader-CLI

# Install the package (editable mode)
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

## Command Reference

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

## Project Structure

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

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.