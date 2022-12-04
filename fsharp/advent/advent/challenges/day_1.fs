namespace BeardedPlatypus.advent.challenges

open System

open BeardedPlatypus.advent.common

module internal day_1 =
    let private pre_process (lines: string seq) : int list =
        let folder (acc_v: int, res: int list) (elem: string) = 
            if not (String.IsNullOrEmpty elem) then
                acc_v + (Int32.Parse elem), res
            else
                0, acc_v :: res

        let _, res = Seq.fold folder (0, []) lines 
        res

    let private compute (n: int) (elems: int list) : int list =
        let folder (l: int list) (elem: int) =
            match l with
            | acc_head :: acc_body when elem > acc_head ->
                elem :: acc_body |> List.sort
            | list ->
                list

        List.fold folder (List.init n (fun _ -> 0)) elems

    let public calculate (n: int) : int =
        file_utils.read_input_file "day_01.txt"
        |> pre_process
        |> (compute n)
        |> List.sum
                

