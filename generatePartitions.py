def generate_partitions(numjobs):
    workers = []
    for i in range(1, numjobs + 1):
        workers.append(i)

    def partitions(workers):
        result = []
        if len(workers) == 0:
            return [[]]
        for partition in partitions(workers[1:]):
            i = 0
            result.append([workers[:1]] + partition)
            for subset in partition:
                result.append(partition[:i] + [workers[:1] + subset] + partition[i + 1:])
                i = i + 1
        return result

    return partitions(workers)
