

def paginate(num, results):
    if num <= 0:
        return []

    import heapq
    from collections import defaultdict
    hostid_map = defaultdict(list)

    for r in results:
        hostid, listing_id, score, city = r.split(',')
        score = float(score)
        hostid_map[hostid].append((score, r))

    for hostid, value in hostid_map.iteritems():
        hostid_map[hostid] = sorted(value, key=lambda x: x[0], reverse=True)

    hq = []
    output = []
    cnt = 0
    while hq or hostid_map:
        if not hq:
            hq = [(-v[0][0], v[0][1], hostid) for hostid, v in hostid_map.iteritems()]
            heapq.heapify(hq)

        top = heapq.heappop(hq)

        score, text, hostid = top
        output.append(text)

        hostid_map[hostid].remove((-score, text))
        if not hostid_map[hostid]:
            del hostid_map[hostid]

        cnt += 1
        if cnt == num:
            cnt = 0
            if hq:
                existed_id = set([v[-1] for v in hq])
                for hostid, value in hostid_map.iteritems():
                    if hostid in existed_id:
                        continue
                    heapq.heappush(hq, (-value[0][0], value[0][1] ,hostid))
            output.append("")

    return output if output[-1] != "" else output[:-1]


if __name__ == "__main__":
    results = [
        "1,28,300.6,San Francisco",
        "4,5,209.1,San Francisco",
        "20,7,203.4,Oakland",
        "6,8,202.9,San Francisco",
        "6,10,199.8,San Francisco",
        "1,16,190.5,San Francisco",
        "6,29,185.3,San Francisco",
        "7,20,180.0,Oakland",
        "6,21,162.2,San Francisco",
        "2,18,161.7,San Jose",
        "2,30,149.8,San Jose",
        "3,76,146.7,San Francisco",
        "2,14,141.8,San Jose"]
    r = paginate(num=5, results=results)
    import pprint
    print pprint.pprint(r)

    expected_r = [
        "1,28,300.6,San Francisco",
        "4,5,209.1,San Francisco",
        "20,7,203.4,Oakland",
        "6,8,202.9,San Francisco",
        "7,20,180.0,Oakland",
        '',
        "6,10,199.8,San Francisco",
        "1,16,190.5,San Francisco",
        "2,18,161.7,San Jose",
        "3,76,146.7,San Francisco",
        "6,29,185.3,San Francisco",
        '',
        "6,21,162.2,San Francisco",
        "2,30,149.8,San Jose",
        "2,14,141.8,San Jose"]
    print r == expected_r
