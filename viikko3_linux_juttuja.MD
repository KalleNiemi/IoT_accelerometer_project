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

Tee omalle kannettavalle TCP-asiakasohjelma Pythonilla, joka hakee, käsittelee ja tallentaa 172.20.241.9 -palvelimelta (HTTP-siirron yli) dataa omalle kannettavalle CSV-tiedostoksi. Käytä HTTP-yhteyteen suosiolla jotain valmista kirjastoa (koska HTTP on erittäin monimutkainen protokolla alkaa kirjoittamaan tyhjästä itse suoraan socketin päälle):

Löytyy mainbranchista koodeista

Tee uusi Python-skripti tietojen hakemiseksi, mutta nyt sellainen, joka hakee datat suoraan tietokannasta (172.20.241.9) MySQL-rajapinnan kautta:

Löytyy mainbranchista koodeista. ***Tietokantapalvelimen tunnus pitää olla joko erillisenä ympäristömuuttujana tai erillisessä tiedostossa mikä on .gitignoressa (mieti miksi näin?)*** Tämä on nyt erillisessä tiedostossa, ja ei toki ole hyvä pistää mitään tietokannan salasanoja julkiseen internettiin vaikka kuinka olisi privaatti repo kyseessä.

Tallenna ja analysoi oman TCP-asiakasohjelman liikennettä Wiresharkilla ja:

   Etsi liikenteestä siirrossa käytetyt TCP-lähde- ja kohdeportit: Lähdeportti = 58719 , kohdeportti = 80
   Tutki MySQL-siirron hyötykuormaa ja etsi sieltä siirrettyä dataa: Noh payloadit vaikuttaa tulevan suurimmaksi osaksi 1425 tavun paketteina UDP protokollalla ja ne on kyllä sen verran kryptisiä että ei sieltä varsinaisesti mysql liittyvää infoa löydy. Etänä teen tätä nyt ja tosiaan on tuo OpenVPN päällä.
    

Määrittele Linux-palvelimeen salasanaton SSH-kirjautuminen ed25519-avaimella:

<img src="https://user-images.githubusercontent.com/117070282/205432692-e53fad94-43fc-495f-9ce3-9ceb799c4155.png" width="400"/>

Ota käyttöön Tailscale-palvelun ilmaisversio ja luo sillä yhteys oman kannettavan ja oman Linux-palvelimen välille.

<img src="https://user-images.githubusercontent.com/117070282/206850536-00e7ec80-5cab-443b-a2d4-632d330cfd67.png" width="400"/>

Ansible:

No kyllähän tämä komento menee läpi mutta joku vika tossa on vaikka tein sen hosts tiedoston:

![kuva](https://user-images.githubusercontent.com/117070282/206855474-68f11306-f0c0-4ac3-a1e0-c01695463b5f.png)


