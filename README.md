# YT Downloader

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-1a1a2e?style=for-the-badge&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white)]()

</div>

A command-line tool to download YouTube videos and audio directly from your terminal. Built with Python, focused on simplicity and flexibility.

---

## Features

- **Video Download** — Download videos in the best available quality.
- **Audio Download** — Extract audio and save as MP3.
- **Quality Selection** — Choose your preferred resolution (e.g. 720p, 1080p).

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-1a1a2e?style=for-the-badge&logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-1a1a2e?style=for-the-badge&logo=youtube&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-1a1a2e?style=for-the-badge&logo=fastapi&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-1a1a2e?style=for-the-badge&logo=python&logoColor=white)

---

## Project Structure

```text
yt-downloader/
├── downloads/
│   ├── videos/
│   └── audios/
├── src/
│   ├── cli/
│   │   └── commands.py
│   ├── helpers/
│   │   └── errors.py
│   ├── services/
│   │   └── downloader.py
│   └── main.py
├── pyproject.toml
└── README.md
```

---

## Running

**1. Clone the repository**
```bash
git clone https://github.com/Hugolelis/yt-downloader.git
cd yt-downloader
```

**2. Install dependencies**
```bash
pip install -e .
```

**3. Run**
```bash
# Download video
yt <url>

# Download audio only
yt <url> --audio

# Choose quality
yt <url> --quality <quality>
```

---

## License

Licensed under the **MIT** License. See [LICENSE](LICENSE) for details.
