
def parse(driver, alias_list, genes, target_frequency, num_claims):
    results = []
    count = [0] * len(alias_list)

    common_words = [ 'chromosome', 'protein', 'cell', 'light', 'gab', 'asp', 'rest', 'lan', 'ara', 'sur', 'mat', 'ace', 'cad', 'act', 'lap', 'pap', 'sah', 'fop', 'pan', 'sac', 'hot', 'ado', 'dar', 'bar', 'alf', 'aga', 'rab', 'rip', 'auh', 'art', 'aid', 'fix', 'arm', 'his', 'alb', 'not', 'alk', 'lak', 'hak', 'alp', 'aly', 'ref', 'mad', 'amt', 'dao', 'mud', 'sap', 'ape', 'arc', 'eld', 'tic', 'car', 'ash', 'ask', 'ase', 'arx', 'bah', 'tug', 'ass', 'tat', 'ham', 'ate', 'nod', 'orf', 'ark', 'zag', 'bat', 'bad', 'hap', 'bis', 'boo', 'bod', 'bam', 'all', 'bid', 'nix', 'pip', 'imp', 'fad', 'nat', 'cap', 'ana', 'bag', 'gip', 'aln', 'cab', 'sip', 'cam', 'cop', 'ice', 'cat', 'dos', 'gif', 'dis', 'aim', 'mal', 'fat', 'bor', 'dup', 'lip', 'bal', 'reh', 'kip', 'cit', 'tog', 'hod', 'sty', 'aft', 'tax', 'fan', 'ich', 'amy', 'cox', 'hug', 'nar', 'cot', 'nip', 'cry', 'nap', 'cut', 'mig', 'wid', 'dag', 'dap', 'zip', 'nep', 'fig', 'pad', 'rig', 'lad', 'sag', 'bet', 'hep', 'pin', 'red', 'eta', 'sin', 'hub', 'hud', 'net', 'ell', 'men', 'fae', 'pob', 'end', 'apa', 'elk', 'era', 'mag', 'erg', 'wad', 'bop', 'jam', 'kat', 'fag', 'fir', 'fib', 'cal', 'jet', 'ago', 'fez', 'ach', 'rhe', 'tap', 'cig', 'fra', 'win', 'fry', 'fur', 'gad', 'gal', 'gas', 'gan', 'gig', 'gem', 'gen', 'cee', 'inn', 'odd', 'edh', 'gam', 'gat', 'aho', 'poh', 'phi', 'bob', 'dip', 'bom', 'ben', 'gyp', 'had', 'hao', 'sup', 'aku', 'ski', 'sit', 'hex', 'hip', 'dob', 'hop', 'ame', 'mot', 'ide', 'wim', 'ilk', 'mar', 'pit', 'ism', 'tip', 'swa', 'par', 'duo', 'kin', 'kit', 'rod', 'oes', 'lat', 'lab', 'lax', 'lac', 'las', 'lox', 'pal', 'rap', 'tal', 'lum', 'mum', 'mel', 'zak', 'tau', 'mir', 'mas', 'eat', 'hic', 'met', 'mib', 'mix', 'cob', 'gaj', 'rox', 'mog', 'uta', 'dug', 'sea', 'mim', 'pam', 'gup', 'san', 'nag', 'dan', 'neb', 'aka', 'nid', 'mop', 'awd', 'nog', 'sar', 'tec', 'can', 'nut', 'oaf', 'oat', 'bey', 'ped', 'dop', 'dor', 'kor', 'kop', 'mor', 'opt', 'gum', 'git', 'pac', 'pep', 'peg', 'pah', 'ken', 'pen', 'sis', 'lim', 'per', 'pes', 'aum', 'rea', 'bap', 'hyp', 'dod', 'pir', 'zac', 'sex', 'sil', 'pon', 'cyp', 'rax', 'pox', 'pry', 'lar', 'ram', 'rah', 'ray', 'ran', 'gap', 'rim', 'bog', 'tar', 'reg', 'rel', 'age', 'get', 'ret', 'rho', 'pia', 'rit', 'tor', 'rad', 'nef', 'saa', 'het', 'sly', 'sat', 'via', 'sla', 'lei', 'set', 'spa', 'mob', 'map', 'sab', 'she', 'bit', 'sao', 'ait', 'mae', 'err', 'ast', 'ant', 'yea', 'led', 'sma', 'cod', 'jab', 'sod', 'son', 'dom', 'sho', 'elf', 'sri', 'pst', 'nam', 'tam', 'lag', 'nak', 'out', 'cha', 'top', 'tie', 'dak', 'aes', 'til', 'hat', 'lit', 'taj', 'van', 'tox', 'ket', 'tra', 'goa', 'lam', 'tst', 'tub', 'bug', 'sky', 'kos', 'soc', 'fip', 'fam', 'ust', 'vim', 'foe', 'was', 'wiz', 'gud', 'for', 'yap', 'yes', 'rog', 'fog', 'flu', 'dub', 'nesh', 'thio', 'acca', 'scad', 'ache', 'bach', 'trap', 'acta', 'adda', 'dreg', 'alba', 'pike', 'crag', 'ager', 'rage', 'mulk', 'spat', 'sahh', 'amid', 'aire', 'harp', 'afar', 'lobe', 'alas', 'flap', 'plap', 'palp', 'race', 'ankh', 'hank', 'mank', 'mask', 'carp', 'liar', 'gapo', 'zeta', 'apex', 'apod', 'grit', 'solo', 'carr', 'arse', 'taps', 'boat', 'aura', 'axil', 'bank', 'sari', 'puma', 'diva', 'clap', 'bean', 'best', 'bash', 'bike', 'zyme', 'boll', 'bora', 'iris', 'temp', 'lord', 'cava', 'cain', 'camb', 'calm', 'camp', 'cart', 'cask', 'mice', 'cast', 'hech', 'tape', 'peho', 'sise', 'marc', 'teck', 'cram', 'nail', 'ecad', 'cell', 'lipa', 'bite', 'cash', 'flip', 'chad', 'chat', 'chia', 'chit', 'call', 'brag', 'hick', 'mint', 'egma', 'clip', 'mist', 'pang', 'coil', 'copa', 'cope', 'cate', 'grog', 'whim', 'eros', 'stap', 'coco', 'find', 'chop', 'vasa', 'cage', 'deft', 'slat', 'dele', 'post', 'desi', 'glow', 'tuba', 'dram', 'ramp', 'neap', 'full', 'mirk', 'mend', 'dine', 'aria', 'heed', 'pika', 'past', 'perk', 'face', 'enam', 'masa', 'lulu', 'tref', 'jama', 'mani', 'simp', 'fast', 'fate', 'mass', 'anoa', 'gugu', 'slim', 'pace', 'gale', 'galp', 'galt', 'pais', 'gast', 'blot', 'gala', 'papa', 'gnat', 'pist', 'gasp', 'grid', 'mona', 'grip', 'bark', 'spin', 'star', 'gulp', 'gype', 'sect', 'soul', 'heel', 'hexa', 'rasp', 'hint', 'fist', 'toto', 'hunk', 'mule', 'gilt', 'nope', 'mise', 'ship', 'skip', 'itch', 'tied', 'shap', 'swap', 'jamb', 'duet', 'mink', 'calp', 'trek', 'task', 'toss', 'kell', 'salp', 'arms', 'kino', 'kras', 'lama', 'lamp', 'lime', 'bara', 'trip', 'crop', 'mall', 'bene', 'mana', 'stop', 'miss', 'mark', 'visa', 'goat', 'memo', 'feat', 'tali', 'mica', 'coda', 'mimp', 'frap', 'mima', 'atip', 'musk', 'idol', 'naga', 'napa', 'soph', 'caph', 'wish', 'nude', 'mail', 'clan', 'poem', 'mare', 'copr', 'saki', 'pomp', 'umph', 'tirr', 'numb', 'hoga', 'scot', 'asor', 'palm', 'pank', 'pari', 'pate', 'terp', 'penk', 'purl', 'sera', 'pick', 'prep', 'plat', 'tech', 'peri', 'plod', 'fels', 'noxa', 'pent', 'soft', 'pole', 'fils', 'polk', 'poll', 'pote', 'prat', 'kepi', 'pram', 'paga', 'loam', 'pact', 'paip', 'iota', 'paca', 'step', 'slob', 'asci', 'prey', 'gata', 'grab', 'narr', 'rasa', 'rain', 'lark', 'swan', 'anes', 'reck', 'rest', 'oboe', 'sudd', 'mina', 'rick', 'rita', 'ding', 'riff', 'scar', 'raga', 'sage', 'sard', 'scap', 'tymp', 'sele', 'selt', 'sell', 'seme', 'mart', 'type', 'caid', 'fish', 'posh', 'shot', 'sike', 'tera', 'siva', 'skil', 'slap', 'slam', 'kali', 'glut', 'smit', 'sert', 'taut', 'indy', 'cape', 'slug', 'snap', 'wisp', 'wise', 'spar', 'mast', 'hash', 'snip', 'fact', 'hare', 'fell', 'stam', 'spak', 'chip', 'stum', 'sync', 'tank', 'tapa', 'tars', 'stud', 'tele', 'spot', 'tiar', 'tram', 'toll', 'hole', 'molt', 'rank', 'troy', 'lard', 'baff', 'klip', 'cark', 'topi', 'tora', 'teap', 'cusp', 'trim', 'sink', 'trio', 'tara', 'stot', 'tube', 'fiat', 'tula', 'kist', 'risp', 'sans', 'melt', 'vill', 'crig', 'warp', 'wasp', 'wave', 'wash', 'prof', 'trag', 'wire', 'whip', 'bomb', 'samp', 'arch', 'nipa', 'ream', 'agrin', 'verge', 'armer', 'tango', 'crash', 'caper', 'atrip', 'boule', 'spurt', 'cocoa', 'cramp', 'shapy', 'flash', 'plack', 'pesky', 'blast', 'cease', 'march', 'flame', 'botch', 'champ', 'clasp', 'helix', 'pilar', 'clint', 'clock', 'alien', 'oasis', 'smile', 'aspic', 'lotus', 'camel', 'pasha', 'dicer', 'soggy', 'delta', 'monad', 'tramp', 'pilot', 'dance', 'carom', 'pinto', 'theta', 'goofy', 'picot', 'homer', 'cameo', 'jerky', 'dream', 'slack', 'slick', 'large', 'pinch', 'lamin', 'clerk', 'rifle', 'armet', 'marco', 'gable', 'atopy', 'lyric', 'jumpy', 'mucin', 'beach', 'mater', 'nodal', 'capon', 'notum', 'minor', 'bravo', 'snark', 'gumby', 'elfin', 'clamp', 'prism', 'chime', 'clove', 'prima', 'prune', 'purga', 'gripe', 'scald', 'renin', 'rhino', 'grail', 'crept', 'baron', 'pacer', 'great', 'saraf', 'scamp', 'shank', 'blame', 'imino', 'chasm', 'snail', 'spart', 'sharp', 'spice', 'strap', 'crest', 'sting', 'strad', 'unrip', 'drago', 'grasp', 'chico', 'trica', 'trade', 'trail', 'tweak', 'thank', 'light', 'mover', 'truss', 'fleer', 'stamp', 'twist', 'vista', 'acinus', 'bright', 'humbug', 'scythe', 'pallid', 'apache', 'flower', 'castor', 'exodus', 'pippin', 'dapper', 'stella', 'pander', 'toupee', 'irisin', 'dieter', 'amylin', 'impact', 'cinema', 'danger', 'sesame', 'oracle', 'simple', 'damage', 'matins', 'myosin', 'minion', 'nobody', 'merlin', 'noggin', 'enigma', 'splash', 'parkin', 'largen', 'canvas', 'dragon', 'gospel', 'raptor', 'pontin', 'enrage', 'mirage', 'secret', 'citrin', 'chisel', 'sorbin', 'spring', 'nuance', 'themis', 'sancho', 'killer', 'trance', 'beacon', 'socius', 'abraxas', 'albumin', 'toddler', 'gracile', 'iceberg', 'tactile', 'flattop', 'cryptic', 'chymase', 'dullard', 'twister', 'stellar', 'elastin', 'genesis', 'trident', 'gastrin', 'guanase', 'lactase', 'gremlin', 'hoatzin', 'activin', 'insulin', 'caprice', 'maestro', 'mustang', 'whistle', 'paladin', 'bazooka', 'staring', 'goliath', 'serrate', 'spatial', 'carabin', 'treacle', 'tuberin', 'twinkle', 'unkempt', 'coaster']



    # TITLE
    # titleStr = driver.find_element_by_id("title").text
    titleStr = driver.title.split(" - ")[1].strip()

    # print(titleStr)
    for aliases in alias_list:
        for cur in aliases:
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in titleStr and str(cur).lower() not in common_words:
                    countTitle = (titleStr.count(" " + str(cur) + " ") + titleStr.count(" " + str(cur) + ".") + \
                                  titleStr.count(" " + str(cur) + ",") + titleStr.count(" " + str(cur) + "'") + \
                                  titleStr.count(" " + str(cur) + "/") + titleStr.count("/" + str(cur) + " ") + \
                                  titleStr.count(" " + str(cur) + ":") + titleStr.count("-" + str(cur) + " ") + \
                                  titleStr.count("(" + str(cur) + ")") + titleStr.count("\"" + str(cur) + "\""))
                    if countTitle != 0:
                        results.append(aliases[0])
                        count[alias_list.index(aliases)] += countTitle
                        print("Found in title: " + aliases[0] + " " + cur)
                        break
                ## MAYBE ADD LENGTH RESTRICTION, len(str(cur))>5 and str(cur).lower() in titleStr
                elif len(str(cur)) > 3 and str(cur).lower() in titleStr and str(cur).lower() not in common_words:
                    lower = str(cur).lower()
                    countTitle = (titleStr.count(" " + lower + " ") + titleStr.count(" " + lower + ".") + \
                                  titleStr.count(" " + lower + ",") + titleStr.count(" " + lower + "'") + \
                                  titleStr.count(" " + lower + "/") + titleStr.count("/" + lower + " ") + \
                                  titleStr.count(" " + lower + ":") + titleStr.count("-" + lower + " ") + \
                                  titleStr.count("(" + lower + ")") + titleStr.count("\"" + lower + "\""))
                    if countTitle != 0:
                        results.append(aliases[0])
                        count[alias_list.index(aliases)] += countTitle
                        print("Found in title (lowercase): " + aliases[0] + " " + cur)
                        break

    # ABSTRACT
    abstractStr = driver.find_element_by_id("abstract").text

    if not abstractStr:
        abstractStr = driver.find_element_by_tag_name("patent-text").text
    # print(abstractStr)

    ## aliases - list of aliases for current gene
    ## cur - the current alias that is being looked for in the text
    for aliases in alias_list:
        for cur in aliases:
            # y=str(y).lower()
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in abstractStr and str(cur).lower() not in common_words:
                    countAbstract = 3 * (
                                abstractStr.count(" " + str(cur) + " ") + abstractStr.count(" " + str(cur) + ".") + \
                                abstractStr.count(" " + str(cur) + ",") + abstractStr.count(" " + str(cur) + "'") + \
                                abstractStr.count(" " + str(cur) + "/") + abstractStr.count("/" + str(cur) + " ") + \
                                abstractStr.count(" " + str(cur) + ":") + abstractStr.count("-" + str(cur) + " ") + \
                                abstractStr.count("(" + str(cur) + ")") + abstractStr.count("\"" + str(cur) + "\""))
                    if countAbstract != 0:
                        count[alias_list.index(aliases)] += countAbstract
                        print("Found in abstract: " + aliases[0] + " " + cur)
                    # print(str(temp) + " gene: "+ str(y))
                elif len(str(cur)) > 3 and str(cur).lower() in abstractStr and str(cur).lower() not in common_words:
                    lower = str(cur).lower()
                    countAbstract = 3 * (abstractStr.count(" " + lower + " ") + abstractStr.count(" " + lower + ".") + \
                                         abstractStr.count(" " + lower + ",") + abstractStr.count(" " + lower + "'") + \
                                         abstractStr.count(" " + lower + "/") + abstractStr.count("/" + lower + " ") + \
                                         abstractStr.count(" " + lower + ":") + abstractStr.count("-" + lower + " ") + \
                                         abstractStr.count("(" + lower + ")") + abstractStr.count("\"" + lower + "\""))
                    if countAbstract != 0:
                        count[alias_list.index(aliases)] += countAbstract
                        print("Found in abstract (lowercase): " + aliases[0] + " " + cur)

    # CLAIMS
    claimList = []

    claims = driver.find_elements_by_class_name("claim-text")
    count_claims = 0
    for x in claims:
        if count_claims >= num_claims:
            break
        claimList.append(x.text + "\n")
        count_claims += 1

    # print(claimList)
    claimStr = ""
    for x in claimList:
        claimStr += x

    # print(claimStr)
    for aliases in alias_list:
        for cur in aliases:
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in claimStr and str(cur).lower() not in common_words:
                    countClaim = (claimStr.count(" " + str(cur) + " ") + claimStr.count(" " + str(cur) + ".") + \
                                  claimStr.count(" " + str(cur) + ",") + claimStr.count(" " + str(cur) + "'") + \
                                  claimStr.count(" " + str(cur) + "/") + claimStr.count("/" + str(cur) + " ") + \
                                  claimStr.count(" " + str(cur) + ":") + claimStr.count("-" + str(cur) + " ") + \
                                  claimStr.count("(" + str(cur) + ")") + claimStr.count("\"" + str(cur) + "\""))
                    if countClaim != 0:
                        count[alias_list.index(aliases)] += countClaim
                        print("Found in claim: " + aliases[0] + " " + cur)
                elif len(str(cur)) > 3 and str(cur).lower() in claimStr and str(cur).lower() not in common_words:
                    lower = str(cur).lower()
                    countClaim = (claimStr.count(" " + lower + " ") + claimStr.count(" " + lower + ".") + \
                                  claimStr.count(" " + lower + ",") + claimStr.count(" " + lower + "'") + \
                                  claimStr.count(" " + lower + "/") + claimStr.count("/" + lower + " ") + \
                                  claimStr.count(" " + lower + ":") + claimStr.count("-" + lower + " ") + \
                                  claimStr.count("(" + lower + ")") + claimStr.count("\"" + lower + "\""))
                    if countClaim != 0:
                        count[alias_list.index(aliases)] += countClaim
                        print("Found in claim (lowercase): " + aliases[0] + " " + cur)

    # DESCRIPTION
    description = driver.find_element_by_id("descriptionText")
    descriptionStrInit = description.text
    desList = descriptionStrInit.split()[:1000]
    descriptionStr = ' '.join(map(str, desList))
    # print(descriptionStr)
    for aliases in alias_list:
        for cur in aliases:
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in descriptionStr and str(cur).lower() not in common_words:
                    countDescription = (descriptionStr.count(" " + str(cur) + " ") + descriptionStr.count(
                        " " + str(cur) + ".") + \
                                        descriptionStr.count(" " + str(cur) + ",") + descriptionStr.count(
                                " " + str(cur) + "'") + \
                                        descriptionStr.count(" " + str(cur) + "/") + descriptionStr.count(
                                "/" + str(cur) + " ") + \
                                        descriptionStr.count(" " + str(cur) + ":") + descriptionStr.count(
                                "-" + str(cur) + " ") + \
                                        descriptionStr.count("(" + str(cur) + ")") + descriptionStr.count(
                                "\"" + str(cur) + "\""))
                    if countDescription != 0:
                        count[alias_list.index(aliases)] += countDescription
                        print("Found in description: " + aliases[0] + " " + cur)
                elif len(str(cur)) > 3 and str(cur).lower() in descriptionStr and str(cur).lower() not in common_words:
                    lower = str(cur).lower()
                    countDescription = (
                                descriptionStr.count(" " + lower + " ") + descriptionStr.count(" " + lower + ".") + \
                                descriptionStr.count(" " + lower + ",") + descriptionStr.count(" " + lower + "'") + \
                                descriptionStr.count(" " + lower + "/") + descriptionStr.count("/" + lower + " ") + \
                                descriptionStr.count(" " + lower + ":") + descriptionStr.count("-" + lower + " ") + \
                                descriptionStr.count("(" + lower + ")") + descriptionStr.count("\"" + lower + "\""))
                    if countDescription != 0:
                        count[alias_list.index(aliases)] += countDescription
                        print("Found in description (lowercase): " + aliases[0] + " " + cur)

    sort = sorted(zip(count, genes), reverse=True)
    count = 0
    r = []
    print_stuff = []
    for x in sort:
        if count >= 3 or x[0] == 0:
            break
        elif x[1] not in results:
            r.append(x)
            print_stuff.append(x)
            count += 1
        elif x[1] in results:
            print_stuff.append(x)

    # print("r:")
    # for x in r:
    #    print(x)

    for x in r:
        if x[0] >= target_frequency:
            results.append(x[1])
        elif x[0] > 0 and len(results) < 3:
            results.append(x[1])
        elif x[0] > 0 and len(results) >= 3:
            results.append(x[1])
            break

    print(print_stuff)

    return results


