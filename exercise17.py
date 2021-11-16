#!/usr/bin/python3
import re
accessions = ['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']

# PROCESS list of accessions
for acc in accessions:
    print(acc)


#All we need to do is to add the criteria as we loop through each of the accessions; we can add them one by one to check each one is working first...

# INPUT list of accessions
accessions = [
  'xkn59438', 
  'yhdck2', 
  'eihd39d9', 
  'chdsye847', 
  'hedle3455', 
  'xjhd53e', 
  '45da', 
  'de37dp']

outputs = []

# PROCESS list of accessions
for acc in accessions: 
# contain the number 5 (could also do if '5' in acc :)
    if re.search(r'5', acc) : 
        outputs.append('contain the number 5: ' + acc)
# contain the letter d or e
    if re.search(r'[de]', acc) : 
        outputs.append('contain the letter d or e: ' + acc)
# contain the letters d and e (adjacent)
    if re.search(r'de', acc) : 
        outputs.append('contain the letter d and e (have to be adjacent): ' + acc)
# contain the letters d and e in that order (dont have to be adjacent, but can be)
    if re.search(r'd.*e', acc) : 
        outputs.append('contain the letter d and e in that order (dont have to be adjacent): ' + acc)
# contain the letters d and e in that order with a single letter between them
    if re.search(r'd.e', acc) : 
        outputs.append('contain the letter d and e in that order with a single letter between them: ' + acc)
# contain both the letters d and e in any order
    if re.search(r'd', acc) and re.search(r'e', acc) : 
        outputs.append('contain both the letters d and e in any order: ' + acc)
# start with x or y
# could have used if acc.startswith('x') or acc.startswith('y') :
# could have used if re.search(r'^[xy]', acc) :
    if re.search(r'(^x|^y)', acc) : 
        outputs.append('start with x or y: ' + acc)
# start with x or y and end with e
# could have used if (acc.startswith('x') or acc.startswith('y')) and acc.endswith('e') :
# could have used if re.search('(^x|^y).+e$',acc) :
# could have used if re.search('"[xy].+e$',acc) :
    if re.search(r'(^x|^y)', acc) and re.search(r'(e$)', acc) : 
        outputs.append('start with x or y and end with e: ' + acc)
# contains any 3 numbers in any order
    if len(re.findall(r'\d',acc)) == 3 :
        outputs.append('contains any 3 numbers in any order: ' + acc)
# contains 3 different numbers
    if len(set(re.findall(r'\d',acc))) == 3 :
        outputs.append('contains 3 different numbers: ' + acc)
# contain three or more numbers in a row
# could have used if re.search(r'[0123456789]{3,}', acc) :
    if re.search(r'\d{3,}', acc): 
        outputs.append('contain three or more numbers in a row: ' + acc)
# end with d then either a, r or p
    if re.search(r'd[arp]$', acc): 
        outputs.append('end with d followed by either a, r or p: ' + acc)

outputs.sort()
print(('\n').join(outputs))
# Could have used a dictionary to store all the different
# accessions etc in Key/value pairs
dict_approach = {}
dict_approach['contain the letter d or e'] = '45da'
# Adding another string, so we can just use + (and a comma to make it look nicer)

dict_approach['contain the letter d or e'] = dict_approach['contain the letter d or e'] + ', chdsye847'

# Whats there now?
dict_approach

list(dict_approach.values())

list(dict_approach.values())[0].split(',')

list(dict_approach.items())


####question2


dna = open('/localdisk/data/BPSM/Lecture17/long_dna.txt').read().rstrip('\n')
len(dna)
dna
print("\n".join(re.findall('.{1,60}', dna)))
BpsmI='A[GATC]TAAT'
print('BpsmI cuts at:',BpsmI)
for matching in re.finditer(BpsmI, dna): 
    print(matching.start()+3)
dna = open('/localdisk/data/BPSM/Lecture17/long_dna.txt').read().rstrip('\n') 
last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
    findnum += 1
    cut_position = matching.start() + 3
# Distance from the current cut site to the previous one
    fragment_size = cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
# We also have to remember the last fragment, from the last cut to the end:
    if findnum == len(list(re.finditer(BpsmI, dna))) :
       fragment_size = len(dna) - last_cut
       print('Fragment size is ' + str(fragment_size))

##What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?

##Doing the same for two enzymes is trickier. Ambiguity code 'R' corresponds to the purines A or G, while 'W' corresponds to A or T, so we will need to 'convert' it too...

# First, define both enzymes sites
BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'

# Make a list to store the cut positions for both enzymes
all_cuts = []
# Add cut positions for BpsmI
for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3) 

# Add cut positions for BpsmII
for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)

print(all_cuts)

# These aren't in sequential order, so just sort them
all_cuts.sort()
all_cuts

##Now we can go through the list of all cuts with the same logic as before.

# Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position
# Now the last fragment
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

# Let's use a dictionary to store the fragment sequences
fragment_sequences = {}


# Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
# Get the sequence substring
    fragment_sequences['Fragment'+str(counter)] = dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])
# Get the fragment start and end
    fragends = dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut = cut_position
# Now the last fragment
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
fragment_sequences['Fragment'+str(counter)] = dna[last_cut:]
print(fragment_sequences['Fragment'+str(counter)])
fragends = dna[last_cut:][0:6] + '...' + dna[last_cut:][-6:]
print('Fragment has ends: '+fragends)
# Show all the sequences
print(('\n########\n').join(list(fragment_sequences.values())))
# Are the fragments actually adjacent? Quick check!
# End of Fragment 1 ACGCGT should be next to
# beginning of Fragment 2 TGAACA
# so lets use ACGCGTTGAACA as a query against our sequence
re.search(r'ACGCGTTGAACA',dna)
