use std::cmp::{max, Reverse};
use std::collections::HashSet;

fn main() {
    let n = read_int();

    for case in 0..n {
        let v = read_ints();
        let ma = v[0];
        let mb = v[1];
        let k = v[2];

        let mut pairs = (0..k)
            .map(|_| {
                let v = read_ints();
                (v[0], v[1])
            })
            .collect::<Vec<_>>();

        pairs.sort_by_key(|&a| Reverse(a));

        let mut cache = HashSet::new();
        let mut best = 0;
        f(ma, mb, &pairs, &mut cache, &mut best, 0, 0, 0, 0);
        println!("{} {best}", case + 1);
    }
}

fn f(
    ma: u64,
    mb: u64,
    pairs: &[(u64, u64)],

    cache: &mut HashSet<(u64, u64, u64, u64)>,
    best: &mut u64,

    next: u64,
    taken: u64,
    ca: u64,
    cb: u64,
) {
    if taken + pairs.len() as u64 - next <= *best {
        return;
    }
    if next == pairs.len() as u64 {
        *best = max(*best, taken);
        return;
    }

    if !cache.insert((next, taken, ca, cb)) {
        return;
    }

    // take
    let (pa, pb) = pairs[next as usize];
    let na = ca + pa;
    let nb = cb + pb;
    if na <= ma && nb <= mb {
        f(ma, mb, pairs, cache, best, next + 1, taken + 1, na, nb);
    }

    // skip
    f(ma, mb, pairs, cache, best, next + 1, taken, ca, cb);
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    if s.is_empty() {
        panic!("empty stdin");
    }
    s.trim_end_matches('\n').to_owned()
}

fn read_int() -> u64 {
    read_line().parse().unwrap()
}

fn read_ints() -> Vec<u64> {
    read_line().split(" ").map(|s| s.parse().unwrap()).collect()
}
