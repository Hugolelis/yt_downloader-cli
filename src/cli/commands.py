import typer
from src.cli.services.downloader import Downloader
from src.cli.helpers.errors import DownloaderError

app = typer.Typer()

@app.command()
def download(url: str, audio: bool = False, quality: int = 720) -> None:
    try:
        downloader = Downloader(url)
        downloader.audio() if audio else downloader.video(quality)
    except DownloaderError as e:
        typer.echo(f"Erro: {e.message}")
        raise typer.Exit(1)