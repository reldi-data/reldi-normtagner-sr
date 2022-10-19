COLUMNS = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS', 'FEATS', 'HEAD', 'DEPREL', 'DEPS', 'MISC',
           'RELDI:NE', 'RELDI:DP', 'RELDI:SRL', 'RELDI:MISC']

with open('reldi-normtagner-sr.conllup', 'w') as f:
    f.write('# global.columns = {}\n'.format(' '.join(COLUMNS)))

    for line in open('reldi-normtagner-sr.edited.conllu'):
        if line.startswith('#'):
            f.write(line)

        elif line.strip() == '':
            f.write('\n')

        else:
            tid, form, lemma, upos, xpos, feats, head, deprel, deps, misc = line.strip().split('\t')
            ner = '*'
            dp = '*'
            srl = '*'
            rmisc = {}

            if misc != '_':
                misc = dict([f.split('=', 1) for f in misc.split('|')])

                ner = misc.pop('NER', '*')
                dp = misc.pop('DP', '*')
                srl = misc.pop('SRL', '*')

                if 'Normalized' in misc:
                    misc['CorrectForm'] = misc.pop('Normalized')

                if ner != '*':
                    misc['NamedEntity'] = 'Yes'

                if 'ToDo' in misc:
                    rmisc['ToDo'] = misc.pop('ToDo')

                misc = '|'.join(['='.join(f) for f in misc.items()])

            rmisc = '|'.join(['='.join(f) for f in rmisc.items()]) or '_'

            f.write('\t'.join((tid, form, lemma, upos, xpos, feats, head, deprel, deps, misc, ner, dp, srl, rmisc)))
            f.write('\n')
