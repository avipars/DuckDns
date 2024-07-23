import requests


def update_duckdns(domain, token, txt, verbose=False, clear=False, ip="192.168.1.1"):
    # Base URL
    base_url = "https://www.duckdns.org/update?"

    # Construct URL with parameters
    url = f"{base_url}domains={domain}&token={token}&txt={txt}&ip={ip}"

    # Add optional parameters
    if verbose:
        url += "&verbose=true"
    if clear:
        url += "&clear=true"

    # encode txt as it may contain special characters and spaces
    url = url.replace(" ", "%20")
    print(url)
    # Make the request
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200 and response.text.strip() == "OK":
        print("DuckDNS update successful!")
        print("Response:", response.text)
    else:
        print("Failed to update DuckDNS.")
        print("Response code:", response.status_code)
        print("Response:", response.text)


if __name__ == "__main__":
    # Get user input
    domain = input("Enter the domain: ")
    token = input("Enter the token: ")
    txt = input("Enter the txt value: ")
    ip = input("Enter the ipv4 address (can be any random valid ip): ")
    # Ask for optional parameters
    verbose = input(
        "Do you want verbose output? (yes/no): ").strip().lower() == 'yes'
    clear = input(
        "Do you want to clear the existing txt record? (yes/no): ").strip().lower() == 'yes'

    # Update DuckDNS
    update_duckdns(domain, token, txt, verbose, clear, ip)
