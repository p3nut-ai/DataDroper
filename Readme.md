## DataDroper

DataDroper is a proof-of-concept (PoC) Python script that exploits a known, unsecured endpoint to extract sensitive data. It is designed to demonstrate the real-world impact of endpoint misconfigurations during security assessments, red teaming exercises, or CTF challenges.

⚠️ Warning: Use this tool only on systems you own or have explicit permission to test. Misuse is illegal and unethical.

🚀 Features

Targets a specific vulnerable endpoint (URL must be provided by the user)

Extracts and dumps exposed sensitive information (environment variables, credentials, tokens, etc.)

Simple and fast: minimal dependencies and easy to customize

🛠️ Prerequisites

Python 3.6+

requests library

pip install requests

📥 Installation

Clone the repository

git clone https://github.com/p3nut-ai/DataDroper.git
cd DataDroper



⚙️ Configuration

Uncomment data-dropping sections

In datadroper.py, there are commented blocks responsible for dropping all extracted data to the attacker’s endpoint. To enable full data exfiltration, locate:

target_link = "http://your-URL.com/"


Provide the vulnerable endpoint URL

This PoC does not include a target URL. You must supply the exact vulnerable endpoint via the command line when running the script.

▶️ Usage

Run the script with the target endpoint URL as an argument:

python data_droper.py 



📝 POC

![alt text](https://cdn.discordapp.com/attachments/1332707393498255440/1362514265851826428/image.png?ex=6802abcb&is=68015a4b&hm=273b11f597d3946bb358b28c0fabd8b3d586755b91adf5911a3ae2955c72e58c&)
