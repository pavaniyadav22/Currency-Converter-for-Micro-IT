import requests

def convert_currency(from_currency, to_currency, amount):
    try:
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(f"Full API response: {data}")  # Debug print
            if data.get("result") is not None:
                return data["result"]
            else:
                print("❌ Conversion failed. 'result' not found in response.")
        else:
            print(f"❌ API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Exception occurred: {e}")

    return None

