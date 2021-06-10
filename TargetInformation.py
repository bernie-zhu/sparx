from OpenTargetsAliases import OpenTargetAndAliases

diseases = []
aliases = []
tentargets = ["TP53", "TNF", "EGFR", "VEGFA", "APOE", "IL6", "TGFBI", "MTHFR", "ESR1", "AKT1"]
aliaslists = [['Tumor Protein P53', 'P53', 'Cellular Tumor Antigen P53', 'Phosphoprotein P53', 'Antigen NY-CO-13', 'LFS1', 'Transformation-Related Protein 53', 'Mutant Tumor Protein 53', 'Li-Fraumeni Syndrome', 'P53 Tumor Suppressor', 'Tumor Suppressor P53', 'Tumor Supressor P53', 'Tumor Protein 53', 'BMFS5', 'TRP53', 'BCC7', 'TP53'],
['Tumor Necrosis Factor', 'TNF-Alpha', 'TNFSF2', 'Tumor Necrosis Factor Ligand Superfamily Member 2', 'TNF-A', 'TNFA', 'DIF', 'Tumor Necrosis Factor (TNF Superfamily, Member', 'Tumor Necrosis Factor Ligand 1F', 'Tumor Necrosis Factor-Alpha', 'TNF Superfamily, Member', 'TNF, Macrophage-Derived', 'TNF, Monocyte-Derived', 'APC1 Protein', 'Cachectin', 'TNLG1F', 'TNF'],
['Epidermal Growth Factor Receptor', 'ERBB1', 'Receptor Tyrosine-Protein Kinase ErbB-1', 'Erb-B2 Receptor Tyrosine Kinase 1', 'Proto-Oncogene C-ErbB-1', 'EC 2.7.10.1', 'ERBB', 'ERRP', 'HER1', 'Epidermal Growth Factor Receptor (Avian Erythroblastic Leukemia Viral (V-Erb-B) Oncogene Homolog)', 'Erythroblastic Leukemia Viral (V-Erb-B) Oncogene Homolog (Avian)', 'Avian Erythroblastic Leukemia Viral (V-Erb-B) Oncogene Homolog', 'Epidermal Growth Factor Receptor Tyrosine Kinase Domain', 'Cell Proliferation-Inducing Protein 61', 'Cell Growth Inhibiting Protein 40', 'EC 2.7.10', 'NISBD2', 'PIG61', 'MENA', 'EGFR'],
['Vascular Endothelial Growth Factor A', 'VPF', 'Vascular Permeability Factor', 'VEGF-A', 'VEGF', 'Vascular Endothelial Growth Factor A121', 'Vascular Endothelial Growth Factor A165', 'Vascular Endothelial Growth Factor', 'MVCD1', 'VEGFA'],
['Apolipoprotein E', 'Alzheimer Disease', 'Apolipoprotein E3', 'LDLCQ5', 'APO-E', 'ApoE4', 'Apo-E', 'APOE', 'AD2', 'LPG'],
['Interleukin 6', 'IL-6', 'B-Cell Stimulatory Factor 2', 'CTL Differentiation Factor', 'Hybridoma Growth Factor', 'Interferon Beta-2', 'Interleukin-6', 'IFN-Beta-2', 'BSF-2', 'IFNB2', 'BSF2', 'CDF', 'HGF', 'HSF', 'Interleukin 6 (Interferon, Beta', 'B-Cell Differentiation Factor', 'Interferon, Beta', 'Interleukin BSF-2', 'IL6'],
['Transforming Growth Factor Beta Induced', 'BIGH3', 'Transforming Growth Factor-Beta-Induced Protein Ig-H3', 'Transforming Growth Factor, Beta-Induced, 68kD', 'RGD-Containing Collagen-Associated Protein', 'Kerato-Epithelin', 'Beta Ig-H3', 'RGD-CAP', 'CDGG1', 'CDB1', 'Transforming Growth Factor, Beta-Induced, 68kDa', 'Transforming Growth Factor Beta-Induced 68kDa', 'Betaig-H3', 'TGFBI', 'CDG2', 'CSD1', 'CSD2', 'CSD3', 'EBMD', 'LCD1', 'CSD'],
['Methylenetetrahydrofolate Reductase', '5,10-Methylenetetrahydrofolate Reductase (NADPH)', 'Methylenetetrahydrofolate Reductase (NAD(P)H)', 'EC 1.5.1.20', 'MTHFR'],
['Estrogen Receptor 1', 'Nuclear Receptor Subfamily 3 Group A Member 1', 'ER-Alpha', 'NR3A1', 'Oestrogen Receptor Alpha', 'Estradiol Receptor', 'E2 Receptor Alpha', 'Estrogen Receptor', 'ESR', 'Era', 'ER', 'Estrogen Receptor Alpha E1-N2-E2-1-2', 'Estrogen Receptor Alpha E1-E2-1-2', 'Estrogen Nuclear Receptor Alpha', 'Estrogen Receptor Alpha', 'ESTRR', 'ESRA', 'ESR1'],
['AKT Serine/Threonine Kinase 1', 'PKB', 'RAC', 'V-Akt Murine Thymoma Viral Oncogene Homolog 1', 'RAC-Alpha Serine/Threonine-Protein Kinase', 'Protein Kinase B Alpha', 'Proto-Oncogene C-Akt', 'Protein Kinase B', 'RAC-PK-Alpha', 'EC 2.7.11.1', 'PKB Alpha', 'PRKBA', 'AKT', 'V-Akt Murine Thymoma Viral Oncogene-Like Protein 1', 'Serine-Threonine Protein Kinase', 'Rac Protein Kinase Alpha', 'PKB-ALPHA', 'RAC-ALPHA', 'RAC-Alpha', 'EC 2.7.11', 'AKT1m', 'AKT1']]


def targetinformation():
    for target in tentargets:
        targetalias = OpenTargetAndAliases()

        diseaseconditions, alias, genename, link1, link2, closestpossibletarget = targetalias.getopentargets(target)
        diseases.append(diseaseconditions)
        aliases.append(alias)
        print(diseaseconditions)
        print(alias)

    return diseases, aliases
