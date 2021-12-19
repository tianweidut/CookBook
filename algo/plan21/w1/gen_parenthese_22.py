class Solution:
	def generateParenthesis(self, n):
		self.results = []
		track = []
		self._gen_p(n, n, track)
		return self.results

	def _gen_p(self, left, right, track):
		if left > right or left < 0 or right < 0:
			return
		
		if left == 0 and right == 0:
			self.results.append("".join(track))
			return

		track.append("(")
		self._gen_p(left - 1, right, track)
		track.pop()

		track.append(")")
		self._gen_p(left, right-1, track)
		track.pop()

if __name__ == "__main__":
	print(Solution().generateParenthesis(3))

		
		