Tagger Comparison
=====
1. UD tagger.
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
UPOS       |     94.74 |     94.74 |     94.74 |     94.74
2. perceptron tagger.
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
UPOS       |     90.52 |     90.52 |     90.52 |     90.52
3. unigram tagger.
Accuracy of 1.3777513830361266e-05%

Constraint Grammar
=====

DELIMITERS = "." ;

LIST DET = DET ;
LIST PUNCT = PUNCT ;
LIST ADP = ADP ;
LIST VERB = VERB ;
LIST SCONJ = SCONJ ;
LIST CCONJ = CCONJ ;
LIST ADV = ADV ;

SECTION

REMOVE DET IF (1C PUNCT) ;
SELECT ADP IF (-1C VERB) ;
SELECT SCONJ IF (-1C SCONJ) ;
SELECT CCONJ IF (-1C VERB) ;



Perceptron Tagger
=====

* out of the box tagger:
% python3 conll17_ud_eval.py --verbose UD_Dutch-Alpino/nl_alpino-ud-test.conllu nl-ud-test.out 
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     92.72 |     92.72 |     92.72 |     92.72
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     92.72 |     92.72 |     92.72 |     92.72
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

* in tagger.py, I added a category for a 2-character suffix (preterite forms). This didn't appear to have an immense effect on the dev file. 
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.16 |     94.16 |     94.16 |     94.16
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     94.16 |     94.16 |     94.16 |     94.16
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

* I then added a similar 2-character prefix option 
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.28 |     94.28 |     94.28 |     94.28
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     94.28 |     94.28 |     94.28 |     94.28
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

* I then added a similar 3-character prefix option ('aan-', 'ver-', 'ont-', etc.)
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.39 |     94.39 |     94.39 |     94.39
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     94.39 |     94.39 |     94.39 |     94.39
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

* This actually did not help, so I deleted it and tried something else. I removed the 3-character suffix.

* This made it worse, so I reverted.
* I decided having the prefix information of i+2 would be important in In simple Subject-Auxiliary-Object-PP sentences since PP almost always begins with 'ge'. This helped.
Iter 4: 179987/185999=96.76772455765891
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.06 |     94.06 |     94.06 |     94.06
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     94.06 |     94.06 |     94.06 |     94.06
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

* I then did it with i+1 prefixes and got slightly improved results.
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.08 |     94.08 |     94.08 |     94.08
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     94.08 |     94.08 |     94.08 |     94.08
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

LOGS
=====


Adding UDPipe to the PATH
-----

$ PATH=/Users/tyler/udpipe/src/:$PATH
$ export PATH     

Training the UD tagger.
-----

$ cat fi_tdt-ud-train.conllu | udpipe --tokenizer=none --parser=none --train fi.udpipe
Loading training data: done.
Training the UDPipe model.
Tagger model 1 columns: lemma use=1/provide=1, xpostag use=1/provide=1, feats use=1/provide=1
Creating morphological dictionary for tagger model 1.
Tagger model 1 dictionary options: max_form_analyses=0, custom dictionary_file=none
Tagger model 1 guesser options: suffix_rules=8, prefixes_max=4, prefix_min_count=10, enrich_dictionary=6
Tagger model 1 options: iterations=20, early_stopping=0, templates=tagger
Training tagger model 1.
Iteration 1: done, accuracy 82.26%
Iteration 2: done, accuracy 94.93%
Iteration 3: done, accuracy 97.18%
Iteration 4: done, accuracy 98.12%
Iteration 5: done, accuracy 98.70%
Iteration 6: done, accuracy 99.04%
Iteration 7: done, accuracy 99.21%
Iteration 8: done, accuracy 99.36%
Iteration 9: done, accuracy 99.51%
Iteration 10: done, accuracy 99.61%
Iteration 11: done, accuracy 99.62%
Iteration 12: done, accuracy 99.71%
Iteration 13: done, accuracy 99.71%
Iteration 14: done, accuracy 99.78%
Iteration 15: done, accuracy 99.76%
Iteration 16: done, accuracy 99.80%
Iteration 17: done, accuracy 99.83%
Iteration 18: done, accuracy 99.86%
Iteration 19: done, accuracy 99.88%
Iteration 20: done, accuracy 99.90%
The trained UDPipe model was saved.

testing the trained tagger.
-----
$ cat fi_tdt-ud-test.conllu| udpipe --tag fi.udpipe > fi_tdt-ud-test_output.connlu
Loading UDPipe model: done.

%%http://universaldependencies.org/conll17/eval.zip%%

$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu fi_tdt-ud-test_output.connlu

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.74 |     94.74 |     94.74 |     94.74
XPOS       |     95.89 |     95.89 |     95.89 |     95.89
Feats      |     91.00 |     91.00 |     91.00 |     91.00
AllTags    |     89.98 |     89.98 |     89.98 |     89.98
Lemmas     |     84.97 |     84.97 |     84.97 |     84.97
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00 

trying a perceptron tagger
-----

