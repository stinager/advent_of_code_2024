def count_safe_reports():
    with open('input-day02.txt') as file:
        safe_count = 0
        for line in file:
            levels = list(map(int, line.split()))
            is_increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
            is_decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
            if is_increasing or is_decreasing:
                safe_count += 1
    return safe_count


def count_safe_reports_with_removed_level():
    def is_safe(levels):
        # Check if the levels are increasing or decreasing with differences within 1-3
        is_increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
        is_decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
        return is_increasing or is_decreasing

    safe_count = 0
    with open('input-day02.txt', 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe(levels):
                safe_count += 1
            else:
                # Remove each level to see if it becomes safe
                for i in range(len(levels)):
                    modified_levels = levels[:i] + levels[i+1:]
                    if is_safe(modified_levels):
                        safe_count += 1
                        break
    return safe_count


if __name__ == "__main__":
    print("---Part One---")
    print("Total number of safe reports: ", count_safe_reports())
    print("---Part Two---")
    print("Total number of safe reports by removing one level: ", count_safe_reports_with_removed_level())


