Här är en fullständig och utvecklad uppgift för **"Räddningsrobot: Hybridagent i katastrofscenario"**:

---

### **Uppgift: Räddningsrobot – Hybridagent i katastrofscenario**

#### **Scenario**
Du är en AI-utvecklare som ska skapa en hybridagent för en räddningsrobot som verkar i en katastrofzon, till exempel efter en jordbävning. Katastrofzonen är en simulerad 2D-värld där roboten ska navigera mellan hinder, undvika faror och rädda offer innan tiden och batteriet tar slut.

---

### **Mål**
- Designa en hybridagent som kombinerar reflexbaserat beteende, modellbaserad planering, målbaserad prioritering och nyttobaserad optimering.
- Implementera en simulering där agenten kan testas och utvärderas.
- Utforska hur olika komponenter samverkar i komplexa miljöer.

---

### **Kravspecifikation**
1. **Miljön:**
   - Representeras som ett 10x10 rutnät.
   - Varje cell kan innehålla:
     - Tom mark
     - Hinder (väggar, bråte)
     - Ett "offer" (målet för räddning)
     - En fara (t.ex. giftig gas)
   - Roboten har en begränsad synradie på 3 celler.
   
2. **Roboten:**
   - Bör kunna röra sig upp, ner, vänster eller höger.
   - Startar i en slumpmässig position och har en batterinivå som minskar med varje rörelse.
   - Kan "rädda" ett offer genom att stanna på samma cell som offret i 2 sekunder.

3. **Hybridagentens komponenter:**
   - **Reflexbeteende:** Undvik direkt faror (t.ex. flytta bort från giftig gas).
   - **Modellbaserad planering:** Bygg en karta över den utforskade miljön.
   - **Måldrivet beteende:** Prioritera att rädda offer.
   - **Nyttobaserad optimering:** Maximera antalet räddade offer inom begränsad tid och batterinivå.

4. **Uppdragsmål:**
   - Rädda så många offer som möjligt.
   - Minimera tid och batteriförbrukning.

---

### **Arbetsmoment**

#### **1. Reflexbeteende**
- Implementera en funktion som låter roboten omedelbart undvika faror.
- Exempel: Om giftig gas upptäcks inom synradien, flytta bort från gasen.

#### **2. Modellbaserad planering**
- Skapa en funktion som låter roboten bygga en karta över miljön baserat på sin rörelse.
- Exempel: Kartan uppdateras med varje utforskat område, inklusive identifiering av hinder och offer.

#### **3. Måldrivet beteende**
- Implementera en algoritm som låter roboten prioritera att nå celler med offer.
- Exempel: Använd en enkel sökalgoritm som A* för att hitta den kortaste vägen till närmaste offer.

#### **4. Nyttobaserad optimering**
- Skapa en funktion som utvärderar möjliga handlingar baserat på en nyttofunktion.
- Exempel på nyttofunktion:  
  $$
  U = 10 \times (\text{Antal räddade offer}) - 1 \times (\text{Batteriförbrukning}) - 5 \times (\text{Tid förbrukad})
  $$

#### **5. Integrering och testning**
- Kombinera alla komponenter till en hybridagent.
- Testa agenten i olika simulerade miljöer och utvärdera dess prestanda.

---

### **Simuleringsmiljö**
För att implementera uppgiften kan du använda följande verktyg:
- **Python** med bibliotek som:
  - `Pygame` för grafisk simulering.
  - `NetworkX` eller egen implementation för sökalgoritmer (t.ex. A*).
- **Alternativ:** Bygg en enklare textbaserad simulering om grafisk miljö inte är möjlig.

---

### **Leverabler**
1. **Kod:**
   - En Python-fil som innehåller implementeringen av räddningsroboten.
2. **Dokumentation:**
   - En kort rapport (1-2 sidor) som beskriver hur hybridagenten fungerar och hur den utvärderades.
3. **Resultat:**
   - Statistik över prestanda, t.ex. antal räddade offer, tid och batteriförbrukning.

---

### **Utvärderingskriterier**
1. **Funktionalitet:**
   - Fungerar agenten enligt kravspecifikationen?
2. **Effektivitet:**
   - Hur många offer kan agenten rädda med minimala resurser?
3. **Kreativitet:**
   - Har studenten lagt till unika lösningar eller förbättringar?
4. **Kodkvalitet:**
   - Är koden välstrukturerad och läsbar?
5. **Dokumentation:**
   - Är agentens design och resultat tydligt presenterade?

---

### **Bonusutmaningar**
1. Implementera flera räddningsrobotar som samarbetar.
2. Lägg till dynamiska händelser, t.ex. nya faror som uppstår över tid.
3. Utöka nyttobaserad optimering med fler faktorer, som säkerhet och samarbete.

---

Behöver du en kodmall eller exempel på en grundläggande implementation?