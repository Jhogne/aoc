fn consume_bits(s: &mut String, n: usize) -> usize {
    let res: String = s.drain(..n).collect();
    usize::from_str_radix(&res, 2).unwrap()
}

struct Packet {
    version: usize,
    type_id: usize,
    content: Content
}

impl Packet {
    fn from_hex(hex: &str) -> Packet {
        let mut bin = hex.bytes()
            .map(|b| {
                if b > b'9' { 
                    format!("{:04b}", b - b'7') 
                } else { 
                    format!("{:04b}", b - b'0') 
                }})
        .collect();

        Packet::from_bin(&mut bin)
    }

    fn from_bin(s: &mut String) -> Packet {
        let version = consume_bits(s, 3);
        let type_id = consume_bits(s, 3);

        let content: Content = if type_id == 4 {
            Content::parse_literal(s)
        } else if consume_bits(s, 1) == 0 {
                let length = consume_bits(s, 15);
                Content::parse_length(s, length)
        } else {
                let amt = consume_bits(s, 11);
                Content::parse_amount(s, amt)
        };

        Packet { version, type_id,  content }
    }

    fn version_sum(&self) -> usize {
        match &self.content {
            Content::Literal(_) => self.version,
            Content::SubPackets(subs) => subs.iter().fold(self.version, |sum, p| sum + p.version_sum())            
        }
    }

    fn eval(&self) -> usize {
        match &self.content {
            Content::Literal(n) => *n,
            Content::SubPackets(c) => match self.type_id {
                0 => c.iter().map(|p| p.eval()).sum(),
                1 => c.iter().map(|p| p.eval()).product(),
                2 => c.iter().map(|p| p.eval()).min().unwrap(),
                3 => c.iter().map(|p| p.eval()).max().unwrap(),
                5 => if c[0].eval() > c[1].eval() { 1 } else { 0 },
                6 => if c[0].eval() < c[1].eval() { 1 } else { 0 },
                7 => if c[0].eval() == c[1].eval() { 1 } else { 0 },
                _ => unreachable!(),
            }
        }

    }
}

enum Content {
    Literal(usize),
    SubPackets(Vec<Packet>),
}

impl Content {
    fn parse_literal(s: &mut String) -> Content {
        let mut res: usize = 0b0;
        loop {
            let next_group: usize = consume_bits(s, 5);
            res = (res << 4) | (next_group & 0b01111);
            if (next_group & 0b10000) == 0 {
                break;
            }
        }
        Content::Literal(res)
    }

    fn parse_length(s: &mut String, length: usize) -> Content {
        let start = s.len();
        let mut subs = Vec::new();
        while start - s.len() < length {
            subs.push(Packet::from_bin(s));
        }
        Content::SubPackets(subs)
    }

    fn parse_amount(s: &mut String, amt: usize) -> Content {
        let subs = (0..amt).map(|_| Packet::from_bin(s)).collect();
        Content::SubPackets(subs)

    }
}

pub fn solve_1(input: &str) -> String {
    let p: Packet = Packet::from_hex(input.trim());
    p.version_sum().to_string()
}

pub fn solve_2(input: &str) -> String {
    let p: Packet = Packet::from_hex(input.trim());
    p.eval().to_string()
}


#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1("8A004A801A8002F478"), "16");
        assert_eq!(solve_1("620080001611562C8802118E34"), "12");
        assert_eq!(solve_1("C0015000016115A2E0802F182340"), "23");
        assert_eq!(solve_1("A0016C880162017C3686B18A3D4780"), "31");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2("C200B40A82"), "3");
        assert_eq!(solve_2("04005AC33890"), "54");
        assert_eq!(solve_2("880086C3E88112"), "7");
        assert_eq!(solve_2("CE00C43D881120"), "9");
        assert_eq!(solve_2("D8005AC2A8F0"), "1");
        assert_eq!(solve_2("F600BC2D8F"), "0");
        assert_eq!(solve_2("9C005AC2F8F0"), "0");
        assert_eq!(solve_2("9C0141080250320F1802104A08"), "1");
    }
}

