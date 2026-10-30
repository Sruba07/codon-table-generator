# ==========================================
# PYTHON PROJECT: CODON TABLE GENERATOR
# ==========================================

# Step 1: Create the complete RNA codon table

codon_table = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine",
    "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UAA": "Stop", "UAG": "Stop",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGA": "Stop", "UGG": "Tryptophan",

    "CUU": "Leucine", "CUC": "Leucine",
    "CUA": "Leucine", "CUG": "Leucine",
    "CCU": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAU": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGU": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "AUU": "Isoleucine", "AUC": "Isoleucine",
    "AUA": "Isoleucine", "AUG": "Methionine",
    "ACU": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAU": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGU": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GUU": "Valine", "GUC": "Valine",
    "GUA": "Valine", "GUG": "Valine",
    "GCU": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAU": "Aspartic Acid", "GAC": "Aspartic Acid",
    "GAA": "Glutamic Acid", "GAG": "Glutamic Acid",
    "GGU": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

# Step 2: Display all 64 codons

def display_codon_table():
    print("\n========== CODON TABLE ==========")

    for codon, amino_acid in codon_table.items():
        print(codon, ":", amino_acid)

    print("Total codons:", len(codon_table))

# Step 3: Accept sequence from user

def get_sequence():
    sequence = input("\nEnter your DNA or RNA sequence: ")
    return sequence.upper().replace(" ", "")

# Step 4: Validate the DNA or RNA sequence

def validate_sequence(sequence):

    if not sequence:
        print("Error: Sequence cannot be empty.")
        return False

    if "T" in sequence and "U" in sequence:
        print("Error: Do not mix DNA (T) and RNA (U) nucleotides.")
        return False

    if not all(base in "ATGC" for base in sequence) and not all(base in "AUGC" for base in sequence):
        print("Error: Invalid nucleotide detected.")
        print("Please enter only A, T, G, C for DNA or A, U, G, C for RNA.")
        return False

    return True

# Step 5: Translate DNA or RNA sequence

def translate_sequence(sequence):

    # Convert DNA into RNA for translation
    rna_sequence = sequence.replace("T", "U")

    codons = []
    amino_acids = []
    incomplete_codon = ""

    for i in range(0, len(rna_sequence), 3):

        codon = rna_sequence[i:i + 3]

        if len(codon) < 3:
            incomplete_codon = codon
            break

        amino_acid = codon_table[codon]

        # Keep original DNA/RNA codon for display
        original_codon = sequence[i:i + 3]

        codons.append(original_codon)
        amino_acids.append(amino_acid)

    return codons, amino_acids, incomplete_codon

    # Step 6: Identify start and stop codons

def identify_start_stop(codons):

    start_codons = ["ATG"]
    stop_codons = ["TAA", "TAG", "TGA"]

    found_starts = []
    found_stops = []

    for codon in codons:

        # Convert RNA codons into DNA format for checking
        normalized_codon = codon.replace("U", "T")

        if normalized_codon in start_codons:
            found_starts.append(codon)

        if normalized_codon in stop_codons:
            found_stops.append(codon)

    return found_starts, found_stops


# Step 7: Display translation in a structured table

def display_translation_table(codons, amino_acids):

    print("\n" + "=" * 55)
    print("              TRANSLATION TABLE")
    print("=" * 55)

    print(f"{'Position':<12}{'Codon':<12}{'Amino Acid':<20}{'Role'}")
    print("-" * 55)

    for i, (codon, amino_acid) in enumerate(zip(codons, amino_acids), 1):

        if codon.replace("U", "T") == "ATG":
            role = "Start"

        elif amino_acid == "Stop":
            role = "Stop"

        else:
            role = "Coding"

        print(f"{i:<12}{codon:<12}{amino_acid:<20}{role}")

    print("=" * 55)

# Step 8: Count amino acids in the translated sequence

def display_amino_acid_summary(amino_acids):

    print("\n" + "=" * 40)
    print("       AMINO ACID SUMMARY")
    print("=" * 40)

    amino_acid_counts = {}

    for amino_acid in amino_acids:
        amino_acid_counts[amino_acid] = amino_acid_counts.get(amino_acid, 0) + 1

    for amino_acid, count in amino_acid_counts.items():
        print(f"{amino_acid:<20}: {count}")

    print("=" * 40)

# Step 9: Main program

def main():

    print("\n===================================")
    print("       CODON TABLE GENERATOR")
    print("===================================")

    display_codon_table()

    sequence = get_sequence()

    if validate_sequence(sequence):

        codons, amino_acids, incomplete = translate_sequence(sequence)

        start_codons, stop_codons = identify_start_stop(codons)
        display_translation_table(codons, amino_acids)
        display_amino_acid_summary(amino_acids)

        print("\n========== TRANSLATION RESULT ==========")

        print("Original Sequence:", sequence)

        print("\nSequence Statistics:")
        print("Total nucleotides:", len(sequence))

        gc_count = sequence.count("G") + sequence.count("C")
        gc_percentage = (gc_count / len(sequence)) * 100
        print(f"GC Content: {gc_percentage:.2f}%")

        print("\nNucleotide Composition:")
        print("A (Adenine):", sequence.count("A"))
        print("T (Thymine):", sequence.count("T"))
        print("U (Uracil):", sequence.count("U"))
        print("G (Guanine):", sequence.count("G"))
        print("C (Cytosine):", sequence.count("C"))
        print("Complete codons:", len(codons))
        print("Incomplete nucleotides:", len(incomplete))

        print("\nCodons:")
        print(" - ".join(codons))

        print("\nAmino Acids:")
        print(" - ".join(amino_acids))

        print("\nStart Codons:")
        if start_codons:
            print(" - ".join(start_codons))
        else:
            print("No start codon found.")

        print("\nStop Codons:")
        if stop_codons:
            print(" - ".join(stop_codons))
        else:
            print("No stop codon found.")

        if incomplete:
            print("\nIncomplete codon at the end:", incomplete)

    else:

        print("\nInvalid sequence!")
        print("Please enter only A, T, G, C or A, U, G, C.")
        print("Do not mix DNA and RNA letters.")

    print("\nThank you for using Codon Table Generator!")

# Step 10: Run the program

if __name__ == "__main__":
    main()
