from challenges import day_01, day_02, day_03, day_04, day_05
from advent.common.parts import Part
import typer


app = typer.Typer()


mapping = {
    "1.1": lambda: day_01.calculate(1),
    "1.2": lambda: day_01.calculate(3),
    "2.1": lambda: day_02.calculate(Part.one),
    "2.2": lambda: day_02.calculate(Part.two),
    "3.1": lambda: day_03.calculate(Part.one),
    "3.2": lambda: day_03.calculate(Part.two),
    "4.1": lambda: day_04.calculate(Part.one),
    "4.2": lambda: day_04.calculate(Part.two),
    "5.1": lambda: day_05.calculate(Part.one),
    "5.2": lambda: day_05.calculate(Part.two),
}


@app.command()
def run(exercise_id: str):
    if exercise_id in mapping:
        typer.echo(f"Day {exercise_id}: {mapping[exercise_id]()}")
    else:
        typer.echo("Incorrect exercise index.")
