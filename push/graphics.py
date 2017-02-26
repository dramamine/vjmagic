import itertools;

class Graphics:
  def __init__(self):
    return

  # (0,0), (3,3) gives you the lower left quadrant
  # (0,0), (7,7) gives you the whole thing
  # 0,0 is midi 36
  # 7,7 is midi 99
  def coords_to_quadrant(self, coord_a, coord_b):
    (xa, ya) = coord_a
    (xb, yb) = coord_b

    width = xb - xa + 1

    ranges = list()
    for y_iterator in range(ya, yb + 1):
      point = 36 + (y_iterator * 8) + xa
      ranges.append(range(
        point, point + width
      ))

    return list(itertools.chain.from_iterable(ranges))
