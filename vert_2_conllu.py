import sys
import re
attrs=re.compile(r'id="tid\.(.+?)" .+? type="tweet" std_tech="(.+?)" std_ling="(.+?)">')
type_re=re.compile(r'type="(.+?)"')
ner=None
out=open('reldi-normtagner-sr.conllu','w')
for line in open('reldi-normtagner-sr.vert'):
	if line.startswith('<text'):
		tweetid,t,l=attrs.search(line).groups()
		out.write("# newdoc id = "+tweetid+"\n")
		out.write("# T = "+t[-1]+'\n')
		out.write("# L = "+l[-1]+'\n')
		sid=0
		#print(tid,t,l)
	elif line.startswith('<s>'):
		sid+=1
		tid=0
		out.write('# sent_id = '+tweetid+'.'+str(sid)+'\n')
		sent=[]
	elif line.startswith('<name '):
		ner=type_re.search(line).group(1)
		first=True
	elif line.startswith('</name>'):
		ner=None
	elif line.startswith('<g/>'):
		sent[-1][-1].append('SpaceAfter=No')
	elif line.startswith('</s>'):
		text = ''
		for token in sent:
			text+=token[0]
			if not 'SpaceAfter=No' in token[-1]:
				text+=' '
		out.write('# text = '+text.strip()+'\n')
		tid=0
		for token in sent:
			tid+=1
			if ' ' in token[1]:
				tokens = token[-1][0][11:].split(' ')
				lemmas = token[1].split(' ')
				lemmas[0] = lemmas[0][:-2]
				upos = token[2].split(' ')
				msd = token[3].split(' ')
				upos_feats = token[4].split(' ')
				token[-1]=token[-1][1:]
				if len(token[-1])>0:
					out.write(str(tid)+'-'+str(tid+1)+'\t'+token[0]+'\t_'*7+'\t'+'|'.join(token[-1])+'\n')
				else:
					out.write(str(tid)+'-'+str(tid+1)+'\t'+token[0]+'\t_'*8+'\n')
				if upos[0]=='_':
					upos[0]={'Xa':'SYM','Xh':'SYM','Xe':'SYM','Xf':'X','X':'X','Xw':'SYM'}[msd[0]]
				if upos[1]=='_':
					upos[1]={'Xa':'SYM','Xh':'SYM','Xe':'SYM','Xf':'X','X':'X','Xw':'SYM'}[msd[1]]
				out.write(str(tid)+'\t'+tokens[0]+'\t'+lemmas[0]+'\t'+upos[0]+'\t'+msd[0]+'\t'+upos_feats[0]+'\t_\t_\t_\t_\n')
				out.write(str(tid+1)+'\t'+tokens[1]+'\t'+lemmas[1]+'\t'+upos[1]+'\t'+msd[1]+'\t'+upos_feats[1]+'\t_\t_\t_\t_\n')
				tid += 1
				continue
			if len(token[-1])>0:
				out.write(str(tid)+'\t'+'\t'.join(token[:5])+'\t_\t_\t_\t'+'|'.join(token[-1])+'\n')
			else:
				out.write(str(tid)+'\t'+'\t'.join(token[:5])+'\t_\t_\t_\t_\n')
		out.write('\n')
	elif '\t' in line:
		token, norm, lemma, msd, msd_feats, upos, upos_feats, normed=line.split('\t')
		if upos=='_':
			upos={'Xa':'SYM','Xh':'SYM','Xe':'SYM','Xf':'X','X':'X','Xw':'SYM'}[msd]
		sent.append([token,lemma[:-2],upos,msd,upos_feats,[]])
		if norm!=token:
			sent[-1][-1].append('Normalized='+norm)
		if ner!=None:
			if first:
				sent[-1][-1].append('NER=B-'+ner)
				first=False
			else:
				sent[-1][-1].append('NER=I-'+ner)

out.close()
