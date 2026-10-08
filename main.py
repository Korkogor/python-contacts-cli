contacts = []
N = 4
Z = 2
while True:
    cmd = input("Enter command: quit, add, contacts, find or filter ").strip().lower()
    if cmd == "quit":
        break

    elif cmd == "add":
        name = input("Enter your name: ").strip()
        if not 2 <= len(name) <= 30:
            print("Name from 2 to 30 symbols")
            continue

        phone = input("Enter your phone number: ").strip()
        ok = phone.startswith("+7") and len(phone) == 12
        # string[1:]
        for ch in phone[2:]:
            if ch not in "0123456789":  # есть ещё isdigit
                ok = False
                break
        if not ok:
            print("Phone number is not valid, format +7XXXXXXXXXX")
            continue
        contacts.append([name, phone])
        print(f"Имя {name} добавлено в записную книжку")

    elif cmd == "contacts":
        print("Всего контактов:\n", len(contacts))
        for i, contact in enumerate(contacts, 1):
            start = contact[1][:N]
            end = contact[1][-Z:]
            stealth = len(contact[1][N:-Z]) * "*"
            masked_phone = start + stealth + end
            print(f"{i}. {contact[0]} - {masked_phone}")

    elif cmd == "find":
        query = input("Enter word: ").strip().lower()
        is_any_founded = False
        for name, phone in contacts:
            if query in name.lower() or query in phone:
                start = phone[:N]
                end = phone[-Z:]
                stealth = len(phone[N:-Z]) * "*"
                masked_phone = start + stealth + end
                print(name, "-", masked_phone)
                is_any_founded = True
        if not is_any_founded:
            print("Nothing found, try again.")

    elif cmd == "filter":
        print("Filters:: 1 - first letter")
        kind = input("Filter: ").strip()
        if kind == "1":
            letter = input("Enter your letter: ").strip().upper()[:1]
            count = 0
            for name, phone in contacts:
                if name[:1] == letter:
                    start = phone[:N]
                    end = phone[-Z:]
                    stealth = len(phone[N:-Z]) * "*"
                    masked_phone = start + stealth + end
                    print(name, "-", masked_phone)
                    count += 1
            print("Find:", count)
        else:
            print("Nothing found, try again.")

    else:
        print("Invalid command. Try again.")


# count = 0
# book = ""
# while True:
#     name = input("Enter your name or \"stop\" for end the cycle: ").strip()
#     if name.lower() == "stop":
#         break
#
#     if not 2 <= len(name) <= 30:
#         print("Name from 2 to 30 symbols")
#         continue
#
#     phone = input("Enter your phone number: ").strip()
#     ok = phone.startswith("+7") and len(phone) == 12
#     # string[1:]
#     for ch in phone[2:]:
#         if ch not in "0123456789": #есть ещё isdigit
#             ok = False
#             break
#     if not ok:
#         print("Phone number is not valid, format +7XXXXXXXXXX")
#         continue
#
#     count += 1
#     book += f"{count}. {name} - {phone}\n"
#     # f - форматированная строка
#     print(f"Имя {name} добавлено в записную книжку")
# print("Всего контактов:\n", book)


# contacts = []
# while True:
#     name = input("Enter your name or stop: ").strip()
#     if name.lower() == "stop":
#         break
#     phone = input("Phone number: ").strip()
#     contacts.append([name, phone])
#
# print("All contacts: ", len(contacts))
# for i, c in enumerate(contacts, 1):
#     print(f"{i}. {c[0]} - {c[1]}")
#
# found = []
# q = input("Введите имя для поиска: ").strip().lower()
# for name, phone in contacts:
#     if q in name.lower() or q in phone:
#         found.append([name, phone])
# if not found:
#     print("Ничего не найдено")
# for name, phone in found:
#     print(name, "-", phone)
