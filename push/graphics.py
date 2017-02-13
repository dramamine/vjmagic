
class Graphics:
	def coords_to_quadrant(coordA, coordB):
		# 0,0 is midi 36
		# 8,8 is midi 105
		(xa, ya) = coordA
		(xb, yb) = coordB
		origin = 36 + (ya * 8) + xa
		return list(itertools.chain(
		  range(36, 40),
		  range(44, 48),
		  range(52, 56),
		  range(60, 64),
		  range(101, 105)
		))
