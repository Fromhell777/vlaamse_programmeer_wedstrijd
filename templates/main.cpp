//#include "prettyprint.hpp"

#include <cstddef>
#include <cstdint>
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <unistd.h>
#include <ranges>
#include <tuple>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <cassert>
#include <sstream>

using u32 = uint32_t;
using i32 = int32_t;
using v1d = std::vector<u32>;
using v2d = std::vector<std::vector<u32>>;

std::string spaces = " \t";

inline v1d split_to_numbers(std::string const & line) {
  v1d result;
  std::string::size_type pos = 0;
  u32 ls = line.size();
  while (pos < ls) {
    while (pos < ls && line[pos] == ' ') {
      ++pos;
    }

    std::int32_t val = 0;
    while (pos < ls and line[pos] != ' ') {
      val = val * 10 + line[pos] - '0';
      ++pos;
    }
    result.emplace_back(val);
  }

  return result;
}

inline v1d get_numbers_input(u32 const size) {
  v1d result(size);

  for (u32 i = 0; i < size; ++i) {
    std::cin >> result[i];
  }

  return result;
}

template<typename T>
void fill(std::vector<T> & v, T value)
{
  for (auto & e : v)
    e = value;
}

template<typename T, size_t ... S>
  auto destructure_impl(T &t, std::index_sequence<S...>)
{
  return std::forward_as_tuple(*std::next(std::begin(t), S)...);
}

template<size_t Count, typename T>
auto destructure(T &t)
{
  return destructure_impl(t, std::make_index_sequence<Count>());
}

template<size_t Start, typename T, size_t ... S>
  auto destructure_impl(T &t, std::index_sequence<S...>)
{
  return std::forward_as_tuple(*std::next(std::begin(t), Start+S)...);
}

template<size_t Start, size_t Count, typename T>
auto destructure(T &t)
{
  return destructure_impl<Start>(t, std::make_index_sequence<Count>());
}

int main() {
  std::size_t testCases;
  std::cin >> testCases;

  for (std::size_t t = 0; t < testCases; ++t) {

    v1d const input_data = get_numbers_input(2);

    std::cout << t + 1 << ' '
              << todo << '\n';
  }

  return 0;
}
