class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_happened = True

        while(collision_happened):
            collision_happened = False
            for i in range(len(asteroids) - 1):
                if asteroids[i] > 0 and asteroids[i + 1] < 0:
                    collision_happened = True
                    if (asteroids[i] > abs(asteroids[i + 1])):
                        del asteroids[i + 1]
                    elif (asteroids[i] < abs(asteroids[i + 1])):
                        del asteroids[i]
                    else:
                        del asteroids[i + 1]
                        del asteroids[i]

                    break

        return asteroids