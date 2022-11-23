tcpdump host 172.20.241.9 -w measurement_cap.pcap -v #tää kirjottaa tiedoston ainoastaan linux laatikon ja mysql serverin väliltä, toi -v antaa countterin että kuin monta pakettia on kaapattu

<img src="https://user-images.githubusercontent.com/117070282/202844131-e51c4f91-a463-48eb-bcaa-b29a3ef93eb9.png" width="400"/>

Wireshark ilmottaa viimeisen yhteyden ajaksi 0.028468 = ~28,47 ms- viimeinen mysql response missä on jotain payloadiakin mukana tulee kuitenkin jo ~ 25,41 ms kohdalla

Update: jahas, tehtävä oli päivittynyt joten mennäänpäs uudestaan:

sudo tcpdump -n -i enp1s0 -v -w /tmp/kaappausnayte.pcap tcp port 80 #tänne taas tuo -v niin näki missä vaiheessa se ei enään nouse.
Wiresharkki kuva scp:llä ladatusta uudesta tiedostosta:
<img src="https://user-images.githubusercontent.com/117070282/203501081-e7710676-99c4-45ad-a695-3b7fe35ef110.png" width="400"/>

Tässä meni 5.142136 millisekuntia yhteensä.

Tutki web-palvelimen antamasta vastauksesta HTTP-otsaketietoja. Mikä oli vastauksen content-type?
text/html, charset=UTF-8
Entä server-kentässä?
Apache/2.4.52 (Ubuntu)

Sama uudestaan selaimella:
<img src="https://user-images.githubusercontent.com/117070282/203500653-2b3fea7d-3d00-44a5-8b63-a756bd4a746f.png" width="400"/>

Selain näytti ton php skriptin lataamisajaksi 95-130 ms
