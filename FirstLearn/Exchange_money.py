def exchange_from_riel():
    riel = float(input("Enter amount in Riel (KHR): "))

    # First conversion to USD (auto)
    usd_rate = float(input("Enter exchange rate for 1 USD in KHR: "))
    usd = riel / usd_rate
    print(f"\n→ You get: {usd:.2f} USD")

    # Ask before doing second conversion
    another = input("\nDo you want to convert to AUD too? (yes/no): ").strip().lower()
    if another == 'yes':
        aud_rate = float(input("Enter exchange rate for 1 AUD in KHR: "))
        aud = riel / aud_rate
        print(f"→ You also get: {aud:.2f} AUD")


def exchange_from_usd():
    usd = float(input("Enter amount in USD: "))

    # First conversion to KHR (auto)
    khr_rate = float(input("Enter exchange rate for 1 USD in KHR: "))
    khr = usd * khr_rate
    print(f"\n→ You get: {khr:.2f} Riel (KHR)")

    # Ask before doing second conversion
    another = input("\nDo you want to convert to AUD too? (yes/no): ").strip().lower()
    if another == 'yes':
        aud_rate = float(input("Enter exchange rate for 1 USD in AUD: "))
        aud = usd * aud_rate
        print(f"→ You also get: {aud:.2f} AUD")

def main():
    print("===== Currency Exchange Menu =====")
    print("X - Exchange from Riel")
    print("Y - Exchange from USD")
    print("==================================")
    choice = input("Choose your option (X or Y): ").strip().upper()

    if choice == 'X':
        exchange_from_riel()
    elif choice == 'Y':
        exchange_from_usd()
    else:
        print("❌ Invalid option. Please choose 'X' or 'Y'.")


# Run the program
main()