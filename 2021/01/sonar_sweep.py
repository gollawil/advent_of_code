from pathlib import Path

def part1(depths):
  depth_increases = 0
  last_depth = int(depths[0])

  for depth in depths:
    if int(depth) > last_depth:
      depth_increases += 1

    last_depth = int(depth)

  return depth_increases

def part2(depths):
  windows = []
  window_size = 3
  for idx, depth in enumerate(depths):
    if idx > len(depths) - window_size:
      continue

    windows.append(
      int(depth) + int(depths[idx+1]) + int(depths[idx+2])
    )

  return part1(windows)

if __name__ == "__main__":
  current_dir = Path(__file__).parent.resolve()
  with open(f"{current_dir}/input.txt", "r") as f:
    depths = f.readlines()

  print(part1(depths))
  print(part2(depths))
