#include "timer.hpp"
#include "prettyprint.hpp"

#include <cstddef>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <numeric>
#include <utility>
#include <algorithm>

std::int32_t find_min_moves1(std::vector<std::int32_t> & all_weights,
                             std::int32_t const diff) {

  std::int32_t const total = std::accumulate(all_weights.begin(),
                                             all_weights.end(),
                                             0,
                                             [](std::uint32_t acc, std::int32_t elem) {
                                               return acc + std::abs(elem);
                                             });

  std::vector<std::pair<std::int32_t, std::vector<bool>>> reachable_numbers(1, {diff / 2,
                                                                                std::vector<bool>(all_weights.size())});

  std::vector<bool> reached_numbers(total * 2, false);
  reached_numbers[diff / 2 + total] = true;

  std::sort(all_weights.begin(), all_weights.end());

  // Do only half
  for (std::size_t i = 0; i < (all_weights.size() + 1) / 2; ++i) {

    std::vector<std::pair<std::int32_t, std::vector<bool>>> new_reachable_numbers;

    for (std::size_t j = i; j < all_weights.size(); ++j) {

      for (auto const & reachable_number : reachable_numbers) {
        if (not reachable_number.second[j]) {
          std::int32_t const new_number = reachable_number.first + all_weights[j];

          if (new_number == 0) {
            return i + 1;
          }

          if (not reached_numbers[new_number + total]) {
            new_reachable_numbers.emplace_back(new_number, reachable_number.second);
            new_reachable_numbers.back().second[j] = true;
            reached_numbers[new_number + total] = true;
          }
        }
      }

    }

    reachable_numbers = std::move(new_reachable_numbers);
  }

  return -1;
}

std::int32_t find_min_moves2(std::vector<std::int32_t> & all_weights,
                             std::int32_t const diff) {

  std::int32_t const total = std::accumulate(all_weights.begin(),
                                             all_weights.end(),
                                             0,
                                             [](std::uint32_t acc, std::int32_t elem) {
                                               return acc + std::abs(elem);
                                             });

  std::vector<std::pair<std::int32_t, std::vector<bool>>> reachable_numbers(1, {diff / 2,
                                                                                std::vector<bool>(all_weights.size())});

  std::vector<bool> reached_numbers(total * 2, false);
  reached_numbers[diff / 2 + total] = true;

  std::sort(all_weights.begin(), all_weights.end());

  std::int32_t upper_bound = 0;
  std::int32_t lower_bound = 0;

  // Do only half
  for (std::size_t i = 0; i < (all_weights.size() + 1) / 2; ++i) {

    std::vector<std::pair<std::int32_t, std::vector<bool>>> new_reachable_numbers;

    if (diff < 0) {
      lower_bound = -all_weights[all_weights.size() - i - 1];
    } else {
      upper_bound = -all_weights[i];
    }

    new_reachable_numbers.reserve(upper_bound - lower_bound);

    for (std::size_t j = i; j < all_weights.size(); ++j) {

      for (auto const & reachable_number : reachable_numbers) {
        if (not reachable_number.second[j]) {
          std::int32_t const new_number = reachable_number.first + all_weights[j];

          if (new_number == 0) {
            return i + 1;
          }

          if ((all_weights[j] >= 0 and new_number <= upper_bound) or
              (all_weights[j] < 0 and new_number >= lower_bound)) {
            if (not reached_numbers[new_number + total]) {
              new_reachable_numbers.emplace_back(new_number, reachable_number.second);
              new_reachable_numbers.back().second[j] = true;
              reached_numbers[new_number + total] = true;
            }
          }
        }
      }

    }

    reachable_numbers = std::move(new_reachable_numbers);
  }

  return -1;
}

