def calculate_priority(data):
    # Calculate priority based on weighted factors
    score = 0
    score += 4 * int(data['affected_people'])
    score += 3 * int(data['production_impact'])
    score += 2 * int(data['vip_status'])
    score += 1 * int(data['waiting_time'])

    if score >= 24:
        return "URGENT"
    elif score >= 18:
        return "HIGH"
    elif score >= 12:
        return "MEDIUM"
    else:
        return "LOW"

def main():
    print("Welcome to the IT issue prioritizer.")

    while True:
        # Gather inputs
        data = {}
        data['affected_people'] = int(input("On a scale of 1-3, how many people are affected? (1: Few, 3: Many): "))
        data['vip_status'] = int(input("On a scale of 1-3, how important is the user? (1: Regular, 3: VIP): "))
        data['production_impact'] = int(input("On a scale of 1-3, what's the production impact? (1: Low, 3: High): "))
        data['waiting_time'] = int(input("On a scale of 1-3, how long has the issue been waiting? (1: Short, 3: Long): "))

        # Calculate priority
        priority = calculate_priority(data)

        print(f"The issue should be marked as {priority} priority.\n")

if __name__ == "__main__":
    main()
