# DuckDns
Update DUCKDNS IP and TXT Records via a simple python script

Dependencies:
pip install requests (to make a web (https) request

IP = any valid ipv4 address (for whatever reason, a txt record won't update if an IP is not provided)

Copy this token and provide it to the script (when it asks) - keep this token secret

![image](https://github.com/user-attachments/assets/f6ae9cc6-d369-4ecf-8a1c-7d3939373b43)


If you get KO as a response (it means it failed)... only succeeded if you get an OK response

![image](https://github.com/user-attachments/assets/f9a50ad4-f33b-4aaa-8666-983e3a8dbfae)

You can refresh the page to see if/when it got your update... TXT records cannot be changed nor viewed via the duckdns website... 
Additionally, it takes up to 24 hours for a new or changed record to propogate.



You can check if the record has been changed by running one of these commands in your terminal: 

* nslookup -q=txt yourdomain.duckdns.org (windows, macos, and linux)

* dig txt yourdomain.duckdns.org (macos, linux)



Drawbacks: 

* Max of 5 duckdns subdomains per account

* DuckDNS only supports A, AAAA, and TXT records

* Cannot update TXT record via their website
