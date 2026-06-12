from flask import Flask, render_template, request

app = Flask(__name__)

topics =  {

    "pcr": {
"explanation": """
• PCR (Polymerase Chain Reaction) is a molecular biology technique.
• It is used to make millions of copies of a DNA sequence.
• It works like a photocopy machine for DNA.

Steps of PCR:

1. Denaturation – DNA strands separate.
2. Annealing – Primers attach to target DNA.
3. Extension – DNA polymerase synthesizes new DNA strands.

These steps repeat many times to amplify DNA.
""",
"application": """
• Disease diagnosis (COVID-19, genetic disorders)
• Forensic science and DNA fingerprinting
• Research laboratories
• Gene cloning
• Evolutionary studies
""",

    "viva": """
1. What is the full form of PCR?
2. Who invented PCR?
3. What enzyme is used in PCR?
4. What are the three steps of PCR?
5. Why is Taq polymerase used in PCR?
""",
},

    "dna": {
    "explanation": """
• DNA stands for Deoxyribonucleic Acid.
• DNA is the hereditary material present in almost all living organisms.
• It carries genetic information from one generation to the next.
• DNA is mainly found in the nucleus of eukaryotic cells and in the cytoplasm of prokaryotic cells.
• DNA consists of smaller units called nucleotides.
• Each nucleotide contains a phosphate group, deoxyribose sugar, and a nitrogenous base.
• The four nitrogenous bases present in DNA are Adenine (A), Thymine (T), Guanine (G), and Cytosine (C).
• Adenine always pairs with Thymine, while Guanine pairs with Cytosine.
• DNA has a double-helix structure discovered by James Watson and Francis Crick in 1953 based on Rosalind Franklin's X-ray diffraction studies.
• The sequence of bases in DNA determines the genetic information of an organism.
• DNA controls protein synthesis and regulates cell activities.
• Replication of DNA ensures that genetic information is accurately passed to daughter cells during cell division.
""",

    "application": """
• DNA fingerprinting in forensic science.
• Detection of genetic disorders.
• Paternity testing.
• Genetic engineering and recombinant DNA technology.
• Development of genetically modified crops.
• Disease diagnosis and personalized medicine.
• Evolutionary and biodiversity studies.
• Biotechnology and pharmaceutical research.
""",

    "viva": """
1. What is the full form of DNA?
2. Who discovered the double-helix structure of DNA?
3. What are the components of a nucleotide?
4. Name the four nitrogenous bases present in DNA.
5. Which bases pair together in DNA?
6. Why is DNA called the hereditary material?
7. Where is DNA located in eukaryotic cells?
8. What is DNA replication?
9. What is the function of DNA?
10. What is the significance of the double-helix structure?
"""
},

  "rna": {
    "explanation": """
• RNA stands for Ribonucleic Acid.
• RNA is a nucleic acid that plays an essential role in protein synthesis.
• It acts as a messenger between DNA and proteins.
• Unlike DNA, RNA is usually single-stranded.
• RNA contains ribose sugar instead of deoxyribose sugar.
• The nitrogenous bases present in RNA are Adenine (A), Uracil (U), Guanine (G), and Cytosine (C).
• In RNA, Uracil replaces Thymine which is present in DNA.
• RNA is synthesized from DNA through a process called transcription.
• RNA helps in translating genetic information into proteins.
• There are three major types of RNA:
   1. mRNA (Messenger RNA) – Carries genetic information from DNA to ribosomes.
   2. tRNA (Transfer RNA) – Brings amino acids to ribosomes during protein synthesis.
   3. rRNA (Ribosomal RNA) – Forms the structure of ribosomes and helps in protein synthesis.
• RNA plays a crucial role in gene expression and regulation.
• Some viruses such as HIV and Coronavirus use RNA as their genetic material.
""",

    "application": """
• Protein synthesis in cells.
• Vaccine development (mRNA vaccines).
• Gene expression studies.
• Molecular biology research.
• Disease diagnosis.
• Genetic engineering.
• Biotechnology and pharmaceutical industries.
• RNA interference (RNAi) studies.
""",

    "viva": """
1. What is the full form of RNA?
2. How is RNA different from DNA?
3. Which sugar is present in RNA?
4. Which base replaces thymine in RNA?
5. Name the three major types of RNA.
6. What is the function of mRNA?
7. What is the function of tRNA?
8. What is the function of rRNA?
9. What is transcription?
10. Why is RNA important in protein synthesis?
"""
},

   "gene": {
    "explanation": """
• A gene is the basic unit of heredity.
• A gene is a specific segment of DNA that contains instructions for making a protein or functional RNA molecule.
• Genes are responsible for the transmission of traits from parents to offspring.
• Genes are located on chromosomes inside the nucleus of cells.
• Every organism has thousands of genes that control different characteristics.
• Genes determine traits such as eye color, hair color, height, and blood group.
• The information present in genes is encoded in the sequence of DNA bases.
• During gene expression, the information in a gene is used to produce proteins.
• Mutations in genes can lead to changes in traits and may cause genetic disorders.
• Genes play an important role in growth, development, metabolism, and reproduction.
• The complete set of genes in an organism is called its genome.
""",

    "application": """
• Identification of genetic disorders.
• Gene therapy for disease treatment.
• Production of genetically modified organisms (GMOs).
• Crop improvement in agriculture.
• Personalized medicine.
• Biotechnology and pharmaceutical research.
• DNA fingerprinting and forensic analysis.
• Evolutionary and population genetics studies.
""",

    "viva": """
1. What is a gene?
2. Why is a gene called the unit of heredity?
3. Where are genes located?
4. What is the function of a gene?
5. What is gene expression?
6. What is a mutation?
7. How do genes influence traits?
8. What is a genome?
9. Can genes be transferred from parents to offspring?
10. What are the applications of genes in biotechnology?
"""
},
   "protein": {
    "explanation": """
• Proteins are large and complex biological molecules essential for life.
• They are made up of smaller units called amino acids.
• Amino acids are linked together by peptide bonds to form proteins.
• Proteins perform structural, functional, and regulatory roles in living organisms.
• They are involved in growth, repair, and maintenance of body tissues.
• Enzymes are specialized proteins that speed up biochemical reactions.
• Proteins are synthesized in ribosomes through the process of translation.
• The sequence of amino acids determines the structure and function of a protein.
• Proteins can be classified into primary, secondary, tertiary, and quaternary structures.
• Examples of proteins include hemoglobin, insulin, collagen, keratin, and enzymes.
• Proteins are essential for metabolism, immunity, transport, and cell signaling.
""",

    "application": """
• Production of therapeutic proteins such as insulin.
• Enzyme technology in industries.
• Drug development and pharmaceutical research.
• Medical diagnostics.
• Biotechnology and genetic engineering.
• Nutritional studies.
• Disease detection and treatment.
• Industrial fermentation processes.
""",

    "viva": """
1. What are proteins?
2. What are proteins made of?
3. What is an amino acid?
4. What bond joins amino acids together?
5. Where are proteins synthesized in the cell?
6. What are enzymes?
7. Name the levels of protein structure.
8. Give two examples of proteins.
9. What is the function of proteins in the body?
10. Why are proteins important for life?
"""
},
  "bioinformatics": {
    "explanation": """
• Bioinformatics is an interdisciplinary field that combines Biology, Computer Science, Mathematics, and Statistics.
• It is used to collect, store, analyze, and interpret biological data.
• Bioinformatics helps scientists understand DNA, RNA, proteins, and genomes using computational tools.
• With the development of genome sequencing technologies, huge amounts of biological data are generated every day.
• Bioinformatics provides tools and databases to manage and analyze this information efficiently.
• It is widely used in genomics, proteomics, transcriptomics, and drug discovery.
• Common bioinformatics tools include BLAST, Clustal Omega, MEGA, GenBank, and Biopython.
• Bioinformatics helps identify genes, predict protein structures, study evolutionary relationships, and understand diseases.
• It has become an essential part of modern biotechnology and medical research.
• Bioinformatics plays a major role in personalized medicine and precision healthcare.
""",

    "application": """
• Genome sequencing and analysis.
• Drug discovery and development.
• Disease diagnosis and prediction.
• Protein structure prediction.
• Evolutionary studies and phylogenetic analysis.
• Identification of genes and genetic mutations.
• Agricultural biotechnology research.
• Personalized medicine and healthcare.
""",

    "viva": """
1. What is bioinformatics?
2. Which disciplines are combined in bioinformatics?
3. Why is bioinformatics important?
4. Name some commonly used bioinformatics tools.
5. What is BLAST?
6. What is GenBank?
7. How is bioinformatics used in drug discovery?
8. What is genome analysis?
9. How does bioinformatics help in personalized medicine?
10. What are the applications of bioinformatics in biotechnology?
"""
},
  "crispr": {
    "explanation": """
• CRISPR stands for Clustered Regularly Interspaced Short Palindromic Repeats.
• It is a powerful gene-editing technology used to modify DNA sequences.
• CRISPR was originally discovered as a natural defense mechanism in bacteria against viruses.
• The system works with a protein called Cas9, which acts like molecular scissors.
• Cas9 can cut DNA at a specific location directed by a guide RNA (gRNA).
• Scientists can use CRISPR-Cas9 to add, remove, or alter genetic material.
• It is faster, cheaper, and more accurate than many older gene-editing methods.
• CRISPR has revolutionized biotechnology, medicine, and genetic research.
• Researchers are exploring CRISPR for treating inherited genetic disorders.
• It has become one of the most important tools in modern molecular biology.
""",

    "application": """
• Treatment of genetic diseases.
• Gene therapy research.
• Development of disease-resistant crops.
• Drug discovery and development.
• Cancer research.
• Functional genomics studies.
• Creation of genetically modified organisms (GMOs).
• Biomedical and biotechnology research.
""",

    "viva": """
1. What is the full form of CRISPR?
2. What is the role of Cas9 in CRISPR technology?
3. Why is Cas9 called molecular scissors?
4. What is guide RNA (gRNA)?
5. How was CRISPR originally discovered?
6. What are the advantages of CRISPR over older techniques?
7. Can CRISPR be used to treat genetic disorders?
8. What are the applications of CRISPR in agriculture?
9. What is gene editing?
10. Why is CRISPR considered a revolutionary technology?
"""
},

    "plasmid": {
        "explanation": "A plasmid is a small circular DNA molecule in bacteria.",
        "application": "Genetic engineering.",
        "viva": "What is a plasmid?"
    },

    "cloning": {
        "explanation": "Cloning creates identical copies of DNA or organisms.",
        "application": "Research and biotechnology.",
        "viva": "What is cloning?"
    },

   "elisa": {
    "explanation": """
• ELISA stands for Enzyme-Linked Immunosorbent Assay.
• It is a laboratory technique used to detect and measure specific antigens or antibodies in a sample.
• ELISA is based on the specific interaction between an antigen and an antibody.
• The technique uses an enzyme-linked antibody that produces a color change when a substrate is added.
• The intensity of the color produced is directly proportional to the amount of antigen or antibody present.
• ELISA is highly sensitive, specific, and widely used in diagnostic laboratories.
• It is commonly performed using microtiter plates containing multiple wells.
• There are different types of ELISA such as Direct ELISA, Indirect ELISA, Sandwich ELISA, and Competitive ELISA.
• ELISA is one of the most commonly used immunological techniques in research and medicine.
• It plays a crucial role in disease diagnosis and monitoring.
""",

    "application": """
• Detection of HIV infection.
• Detection of COVID-19 antibodies.
• Diagnosis of Hepatitis B and Hepatitis C.
• Pregnancy testing.
• Detection of hormones and proteins.
• Vaccine research and development.
• Food allergy testing.
• Biomedical and pharmaceutical research.
""",

    "viva": """
1. What is the full form of ELISA?
2. What is the principle of ELISA?
3. What is the role of antibodies in ELISA?
4. Why is an enzyme used in ELISA?
5. Name the different types of ELISA.
6. What is a substrate in ELISA?
7. Why is ELISA considered a sensitive technique?
8. What diseases can be detected using ELISA?
9. What is the advantage of Sandwich ELISA?
10. What is the importance of ELISA in diagnostics?
"""
},
"gel electrophoresis": {
    "explanation": """
• Gel Electrophoresis is a laboratory technique used to separate DNA, RNA, or proteins based on their size and charge.
• It is one of the most important techniques in molecular biology and biotechnology.
• The technique uses an electric field to move charged molecules through a gel matrix.
• DNA molecules are negatively charged due to the presence of phosphate groups.
• When an electric current is applied, DNA moves towards the positive electrode (anode).
• Smaller DNA fragments move faster through the gel than larger fragments.
• Agarose gel is commonly used for DNA separation, while polyacrylamide gel is often used for proteins.
• After separation, the DNA bands are visualized using staining agents and UV light.
• Each band represents DNA fragments of a specific size.
• Gel electrophoresis helps scientists analyze and compare genetic material.
""",

    "application": """
• DNA fingerprinting.
• Analysis of PCR products.
• Detection of genetic mutations.
• Verification of recombinant DNA.
• Forensic investigations.
• Paternity testing.
• Genome research.
• Biotechnology and molecular biology experiments.
""",

    "viva": """
1. What is gel electrophoresis?
2. What is the principle of gel electrophoresis?
3. Why does DNA move towards the positive electrode?
4. Which gel is commonly used for DNA separation?
5. Why do smaller DNA fragments move faster?
6. What is the role of agarose gel?
7. How are DNA bands visualized?
8. What is the function of electrophoresis buffer?
9. What are the applications of gel electrophoresis?
10. Why is gel electrophoresis important in biotechnology?
"""
},
"blast": {
    "explanation": """
• BLAST stands for Basic Local Alignment Search Tool.
• It is one of the most widely used bioinformatics tools for comparing biological sequences.
• BLAST helps scientists compare a DNA, RNA, or protein sequence against a large database.
• It identifies regions of similarity between sequences.
• Similar sequences often indicate similar functions or evolutionary relationships.
• BLAST was developed by Stephen Altschul and his colleagues in 1990.
• The tool works by searching databases for sequences that closely match the query sequence.
• BLAST is available through the National Center for Biotechnology Information (NCBI).
• Different types of BLAST are available for different purposes, such as BLASTn, BLASTp, BLASTx, tBLASTn, and tBLASTx.
• BLAST is considered one of the most important tools in modern bioinformatics research.
""",

    "application": """
• Identification of unknown DNA sequences.
• Finding homologous genes and proteins.
• Evolutionary and phylogenetic studies.
• Genome annotation.
• Identification of disease-related genes.
• Drug discovery research.
• Comparative genomics.
• Molecular biology and biotechnology research.
""",

    "viva": """
1. What is the full form of BLAST?
2. Who developed BLAST?
3. What is the purpose of BLAST?
4. What types of sequences can be analyzed using BLAST?
5. What is BLASTn?
6. What is BLASTp?
7. What is sequence alignment?
8. Which organization provides BLAST online?
9. Why is BLAST important in bioinformatics?
10. What are the applications of BLAST?
"""
},
"ncbi": {
    "explanation": """
• NCBI stands for National Center for Biotechnology Information.
• It is a part of the United States National Library of Medicine (NLM).
• NCBI was established in 1988 to develop information systems for molecular biology.
• It provides access to a large collection of biological databases and bioinformatics tools.
• NCBI stores information related to DNA sequences, RNA sequences, proteins, genomes, scientific articles, and genetic variations.
• Researchers worldwide use NCBI to retrieve and analyze biological data.
• One of the most popular tools provided by NCBI is BLAST, which is used for sequence similarity searching.
• NCBI also maintains GenBank, one of the world's largest nucleotide sequence databases.
• It plays a crucial role in genomics, molecular biology, medicine, and biotechnology research.
• NCBI resources are freely available to researchers, students, and scientists around the world.
""",

    "application": """
• Accessing DNA and protein sequence databases.
• Genome analysis and annotation.
• Sequence similarity searching using BLAST.
• Literature search through PubMed.
• Comparative genomics studies.
• Disease and mutation research.
• Drug discovery and development.
• Biotechnology and bioinformatics research.
""",

    "viva": """
1. What is the full form of NCBI?
2. When was NCBI established?
3. What is the main function of NCBI?
4. What is GenBank?
5. What is PubMed?
6. Which sequence search tool is provided by NCBI?
7. Why is NCBI important in bioinformatics?
8. What type of information is stored in NCBI databases?
9. Is NCBI freely accessible?
10. What are the applications of NCBI in biotechnology?
"""
},
"genomics": {
    "explanation": """
• Genomics is the branch of biology that studies the complete set of genetic material (genome) of an organism.
• The genome includes all the DNA present in an organism, including genes and non-coding sequences.
• Genomics focuses on the structure, function, mapping, sequencing, and analysis of genomes.
• The development of genome sequencing technologies has greatly advanced genomics research.
• One of the most important achievements in genomics was the Human Genome Project, which successfully mapped the entire human genome.
• Genomics helps scientists understand how genes interact with each other and with the environment.
• It provides insights into genetic diseases, evolution, and biological processes.
• Modern genomics uses computational tools and bioinformatics for analyzing large amounts of genetic data.
• Genomics has become an important field in medicine, agriculture, and biotechnology.
• It plays a major role in personalized medicine and disease prevention.
""",

    "application": """
• Identification of disease-causing genes.
• Personalized medicine and precision healthcare.
• Drug discovery and development.
• Crop improvement and agricultural biotechnology.
• Evolutionary and population genetics studies.
• Detection of genetic disorders.
• Cancer genomics research.
• Genome sequencing projects.
""",

    "viva": """
1. What is genomics?
2. What is a genome?
3. How is genomics different from genetics?
4. What was the Human Genome Project?
5. Why is genomics important?
6. How is genomics used in medicine?
7. What role does bioinformatics play in genomics?
8. What are the applications of genomics in agriculture?
9. How does genomics help in disease diagnosis?
10. What is personalized medicine?
"""
},
"proteomics": {
    "explanation": """
• Proteomics is the branch of science that studies the complete set of proteins produced by an organism, cell, or tissue.
• The complete collection of proteins in a cell is called the proteome.
• Proteomics helps scientists understand the structure, function, and interactions of proteins.
• Unlike the genome, the proteome is dynamic and changes according to environmental conditions and cellular activities.
• Proteins are responsible for most biological functions in living organisms.
• Proteomics involves identification, quantification, and characterization of proteins.
• Techniques such as SDS-PAGE, Western Blotting, and Mass Spectrometry are commonly used in proteomics.
• Proteomics helps in understanding diseases, cellular pathways, and biological processes.
• It plays a major role in drug discovery and biomarker identification.
• Proteomics is considered an important field in biotechnology, medicine, and pharmaceutical research.
""",

    "application": """
• Identification of disease biomarkers.
• Drug discovery and development.
• Cancer research.
• Protein structure and function analysis.
• Personalized medicine.
• Study of cellular signaling pathways.
• Biotechnology and pharmaceutical research.
• Identification of therapeutic targets.
""",

    "viva": """
1. What is proteomics?
2. What is a proteome?
3. How is proteomics different from genomics?
4. Why is the proteome considered dynamic?
5. Name some techniques used in proteomics.
6. What is the role of mass spectrometry in proteomics?
7. How is proteomics used in drug discovery?
8. What are biomarkers?
9. How does proteomics help in disease diagnosis?
10. What are the applications of proteomics in biotechnology?
"""
}, 
"sds-page": {
    "explanation": """
• SDS-PAGE stands for Sodium Dodecyl Sulfate Polyacrylamide Gel Electrophoresis.
• It is a technique used to separate proteins based on their molecular weight.
• SDS is a detergent that denatures proteins and gives them a uniform negative charge.
• Because all proteins receive a similar charge-to-mass ratio, they are separated mainly according to size.
• Polyacrylamide gel acts as a molecular sieve through which proteins migrate.
• Smaller proteins move faster through the gel, while larger proteins move more slowly.
• After electrophoresis, protein bands can be visualized using staining methods such as Coomassie Brilliant Blue.
• SDS-PAGE is widely used in molecular biology, biochemistry, and biotechnology laboratories.
• It is often used before Western Blotting for protein identification.
• SDS-PAGE is considered one of the most important methods for protein analysis.
""",

    "application": """
• Separation of proteins based on molecular weight.
• Analysis of protein purity.
• Estimation of protein size.
• Preparation of samples for Western Blotting.
• Biotechnology and pharmaceutical research.
• Study of protein expression.
• Identification of recombinant proteins.
• Academic and industrial research laboratories.
""",

    "viva": """
1. What is the full form of SDS-PAGE?
2. What is the principle of SDS-PAGE?
3. Why is SDS used in SDS-PAGE?
4. What is the function of polyacrylamide gel?
5. Why do smaller proteins move faster?
6. How are protein bands visualized after electrophoresis?
7. What is the role of SDS in protein separation?
8. How does SDS-PAGE differ from agarose gel electrophoresis?
9. What are the applications of SDS-PAGE?
10. Why is SDS-PAGE important in biotechnology?
"""
},
"western blotting": {
    "explanation": """
• Western Blotting is a laboratory technique used to detect specific proteins in a sample.
• It combines protein separation by SDS-PAGE with antibody-based detection.
• First, proteins are separated according to their molecular weight using SDS-PAGE.
• The separated proteins are then transferred from the gel onto a membrane, usually nitrocellulose or PVDF.
• The membrane is blocked to prevent non-specific binding of antibodies.
• A primary antibody specific to the target protein is added.
• A secondary antibody linked to an enzyme is then added to detect the primary antibody.
• After adding a substrate, a visible signal is produced indicating the presence of the target protein.
• Western Blotting is highly sensitive and specific for protein detection.
• It is widely used in research, diagnostics, and biotechnology laboratories.
""",

    "application": """
• Detection of specific proteins.
• Confirmation of protein expression.
• HIV diagnostic testing.
• Biomedical research.
• Cancer research.
• Drug development studies.
• Biotechnology and pharmaceutical research.
• Identification of recombinant proteins.
""",

    "viva": """
1. What is Western Blotting?
2. What is the principle of Western Blotting?
3. Why is SDS-PAGE performed before Western Blotting?
4. What is the purpose of transferring proteins to a membrane?
5. Which membranes are commonly used in Western Blotting?
6. What is the role of the primary antibody?
7. What is the role of the secondary antibody?
8. Why is blocking necessary in Western Blotting?
9. What are the applications of Western Blotting?
10. Why is Western Blotting considered a specific protein detection technique?
"""
},
"plasmid dna isolation": {
    "explanation": """
• Plasmid DNA Isolation is the process of extracting plasmid DNA from bacterial cells.
• Plasmids are small, circular, double-stranded DNA molecules found in bacteria.
• They replicate independently of the bacterial chromosome.
• Plasmids are commonly used as vectors in genetic engineering.
• The most widely used method for plasmid isolation is the Alkaline Lysis Method.
• In this method, bacterial cells are first harvested and lysed using alkaline solutions.
• Cell membranes and proteins are disrupted, releasing cellular contents.
• Upon neutralization, chromosomal DNA and proteins precipitate, while plasmid DNA remains in solution.
• The plasmid DNA is then purified and collected by centrifugation.
• The isolated plasmid DNA can be used for cloning, sequencing, PCR, and other molecular biology applications.
""",

    "application": """
• Gene cloning experiments.
• Recombinant DNA technology.
• DNA sequencing.
• PCR template preparation.
• Genetic engineering studies.
• Production of recombinant proteins.
• Biotechnology research.
• Development of genetically modified organisms (GMOs).
""",

    "viva": """
1. What is a plasmid?
2. Why are plasmids called extra-chromosomal DNA?
3. What is the principle of plasmid DNA isolation?
4. Which method is commonly used for plasmid isolation?
5. Why is alkaline lysis used?
6. What happens during the neutralization step?
7. Why does plasmid DNA remain in solution?
8. What are the applications of isolated plasmid DNA?
9. Why are plasmids important in genetic engineering?
10. What is the difference between plasmid DNA and chromosomal DNA?
"""
},
"restriction enzymes": {
    "explanation": """
• Restriction enzymes are specialized proteins that cut DNA at specific nucleotide sequences.
• They are also known as restriction endonucleases.
• These enzymes were first discovered in bacteria, where they act as a defense mechanism against invading viruses (bacteriophages).
• Restriction enzymes recognize specific DNA sequences called recognition sites.
• Once the recognition site is identified, the enzyme cuts the DNA at or near that site.
• Different restriction enzymes recognize different DNA sequences.
• Some enzymes produce sticky ends, while others produce blunt ends.
• Sticky ends contain single-stranded overhangs that can easily pair with complementary DNA fragments.
• Restriction enzymes are essential tools in recombinant DNA technology and genetic engineering.
• Examples of commonly used restriction enzymes include EcoRI, HindIII, BamHI, and HaeIII.
""",

    "application": """
• Gene cloning.
• Recombinant DNA technology.
• DNA mapping.
• Genetic engineering.
• Production of genetically modified organisms (GMOs).
• DNA fingerprinting.
• Molecular biology research.
• Biotechnology and pharmaceutical industries.
""",

    "viva": """
1. What are restriction enzymes?
2. Why are they called molecular scissors?
3. What is a recognition site?
4. What is the difference between sticky ends and blunt ends?
5. Name two commonly used restriction enzymes.
6. What is the role of restriction enzymes in bacteria?
7. How are restriction enzymes used in genetic engineering?
8. What are sticky ends?
9. What are blunt ends?
10. Why are restriction enzymes important in biotechnology?
"""
},
"dna sequencing": {
    "explanation": """
• DNA Sequencing is the process of determining the exact order of nucleotides in a DNA molecule.
• The nucleotides present in DNA are Adenine (A), Thymine (T), Guanine (G), and Cytosine (C).
• DNA sequencing helps scientists understand genetic information stored in DNA.
• The first widely used sequencing method was developed by Frederick Sanger and is known as Sanger Sequencing.
• Modern sequencing technologies are called Next Generation Sequencing (NGS).
• DNA sequencing is used to identify mutations, study genes, and analyze genomes.
• It plays an important role in genomics, biotechnology, and medical research.
• Sequencing helps in understanding genetic diseases and evolutionary relationships.
• Large-scale sequencing projects such as the Human Genome Project have greatly advanced biological research.
• DNA sequencing is considered one of the most powerful tools in molecular biology.
""",

    "application": """
• Identification of genetic disorders.
• Genome sequencing projects.
• Personalized medicine.
• Cancer research.
• Drug discovery and development.
• Evolutionary studies.
• Forensic science and DNA fingerprinting.
• Biotechnology and bioinformatics research.
""",

    "viva": """
1. What is DNA sequencing?
2. Who developed the Sanger sequencing method?
3. What are the four nucleotides present in DNA?
4. What is the purpose of DNA sequencing?
5. What is Next Generation Sequencing (NGS)?
6. How is DNA sequencing used in medicine?
7. What was the Human Genome Project?
8. Why is DNA sequencing important in biotechnology?
9. How does DNA sequencing help in disease diagnosis?
10. What are the applications of DNA sequencing?
"""
},
"transformation": {
    "explanation": """
• Transformation is the process by which a bacterial cell takes up foreign DNA from its surroundings.
• It is one of the most important techniques used in genetic engineering and molecular biology.
• During transformation, plasmid DNA is introduced into bacterial cells.
• The bacteria that can take up foreign DNA are called competent cells.
• Competent cells are usually prepared using calcium chloride treatment or electroporation.
• Once the plasmid enters the bacterial cell, it can replicate independently.
• The transformed bacteria can express new genes carried by the plasmid.
• Transformation is commonly performed in Escherichia coli (E. coli).
• Selection markers such as antibiotic resistance genes help identify transformed cells.
• Transformation is widely used in cloning, recombinant DNA technology, and biotechnology research.
""",

    "application": """
• Gene cloning experiments.
• Recombinant DNA technology.
• Production of recombinant proteins.
• Genetic engineering research.
• Development of genetically modified organisms (GMOs).
• Pharmaceutical protein production.
• Biotechnology research.
• Molecular biology studies.
""",

    "viva": """
1. What is transformation?
2. What are competent cells?
3. Why are competent cells required for transformation?
4. Which bacterium is commonly used for transformation?
5. What is the role of plasmids in transformation?
6. What is calcium chloride treatment?
7. What is electroporation?
8. How are transformed cells identified?
9. Why are antibiotic resistance genes used?
10. What are the applications of transformation in biotechnology?
"""
},
"recombinant dna technology": {
    "explanation": """
• Recombinant DNA Technology (rDNA Technology) is a technique used to combine DNA from different sources into a single DNA molecule.
• It is one of the most important tools in modern biotechnology and genetic engineering.
• The DNA molecule produced by joining DNA from different organisms is called recombinant DNA.
• This technology involves the use of restriction enzymes, DNA ligase, vectors, and host cells.
• Restriction enzymes cut DNA at specific recognition sites.
• DNA ligase joins DNA fragments together to form recombinant DNA.
• Vectors such as plasmids are used to carry foreign DNA into host cells.
• The recombinant DNA is introduced into host cells through transformation.
• The host cells then replicate and express the inserted gene.
• Recombinant DNA technology has revolutionized medicine, agriculture, and industrial biotechnology.
• One of the most successful applications is the production of human insulin using genetically modified bacteria.
""",

    "application": """
• Production of human insulin.
• Development of genetically modified crops.
• Gene therapy research.
• Vaccine production.
• Production of recombinant proteins.
• Treatment of genetic disorders.
• Agricultural biotechnology.
• Pharmaceutical and industrial biotechnology.
""",

    "viva": """
1. What is recombinant DNA technology?
2. What is recombinant DNA?
3. What are the main steps involved in rDNA technology?
4. What is the role of restriction enzymes?
5. What is the function of DNA ligase?
6. What are vectors?
7. Why are plasmids commonly used as vectors?
8. How is recombinant DNA introduced into host cells?
9. What are the applications of recombinant DNA technology?
10. How is insulin produced using recombinant DNA technology?
"""
},
"gene cloning": {
    "explanation": """
• Gene cloning is the process of producing multiple identical copies of a specific gene or DNA fragment.
• It is one of the most important techniques in molecular biology and genetic engineering.
• The process begins with the isolation of the desired gene from a DNA source.
• The gene is inserted into a vector such as a plasmid using restriction enzymes and DNA ligase.
• The recombinant plasmid is then introduced into a host cell, usually E. coli.
• The host cell multiplies and produces many copies of the inserted gene.
• Selection markers such as antibiotic resistance genes help identify successfully transformed cells.
• Gene cloning allows scientists to study gene structure and function in detail.
• It is widely used in research, medicine, agriculture, and biotechnology.
• Gene cloning has played a major role in the production of recombinant proteins and therapeutic products.
""",

    "application": """
• Production of recombinant insulin.
• Gene function studies.
• Production of therapeutic proteins.
• Development of genetically modified crops.
• Vaccine production.
• Gene therapy research.
• Drug discovery and development.
• Biotechnology and pharmaceutical industries.
""",

    "viva": """
1. What is gene cloning?
2. What is the purpose of gene cloning?
3. What are vectors in gene cloning?
4. Why are plasmids commonly used as vectors?
5. What is the role of DNA ligase?
6. What are restriction enzymes?
7. Which host organism is commonly used in gene cloning?
8. What are selectable markers?
9. What are the applications of gene cloning?
10. How is recombinant insulin produced using gene cloning?
"""
},
"stem cells": {
    "explanation": """
• Stem cells are special cells that have the ability to divide and develop into different types of specialized cells.
• They are considered the basic building blocks of tissues and organs.
• Stem cells have two unique properties: self-renewal and differentiation.
• Self-renewal means they can divide and produce more stem cells.
• Differentiation means they can develop into specialized cells such as muscle cells, nerve cells, or blood cells.
• There are two main types of stem cells: Embryonic Stem Cells and Adult Stem Cells.
• Embryonic stem cells are pluripotent, meaning they can develop into almost any cell type in the body.
• Adult stem cells are found in tissues such as bone marrow and help repair damaged tissues.
• Stem cell research has opened new possibilities for treating diseases and injuries.
• Stem cells are considered one of the most promising areas of modern biotechnology and medicine.
""",

    "application": """
• Treatment of blood disorders such as leukemia.
• Regenerative medicine and tissue repair.
• Research on genetic diseases.
• Drug testing and development.
• Treatment of spinal cord injuries.
• Organ and tissue engineering.
• Personalized medicine.
• Biomedical research.
""",

    "viva": """
1. What are stem cells?
2. What are the unique properties of stem cells?
3. What is self-renewal?
4. What is differentiation?
5. Name the main types of stem cells.
6. What are embryonic stem cells?
7. What are adult stem cells?
8. How are stem cells used in medicine?
9. What is regenerative medicine?
10. Why are stem cells important in biotechnology?
"""
},

"monoclonal antibodies": {
    "explanation": """
• Monoclonal antibodies are identical antibodies produced by a single clone of B-lymphocytes.
• They are designed to recognize and bind to a specific antigen.
• Monoclonal antibodies were first developed by Georges Köhler and César Milstein in 1975.
• They are produced using hybridoma technology.
• In hybridoma technology, antibody-producing B cells are fused with myeloma (cancer) cells.
• The resulting hybrid cells, called hybridomas, can produce large quantities of identical antibodies.
• Monoclonal antibodies are highly specific because they recognize only one antigenic site (epitope).
• They are widely used in diagnosis, treatment, and biomedical research.
• Monoclonal antibodies have revolutionized the treatment of many diseases, especially cancer and autoimmune disorders.
• They are considered one of the most important products of modern biotechnology.
""",

    "application": """
• Cancer therapy.
• Diagnosis of infectious diseases.
• ELISA and other immunological tests.
• Treatment of autoimmune diseases.
• Pregnancy testing.
• Drug delivery systems.
• Biomedical research.
• Detection of specific proteins and biomarkers.
""",

    "viva": """
1. What are monoclonal antibodies?
2. What is the principle behind monoclonal antibody production?
3. What is hybridoma technology?
4. Who developed monoclonal antibodies?
5. What are hybridoma cells?
6. Why are monoclonal antibodies highly specific?
7. What is an antigen?
8. What are the applications of monoclonal antibodies?
9. How are monoclonal antibodies used in cancer treatment?
10. Why are monoclonal antibodies important in biotechnology?
"""
},
}
@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    topic = request.args.get("topic")
    if topic and topic in topics:
        result = topics[topic]

    if request.method == "POST":

        topic = request.form["topic"].strip().lower()

        if topic in topics:
            result = topics[topic]

        else:
            result = {
                "explanation": "Topic not available.",
                "application": "-",
                "viva": "-"
            }

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)