std::int32_t find_min_moves3(std::vector<std::int32_t> const & all_weights,
                             std::int32_t const diff) {

  std::int32_t const total = std::accumulate(all_weights.begin(),
                                             all_weights.end(),
                                             0,
                                             [](std::uint32_t acc, std::int32_t elem) {
                                               return acc + std::abs(elem);
                                             });

  std::vector<std::int32_t> all_weights_pos;
  std::vector<std::int32_t> all_weights_neg;

  for (auto const weight : all_weights) {
    if (weight < 0) {
      all_weights_neg.emplace_back(weight);
    } else {
      all_weights_pos.emplace_back(weight);
    }
  }

  std::vector<std::pair<std::int32_t, std::vector<bool>>> reachable_numbers_neg;
  std::vector<std::pair<std::int32_t, std::vector<bool>>> reachable_numbers_pos;

  if (diff < 0) {
    reachable_numbers_neg.emplace_back(diff / 2, std::vector<bool>(all_weights.size()));
  } else {
    reachable_numbers_pos.emplace_back(diff / 2, std::vector<bool>(all_weights.size()));
  }

  std::vector<bool> reached_numbers(total * 2, false);
  reached_numbers[diff / 2 + total] = true;

  // Do only half
  for (std::size_t i = 0; i < (all_weights.size() + 1) / 2; ++i) {

    std::vector<std::pair<std::int32_t, std::vector<bool>>> new_reachable_numbers_pos;
    std::vector<std::pair<std::int32_t, std::vector<bool>>> new_reachable_numbers_neg;

    // Add the positive weights to the negative reachable numbers
    for (std::size_t j = i; j < all_weights_pos.size(); ++j) {

      for (auto const & reachable_number : reachable_numbers_neg) {
        if (not reachable_number.second[j]) {
          std::int32_t const new_number = reachable_number.first + all_weights_pos[j];

          if (new_number == 0) {
            return i + 1;
          }

          if (not reached_numbers[new_number + total]) {
            if (new_number < 0) {
              new_reachable_numbers_neg.emplace_back(new_number, reachable_number.second);
              new_reachable_numbers_neg.back().second[j] = true;
            } else {
              new_reachable_numbers_pos.emplace_back(new_number, reachable_number.second);
              new_reachable_numbers_pos.back().second[j] = true;
            }
            reached_numbers[new_number + total] = true;
          }
        }
      }
    }

    // Add the negative weights to the positive reachable numbers
    for (std::size_t j = 0; j < all_weights_neg.size(); ++j) {

      for (auto const & reachable_number : reachable_numbers_pos) {
        if (not reachable_number.second[j + all_weights_pos.size()]) {
          std::int32_t const new_number = reachable_number.first + all_weights_neg[j];

          if (new_number == 0) {
            return i + 1;
          }

          if (not reached_numbers[new_number + total]) {
            if (new_number < 0) {
              new_reachable_numbers_neg.emplace_back(new_number, reachable_number.second);
              new_reachable_numbers_neg.back().second[j] = true;
            } else {
              new_reachable_numbers_pos.emplace_back(new_number, reachable_number.second);
              new_reachable_numbers_pos.back().second[j] = true;
            }
            reached_numbers[new_number + total] = true;
          }
        }
      }
    }

    reachable_numbers_pos = std::move(new_reachable_numbers_pos);
    reachable_numbers_neg = std::move(new_reachable_numbers_neg);
  }

  return -1;
}

int main() {
  std::size_t testCases;
  std::cin >> testCases;

  std::string line;
  std::getline(std::cin, line);

  for (std::size_t t = 0; t < testCases; ++t) {

    std::vector<std::int32_t> all_weights;

    // Read in the first set of weights
    std::getline(std::cin, line);
    std::string::size_type pos = 0;
    std::uint32_t ls = line.size();
    while (pos < ls) {
      while (pos < ls && line[pos] == ' ') {
        ++pos;
      }

      std::int32_t val = 0;
      while (pos < ls and line[pos] != ' ') {
        val = val * 10 + line[pos] - '0';
        ++pos;
      }
      all_weights.emplace_back(val);
    }

    // Read in the second set of weights
    std::getline(std::cin, line);
    pos = 0;
    ls = line.size();
    while (pos < ls) {
      while (pos < ls && line[pos] == ' ') {
        ++pos;
      }

      std::int32_t val = 0;
      while (pos < ls and line[pos] != ' ') {
        val = val * 10 + line[pos] - '0';
        ++pos;
      }
      all_weights.emplace_back(-val);
    }

    std::int32_t const diff = -std::accumulate(all_weights.begin(),
                                               all_weights.end(),
                                               0);

    if (diff % 2 != 0) {
      std::cout << t + 1 << " onmogelijk" << '\n';
      continue;
    } else if (diff == 0) {
      std::cout << t + 1 << " 0" << '\n';
      continue;
    }

    std::int32_t const min_moves = find_min_moves1(all_weights, diff);

    if (min_moves == -1) {
      std::cout << t + 1 << " onmogelijk" << '\n';
    } else {
      std::cout << t + 1 << " " << min_moves << '\n';
    }

  }

  return 0;
}
