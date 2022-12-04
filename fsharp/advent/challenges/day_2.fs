namespace BeardedPlatypus.advent.challenges

open BeardedPlatypus.advent.common

module internal day_2 = 
    type private Hand =
        | Rock
        | Paper
        | Scissors

    let private to_opponent_hand (c: string) : Hand =
        match c with
        | "A" -> Rock
        | "B" -> Paper
        | "C" -> Scissors
        | _   -> raise (System.NotSupportedException "Invalid Value")
    
    let private to_player_hand (c: string) : Hand =
        match c with
        | "X" -> Rock
        | "Y" -> Paper
        | "Z" -> Scissors
        | _   -> raise (System.NotSupportedException "Invalid Value")

    type private Element = Hand * Hand

    let private pre_process_part1(lines: string seq) : Element seq =
        let mapper (s: string) : Element =
            let split = s.Split(' ')
            to_opponent_hand split.[0], to_player_hand split.[1]
        Seq.map mapper lines

    type Strategy =
        | Lose
        | Draw
        | Win

    let private to_strategy (c: string) : Strategy =
        match c with
        | "X" -> Lose
        | "Y" -> Draw
        | "Z" -> Win
        | _   -> raise (System.NotSupportedException "Invalid Value")

    let private to_player_hand_strategy (opponent: Hand) (s: Strategy) : Hand =
        match s, opponent with
        | Draw, hand -> hand
        | Win,  Rock -> Paper
        | Lose, Rock -> Scissors 
        | Win,  Paper -> Scissors
        | Lose, Paper -> Rock
        | Win,  Scissors -> Rock
        | Lose, Scissors -> Paper

    let private pre_process_part2(lines: string seq) : Element seq =
        let mapper (s: string) : Element =
            let split = s.Split(' ')
            let opponent = to_opponent_hand split.[0]
            let player = split.[1] |> to_strategy |> (to_player_hand_strategy opponent)
            opponent, player

        Seq.map mapper lines
        

    let private calculate_score (elem: Element) : int =
        let match_score = 
            match elem with
            | opponent, player when opponent = player -> 3
            | Rock, Paper                             -> 6
            | Paper, Scissors                         -> 6
            | Scissors, Rock                          -> 6
            | _                                       -> 0
        
        let hand_score = 
            match elem with
            | _, Rock -> 1
            | _, Paper -> 2
            | _, Scissors -> 3

        match_score + hand_score


    [<RequireQualifiedAccess>]
    type public Part =
         | One
         | Two

    let public calculate (part: Part) : int =
        let preprocess = 
            match part with
            | Part.One -> pre_process_part1
            | Part.Two -> pre_process_part2

        file_utils.read_input_file "day_02.txt"
        |> preprocess
        |> Seq.map calculate_score
        |> Seq.sum
        
