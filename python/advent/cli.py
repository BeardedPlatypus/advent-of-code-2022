from challenges import day_01, day_02
import typer


app = typer.Typer()


mapping = {
    "1.1": lambda: day_01.calculate(1),
    "1.2": lambda: day_01.calculate(3),
    "2.1": lambda: day_02.calculate(),
}


@app.command()
def run(exercise_id: str):
    if exercise_id in mapping:
        typer.echo(f"Day {exercise_id}: {mapping[exercise_id]()}")
    else:
        typer.echo("Incorrect exercise index.")
