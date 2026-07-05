class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        for a in asteroids:
            alive = True
            while output and output[-1] > 0 and a < 0:
                if output[-1] < abs(a):
                    output.pop()
                    continue
                elif output[-1] == abs(a):
                    output.pop()
                alive = False
                break
            
            if alive:
                output.append(a)

        return output 