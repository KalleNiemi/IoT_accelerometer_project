tcpdump host 172.20.241.9 -w measurement_cap.pcap -v #tää kirjottaa tiedoston ainoastaan linux laatikon ja mysql serverin väliltä, toi -v antaa countterin että kuin monta pakettia on kaapattu

<img src="https://user-images.githubusercontent.com/117070282/202844131-e51c4f91-a463-48eb-bcaa-b29a3ef93eb9.png" width="400"/>

Wireshark ilmottaa viimeisen yhteyden ajaksi 0.028468 = ~28,47 ms- viimeinen mysql response missä on jotain payloadiakin mukana tulee kuitenkin jo ~ 25,41 ms kohdalla
