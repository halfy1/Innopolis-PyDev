def find_common_participants(part1:str,part2:str, seporator = ",") -> list:
    group1 = part1.split(seporator)
    group2 = part2.split(seporator)
    return sorted([i for i in group1 if i in group2])


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, "|"))
