
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        cnt = len(tasks)
        c = Counter(tasks)
        tasks = sorted(c.values(), reverse=True)

        max_n = tasks[0]
        idle_slots = (max_n - 1) * (n + 1)

        for t in tasks:
            idle_slots -= min(t, max_n - 1)

        return cnt + (idle_slots if idle_slots > 0 else 0)

