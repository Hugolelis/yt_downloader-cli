import typer
from rich.console import Console
from rich.panel import Panel
from src.services.downloader import Downloader
from src.helpers.errors import DownloaderError

app = typer.Typer(
    name="yt-downloader",
    help="YT Downloader - YouTube video and audio downloader",
    add_completion=False,
)
console = Console()


def _handle_error(e: DownloaderError) -> None:
    console.print(f"[bold red]Error:[/bold red] {e}")
    raise typer.Exit(code=1)


@app.command(name="download")
def download(
    url: str = typer.Argument(..., help="URL do vídeo do YouTube"),
    audio: bool = typer.Option(False, "--audio", "-a", help="Baixar apenas o áudio"),
    quality: int = typer.Option(720, "--quality", "-q", help="Qualidade do vídeo (ex: 720, 1080)"),
):
    """Download vídeo or audio in YouTube."""
    try:
        console.print()
        console.print(Panel.fit(
            f"[bold cyan]YT Downloader[/bold cyan]\nURL: [bold]{url}[/bold]",
            border_style="cyan",
        ))
        downloader = Downloader(url)
        downloader.audio() if audio else downloader.video(quality)
        console.print("[bold green]Download concluído![/bold green]")
    except DownloaderError as e:
        _handle_error(e)


@app.command()
def version():
    """Show the version."""
    console.print("[bold blue]YT Downloader v0.1.0[/bold blue]")


if __name__ == "__main__":
    app()