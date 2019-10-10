#######################################################
#PART 1: Tokenization
#tried two sentence tokenisers, pragmatic_segmenter and nltk's PUNKT

#pragmatic_segmenter worked well once I set the language settings in my segmenter.rb file to "de" as I am working with a niederdeutsch corpus:
#quantitative:
#accuracy percentage: 1 error per 100 lines. not bad! there was another 'error' which turned out to be a problem with the wiki, not the segmenter
#qualitative: 
#kinds of mistakes:in-line quotation of the type text: "quote." perhaps due to the period being inside of the quote.
#see 01/Tokenisation/pragmatic_segmenter/lib/ps_test.txt

#punkt
#quantitative:
#accuracy percentage: 2 errors per 100 lines
#qualitative:
#kinds of mistakes: accidentally created a boundary after t.B. (low german for z.B.). Also artificially created a boundary after the combined abbreviation-parentheses in "Anion (n.) ist..."
#see 01_Tokenisation/segmented.txt

#######################################################
#PART 2: MAXMATCH
#maxmatch.py takes a string of japanese characters and returns that string
#tokenized by a maximum matching algorithm trained from 
#UD_Japanese-GSD/ja_gsd-ud-train.conllu which is in this directory ja_dict.txt
#requried to run properly.

#its performance depends entirely upon the size of the dictionary ja_dict.txt
#see the files key.txt, 20ktest.txt, etc.

#WER for different dictionary sizes:
10k 
REF: これ に 不快感         を 示す 住民 は い    まし た が , 現在 , 表立っ て        反対 や 抗議 の 声 を 挙げ     て いる 住民 は い ない よう です         。
HYP: これ に 不       快 感 を 示す 住民 は いま し    た が , 現在 , 表       立 って 反対 や 抗議 の 声 を 挙    げ て いる 住民 は い ない よ    う    で す 。
EVA:            S         I   I                         S      S                         S         S   I                                    S      I                                    S      S      I   I      
WER: 43.75%

20k 
REF: これ に 不快感         を 示す 住民 は    い まし た が , 現在 , 表立っ て        反対 や 抗議 の 声 を 挙げ     て いる 住民 は い    ない よう です         。
HYP: これ に 不       快 感 を 示す 住民 はい ま し    た が , 現在 , 表       立 って 反対 や 抗議 の 声 を 挙    げ て いる 住民     はい ない よ    う    で す 。
EVA:            S         I   I                     S      S   S                         S         S   I                                    S      I                     D   S             S      S      I   I      
WER: 53.12%

50k 
REF: これ に 不快感     を 示す 住民 は い    まし た が    , 現在 , 表立っ て        反対 や 抗議 の 声 を 挙げ     て いる 住民 は い    ない よう です         。
HYP: これ に 不快    感 を 示す 住民     はい ま    し たが , 現在 , 表       立 って 反対 や 抗議 の 声 を 挙    げ て いる 住民     はい ない よ    う    で す 。
EVA:            S         I                     D   S      S      S   S                 S         S   I                                    S      I                     D   S             S      S      I   I      
WER: 56.25%

100k 
REF: これ に 不快感     を 示す 住民 は い    まし た が    , 現在 , 表立っ て        反対 や 抗議 の 声 を 挙げ て       いる 住民 は い    ない よう です     。
HYP: これ に 不快    感 を 示す 住民     はい ま    し たが , 現在 , 表       立 って 反対 や 抗議 の 声 を        挙げて いる 住民     はい ない よう で    す 。
EVA:            S         I                     D   S      S      S   S                 S         S   I                                    D      S                       D   S                    S      I      
WER: 50.00%



