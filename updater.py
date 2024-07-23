import requests
import urllib.parse


def update_duckdns(domain, token, txt, verbose=False, clear=False, ip="192.168.1.1", ipv6=None):

    txt_encoded = urllib.parse.quote(txt)

    # Base URL
    base_url = "https://www.duckdns.org/update?"

    # Construct URL with parameters
    url = f"{base_url}domains={domain}&token={token}&txt={txt_encoded}&ip={ip}"

    # Add optional parameters
    if verbose:
        url += "&verbose=true"
    if clear:
        url += "&clear=true"
    if ipv6:
        url += f"&ipv6={ipv6}"

    # encode txt as it may contain special characters and spaces
    print("URL", url)
    # Make the request
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200 and "OK" in response.text.strip():
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
    consent_ipv6 = input(
        "Do you want to add/update the ipv6 address? (yes/no): ").strip().lower() == 'yes'
    if consent_ipv6:
        ipv6 = input("Enter the ipv6 address (can be any random valid ip): ")
    else:
        ipv6 = None
    # Ask for optional parameters
    verbose = input(
        "Do you want verbose output? (yes/no): ").strip().lower() == 'yes'
    clear = input(
        "Do you want to clear the existing txt record? (yes/no): ").strip().lower() == 'yes'

    # Update DuckDNS
    update_duckdns(domain, token, txt, verbose, clear, ip, ipv6)
