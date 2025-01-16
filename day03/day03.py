import re

def count_uncorrupted(path):
    uncorrupted_sum=0
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    with open(path) as file:
        for line in file:
            uncorrupted = pattern.findall(line)
            if uncorrupted:
                for match in uncorrupted:
                    mul_result = int(match[0]) * int(match[1])
                    uncorrupted_sum += mul_result
    return uncorrupted_sum

def count_uncorrupted_enable_disable(path):
    uncorrupted_sum=0
    pattern_do_dont = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")
    enable = True
    with open(path) as file:
        content = "".join(file.readlines())
        matches = pattern_do_dont.findall(content)
        if matches:
            for match in matches:
                if match[0] == "don't()":
                    enable = False
                elif match[0] == "do()":
                    enable = True
                elif match[0].startswith("mul(") and enable == True:
                    mul_result = int(match[1]) * int(match[2])
                    uncorrupted_sum += mul_result
    return uncorrupted_sum

if __name__ == "__main__":
    print("---Part One---")
    print("Total number of uncorrupted with test input: ", count_uncorrupted('input-example-day03-part1.txt'))
    print("Total number of uncorrupted: ", count_uncorrupted(('input-day03.txt')))
    print("---Part Two---")
    print("Total number of uncorrupted with disable/enable with test input: ", count_uncorrupted_enable_disable('input-example-day03-part2.txt'))
    print("Total number of uncorrupted with disable/enable: ", count_uncorrupted_enable_disable('input-day03.txt'))
