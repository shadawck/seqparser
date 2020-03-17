# SeqParse


## Install prerequisite

Install python3 module
```bash
pip3 install -r requirements.txt
# If you don't have pip3 
python3 -m pip install -r requirements.txt
```

And that's it, you're ready to go ! 

## seqparse

### Find command 


Search through all regex from regIndex.txt in test/random.txt
```bash
./seqparse.py find --all -f regindex.txt -s test/random.txt

validEmail: ['sometest@gmail.com']
ip_adress: ['198.127.158.45', '192.168.1.1']
macAdress: ['406068601171', '454415000055', 'FF:FF:FF:FF:FF:FF', '00:A0:C9:14:C8:29', '00:00:5E:00:01:28', '406067601871', '006129876543', '406017401951']
bitcoin: ['3npMjJYuAEGyZr1uLBsDWSwz1xuPzdxcL4Y', '3cLwdE1xcNGpx3usW9jzYC3erDS3d', '17ZtZF9r8BruWo62ddHYH6ucMVUfKQR', '1kV8NfTA7X1bh5cPekpWmEfg6MiD', '3QWz49mGLkg1gw9T8kUWV8TeCxFCJKpKmQ7', '3XpULLXUcTpBp1VUh3aDYrkEymySWm8pjnJ', '1j2Gjjehdi5KRQW3yHCEWjCHZpn9sxDupN', '13rV3W8pVTKjYXVUK6eS9E4AyMn3YuEQa9E', '39ui5NBjs82TkbTKrV2nkub4RX7hjDwdD', '3935XvxKuSDXHgd1EyaNvUHUr78nspTLCBF', '1XVLr6QYeCSFkAT2hc43uKrZEJsL', '33689657852p1234AxX7kbN4K8D1f1m1rD7', '1Wrcy4pXFfHJsr4xhATMQdqkMKsYgDPRjHu', '197TPY8Rviih6ykQ6aikdc7p5gcJG', '3DbEb6pqptsmmW5TnfpQ9Sd2fv47USFL', '1MyXo1o3vPeWB1tDHfvKVrCmChCNJ', '3E1DLQUmm7u2vePTa2Qz9LrUp2QnfvepQvc', '1zsbg36cXCzD4kQpuhQUe1j2V2hPyntdsWH', '1b61jMdJwGoejWTc1TF8Y23E722vn4RTa', '3vkiwibfiwucd6vxijskbhpjdyajmzeor4m', '1F1vvS15QLi7YE4nkYn239Wd5vDXL49Qs', '1xk4RwYpaySpdCPmsh61FpWKuGr7K1Gvsfs', '1zsbg36cXCzD4kQpuhQUe1j2V2hPyntdsWH', '1b61jMdJwGoejWTc1TF8Y23E722vn4RTa']
onion_v2: ['c4i7yopvpo4p7cyd.onion']
onion_v3: ['jamie3vkiwibfiwucd6vxijskbhpjdyajmzeor4mc4i7yopvpo4p7cyd.onion']
```

Search a specific regex from regIndex.txt in test/random.txt
```bash
./seqparse.py find --partial ip_adress -f regindex.txt -s test/random.txt -s test/random.txt

ip_adress: ['198.127.158.45', '192.168.1.1']
```

# List Command 
Just list all the regular expression available in regIndex.txt
```bash 
./seqparse.py list

validEmail
ip_adress
macAdress
bitcoin
onion_v2
onion_v3
...
```
