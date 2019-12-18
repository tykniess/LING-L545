Parser
======
The udpipe-trained German Parser performed fairly well, with an unlabelled attachment score (UAS) of 84.90 and a labelled attachment score (LAS) of 80.12.

Performance
======
1. In sentence test-s1, _Der Hauptgang war in Ordnung , aber alles andere als umwerfend ._, The parser got quite confused and made Ordnung a direct dependent of Root and head of umwerfend (and therefore the rest of the sentence after the coordinating conjunction). The gold standard has it correctly that umwerfend is dependent of Root. 

2. In sentence test-s2, _Ich habe dort 2007 meinen OWD gemacht und weil mir das Tauchen so gefiel hab ich dort noch in dem selben Jahr den AOWD und den Deep drangehängt ._, the gold standard correctly has the two past participles as heads: Root -> gemacht -> drangehängt. The parser got thrown off by the preterite finite verb gefiel and broke up the connection, resulting in a structure Root -> gemacht -> gefiel -> drangehängt.

3. In sentence test-s3, _Ist ja wohl ein Witz ._, everything is perfect.

4. In sentence test-s4, _"Bitte Termin im Internet machen."_, the trained parser incorrectly interpreted the punctuation " as a dependent of Termin. In fact, this was very consistent across the board: initial punctuation was always interpreted as a dependent of the first noun in the sentence.

5. In sentence test-s5, _" Welcher Kollege hat Ihnen denn 99 gesagt ? "_ the punctuation _"_ is interpreted as a dependent of the first noun in the sentence rather than of the head verb gesagt. Furthermore, _'denn'_ was determined to be dependent of 99 for some reason.

6. In sentence test-s6 (which was particularly complex), _( Bei den Damen und Herren des besagten Mobilfunkanbieters bin ich in dem Gegensatz dazu bisher ausschließlich auf arrogante Unkenntnis gestossen ) ._, _'dazu'_ was interpreted as a dependent of _'gestossen'_ (a verb) rather than _'Gegensatz'_ (a noun).

7. In sentence test-s7 _10 Euro günstiger selbst hätte kaufen können ._, the phrase _'10 Euro günstiger'_ is misanalyzed. Instead, Euro is made a dependent of kaufen, with two daughters: 10 and selbst, where günstiger is a dependent of selbst. This is extremely odd because in the properly annotated gold standard, 10 is a dependent of Euro which is a dependent of günstiger which is a direct dependent of head kaufen.

8. In sentence test-s8 _Aber mal abwarten , was sich in näherer Zukunft abspielt ...._, all is well.

9. In sentence test-s9, _Aber über die Freundlichkeit , Zuverlässlichkeit und Komptenz des gesamten Team kann man nur eines Sagen -- PEFERKTION_, the  CCONJ _'aber'_ is falsely interpreted to be dependent of _'PERFEKTION'_ and head of the entire first half of the sentence. Other than that, though, the parser nailed the sentence up to the end of the prepositional phrase dependent upon _'über'_. It also seems to have been thrown off by _'PERFEKTION'_ because it interprets it as a head rather than _'sagen'_ which as a verb should not be capitalized but is incorrect in the gold standard.

10. In sentence test-s10, _Absolut empfehlenswert ist auch der Service ._, the ADV _'auch'_ is falsely interpreted as a dependent of _'Service'_. Otherwise, it looks great.