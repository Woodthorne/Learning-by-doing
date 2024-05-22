__1. Vad är ett neuralt nätverk?__<br>
En artificiell modell för predikering som använder sig av dolda lager av 'neuroner' för att succesivt ta sig fram till 'rätt' svar. Konceptet är inspirerat av hjärnan fungerar.

__2. Vad är en convolutional neural network (CNN)?__<br>
En CNN använder sig av ett 'convolutional layer' för att bryta ner datan i mindre matriser för att fokusera på särskilda egenskaper.

__3. Hur fungerar convolutional layers?__<br>
Modellen har ett filter (oftast en 3x3 matris) med vikter som används för att panorera över datan och beräkna skalärprodukten som sen skickas in i en mindre resultatmatris.

__4. Vad är filter/kärnor och hur används de i CNNs__<br>
En tvådimensionell matris med viktvärden som panorerar över datan och används för att beräkna skalärprodukten av vad den 'ser'.

__5. Vad är padding och stride?__<br>
Padding avgör vad som händer när filtret inte har någon data från inputmatrisen på grund av olika dimensioner:
* _Valid padding_ avbryter panoreringen när tomma datan stöts på.
* _Same padding_ säkerställer att output matrisen har samma dimensioner som input matrisen.
* _Full padding_ fyller saknade platser i filtret med nollor.

Stride bestämmer hur många steg filtret tar när det panorerar över startdatan.

__6. Vad är pooling layers och varför används dem?__<br>
Likt ett convolution layer används ett filter, men istället för vikter appliceras en aggregeringsfunktion:
* _max pooling_ sätter maxvärdet i filtret till nya matrisen.
* _average pooling_ sätter genomsnittsvärdet i filtret till nya matrisen.

Meningen är att förenkla matrisen och förhindra overfitting.

__7. Hur fungerar fully connected layers?__<br>
I ett _fully connected layer_ är alla neuroner kopplade till alla neuroner i ett föregående lager. Detta gör att lagret kan klassificera input genom att titta på värden från flera tidigare neuroner och kombinera dessa för att räkna ut en sannolikhet med hjälp av exempelvis _soft max activation_.

__8. Vad är en aktiveringsfunktion och vilka används i CNNs?__<br>
En aktiveringsfunktion avgör om en neuron aktiveras eller inte av inputdata.
* _ReLu_ ger ett värde från 0 och uppåt, beroende på om neuronens värde är lika med eller större än noll.
* _Sigmoid_ ger ett värde mellan 0 och 1.
* _Tanh_ ger ett värde mellan -1 och 1.

__9. Hur tränas CNNs?__<br>
Vikter och filter tilldelas godtyckligt för första iterationen. Inför varje efterföljande iteration utvärderas varje lagers filter och vikter genom att räkna ut felets grad från sista till första lagret.
*_Backpropagation_ innebär att vi går från sista lager till första. Detta för att minska mängden beräkningar som krävs.
*_Gradient descent_ är en metod där vi försöker hitta det lokala minimivärdet för felet i en neuron.

__10. Hur kan överanpassning förhindras?__<br>
* _Dropout_ tar slumpmässigt bort vissa neuroner i ett lager för att se om resultatet påverkas.
* _Data augmentation_ använder olika metoder för att justera datan, genom att exempelvis rotera eller ändra storlek på datan.
* _Regularization_ skiftar vikterna hos lågpresterande data så att deras inverkan minimeras. 

__11. Vad är en loss function och vilken används för bildklassificering?__<br>
En _loss function_ används för att beräkna resultatets fel i varje iteration. Genom att använda _soft max_ kan vi till exempel räkna ut avståndet mellan prediktion och faktiskt resultat.

__12. Hur utvärderar man prestandan hos en CNN?__<br>


__13. Vad är transfer learning och hur kan det tillämpas i CNNs__<br>


__14. Vilka är de vanligaste arkitekturerna för CNNs?__<br>


__15. Hur kan man implementera en CNN i praktiken?__<br>