def parse_only_genes(driver, genes, target_frequency, num_claims):
    genes = list(genes)
    if target_frequency == 0:
        target_frequency = 1
    results = []
    count = [0] * len(genes)

    common_words = ['for', 'can', 'not', 'cell', 'large', 'has', 'light', 'the', 'be', 'to', 'of', \
                    'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', \
                    'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', \
                    'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', \
                    'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', \
                    'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', \
                    'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', \
                    'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', \
                    'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', \
                    'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', \
                    'because', 'any', 'these', 'give', 'day', 'most', 'us']

    # TITLE
    # titleStr = driver.find_element_by_id("title").text
    titleStr = driver.title.split(" - ")[1].strip()

    # print(titleStr)
    for cur in genes:
        if len(str(cur)) >= 3:
            # print("entered")
            if str(cur) in titleStr:
                countTitle = (titleStr.count(" " + str(cur) + " ") + titleStr.count(" " + str(cur) + ".") + \
                              titleStr.count(" " + str(cur) + ",") + titleStr.count(" " + str(cur) + "'") + \
                              titleStr.count(" " + str(cur) + "/") + titleStr.count("/" + str(cur) + " ") + \
                              titleStr.count(" " + str(cur) + ":") + titleStr.count("-" + str(cur) + " "))
                if countTitle != 0:
                    results.append(cur)
                    count[genes.index(cur)] += countTitle
                    print("Found in title: " + cur)
                    break
                ## MAYBE ADD LENGTH RESTRICTION, len(str(cur))>5 and str(cur).lower() in titleStr
            elif str(cur).lower() in titleStr and str(cur).lower() not in common_words:
                lower = str(cur).lower()
                countTitle = (titleStr.count(" " + lower + " ") + titleStr.count(" " + lower + ".") + \
                              titleStr.count(" " + lower + ",") + titleStr.count(" " + lower + "'") + \
                              titleStr.count(" " + lower + "/") + titleStr.count("/" + lower + " ") + \
                              titleStr.count(" " + lower + ":") + titleStr.count("-" + lower + " "))
                if countTitle != 0:
                    results.append(cur)
                    count[genes.index(cur)] += countTitle
                    print("Found in title (lowercase): " + cur)
                    break

    # ABSTRACT
    abstractStr = driver.find_element_by_id("abstract").text

    if not abstractStr:
        abstractStr = driver.find_element_by_tag_name("patent-text").text
    # print(abstractStr)

    ## cur - the current gene that is being looked for in the text
    for cur in genes:
        # y=str(y).lower()
        if len(str(cur)) >= 3:
            # print("entered")
            if str(cur) in abstractStr:
                countAbstract = 3 * (abstractStr.count(" " + str(cur) + " ") + abstractStr.count(" " + str(cur) + ".") + \
                                     abstractStr.count(" " + str(cur) + ",") + abstractStr.count(" " + str(cur) + "'") + \
                                     abstractStr.count(" " + str(cur) + "/") + abstractStr.count("/" + str(cur) + " ") + \
                                     abstractStr.count(" " + str(cur) + ":") + abstractStr.count("-" + str(cur) + " "))
                if countAbstract != 0:
                    count[genes.index(cur)] += countAbstract
                    #print("Found in abstract: " + cur)
                # print(str(temp) + " gene: "+ str(y))
            elif str(cur).lower() in abstractStr and str(cur).lower() not in common_words:
                lower = str(cur).lower()
                countAbstract = 3 * (abstractStr.count(" " + lower + " ") + abstractStr.count(" " + lower + ".") + \
                                     abstractStr.count(" " + lower + ",") + abstractStr.count(" " + lower + "'") + \
                                     abstractStr.count(" " + lower + "/") + abstractStr.count("/" + lower + " ") + \
                                     abstractStr.count(" " + lower + ":") + abstractStr.count("-" + lower + " "))
                if countAbstract != 0:
                    count[genes.index(cur)] += countAbstract
                    #print("Found in abstract (lowercase): " + cur)

    # CLAIMS
    claimList = []

    claims = driver.find_elements_by_class_name("claim-text")
    count_claims = 0
    for x in claims:
        if count_claims >= num_claims:
            break
        claimList.append(x.text + "\n")
        count_claims += 1

    # print(claimList)
    claimStr = ""
    for x in claimList:
        claimStr += x

    # print(claimStr)
    for cur in genes:
        if len(str(cur)) >= 3:
            # print("entered")
            if str(cur) in claimStr:
                countClaim = claimStr.count(" " + str(cur) + " ") + claimStr.count(" " + str(cur) + ".") + \
                             claimStr.count(" " + str(cur) + ",") + claimStr.count(" " + str(cur) + "'") + \
                             claimStr.count(" " + str(cur) + "/") + claimStr.count("/" + str(cur) + " ") + \
                             claimStr.count(" " + str(cur) + ":") + claimStr.count("-" + str(cur) + " ")
                if countClaim != 0:
                    count[genes.index(cur)] += countClaim
                    #print("Found in claim: " + cur)
            elif str(cur).lower() in claimStr and str(cur).lower() not in common_words:
                lower = str(cur).lower()
                countClaim = claimStr.count(" " + lower + " ") + claimStr.count(" " + lower + ".") + \
                             claimStr.count(" " + lower + ",") + claimStr.count(" " + lower + "'") + \
                             claimStr.count(" " + lower + "/") + claimStr.count("/" + lower + " ") + \
                             claimStr.count(" " + lower + ":") + claimStr.count("-" + lower + " ")
                if countClaim != 0:
                    count[genes.index(cur)] += countClaim
                    #print("Found in claim (lowercase): " + cur)

    sort = sorted(zip(count, genes), reverse=True)
    count = 0
    r = []
    print_stuff = []
    for x in sort:
        if count >= 3:
            break
        elif x[1] not in results:
            r.append(x)
            print_stuff.append(x)
            count += 1
        elif x[1] in results:
            print_stuff.append(x)

    for x in r:
        if int(x[0]) >= target_frequency:
            #print(x[1] + " appended")
            results.append(x[1])
        elif int(x[0] > 0) and len(results) == 0:
            results.append(x[1])
            break

    #print(print_stuff)
   # print(results)

    return results