$ git clone https://github.com/ftyers/conllu-perceptron-tagger.git
$ cd conllu-perceptron-tagger
$ conllu-perceptron-tagger % cat ../UD_Finnish-TDT/fi_tdt-ud-train.conllu| python3 tagger.py -t model.dat
163223
Iter 0: 132054/163223=80.90403925917303
163208
Iter 1: 144840/163223=88.73749410315949
163213
Iter 2: 152012/163223=93.13148269545346
163210
Iter 3: 156021/163223=95.58763164505002
163213
Iter 4: 158061/163223=96.8374555056579

$ cat ../UD_Finnish-TDT/fi_tdt-ud-test.conllu| python3 tagger.py model.dat > perceptron_output

$ cd ../UD_Finnish-TDT/
$ cd UD_Finnish-TDT 
$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu ../conllu-perceptron-tagger/perceptron_output 
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.52 |     90.52 |     90.52 |     90.52
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.52 |     90.52 |     90.52 |     90.52
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

unigram tagger
-----
%I made a veeeeeery simple unigram tagger (which is basically just a unigram dictionary lookup tool). It performs absolutely terribly: nltk-fi-tagger.py
%To improve it I would suggest looking at headwords and not just surface forms, syntactic annotation and context.


morphological analysis
-----

echo "Однако стиль работы Семена Еремеевича заключался в том, чтобы принимать всех желающих и лично вникать в дело." | python3 ud-scripts/conllu-analyser.py ru-analyser.tsv | vislcg3 -t -g rus.cg3


"<Однако>"
	"однако" ADV Degree=Pos
"<стиль>"
	"стиль" NOUN Animacy=Inan Case=Nom Gender=Masc Number=Sing
	"стиль" NOUN Animacy=Inan Case=Acc Gender=Masc Number=Sing
"<работы>"
	"работа" NOUN Animacy=Inan Case=Gen Gender=Fem Number=Sing
	"работа" NOUN Animacy=Inan Case=Nom Gender=Fem Number=Plur
	"работа" NOUN Animacy=Inan Case=Acc Gender=Fem Number=Plur
"<Семена>"
	"Семен" PROPN Animacy=Anim Case=Gen Gender=Masc Number=Sing
	"Семен" PROPN Animacy=Anim Case=Acc Gender=Masc Number=Sing
"<Еремеевича>"
	"Еремеевич" PROPN Animacy=Anim Case=Gen Gender=Masc Number=Sing
	"Еремеевич" PROPN Animacy=Anim Case=Acc Gender=Masc Number=Sing
"<заключался>"
	"заключаться" VERB Aspect=Imp Gender=Masc Mood=Ind Number=Sing Tense=Past VerbForm=Fin Voice=Mid
"<в>"
	"в" ADP SELECT:14
	"в1" ADP SELECT:14
;	"век" NOUN Animacy=Inan Case=Gen Gender=Masc Number=Sing SELECT:14
"<том>"
	"то" PRON Animacy=Inan Case=Loc Gender=Neut Number=Sing
	"том" NOUN Animacy=Inan Case=Nom Gender=Masc Number=Sing
	"то" PRON Animacy=Inan Case=Acc Gender=Masc Number=Sing
	"том" NOUN Animacy=Inan Case=Acc Gender=Masc Number=Sing
;	"тот" DET Case=Loc Gender=Neut Number=Sing REMOVE:13
;	"тот" DET Case=Loc Gender=Masc Number=Sing REMOVE:13
;	"тот" DET Case=Acc Gender=Masc Number=Sing REMOVE:13
"<,>"
	"," PUNCT
"<чтобы>"
	"чтобы" SCONJ Mood=Cnd
	"чтобы" SCONJ
"<принимать>"
	"принимать" VERB Aspect=Imp VerbForm=Inf Voice=Act
"<всех>"
	"весь" DET Case=Gen Number=Plur
	"весь" DET Case=Loc Number=Plur
	"весь" DET Case=Acc Number=Plur
	"все" PRON Animacy=Anim Case=Acc Number=Plur
	"все" PRON Animacy=Anim Case=Gen Number=Plur
	"все" PRON Animacy=Anim Case=Loc Number=Plur
	"все" PRON Animacy=Anim Case=Acc Gender=Masc Number=Plur
"<желающих>"
	"желать" VERB Aspect=Imp Case=Gen Number=Plur Tense=Pres VerbForm=Part Voice=Act
	"желать" VERB Animacy=Anim Aspect=Imp Case=Acc Number=Plur Tense=Pres VerbForm=Part Voice=Act
"<и>"
	"и" CCONJ SELECT:16
;	"и" PART SELECT:16
;	"и" X Foreign=Yes SELECT:16
"<лично>"
	"лично" ADV Degree=Pos
"<вникать>"
	"вникать" VERB Aspect=Imp VerbForm=Inf Voice=Act
"<в>"
	"в" ADP SELECT:14
	"в1" ADP SELECT:14
;	"век" NOUN Animacy=Inan Case=Gen Gender=Masc Number=Sing SELECT:14
"<дело>"
	"дело" NOUN Animacy=Inan Case=Nom Gender=Neut Number=Sing
	"дело" NOUN Animacy=Inan Case=Acc Gender=Neut Number=Sing
"<.>"
	"." PUNCT



