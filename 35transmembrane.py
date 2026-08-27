import sys
import mcb185
import sequence

# handle arguments
args = sys.argv
if len(args) != 2:
	sys.exit('Error: unexpected number of arguments')
file = args[1]

# get deflines and sequences
seqs = mcb185.read_fasta(file)

# transmembrane proteins
# hydrophobic N-terminal signal peptide
	# 8 aa long segment with average KD >= 2.5 in first 30 aas
# transmembrane region(s)
	# 11 aa long segment with average KD >= 2.0 after first 30 aas
# neither signal or transmembrane should have Proline (P)

# find hydrophobic signal
for defline, seq in seqs:
	sig_flag = False
	txm_flag = False

	## signal check
	# check first 8 aminos
	nterm = seq[0:30]
	window = nterm[0:8]
	kd = sequence.kyte_doolittle(window)
	if kd / 8 >= 2.5 and 'P' not in window: sig_flag = True
	
	# check every other window of 8 aminos
	if sig_flag == False:
		for i in range(1, len(nterm) -8 +1):
			window = nterm[i:i+8]
			lose   = nterm[i-1]
			gain   = nterm[i+8-1]
			if lose in sequence.AMINOKD: kd -= sequence.AMINOKD[lose]
			if gain in sequence.AMINOKD: kd += sequence.AMINOKD[gain]
			if kd / 8 >= 2.5 and 'P' not in window:
				sig_flag = True
				break

	if sig_flag == False: continue

	## transmembrane region check
	# check first window
	postnt = seq[31:len(seq)]
	window = postnt[0:11]
	kd = sequence.kyte_doolittle(window)
	if kd / 11 >= 2.0 and 'P' not in window: txm_flag = True
	
	# check every other window of 11 aminos
	if txm_flag == False:
		for i in range(1, len(postnt) -11 +1):
			window = postnt[i:i+11]
			lose   = postnt[i-1]
			gain   = postnt[i+11-1]
			if lose in sequence.AMINOKD: kd -= sequence.AMINOKD[lose]
			if gain in sequence.AMINOKD: kd += sequence.AMINOKD[gain]
			if kd / 11 >= 2.0 and 'P' not in window:
				txm_flag = True
				break

	if txm_flag == True: print(f'{defline:.50}')