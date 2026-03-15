from typing import Never
import validators

class DownloaderError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.message = msg

    @staticmethod
    def invalid_url(url: str) -> None:
        clean_url = url.replace("\\", "")

        if not validators.url(clean_url):
            raise DownloaderError("URL inválida ou não suportada.")
        
    @staticmethod
    def download_failed() -> Never:
        raise DownloaderError("Falha ao realizar o download.")

    @staticmethod
    def invalid_quality(quality: int) -> None:
        if quality not in [720, 1080, 1440]:
            raise DownloaderError("Qualidade inválida. Use: 720, 1080 ou 1440.")
        