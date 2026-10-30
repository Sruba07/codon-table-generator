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
git clone https://github.com/YOUR-GITHUB-USERNAME/codon-table-generator.git
```

Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username.

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

To understand how this project's dictionary-based approach compares with existing bioinformatics tools, its implementation was compared with **Biopython**, an open-source Python library used in computational molecular biology.

**Reference project:** Biopython
**Module:** `Bio.Data.CodonTable`

### Comparison Table

| Feature                   | This Project                                                   | Biopython                                                     |
| ------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------- |
| Main purpose              | Educational DNA and RNA codon translation                      | General-purpose bioinformatics functionality                  |
| Codon representation      | Python dictionary                                              | CodonTable objects and dictionaries                           |
| Amino acid representation | Full amino acid names                                          | Commonly uses one-letter amino acid symbols                   |
| Stop codons               | Explicitly represented as `Stop` in the translation dictionary | Maintained separately using `stop_codons`                     |
| Start codons              | Identified by the program                                      | Maintained using `start_codons`                               |
| Genetic code support      | Focuses on the standard genetic code                           | Supports multiple genetic code tables                         |
| DNA and RNA support       | Accepts both DNA and RNA input                                 | Provides separate DNA and RNA codon-table types               |
| Output                    | User-friendly terminal translation tables                      | Programmable codon-table representations                      |
| Complexity                | Simple and beginner-friendly                                   | More extensive and suitable for advanced bioinformatics tasks |

### Key Observations

**1. Data Structure**

This project uses a straightforward Python dictionary for codon-to-amino-acid mapping.

Biopython provides a more structured `CodonTable` implementation with attributes such as `forward_table`, `start_codons`, and `stop_codons`.

**2. Amino Acid Representation**

This project displays full amino acid names, such as `Methionine` and `Alanine`, to make the output easier to understand.

Biopython commonly uses standard one-letter amino acid symbols, such as `M` for Methionine and `A` for Alanine.

**3. Stop Codon Handling**

This project explicitly represents stop codons as `Stop` in its translation dictionary.

Biopython maintains stop codons separately through its `stop_codons` attribute.

**4. Genetic Code Support**

This project focuses on the standard genetic code and is designed for educational purposes.

Biopython supports multiple genetic code tables, including alternative genetic codes.

**5. DNA and RNA Support**

This project accepts both DNA and RNA sequences and handles the difference between Thymine and Uracil during translation.

Biopython provides separate DNA and RNA codon-table implementations.

### Conclusion of Comparison

The comparison demonstrates that both implementations use codon-to-amino-acid relationships to perform genetic translation.

However, this project prioritizes simplicity, readability, and understanding the fundamentals of codon translation, whereas Biopython provides a more extensive and flexible framework for bioinformatics applications.

This project is therefore useful as an introductory implementation of a genetic code translator.

---

## 8. Project Structure

The project currently contains the following files:

```text
Codon-Table-Generator/
│
├── main.py
│   └── Main Python program containing the codon dictionary,
│       sequence validation, translation, and output functions.
│
└── README.md
    └── Project description, features, instructions,
        examples, and comparison with Biopython.
```

---

## 9. Author

**Created by:** Srushti B A
**Project Title:** Development of a Codon Table Generator
**Programming Language:** Python
**Project Type:** Bioinformatics / Python Programming Assignment

---

## 10. References

1. **Biopython Official GitHub Repository** – Open-source Python library for computational molecular biology.
2. **Biopython CodonTable Documentation** – Documentation describing codon-table objects, forward tables, start codons, and stop codons.
3. **National Center for Biotechnology Information (NCBI)** – Reference information on the standard genetic code.

---

**Project developed by Srushti B A**
