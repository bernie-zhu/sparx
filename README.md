# sparx

To run OpenTargets+Aliases.ipynb, download and extract the geckodriver.exe file from https://github.com/mozilla/geckodriver/releases, then paste it into the first cell where it says "driver.webdriver()" so that it looks like "driver.webdriver(executable_path=r'your_system_path\geckodriver.exe')". Also, make sure Firefox is installed on your system, too. In the second cell, where it says "diseaseconditions, names, genename, link1, link2, closestpossibletarget = getopentargets('GeneNameHere')", type in any gene name. 

If the target is found, it'll show up and return the alias names + the www.opentargets.org associated diseases/conditions. If it's not found initially but has a similar or related gene, it will show the similar target instead. If that can't be found, then it'll say it can't be found.
