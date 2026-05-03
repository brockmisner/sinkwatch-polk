import typer

app = typer.Typer(help="SinkWatch command line interface")
ingest_app = typer.Typer()
features_app = typer.Typer()
candidates_app = typer.Typer()
train_app = typer.Typer()

app.add_typer(ingest_app, name="ingest")
app.add_typer(features_app, name="features")
app.add_typer(candidates_app, name="candidates")
app.add_typer(train_app, name="train")


@ingest_app.command("opera")
def ingest_opera(aoi: str, start: str, end: str) -> None:
    """Placeholder OPERA ingest command."""
    typer.echo(f"Ingest OPERA for {aoi} from {start} to {end}")


@ingest_app.command("fdep-subsidence")
def ingest_fdep_subsidence(file: str) -> None:
    """Placeholder FDEP ingest command."""
    typer.echo(f"Ingest FDEP incidents from {file}")
