def hanging_out():
    fire_safe, events = map(int, input().split())
    total_people = 0
    groups_not_allowed = 0

    for _ in range(events):
        parts = input().split()
        if len(parts) != 2:
            # Unexpected format — skip or handle
            continue
        action, num_str = parts
        # optionally: convert action to lowercase
        action = action.strip().lower()
        try:
            x = int(num_str)
        except ValueError:
            # Invalid number — skip
            continue

        if action == "enter":
            if total_people + x > fire_safe:
                groups_not_allowed += 1
            else:
                total_people += x
        elif action == "leave":
            total_people -= x
        else:
            # Unknown action — do nothing
            pass

    print(groups_not_allowed)

if __name__ == "__main__":
    hanging_out()
