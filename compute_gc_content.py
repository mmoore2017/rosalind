from Bio import SeqIO


def compute_gc_content(path):
    name_to_gc = SeqIO.to_dict(SeqIO.parse(path, 'fasta'))

    for record in SeqIO.parse(path, 'fasta'):
        seq = str(record.seq)
        num = seq.count('C') + seq.count('G')
        percent = num / len(seq) * 100
        name_to_gc[record.id] = percent

    maximum = max(name_to_gc.values())
    name = ''
    for key in name_to_gc.keys():
        if name_to_gc[key] == maximum:
            name = key
    print(name + '\n' + str(maximum))


compute_gc_content('/Users/michaelmoore/Downloads/rosalind_gc-2.txt')
