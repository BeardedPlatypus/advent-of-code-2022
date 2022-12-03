from challenges import day_01
import typer


app = typer.Typer()


mapping = {
    "1.1": day_01.calculate
}


@app.command()
def run(exercise_id: str):
    if exercise_id in mapping:
        typer.echo(f"Day {exercise_id}: {mapping[exercise_id]()}")
    else:
        typer.echo("Incorrect exercise index.")
