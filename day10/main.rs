use std::fs;

fn part1(data: String) -> i64{
    let mut result: i64 = 0;
    let mut previous: Vec<char> = vec![];

    for line in data.lines() {
        for c in line.chars(){
            if c == '('{ previous.push(c); }
            if c == '['{ previous.push(c); }
            if c == '{'{ previous.push(c); }
            if c == '<'{ previous.push(c); }

            let mut was_valid = false;
            if c == ')'{ was_valid = previous.pop().unwrap() == '('; }
            if c == ']'{ was_valid = previous.pop().unwrap() == '['; }
            if c == '}'{ was_valid = previous.pop().unwrap() == '{'; }
            if c == '>'{ was_valid = previous.pop().unwrap() == '<'; }

            if !was_valid{
                if c == ')'{ result += 3; }
                if c == ']'{ result += 57; }
                if c == '}'{ result += 1197; }
                if c == '>'{ result += 25137; }
            }
        }
    }

    return result;
}

fn part2(data: String) -> i64{

    let mut results: Vec<i64> = vec![];

    for line in data.lines() {
        let mut was_valid = true;
        let mut score: i64 = 0;
        let mut previous: Vec<char> = vec![];

        for c in line.chars(){
            if c == '('{ previous.push(c); }
            if c == '['{ previous.push(c); }
            if c == '{'{ previous.push(c); }
            if c == '<'{ previous.push(c); }

            if c == ')'{ was_valid = previous.pop().unwrap() == '('; }
            if c == ']'{ was_valid = previous.pop().unwrap() == '['; }
            if c == '}'{ was_valid = previous.pop().unwrap() == '{'; }
            if c == '>'{ was_valid = previous.pop().unwrap() == '<'; }

            if !was_valid{
                break;
            }
        }

        if was_valid{
            for c in previous.iter().rev(){
                score = score * 5;
                if *c == '('{ score += 1; };
                if *c == '['{ score += 2; };
                if *c == '{'{ score += 3; };
                if *c == '<'{ score += 4; };
            }

            results.push(score);
        }
    }

    results.sort();
    // println!("{:?}", results);
    return results[results.len() / 2];
}

fn main() {
    // let inputfile = "testinput.txt";
    let inputfile = "input.txt";
    let data = fs::read_to_string(inputfile).expect("Unable to read file");

    // let result = part1(data);
    let result = part2(data);

    println!("{}", result);
}
