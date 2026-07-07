class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []

        for a in asteroids:
            is_alive = True

            while output and output[-1] > 0 and a < 0:
                if output[-1] == abs(a):
                    output.pop()
                    is_alive = False
                    break
                elif output[-1] < abs(a):
                    output.pop()
                    continue
                else:
                    is_alive = False
                    break

            if is_alive:
                output.append(a)

        return output