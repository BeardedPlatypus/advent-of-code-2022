namespace BeardedPlatypus.advent.challenges

open BeardedPlatypus.advent.common

module internal day_3 =
    type Element = Set<char> list

    let priority_mapping : Map<char, int> = 
        Map <| (Seq.mapi (fun i c -> (c, i+1)) "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    let get_priority (v: char) : int =
        priority_mapping |> Map.find v

    let private preprocess_part1 (lines: string seq) : Element seq =
        let mapper (l: string) : Element =
            let split: int = l.Length / 2
            [Set.ofSeq l[..(split-1)]; Set.ofSeq l[split..]]

        Seq.map mapper lines

    let private compute (elements: Element seq) : int =
        let mapper (elem: Element) : int =
            Set.intersectMany elem 
            |> Set.minElement  // At this point the data should only contain a single element
            |> get_priority

        Seq.sum <| Seq.map mapper elements

    let public calculate () : int =
        file_utils.read_input_file "day_03.txt"
        |> preprocess_part1
        |> compute

