def find_motif_in_dna(dna, motif):
    motif_length = len(motif)
    dna_length = len(dna)
    distances = []

    for i in range(0, dna_length - motif_length):
        seq = ''
        for j in range(i, motif_length + i):
            seq += dna[j]
        print(seq)
        if seq == motif:
            distances.append(i + 1)

    print(distances)


find_motif_in_dna('GACATCATCGGTCGCACATCATCAAAACATCATAACATCATAACATCATAACATCATGAACATCATTTACATCATAACATCATGCTTTACATCATAACATCATCCAACATCATCCGACATCATGACATCATACATCATACATCATTGCACATCATGCCGACATCATATACATCATACATCATGGTATTCTACATCATACATCATCTCCACATCATAAACATCATAACATCATACATCATACATCATACATCATACATCATCGCGACATCATGACATCATTGGCAACATCATAACATCATAACATCATACATCATCAACATCATACATCATATAGCACATCATGTGATAACATCATACATCATGAGTGGTACATCATACATCATTACATCATGGACATCATAACATCATGCAACATCATCACATCATTCGTCACATCATTCAACATCATGACATCATTTAACATCATGCTATCCGTACATCATGACATCATCACATCATAGAACATCATCACATCATGACATCATCGGGACATCATACATCATGACATCATGGGACATCATTGAACTCTGGACATCATCAGGGACATCATAGATATAACATCATACATCATTCACATCATGTCACATCATACATCATTACATCATACATCATACATCATGCGACATCATACATCATACATCATTGCTTCATCACATCATACATCATACATCATAGACATCATAGTCAGACATCATACATCATAGAGACATCATACATCATACATCATCCATGGACATCATTAACATCATCGAACATCATCACATCATCACATCATCC', 'ACATCATAC')