namespace BeardedPlatypus.advent.challenges

open BeardedPlatypus.advent.common

module internal day_3 =
    type Element = Set<char> seq

    let priority_mapping : Map<char, int> = 
        Map <| (Seq.mapi (fun i c -> (c, i+1)) "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    let get_priority (v: char) : int =
        priority_mapping |> Map.find v

    let private preprocess_part1 (lines: string seq) : Element seq =
        let mapper (l: string) : Element =
            let split: int = l.Length / 2
            seq { Set.ofSeq l[..(split-1)]; Set.ofSeq l[split..] }

        Seq.map mapper lines

    let private preprocess_part2 (n: int) (lines: string seq) : Element seq =
        lines
        |> Seq.map Set.ofSeq
        |> Seq.indexed
        |> Seq.groupBy (fun (i, _) -> i / n)
        |> Seq.map (fun (_, v) -> v |> Seq.map (fun (_, s) -> s) )

    let private compute (elements: Element seq) : int =
        let mapper (elem: Element) : int =
            Set.intersectMany elem 
            |> Set.minElement  // At this point the data should only contain a single element
            |> get_priority

        Seq.sum <| Seq.map mapper elements

    [<RequireQualifiedAccess>]
    type public Part =
         | One
         | Two

    let public calculate (part: Part) : int =
        let preprocess = 
            match part with
            | Part.One -> preprocess_part1
            | Part.Two -> preprocess_part2 3

        file_utils.read_input_file "day_03.txt"
        |> preprocess
        |> compute

