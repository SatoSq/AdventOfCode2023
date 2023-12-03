pub fn part1(text: &str) -> u32 {
    text.lines().map(|line| {
        //for each line in the text
        let line: Vec<char> = line
            .chars()
            .filter(char::is_ascii_digit)
            .collect();
        format!(
            "{}{}",
            line.first()
                .unwrap_or(&'0'), 
            line.last()
                .unwrap_or(&'0')
        )
        .parse::<u32>()
        .expect("Concatenate")
    })
    .sum()
}

pub fn part2(text: &str) -> u32 {
    let numbers = 
        [("one","o1e"),
            ("two","t2o"),
            ("three","t3e"),
            ("four","f4r"),
            ("five","f5e"),
            ("six","s6x"),
            ("seven","s7n"),
            ("eight","e8t"),
            ("nine","n9e")];

    let newtext = 
        text.lines()
            .map(|line|{
                let mut line=line.to_owned();
                for (key,value) in numbers
                    {
                    line=line.replace(key, value);
                    }
                line
            })
            .collect::<Vec<_>>()
            .join("\n");
    part1(&newtext)
}