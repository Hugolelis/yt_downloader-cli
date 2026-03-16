import yt_dlp

from src.cli.helpers.errors import DownloaderError

class Downloader:
    def __init__(self, url: str) -> None:
        DownloaderError.invalid_url(url)

        self.url = url
        self.videos_path = "downloads/videos/"
        self.audios_path = "downloads/audios/"

    ############################################################################
    # Baixa o vídeo em formato MP4 com a qualidade especificada (padrão: 720p).#
    ############################################################################
    
    def video(self, quality:  int = 720):
        DownloaderError.invalid_quality(quality)

        format_save = f"bestvideo[height<={quality}][vcodec^=avc1]+bestaudio[ext=m4a]/bestvideo[height<={quality}]+bestaudio/best"

        options = {
            "format": format_save,
            "outtmpl": f"{self.videos_path}%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(self.url, download=False)
                title = info.get("title", "")
                DownloaderError.file_already_exists(f"{self.videos_path}{title}.mp4")
                ydl.download([self.url])
        except DownloaderError:
            raise
        except Exception:
            DownloaderError.download_failed()

    ##########################################################
    # Extrai e baixa o áudio em MP3 com qualidade de 192kbps.#
    ##########################################################

    def audio(self) -> None:
        options = {
            "format": "bestaudio/best",
            "outtmpl": f"{self.audios_path}%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(self.url, download=False)
                title = info.get("title", "")
                DownloaderError.file_already_exists(f"{self.audios_path}{title}.mp3")
                ydl.download([self.url])
        except DownloaderError:
            raise
        except Exception:
            DownloaderError.download_failed()