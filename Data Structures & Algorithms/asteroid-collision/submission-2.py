class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            shouldAddToStack = True
            while stack and (asteroid < 0 and stack[-1] > 0):
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) < stack[-1]:
                    shouldAddToStack = False
                    break
                else:
                    stack.pop()
                    shouldAddToStack = False
                    break

            if shouldAddToStack:
                stack.append(asteroid)

        return stack
            