# Grote Programmeer - specificaties

Grote Programmeer is dé website waarop leerlingen op het Voortgezet Onderwijs leren programmeren. Ze leren er niet alleen maar programmeren, ze leren er de kunst van het vak **informatica** en gaan aan de slag met de computer en leren dat, bij gepast gebruik, dat een enorm krachtig apparaat is.

Grote Programmeer ondersteunt leerlingen in dit leerproces en probeert hen op zoveel mogelijk manieren te helpen, dit doen we door interactief te werk te gaan: met opdrachten, quizzes en video's prikkelen we leerlingen om op hun manier de stof eigen te maken. 

Hieronder vind je de specificaties waaraan deze applicatie moet doen om het hierboven beschreven doel zo goed mogelijk te bereiken. 

## Belanghebbenden

Binnen GroteProgrammeer onderscheiden we gebruikers in een hierarchie van systeembeheerder (admin) tot leerling:
* **Systeembeheerder**: dit zijn werknemers van GroteProgrammeer die het systeem beheren en andere gebruikers ondersteunen, zij hebben alle rechten in het systeem.
* **Afdelingsleider**: elke school wijst één afdelingsleider aan die leerlingen over de klassen verdeelt en bepaalt welke lessen docenten hun leerlingen kunnen aanbieden.
* **Docent**: elke klas heeft een docent (en een docent heeft meerdere klassen) die aan zijn leerlingen lessen aanbiedt, hun voortgang kan inzien en toetsen kan nakijken.
* **Leerling**: een leerling is onderdeel van een klas en neemt deel aan lessen, maakt opdrachten en eventueel ook toetsen.

## Terminologie

* Lessen zijn pagina's met tekst, plaatjes, video's en opdrachten.
* Een hoofdstuk bestaat uit meerdere lessen (in de regel 16-20 lessen) en bevat een overkoepelend thema.

## Functionele specificaties

### Gebruikers

* Gebruikers kunnen zichzelf registeren op het systeem, zij kunnen door een gebruiker met meer rechten dan hen worden toegevoegd aan een klas of school.
* Gebruikers kunnen inloggen met hun inloggegevens
* Gebruikers hebben opties om hun inloggegevens te herstellen:
  * door een e-mail te laten sturen voor wachtwoordherstel,
  * of door hun docent hun e-mail of gebruikersnaam aan te laten passen.
* Gebruikers kunnen hun andere gegevens zelf aanpassen zodra ze zijn ingelogd.

### Klassenmanagement

* Afdelingsleiders kunnen klassen toevoegen met een naam en schooljaar en kunnen een of meerdere docenten aan die klas koppelen.
* Docenten kunnen leerlingen aan klassen waarvan zij de docent zijn koppelen of ontkoppelen.
* Docenten kunnen per klas bepalen welke lessen (of hoofdstukken) zichtbaar zijn voor hun leerlingen.

### Voortgang

* Er wordt opgeslagen welke lessen een leerling al bekeken heeft.
* De uitwerkingen van opdrachten en quizzes van leerlingen worden opgeslagen.
* De gemaakte toetsen worden opgeslagen.
* Voortgang is gebonden aan een account, dus als een leerling van klas verandert, neemt hij zijn voortgang mee. 
* Docenten kunnen de voortgang van leerlingen (in zijn geheel) verwijderen.

### Lessen

* Een leerling kan lessen die de docent heeft zichtbaar gemaakt openen en aan deelnemen, waar deelnemen lezen, bekijken en opdrachten maken betekent.
* Een leerling kan de uitwerkingen van opdrachten opslaan.
* Een leerling kan, als alle opdrachten een opgeslagen antwoord hebben, de les als compleet markeren, dit wordt ook in het lessenoverzicht aangegeven.