class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            isSurvived = True
            while stack and (asteroid < 0 and stack[-1] > 0):
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) < stack[-1]:
                    isSurvived = False
                    break
                else:
                    stack.pop()
                    isSurvived = False
                    break

            if isSurvived:
                stack.append(asteroid)

        return stack



