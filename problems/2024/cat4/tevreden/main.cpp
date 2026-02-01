
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
#include <cassert>
#include <sstream>

using u32 = uint32_t;
using i32 = int32_t;
using v1d = std::vector<u32>;
using v2d = std::vector<std::vector<u32>>;
//using triplet = std::tuple<u32,u32,u32>;
struct triplet { u32 a; u32 b; u32 c;
  inline u32 index() const {
    // assert(a<1024);
    // assert(b<1024);
    // assert(c<1024);
    return (u32)a + (u32)b * 1024ll + (u32)c * 1024ll*1024ll; } };

//using maptriplet_u32 = std::unordered_map<triplet, u32>;
using maptriplet_u32 = std::unordered_map<u32, u32>;

maptriplet_u32 mem;

std::string spaces = " \t";
inline v1d splitToNumbers(std::string const & line)
{
  v1d result;
  std::string::size_type pos = 0;
  pos = 0;
  u32 val = 0;
  u32 ls = line.size();
  while (pos <= ls)
    {
      while (pos < ls && line[pos] == ' ')
        ++pos;
      val = val * 10 + line[pos] - '0';
      ++pos;
      if (pos >= ls)
        {
          result.push_back(val);
          break;
        }
      else if (line[pos] == ' ')
        {
          result.push_back(val);
        }
      else
        continue;
      val = 0;
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

void debug() {}

u32 knapsack_0_1(v2d const & weights, u32 max_waffles,
                 u32 max_irons, u32 num_items)
{
  if (num_items == 0 or (max_waffles == 0 and max_irons == 0))
    return 0;

  triplet t = { max_waffles, max_irons, num_items };

  auto needle = mem.find(t.index());
  if (needle != mem.end())
    return needle->second;

  if ((weights[num_items - 1][0] > max_waffles) or
      (weights[num_items - 1][1] > max_irons))
    {
      if (num_items == 1)
        return 0;
      else
        return knapsack_0_1(weights, max_waffles, max_irons, num_items-1);
    }
  else
    {
      if (num_items == 1)
        return 1;
      // use customer
      auto value0 = knapsack_0_1(weights, max_waffles-weights[num_items-1][0],
                                 max_irons - weights[num_items-1][1],
                                 num_items - 1) + 1;
      // don't use customer
      auto value1 = knapsack_0_1(weights, max_waffles, max_irons, num_items-1);

      auto result = std::max(value0, value1);
      mem[t.index()] = result;
      return result;
    }
}

int main() {
  std::size_t testCases;
  std::cin >> testCases;
  std::string line;

  for (std::size_t t = 0; t < testCases; ++t) {

    do std::getline(std::cin, line); while (line.empty());
    auto numbers = splitToNumbers(line);
    auto [ max_waffles, max_irons, num_clients ] = destructure<0,3>(numbers);

    v2d data;

    for (unsigned i=0; i<num_clients; ++i) {
      std::getline(std::cin, line);
      data.emplace_back(splitToNumbers(line));
    }

    mem = {};
    auto result = knapsack_0_1(data, max_waffles, max_irons,
                               num_clients);
    std::cout << t + 1 << ' '
              << result << '\n';
  }

  return 0;
}
