namespace BeardedPlatypus.advent.challenges

open System
open BeardedPlatypus.advent.common

module internal day_4 =
    type private Element = (int * int) * (int * int)

    let private preprocess (lines: string seq) : Element seq =
        let mapper (l: string) : Element =
            match l.Split(',', '-') with
            | [| low_1; high_1; low_2; high_2 |] -> (Int32.Parse low_1, Int32.Parse high_1), (Int32.Parse low_2, Int32.Parse high_2)
            | _   -> raise (System.NotSupportedException "Invalid Value")

        Seq.map mapper lines

    let private contains (low1: int, high1: int) (low2: int, high2: int) : bool =
        low1 >= low2 && high1 <= high2

    let private overlaps (low1: int, high1: int) (low2: int, high2: int) : bool =
        not (low1 > high2 || high1 < low2)

    [<RequireQualifiedAccess>]
    type public Part =
         | One
         | Two

    let private compute (part: Part) (values: Element seq) : int =
        let compare = 
            match part with
            | Part.One -> fun x y -> contains x y || contains y x
            | Part.Two -> overlaps

        values
        |> Seq.filter (fun (x, y) -> compare x y)
        |> Seq.length


    let public calculate (part: Part) : int =

        file_utils.read_input_file "day_04.txt"
        |> preprocess
        |> compute part

