import os
import random
import shodan
import time
import importlib
import sys



def searchapi():
    if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
        with open("api.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api.txt", "w")
        shodan_api_key = input("[!] Please enter a valid Shodan API Key: ")
        file.write(shodan_api_key)
        print ("[~] File written: ./api.txt")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    limit = 0 
    counter = 1

    try:
        print ("[~] Checking Shodan.io API Key...")
        api.search("apikey")
        print ("[^] API Key Authentication: SUCCESS..!")
        time.sleep(0.5)
        limit = int(input("\n[#] How many records are you requesting: "))
        limit = limit + 1
        apikey = input("\n[+] Enter your keyword(s): ")
        #counter = counter + 1
        for banner in api.search_cursor(apikey):
            time.sleep(5)
            print ("\n")
            print ("+" * 60)
            print ("[^] Result: %s. Search query: %s" % (str(counter), str(apikey)))
            print ("[+] IP: " + (banner["ip_str"]))
            print ("[+] Port: " + str(banner["port"]))
            print ("[+] Organization: " + str(banner["org"]))
            #print ("[+] Location: " + str(banner["location"]))
            print ("[+] Layer: " + (banner["transport"]))
            print ("[+] Domains: " + str(banner["domains"]))
            print ("[+] Hostnames: " + str(banner["hostnames"]))
            print ("[+] Services:\n\n" + (banner["data"]))
            print ("+" * 60 + "\n")
            counter += 1
            if counter >= limit:
                print ("_" * 60)
                print ("\\" * 28 + "END" + "/" *29)
                print ("¯" * 60)
                sys.exit()

    except KeyboardInterrupt:
            print ("_" * 60)
            print ("\\" * 28 + "END" + "/" *29)
            print ("¯" * 60)
            print ("\n")
            print ("[!] User Interruption Detected..!")
            time.sleep(0.5)
            print ("\n\n\t[!] See you next time Space Cowboy")
            time.sleep(0.5)
            sys.exit(1)

    except shodan.APIError as oeps:
            print ("[✘] Error: %s" % (oeps))
            sha_api = input("[*] Would you like to change the API Key? <Y/n>: ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                shodan_api_key = input("[✓] Please enter valid Shodan.io API Key: ")
                file.write(shodan_api_key)
                print ("[~] File written: ./api.txt")
                file.close()
                print ("[~] Restarting the Platform, Please wait... \n")
                time.sleep(1)
                searchapi()
            else:
                print ("")
                print ("[•] Exiting Platform... [!] See you next time Space Cowboy \n\n")
                sys.exit()

    print ("\n")
    print ("+" * 60)
    print ("+" * 28 + "END" + "+" *29)
    print ("+" * 60)
    print ("\n")
    print ("\n\n\tYeah I think its time to go \n\n")


# =====# Main #===== #
if __name__ == "__main__":
    searchapi()
