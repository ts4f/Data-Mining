# Panagiotis    Tsiavos A.M 2396

import sys
import random


def random_sampler(filename, k):
    sample = []
    with open(filename) as f:
        for n, line in enumerate(f):
            if n < k:
                sample.append(line.rstrip())
            else:
                r = random.randint(0, n)
                if r < k:
                    sample[r] = line.rstrip()
    return sample


def main():
    if len(sys.argv) != 3:
        sys.exit(-1)

    k_num = int(sys.argv[1])
    input_file = sys.argv[2]

    ret = random_sampler(input_file, k_num)
    print("RESERVOIR: " + ret.__str__())

    with open("output.txt", "w+") as o:
        x = "\n".join(ret)
        o.write(x)


if __name__ == "__main__":
    main()
