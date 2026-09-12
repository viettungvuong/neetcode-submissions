class Solution:

  def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    matched = [False, False, False]

    for t in triplets:
      if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
        continue
      for i in range(3):
        if t[i] == target[i]:
          matched[i] = True

      if all(matched):
        return True

    return all(matched)



