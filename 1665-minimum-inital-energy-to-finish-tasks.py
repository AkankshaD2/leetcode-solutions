class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: (x[1]-x[0]),reverse=True)
        energy=0
        answer=0
        for actual,minimum in tasks:
            if energy<minimum:
                extra=minimum-energy
                answer+=extra
                energy+=extra
            energy-=actual
        return answer  
