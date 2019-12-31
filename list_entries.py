from pykeepass import PyKeePass

kp4_pass = "pass"
kp4 = PyKeePass("keepass_v4_test.kdbx", password=kp4_pass)
kp3_pass = "pass"
kp3 = PyKeePass("keepass_v4_test.kdbx", password=kp3_pass)

kp = kp4

divider = "#" * 50

print("list all groups:")
print(kp.groups)
print(divider)

print("for each group, list all entries:")
for group in kp.groups:
    print(group, " entries:")
    print(group.entries)
    print()
print(divider)

print("for each entry in each group, list entry details:")
for group in kp.groups:
    print(group, " entries:")
    for entry in group.entries:
        print(entry, " details:")
        print("  TITLE: ", entry.title)
        print("  USERNAME: ", entry.username)
        print("  PASSWORD: ", entry.password)
        print("  URL: ", entry.url)
        print("  NOTES: ", entry.notes)
        print("  LAST MODIFIED: ", entry.mtime)
        # print("  TAGS: ", entry.tags)  # not availalbe for test with KeePasXC
        print("  CUSTOM PROPERTIES:")
        for prop_key, prop_value in entry.custom_properties.items():
            print("    " + prop_key + ": " + prop_value)
        print()
print(divider)
