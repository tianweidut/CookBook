
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        ppid_map = defaultdict(set)

        for pid, ppid in zip(pid, ppid):
            ppid_map[ppid].add(pid)

        r = set([kill])
        d = deque([kill])

        while len(d) > 0:
            cur_pid = d.popleft()
            for pid in ppid_map.get(cur_pid, []):
                r.add(pid)
                d.append(pid)

        return list(r)
