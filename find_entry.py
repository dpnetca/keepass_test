from pykeepass import PyKeePass

kp4_pass = "pass"
kp4 = PyKeePass("keepass_v4_test.kdbx", password=kp4_pass)
kp3_pass = "pass"
kp3 = PyKeePass("keepass_v4_test.kdbx", password=kp3_pass)

kp = kp4

divider = "\n" + "#" * 50 + "\n"

find_group = "Group1"
find_group2 = "Group2"
find_group_entry = "Entry1.1"
find_entry = "Entry3.1.1"
find_common_entry = "common_entry"

print("find Group")
all_group = kp.find_groups(name=find_group)
first_group = kp.find_groups(name=find_group, first=True)
first_group_by_name = kp.find_groups_by_name(group_name=find_group, first=True)
print(all_group)
print(first_group)
print(first_group_by_name)

print(divider)
print("find Entry in Group")
all_group_entry = kp.find_entries(group=first_group, title=find_group_entry)
first_group_entry = kp.find_entries(
    group=first_group, title=find_group_entry, first=True
)
group_entry_by_title = kp.find_entries_by_title(
    group=first_group, title=find_group_entry, first=True
)
print(all_group_entry)
print(first_group_entry)
print(group_entry_by_title)
print(divider)

print("find Entry")
all_entry = kp.find_entries(title=find_entry)
first_entry = kp.find_entries(title=find_entry, first=True)
entry_by_title = kp.find_entries_by_title(title=find_entry, first=True)
print(all_entry)
print(first_entry)
print(entry_by_title)
print(divider)

print("find Common Entry")
all_common_entry = kp.find_entries(title=find_common_entry)
first_common_entry = kp.find_entries(title=find_common_entry, first=True)
print(all_common_entry)
print(first_common_entry)
print(divider)

print("find Common Entry by Group")
group2 = kp.find_groups(name=find_group2, first=True)
all_common_entry_by_group = kp.find_entries(
    title=find_common_entry, group=first_group
)
first_common_entry_by_group = kp.find_entries(
    title=find_common_entry, group=first_group, first=True
)
print(all_common_entry_by_group)
print(first_common_entry_by_group)
