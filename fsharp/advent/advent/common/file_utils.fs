namespace BeardedPlatypus.advent.common

open PathLib

module internal file_utils =
    let internal read_input_file (file_name: string) : string seq =
        let file_path = Paths.Create("resources") / file_name
        System.IO.File.ReadLines(file_path.ToString())
        
