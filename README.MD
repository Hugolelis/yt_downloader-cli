```
 ██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
 ╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
   ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
    ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
    ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

# 🎬 YT Downloader
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-em%20desenvolvimento-orange?style=flat-square)]()
[![Version](https://img.shields.io/badge/version-0.1.0-blue?style=flat-square)]()

A command-line tool to download YouTube videos and audio directly from your terminal. Built with Python, focused on simplicity and flexibility.

## ✨ Features

* **Video Download** — Download videos in the best available quality.
* **Audio Download** — Extract audio and save as MP3.
* **Quality Selection** — Choose your preferred resolution (e.g. 720p, 1080p).
* **List Formats** — Preview all available formats before downloading.

---

## 🛠️ Tech Stack

* **Language:** [Python 3.11+](https://www.python.org/)
* **Downloader:** [yt-dlp](https://github.com/yt-dlp/yt-dlp) — robust YouTube download engine
* **CLI:** [Typer](https://typer.tiangolo.com/) — modern CLI framework based on type hints
* **Terminal UI:** [Rich](https://rich.readthedocs.io/) — beautiful terminal output with progress bars

---

## 📂 Project Structure

```text
yt-downloader/
├── src/
│   ├── cli/
│   │   └── commands.py       # CLI commands and argument definitions
│   ├── services/
│   │   └── downloader.py     # Core download logic
│   └── main.py               # Entrypoint
├── pyproject.toml            # Project manifest and dependencies
└── README.md
```

---

## ⚙️ Running

#### 1. Clone the Repository

```bash
git clone https://github.com/Hugolelis/yt-downloader.git
cd yt-downloader
```

#### 2. Install Dependencies

```bash
pip install -e .
```

#### 3. Run

```bash
# Download video
yt download <url>

# Download audio only (mp3)
yt download <url> --audio

# Choose quality
yt download <url> --quality <quality>
```

---

## 📄 License

This project is licensed under the **MIT** License. See the [LICENSE](LICENSE) file for details.
