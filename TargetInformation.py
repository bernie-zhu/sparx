from selenium.webdriver.firefox import webdriver

import gettinggenelist
from OpenTargetsAliases import OpenTargetAndAliases
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time

import TargetInformation

diseases = []
aliases = []
tentargets = [
    'EHHADH', 'EHMT1', 'EHMT2', 'EI24', 'EID1', 'EID2', 'EID2B', 'EID3', 'EIF1', 'EIF1AD', 'EIF1AX', 'EIF1AY', 'EIF1B', 'EIF2A', 'EIF2AK1', 'EIF2AK2', 'EIF2AK3', 'EIF2AK4', 'EIF2B1', 'EIF2B2', 'EIF2B3', 'EIF2B4', 'EIF2B5', 'EIF2D', 'EIF2S1', 'EIF2S2', 'EIF2S3', 'EIF2S3B', 'EIF3A', 'EIF3B', 'EIF3C', 'EIF3CL', 'EIF3D', 'EIF3E', 'EIF3F', 'EIF3G', 'EIF3H', 'EIF3I', 'EIF3J', 'EIF3K', 'EIF3L', 'EIF3M', 'EIF4A1', 'EIF4A2', 'EIF4A3', 'EIF4B', 'EIF4E', 'EIF4E1B', 'EIF4E2', 'EIF4E3', 'EIF4EBP1', 'EIF4EBP2', 'EIF4EBP3', 'EIF4ENIF1', 'EIF4G1', 'EIF4G2', 'EIF4G3', 'EIF4H', 'EIF5', 'EIF5A', 'EIF5A2', 'EIF5AL1', 'EIF5B', 'EIF6', 'EIPR1', 'ELAC1', 'ELAC2', 'ELANE', 'ELAPOR1', 'ELAPOR2', 'ELAVL1', 'ELAVL2', 'ELAVL3', 'ELAVL4', 'ELF1', 'ELF2', 'ELF3', 'ELF4', 'ELF5', 'ELFN1', 'ELFN2', 'ELK1', 'ELK3', 'ELK4', 'ELL', 'ELL2', 'ELL3', 'ELMO1', 'ELMO2', 'ELMO3', 'ELMOD1', 'ELMOD2', 'ELMOD3', 'ELN', 'ELOA', 'ELOA2', 'ELOB', 'ELOC', 'ELOF1', 'ELOVL1', 'ELOVL2', 'ELOVL3', 'ELOVL4', 'ELOVL5', 'ELOVL6', 'ELOVL7', 'ELP1', 'ELP2', 'ELP3', 'ELP4', 'ELP5', 'ELP6', 'ELSPBP1', 'EMB', 'EMC1', 'EMC2', 'EMC3', 'EMC4', 'EMC6', 'EMC7', 'EMC8', 'EMC9', 'EMC10', 'EMCN', 'EMD', 'EME1', 'EME2', 'EMG1', 'EMID1', 'EMILIN1', 'EMILIN2', 'EMILIN3', 'EML1', 'EML2', 'EML3', 'EML4', 'EML5', 'EML6', 'EMP1', 'EMP2', 'EMP3', 'EMSY', 'EMX1', 'EMX2', 'EN1', 'EN2', 'ENAH', 'ENAM', 'ENC1', 'ENDOD1', 'ENDOG', 'ENDOU', 'ENDOV', 'ENG', 'ENGASE', 'ENHO', 'ENKD1', 'ENKUR', 'ENO1', 'ENO2', 'ENO3', 'ENO4', 'ENOPH1', 'ENOSF1', 'ENOX1', 'ENOX2', 'ENPEP', 'ENPP1', 'ENPP2', 'ENPP3', 'ENPP4', 'ENPP5', 'ENPP6', 'ENPP7', 'ENSA', 'ENTHD1', 'ENTPD1', 'ENTPD2', 'ENTPD3', 'ENTPD4', 'ENTPD5', 'ENTPD6', 'ENTPD7', 'ENTPD8', 'ENTR1', 'ENY2']

t = ["EHD4"]

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
    driver = webdriver.Firefox()

    for target in tentargets:
        targetalias = OpenTargetAndAliases()
        diseaseconditions, alias, genename, drivr, link2, closestpossibletarget = targetalias.getopentargets(target, driver)
        diseases.append(diseaseconditions)

        #aliases.append(alias)
        print(diseaseconditions)
        #print(aliases)
        #print(alias)

    driver.close()
    return aliases

def getcertain():
    print(tentargets[82])

