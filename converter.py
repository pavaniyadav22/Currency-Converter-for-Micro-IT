from utils import convert_currency

def main():
    print("\n💱 Currency Converter - Real-time")
    
    from_currency = input("Enter base currency (e.g. USD): ").upper()
    to_currency = input("Enter target currency (e.g. INR): ").upper()
    
    try:
        amount = float(input(f"Enter amount in {from_currency}: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a numeric value.")
        return

    result = convert_currency(from_currency, to_currency, amount)

    if result is not None:
        print(f"✅ {amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("❌ Conversion failed. Please check your inputs or internet connection.")

if __name__ == "__main__":
    main()
