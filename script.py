import urllib.parse


def duckdns_url(domain, token, txt, verbose=False, clear=False, ip=None, ipv6=None):

    txt_encoded = urllib.parse.quote(txt)

    # Base URL
    base_url = "https://www.duckdns.org/update?"

    # Construct URL with parameters
    url = f"{base_url}domains={domain}&token={token}&txt={txt_encoded}"

    # Add optional parameters
    if verbose:
        url += "&verbose=true"
    if clear:
        url += "&clear=true"
    if ip:
        url += f"&ip={ip}"
    if ipv6:
        url += f"&ipv6={ipv6}"

    # encode txt as it may contain special characters and spaces
    print("Update DNS Record:")
    print("Enter this in your web browser: ", url)

    print("or via CLI: ")
    print(f"curl \"{url}\"")

    print("To check DNS record (via CLI):")

    print("Cross platform command:")
    print(f"nslookup -q=txt {domain}.duckdns.org")

    print("For MacOS or Linux only, this also works:")
    print(f"dig {domain}.duckdns.org txt")

    print("(Optional) Verify that your subdomain shows up:")
    print(f"dig @ns1.duckdns.org {domain}.duckdns.org")

def main():
    # Get user input
    domain = input("Enter the subdomain (without duckdns.org): ")
    domain = domain.strip() 

    token = input("Enter the token (keep this private): ")
    token = token.strip()
    
    txt = input("Enter the txt value: ")

    
    ip = None #defaults
    ipv6 = None
    # Ask for optional parameters
    consent_ipv4 = input(
        "Do you want to add/update the ipv4 address? (yes/no): ").strip().lower() == 'yes'
    if consent_ipv4:
        ip = input("Enter the ipv4 address (can be any random valid ipv4 address): ")
    consent_ipv6 = input(
        "Do you want to add/update the ipv6 address? (yes/no): ").strip().lower() == 'yes'
    if consent_ipv6:
        ipv6 = input("Enter the ipv6 address (can be any random valid ipv6 address): ")

    verbose = input(
        "Do you want verbose output? (yes/no): ").strip().lower() == 'yes'
    clear = input(
        "Do you want to clear the existing txt record? (yes/no): ").strip().lower() == 'yes'

    #  DuckDNS
    duckdns_url(domain, token, txt, verbose, clear, ip, ipv6)

if __name__ == "__main__":
    main()
