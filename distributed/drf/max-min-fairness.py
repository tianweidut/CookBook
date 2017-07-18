#coding: utf-8
def max_min_fairness(total_res, expected_requests):
    if not expected_requests:
        return []

    len_requests = len(expected_requests)
    satisfy = [0] * len_requests
    fair = total_res / float(len_requests)
    remain = total_res
    while remain:
        for i in range(len_requests):
            if expected_requests[i] <= 0:
                continue

            if expected_requests[i] - fair >= 0:
                satisfy[i] += fair
                expected_requests[i] -= fair
                remain -= fair
            else:
                satisfy[i] += expected_requests[i]
                remain -= expected_requests[i]
                expected_requests[i] = 0

        fair = remain / float(len(filter(lambda x: x > 0, expected_requests)))

    return satisfy


if __name__ == "__main__":
    print max_min_fairness(10, [2, 2.6, 4, 5])
