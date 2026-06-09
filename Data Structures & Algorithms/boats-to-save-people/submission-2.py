class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        totalBoats = 0
        seen = set()

        left, right = 0, len(people) - 1

        while left <= right:
            weight = people[left] + people[right]
            if weight <= limit:
                totalBoats += 1
                left += 1
                right -= 1
            else:
                totalBoats += 1
                left += 1

        return totalBoats