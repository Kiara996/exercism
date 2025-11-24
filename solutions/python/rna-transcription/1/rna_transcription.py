def to_rna(dna_strand):
    transcription = {
        'G': 'C', 'C': 'G', 'T': 'A', 'A':'U'
    }

    rna = ""

    for nukleosit in dna_strand:
        rna += transcription[nukleosit]

    return rna