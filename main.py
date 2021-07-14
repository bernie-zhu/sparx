import Parsers.ParsePatent
import Parsers.ParsePatentV_2
import TargetInformation
import testFile
from CompanyTargetsDictionary import PatentTargets

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(PatentTargets.RunningCompanyData("Novartis"))
    #print(PatentTargets.GeneListFromFile())
    #print(PatentTargets.RunningCompanyFinal(PatentTargets.CompanyGenesFromFile()))
    #print(TargetInformation.targetinformation())
