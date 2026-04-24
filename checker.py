mist=[{"mac": "AA:BB:CC:11", "vlans": [10, 20, 30]},{"mac": "AA:BB:CC:12", "vlans": [40, 50, 60]}
      ]
aruba=[{"mac": "aa:bb:cc:11", "vlans": [10, 20, 30]},{"mac": "aa:bb:cc:12", "vlans": [40, 50, 60]},{"mac": "aa:bb:cc:13", "vlans": [70, 80, 90]}
      
      ]
def findMismatches(s1,s2):
    mismatch=[]
    for i in range(len(s1)):
        if s1[i]['mac'].lower() in s2[i]['mac'].lower():
            if s1[i]['vlans'] != s2[i]['vlans']:
                mismatch.append(s1[i]['mac'])
        
    if len(mismatch) != 0: 
        return mismatch
    else:
        return "No mismatches found"
    

re=findMismatches(mist,aruba)
print(re) 