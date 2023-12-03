fn part1(text: &str) -> u32 {
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
