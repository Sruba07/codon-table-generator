# 🧬 Development of a Codon Table Generator

## 1. Project Overview

The **Codon Table Generator** is a Python-based bioinformatics project developed to generate the standard 64-codon genetic code table and translate user-provided DNA or RNA sequences into their corresponding amino acid sequences.

In molecular biology, a codon is a sequence of three nucleotides that specifies an amino acid or a stop signal during protein synthesis. The standard genetic code consists of 64 possible codons, including codons that encode amino acids and three stop codons.

This project uses a Python dictionary to represent the standard genetic code. It accepts nucleotide sequences from the user, validates the input, divides the sequence into groups of three nucleotides, and translates each complete codon into its corresponding amino acid.

The program also identifies start and stop codons, handles incomplete codons at the end of a sequence, and displays the translation results in a structured table.

As an additional challenge, the program supports RNA sequence translation by handling Uracil (U) in place of Thymine (T).

The main purpose of this project is to demonstrate how Python programming concepts can be applied to a practical problem in bioinformatics.

---

## 2. Features Implemented

### 2.1 Standard 64-Codon Dictionary

The program uses a Python dictionary to represent the standard genetic code.

It contains all 64 possible codons and their corresponding amino acid names, including the three stop codons.

Examples:

| Codon | Amino Acid    |
| :---: | ------------- |
|  AUG  | Methionine    |
|  GCU  | Alanine       |
|  UUU  | Phenylalanine |
|  UAA  | Stop          |
|  UAG  | Stop          |
|  UGA  | Stop          |

The dictionary allows the program to retrieve the corresponding amino acid for each codon.

### 2.2 DNA Sequence Input

The program accepts a DNA sequence entered by the user.

DNA consists of four types of nucleotides:

* A – Adenine
* T – Thymine
* G – Guanine
* C – Cytosine

The input is converted to uppercase before processing, allowing users to enter sequences in either uppercase or lowercase.

### 2.3 Input Validation

Input validation ensures that the entered sequence contains only valid nucleotide characters.

For DNA sequences, the accepted characters are:

`A, T, G, C`

For RNA sequences, the accepted characters are:

`A, U, G, C`

The program rejects invalid characters and prevents DNA and RNA symbols (T and U) from being mixed in the same sequence.

This helps prevent incorrect translation results.

### 2.4 Codon Splitting

After validation, the nucleotide sequence is divided into groups of three bases.

Each group of three nucleotides is called a codon.

For example:

**Input sequence:**

`ATGGCTTTTTAA`

**Divided codons:**

`ATG - GCT - TTT - TAA`

Each complete codon is then translated individually.

### 2.5 Amino Acid Translation

The program translates each codon into its corresponding amino acid using the standard genetic code dictionary.

For example:

| Codon | Amino Acid    |
| :---: | ------------- |
|  ATG  | Methionine    |
|  GCT  | Alanine       |
|  TTT  | Phenylalanine |
|  TAA  | Stop          |

The resulting amino acid sequence is displayed in the terminal.

### 2.6 Start and Stop Codon Identification

The program identifies start and stop codons present in the input sequence.

**Start codon:**

* DNA: `ATG`
* RNA: `AUG`

The start codon generally signals the beginning of translation.

**Stop codons:**

* DNA: `TAA`, `TAG`, `TGA`
* RNA: `UAA`, `UAG`, `UGA`

Stop codons signal the termination of translation.

The program identifies these codons and displays their roles in the translation table.

### 2.7 Incomplete Codon Handling

A complete codon must contain exactly three nucleotides.

Sometimes, an input sequence may end with one or two extra nucleotides that do not form a complete codon.

For example:

`ATGGCTA`

The sequence is divided into:

* `ATG`
* `GCT`
* Remaining nucleotide: `A`

The program translates the complete codons and reports the incomplete trailing nucleotide instead of attempting to translate it.

This prevents errors during codon lookup.

### 2.8 Formatted Translation Table

The program displays the translation results in a structured table containing:

* Position
* Codon
* Amino Acid
* Role

The role indicates whether a codon is a start codon, a stop codon, or a coding codon.

This makes the translation process easier to read and understand.

---

## 3. Additional Challenge: RNA Sequence Translation

An additional challenge of this project is to support RNA sequences along with DNA sequences.

DNA contains Thymine (T), whereas RNA contains Uracil (U).

The program detects RNA input containing Uracil and processes it using the standard genetic code. It handles the difference between DNA and RNA codons during dictionary lookup.

**Example RNA sequence:**

`AUGGCUUUUUAA`

**Corresponding codons:**

`AUG - GCU - UUU - UAA`

**Translated amino acids:**

`Methionine - Alanine - Phenylalanine - Stop`

This feature extends the functionality of the original DNA codon translator.

---

## 4. Technologies Used

| Technology             | Purpose                                       |
| ---------------------- | --------------------------------------------- |
| Python 3               | Main programming language                     |
| Python Dictionaries    | Store the standard genetic code               |
| Python Functions       | Organize the program into separate operations |
| Conditional Statements | Validate sequences and identify codon roles   |
| Loops                  | Process codons and generate output            |
| String Operations      | Normalize and process nucleotide sequences    |
| Visual Studio Code     | Code development and execution                |
| Git and GitHub         | Version control and project hosting           |

**External libraries:** No additional Python libraries are required for the current implementation.

---

