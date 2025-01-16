def parse_input(path):
    rules = []
    updates = []
    with open(path) as file:
        for line in file:
            if line and "|" in line:
                rules.append(list(map(int, line.strip().split("|"))))
            elif line and "," in line:
                line = line.strip()
                updates.append(list(map(int, line.split(","))))
    return rules, updates

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def is_correct_order(update, rules):
    page_positions = {page: i for i, page in enumerate(update)}
    for rule in rules:
        before, after = rule
        if before in page_positions and after in page_positions:
            if page_positions[before] >= page_positions[after]:
                return False
    return True

def re_order(rules, update):
    for page in update:
        for dependent_page in [r[1] for r in rules if r[0] == page and r[1] in update]:
            if update.index(page) > update.index(dependent_page):
                # Swap positions
                update[update.index(page)], update[update.index(dependent_page)] = (
                    update[update.index(dependent_page)],
                    update[update.index(page)],
                )
    return update

def part1(path):
    correctly_ordered_updates = []
    rules, updates = parse_input(path)
    for update in updates:
        if is_correct_order(update, rules):
            correctly_ordered_updates.append(update)
    middle_page_sum = sum(find_middle_page(update) for update in correctly_ordered_updates)
    return middle_page_sum

def part2(path):
    correctly_ordered_updates = []
    incorrectly_ordered_updates = []
    rules, updates = parse_input(path)
    for update in updates:
        if is_correct_order(update, rules):
            correctly_ordered_updates.append(update)
        else:
            incorrectly_ordered_updates.append(update)
    corrected_updates = [re_order(rules, update) for update in incorrectly_ordered_updates]
    middle_page_sum = sum(find_middle_page(update) for update in corrected_updates)
    return middle_page_sum

if __name__ == "__main__":
    print("---Part One---")
    print("Test input: ", part1('input-example-day05-part1.txt'))
    print("Total number of correctly ordered updates: ", part1('input-day05.txt'))
    print("---Part Two---")
    print("Test input: ", part2('input-example-day05-part1.txt'))
    print("Total number of corrected updates: ", part2('input-day05.txt'))