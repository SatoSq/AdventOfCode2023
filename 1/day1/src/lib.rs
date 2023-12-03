pub fn part1(text: &str) -> u32 {
    let mut sum = 0;

    // text.lines().map(|line| {
    //     //for each line in the text
    //     let line: Vec<char> = line.chars().filter(|i: &char| i.is_digit(10)).collect();
    //     let value = (String::from(line.first().unwrap())).push(String::from(line.last().unwrap()));
    //     value
    // }).sum()

    for line in text.lines() {
        let line: Vec<char> = line.chars().filter(|i: &char| i.is_digit(10)).collect();
        let value = format!("{}{}", line.first().unwrap(), line.last().unwrap()).parse::<u32>().unwrap();
        sum+=value
    }

    sum
}


// fn main() {
//     let text = fs::read_to_string("../1.txt").expect("Should have been able to read the file");
//     println!("Part 1: {}", part1(text);
// }