## 5. How to Run the Program

### Prerequisites

Before running the program, make sure you have:

* Python 3 installed on your computer.
* A code editor such as Visual Studio Code.
* Git installed if you want to clone the repository.

### Step 1: Clone the Repository

Open a terminal and enter:

```bash
git clone https://github.com/Sruba07/codon-table-generator.git
```

### Step 2: Open the Project Folder

```bash
cd codon-table-generator
```

### Step 3: Run the Python Program

```bash
python main.py
```

The program will start in the terminal and ask you to enter a DNA or RNA sequence.



---

## 6. Sample Input and Output

### Example 1: DNA Sequence Translation

========== PROGRAM SUMMARY ==========
Total codons translated: 4
Total amino acids produced: 3
Incomplete nucleotides: 0

**Input:**

```text
ATGGCTTTTTAA
```

**Expected translation table:**

| Position | Codon | Amino Acid    | Role   |
| :------: | :---: | ------------- | ------ |
|     1    |  ATG  | Methionine    | Start  |
|     2    |  GCT  | Alanine       | Coding |
|     3    |  TTT  | Phenylalanine | Coding |
|     4    |  TAA  | Stop          | Stop   |

**Output summary:**

```text
Codons: ATG - GCT - TTT - TAA

Amino acids:
Methionine - Alanine - Phenylalanine - Stop

Start codon: ATG
Stop codon: TAA
```

### Example 2: RNA Sequence Translation

**Input:**

```text
AUGGCUUUUUAA
```

**Expected translation:**

```text
Codons: AUG - GCU - UUU - UAA

Amino acids:
Methionine - Alanine - Phenylalanine - Stop

Start codon: AUG
Stop codon: UAA
```

### Example 3: Incomplete Codon Handling

**Input:**

```text
ATGGCTA
```

**Expected result:**

```text
Complete codons: ATG - GCT

Amino acids:
Methionine - Alanine

Incomplete trailing nucleotide:
A
```

The incomplete nucleotide is reported and excluded from translation.

### Example 4: Invalid Sequence

**Input:**

```text
ATGX123
```

**Expected result:**

```text
Invalid sequence.
Please enter a valid DNA or RNA sequence.
```

The program rejects characters that are not valid nucleotides.

---

## 7. Comparison with Existing GitHub Codon-Table Implementations

This project was compared with three existing GitHub repositories to understand different approaches to codon tables.

### 7.1 Reference Repositories

1. **Biopython:** Provides genetic code tables, codon translation and start/stop codon information.

2. **Python Codon Tables:** Provides organism-specific codon usage frequencies.

3. **EndyLab Codon Tables:** Provides tools for custom codon table representation and optimisation.

### 7.2 Comparison Table

| Feature           | This Project        | Biopython          | Python Codon Tables  | EndyLab                     |
| ----------------- | ------------------- | ------------------ | -------------------- | --------------------------- |
| Main purpose      | DNA/RNA translation | Bioinformatics     | Codon usage analysis | Custom codon tables         |
| Data structure    | Dictionary          | CodonTable objects | Nested dictionaries  | Dictionaries and DataFrames |
| Translation       | Yes                 | Yes                | Mainly usage lookup  | Custom table tools          |
| Start/stop codons | Identified          | Stored separately  | Usage data           | Depends on table            |
| Main output       | Amino acid sequence | Genetic code data  | Codon frequencies    | Custom tables               |

### 7.3 Comparison of Actual Codon Entries

The following examples show how codons are represented in this project and Biopython.

| RNA Codon | This Project  | Biopython     |
| --------- | ------------- | ------------- |
| AUG       | Methionine    | Methionine    |
| GCU       | Alanine       | Alanine       |
| UUU       | Phenylalanine | Phenylalanine |
| UAA       | Stop          | Stop          |

The mappings agree with the standard genetic code.

Python Codon Tables focuses on codon usage frequencies, while EndyLab provides tools for representing and manipulating custom codon tables.

### 7.4 Key Differences

This project uses a Python dictionary containing all 64 standard RNA codons. It translates DNA and RNA sequences, identifies start and stop codons, and handles incomplete codons.

Biopython offers advanced genetic code and translation features. Python Codon Tables focuses on codon usage frequencies, while EndyLab focuses on custom codon table representation and optimisation.

### 7.5 Conclusion

This comparison demonstrates that Python dictionaries provide a simple way to represent codon-to-amino-acid relationships. While existing repositories offer advanced bioinformatics features, this project focuses on implementing the standard genetic code using basic Python concepts.


## 8. Project Structure

The project currently contains the following files:

```text
Codon-Table-Generator/
│
├── main.py
├── test_main.py
└── README.md

```
---

## 9. Author

**Created by:** Srushti B A
**Project Title:** Development of a Codon Table Generator
**Programming Language:** Python
**Project Type:** Bioinformatics / Python Programming Assignment

---

## 10. References

1. **Biopython:** https://github.com/biopython/biopython
2. **Python Codon Tables – Edinburgh Genome Foundry:** https://github.com/Edinburgh-Genome-Foundry/python_codon_tables
3. **EndyLab Codon Tables:** https://github.com/EndyLab/codon-tables
4. **Biopython CodonTable Documentation:** https://biopython.org/docs/latest/api/Bio.Data.CodonTable.html
5. **NCBI:** Standard Genetic Code reference. https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi


---

