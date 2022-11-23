import pandas as pd
url = "http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=77"
csv = pd.read_csv(url, delimiter=';')
csv.to_csv('groupid77data.csv')
print("Tiedosto luotu")