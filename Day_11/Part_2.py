class Monkey: 

    def __init__(self, items, operation, operation_num, test_num, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.operation_num = operation_num
        self.test_num = test_num
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.checked_items = 0

    def interact_with_item(self):

        cur = self.items.pop(0)

        operation_num = self.operation_num

        if operation_num == "old":
            operation_num = cur
        else: 
            operation_num = int(operation_num)

        if self.operation == "*":
            cur = cur * operation_num
        else:
            cur = cur + operation_num

        self.checked_items += 1

        if cur % self.test_num == 0:
            return (cur, self.true_monkey)
        else:
            return (cur, self.false_monkey)

    def get_item_length(self):
        return len(self.items)

    def get_num_checked_items(self):
        return self.checked_items

    def catch_item(self, item):
        self.items.append(item)

file = open('Day_11/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

monkeys = []
values = []

mod = 1

for i in [0,7,14,21,28,35,42,49]:
    starting_items = [int(x_) for x_ in lines[i+1].replace("Starting items: ","").split(",")]
    operation = lines[i+2].split("=")[1][5]
    opertation_num = lines[i+2].split(operation)[1].strip(" ")
    test_num = int(lines[i+3].replace("Test: divisible by ","").strip(" "))
    true_monkey = int(lines[i+4][-1])
    false_monkey = int(lines[i+5][-1])
    monkey = Monkey(starting_items, operation, opertation_num, test_num,
    true_monkey,false_monkey)
    mod = mod* test_num
    monkeys.append(monkey)

for i in range(10000):
    for monkey in monkeys:
        while monkey.get_item_length() > 0:
            it = monkey.interact_with_item()
            monkeys[it[1]].catch_item(it[0]%mod)

active_monkeys = []
for monkey in monkeys:
    active_monkeys.append(monkey.get_num_checked_items())

print(sorted(active_monkeys))
print(sorted(active_monkeys)[-1]*sorted(active_monkeys)[-2])

#5105