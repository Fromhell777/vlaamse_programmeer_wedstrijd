use std::cmp::{max, min, Reverse};
use std::collections::{hash_set, HashMap, HashSet};
use std::collections::hash_map::Entry;
use std::time::Instant;

fn main() {
    let test_cases =read_int();

    for t in 0..test_cases {
        let num_huts = read_int() as usize;
        let mut huts = vec![];

        for _ in 0..num_huts {
            let v = read_ints();
            huts.push((v[0], v[1]));
        }

        huts.rotate_right(min(4, num_huts));

        let mut costs: Vec<_> = (0..num_huts).map(|_| vec![0; num_huts as usize]).collect();
        let mut all_costs = vec![];

        for i in 0..num_huts {
            for j in 0..num_huts {
                let (x1, y1) = huts[i as usize];
                let (x2, y2) = huts[j as usize];

                let dx = (x1 as i64 - x2 as i64).abs();
                let dy = (y1 as i64 - y2 as i64).abs();
                let cost = dx*dx + dy*dy;

                costs[i as usize][j as usize] = cost;
                if i != j && i < j {
                    all_costs.push(cost);
                }
            }
        }

        all_costs.sort();

        let mut min_cost = 1<<30;
        let mut curr_cost = 0;

        let mut set = HashSet::default();
        set.insert(0usize);
        let start =Instant::now();

        let mut best_by_travelled = HashMap::new();

        shortest_route(&start, &costs, &mut min_cost, &mut curr_cost, num_huts, &all_costs, &mut set, 0, &mut best_by_travelled);

        println!("{} {}", t+1, min_cost);
    }
}

fn shortest_route(start: &Instant, costs: &[Vec<i64>], min_cost: &mut i64, curr_cost: &mut i64, num_huts: usize, all_costs: &[i64], travelled: &mut HashSet<usize>, curr_cross: usize, best_by_travelled: &mut HashMap<Vec<usize>, i64>) {
    if start.elapsed().as_secs_f32() > 0.1 {
        return;
    }

    let copy_cost = *curr_cost;

    let mut key: Vec<_> = travelled.iter().copied().collect();
    key.sort();
    key.push(curr_cross);
    match best_by_travelled.entry(key) {
        Entry::Occupied(value) => {
            if value.get() < curr_cost {
                return;
            }
        }
        Entry::Vacant(entry) => {
            entry.insert(*curr_cost);
        }
    }

    let nodes_left = num_huts - travelled.len();
    let heur = all_costs[..nodes_left].iter().sum::<i64>();

    if *curr_cost + heur < *min_cost {
        let mut dists = vec![];
        for i in 0..num_huts {
            if i != curr_cross {
                dists.push((costs[i][curr_cross], i));
            }
        }
        dists.sort();

        for (_, new_cross) in dists {
            if !travelled.contains(&new_cross) {
                travelled.insert(new_cross);

                *curr_cost += costs[curr_cross][new_cross];
                shortest_route(start, costs, min_cost, curr_cost, num_huts, all_costs, travelled, new_cross, best_by_travelled);

                if travelled.len() == num_huts {
                    *curr_cost = *curr_cost + costs[0][new_cross];
                    *min_cost = min(*min_cost, *curr_cost);
                }

                *curr_cost = copy_cost;
                travelled.remove(&new_cross);
            }
        }
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    if s.is_empty() {
        panic!("empty stdin");
    }
    s.trim_end_matches('\n').to_owned()
}

fn read_int() -> i64 {
    read_line().parse().unwrap()
}

fn read_ints() -> Vec<i64> {
    read_line().split(" ").map(|s| s.parse().unwrap()).collect()
}
