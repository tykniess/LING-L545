#final consonants
#works okay. Instances with a frequency of one indicate that there's some non-German alphanumeric letter or symbol in the word (for example, é), a borrowed word (sanskrit 'krta', or something non-wordy but using letters, such as roman numeral XXI, or just a typo


#part 1: just the real words
uconv -x upper | 			#makes all upper
gsed 's/[^ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜ]\+/\n/g' | 			
					#replaces non-alphabetical with newline
					#[A-Z] doesn't include umlaut vowels
sort | 					#sorts 
uniq |  				#removes duplicates
grep '[AEIOUYÜÖÄ]' |			#filter out tokens which have no vowel



#part 2: reverse	
rev |


#part 3: filter out vowel and 'rest of' word
gsed 's/\([AEIOUYÜÖÄ][A-Z]*\)/\n/g'| 	#replaces VC(C(C(C...))) with null
grep '[A-Z]' |				#filters out empty lines or lines with spaces
rev|					#return to normal
sort | uniq -c 	| sort -rn		#sorts, deletes duplicates, counts, sorts again