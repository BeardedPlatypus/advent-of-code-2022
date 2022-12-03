from challenges import day_01, day_02, day_03
import typer


app = typer.Typer()


mapping = {
    "1.1": lambda: day_01.calculate(1),
    "1.2": lambda: day_01.calculate(3),
    "2.1": lambda: day_02.calculate(day_02.Mode.one),
    "2.2": lambda: day_02.calculate(day_02.Mode.two),
    "3.1": lambda: day_03.calculate(day_03.Mode.one),
    "3.2": lambda: day_03.calculate(day_03.Mode.two),
}


@app.command()
def run(exercise_id: str):
    if exercise_id in mapping:
        typer.echo(f"Day {exercise_id}: {mapping[exercise_id]()}")
    else:
        typer.echo("Incorrect exercise index.")
