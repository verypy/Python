count = 0
range_count = 10
for_count = 0
run = True

# while run:
#     print("Hello Cycle")
#
# while run:
#     print(f"Step = {count}")
#     count += 1
#
# while count < range_count:
#     print(f"Step = {count}")
#     count += 1
#     if count == 3:
#         print(f"Step = {count} If body")
#
# while run:
#     print(f"Step = {count}")
#     count += 1
#     if count == range_count:
#         print(f"Stop {count}")
#         break

for item in range(for_count, range_count):
    print(f"Step = {item}")

for item in range(30):
    print(f"Step = {item}")
    if item == 5:
        print(f"Item = {item}")
    if item == 10:
        print(f"Item = {item}")
    if item < 4:
        print(f"Item < {item}")
    if item >= 27:
        print(f"Item >= {item}")

for item in range(0, range_count):
    print(f"Step = {item}")
    if item == 7:
        inner_count = 0
        print(f"-- inner_count = {inner_count}")
        for inner_item in range(0, item):
            print(f"-------- Inner_Step = {inner_item}")
            if inner_item == 5:
                inner_count = inner_item
        print(f"-- inner_count = {inner_count}")
