#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
NLP analysis functions


Author:
Nathan Danielsen
nathan.danielsen@irex.org
"""
import string


import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tag.stanford import NERTagger



class NLP(object):
	"""
	Using some basic NLP methods to analyze text


	Inspiration found here:
	https://github.com/ndanielsen/A-Smattering-of-NLP-in-Python

	"""
	def __init__(self, title, text):
		self.title = title
		self.text = text
		self.tokens = [word for sent in nltk.sent_tokenize(self.text) for word in nltk.word_tokenize(sent)]
		self.sentences = nltk.sent_tokenize(self.text)
	
	# @staticmethod
	# def from_txt(txt, title="", text=""):
	# 	"""Constructs a NLP class object from a text file with line[0] as title and following as text """	
	# 	text = []
	# 	with open(txt, 'r') as f:
	# 		for line in f.readlines():
	# 			text.append(line)
	# 	title, body = text[0], text[1:]
		
	# 	return NLP(title, body)



	def count(self):
		token_dict = {}
		for token in sorted(set(self.tokens))[:30]:
    		 token_dict[token] = str(self.tokens.count(token))
		return token_dict


	def stemmer(self):
		""" 
		Takes a list tokens and stems them into a list.
		Stemming is the process of reducing a word to its base/stem/root form. 
		"""

		stemmer = SnowballStemmer("english")
		stemmed_tokens = [stemmer.stem(t) for t in self.tokens]
		
		for token in sorted(stemmed_tokens):
			print token + ' [' + str(stemmed_tokens.count(token)) + ']'


	def lemmatizer(self):
		lemmatizer = nltk.WordNetLemmatizer()
		temp_sent = "Several women told me I have lying eyes."
		stemmer = SnowballStemmer("english")
		stemmed_tokens = [stemmer.stem(t) for t in self.tokens]

		#print [stemmer.stem(t) for t in nltk.word_tokenize(temp_sent)]
		#print [lemmatizer.lemmatize(t) for t in nltk.word_tokenize(temp_sent)]

		# fdist = nltk.FreqDist(stemmed_tokens)

		# for item in fdist.items()[:25]:
		# 	print item

		stemmed_tokens_no_stop = [stemmer.stem(t) for t in stemmed_tokens if t not in nltk.corpus.stopwords.words('english') ]

		fdist2 = nltk.FreqDist(stemmed_tokens_no_stop)

		for item in fdist2.items()[:25]:
			print item



	def entities(self):
		"""Need to fix loop with hasattr  """
		pass

		# def extract_entities(text):
		# 	entities = []
		# 	for sentence in nltk.sent_tokenize(text):
		# 		chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)))
		# 		#print chunks
		# 		print [chunk for chunk in chunks if hasattr(chunk, 'node')]
		# 	return entities

		# for entity in extract_entities(self.text):
		# 	print '[' + entity.node + '] ' + ' '.join(c[0] for c in entity.leaves())	


	def NER(self):
		"""
		Stanford NER in action, returns a dict of Named Entities by type
		

		I need to clean up the dictionary output and organize by NER
		"""
		NER = {}

				
		st = NERTagger('/home/nathan/nltk_data/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
			'/home/nathan/nltk_data/stanford-ner/stanford-ner.jar', 'utf-8')

		

		body = self.text.strip('\n')
		body = body.split()
		entityName = ""
		entityType = ""

		for sentence in self.sentences:	
			print "Processing"
			for word in st.tag(sentence.split()): #loop through text
				
				if word[1] != "O":

					if word[:-1] == ",": #prevents lists of NER from being clumped together
						continue
					else:	
						entityName += word[0] +" "
						entityType = word[1]

				else: 
					NER[entityName] = [entityType]	
					entityName = ""
				



		return NER





if __name__ == '__main__':
	# title = "This is a title"

	# text = "facilisis lorem tristique aliquet. Phasellus fermentum convallis"

	# mrtesty = NLP(title, text)
	
	# assert len(mrtesty.sentences) == 2

	# assert mrtesty.count() == {'tristique': '1', 'Phasellus': '1', 'lorem': '1', 'convallis': '1', '.': '1', 'facilisis': '1', 'aliquet': '1', 'fermentum': '1'}

	nytitle = "Fear Envelops Russia After Killing of Putin Critic"
	nyurl = "http://www.nytimes.com/2015/03/01/world/europe/russian-authorities-say-fellow-opposition-members-may-have-killed-boris-nemtsov.html"
	
	nytext = u""" MOSCOW  About two weeks before he was shot and killed in the highest-profile political assassination in
				Russia in a decade, Boris Y. Nemtsov met with an old friend to discuss his latest research into what he said
				was dissembling and misdeeds in the Kremlin, Washington. He was, as always, pugilistic and excited, saying he wanted to publish the research in a pamphlet to be
				called “Putin and the War,” about President Vladimir V. Putin and Russian involvement in the Ukraine
				conflict, recalled Yevgenia Albats, the editor of New Times magazine. Both knew the stakes.
				Mr. Nemtsov, a former deputy prime minister, knew his work was dangerous but tried to convince her
				that, as a former high official in the Kremlin, he enjoyed immunity, Ms. Albats said.
				“He was afraid of being killed,” Ms. Albats said. “And he was trying to convince himself, and me, they
				wouldn’t touch him because he was a member of the Russian government, a vice premier, and they wouldn’t
				want to create a precedent. Because as he said, one time the power will change hands in Russia again, and
				those who served Putin wouldn’t want to create this precedent.” 				On Saturday, it was still not clear who was responsible for killing Mr. Nemstov. Some critics of the
				Kremlin accused the security services of responsibility, while others floated the idea of rogue Russian
				nationalists on the loose in Moscow.

								The authorities said they were investigating several theories about the crime, some immediately scorned
				as improbable, including the possibility that fellow members of the opposition had killed Mr. Nemtsov to
				create a martyr. Mr. Putin, for his part, vowed in a letter to Mr. Nemstov’s mother to bring to justice those
				responsible.
				As supporters of Mr. Nemtsov laid flowers on the sidewalk where he was shot and killed late Friday, a
				shiver of fear moved through the political opposition in Moscow.
				The worry was that the killing would become a pivot point toward a revival of lethal violence among the
				leadership elite in Moscow and an intensified climate of fear in Russian domestic politics.
				“Another terrible page has been turned in our history,” Mikhail B. Khodorkovsky, the exiled former
				political prisoner, wrote in a statement about the killing.
				“For more than a year now, the television screens have been flooded with pure hate for us,” he wrote of
				the opposition to Mr. Putin. “And now everyone from the blogger at his apartment desk to President Putin,
				himself, is searching for enemies, accusing one another of provocation. What is wrong with us?”
				Vladimir Milov, a former deputy minister of energy, and co-author with Mr. Nemtsov of pamphlets
				alleging corruption in Mr. Putin’s government, said he was concerned that the state could now target former
				officials like Mr. Nemtsov — or like him — deemed disloyal.
				This comes as analysts of Russian politics say the Kremlin could be worried about, and intent on
				discouraging, further defections to the opposition, given reported high-level schisms between hard-liners and
				liberals over military and economic policy. The government is already under strain from Russia’s
				unacknowledged involvement in the war in Ukraine and runaway inflation in an economic crisis.
				Mr. Milov posted an online statement saying, “There is ever less doubt that the state is behind the
				murder of Boris Nemtsov,” and that the intention was to revive a culture of fear in Moscow. “The motive was
				to sow fear,” he wrote.

				Irina Khakamada, a former member of Parliament, suggested in an interview with Snob magazine that
				splinter groups in the security service intent on retaining Soviet practices, or “radical frozen ones, who think
				anything is allowed,” could be to blame.
				Russian authorities said on Saturday that one line of investigation would be to examine whether Mr.
				Nemtsov, a 55-year-old former first deputy prime minister and longtime leader of the opposition, had
				become a “sacrificial victim” to rally support for opponents of the government, the Investigative Committee
				of the Prosecutor General’s Office said in a statement.
				The statement, the fullest official response so far to Mr. Nemtsov’s killing, said the police were pursing
				half a dozen leads in the case, the highest-profile assassination in Russia during the tenure of Mr. Putin.
				The committee also cited the possibility that Islamic extremists had killed Mr. Nemtsov over his position
				on the Charlie Hebdo shootings in Paris, saying that security forces had been aware of threats against him
				from Islamist militants. The committee also said that “radical personalities” on one or another side of the
				Ukrainian conflict might may have been responsible. The statement said the police were also considering
				possible business or personal disputes as motives.
				“The investigation is considering several versions,” the statements said. The first it listed was: “a murder
				as a provocation to destabilize the political situation in the country, where the figure of Nemtsov could have
				become a sort of sacrificial victim for those who stop at nothing to achieve their political goals.”
				This explanation echoed and elaborated on a statement posted overnight on the Kremlin website, which
				also characterized the murder as a “provocation.”
				“The president noted that this cruel murder has all the signs of a contract killing and carries an
				exclusively provocative character,” the Kremlin statement said. “Vladimir Putin expressed his deep
				condolences to the relatives and loved ones of Boris Nemtsov, who died tragically.”
				Mr. Putin, in a message to Mr. Nemtsov’s mother released by the Kremlin, said, “Everything will be done

				so that the organizers and perpetrators of a vile and cynical murder get the punishment they deserve.”
				Life News, a television station with close ties to the Russian security services, quoted a source as
				suggesting that Mr. Nemtsov was murdered in revenge for having caused a woman to have an abortion.
				Law enforcement critics say that such theories can serve as smoke screen in high-profile cases, but that
				they also reflect a Soviet-era policy for managing the security services, under which investigators are credited
				with making progress when a version of events is ruled out — giving the police an incentive to begin with a
				wide array of improbable assumptions.
				After laying flowers on a floral mound already chest high and kneeling in respect before the blooms
				festooning the sidewalk on a rainy, glum midafternoon, Anatoly Chubais, a co-founder with Mr. Nemtsov of
				the Union of Right Forces political party, scorned the investigators’ claim.
				“Today, we had a statement that the liberal opposition organized the killing,” he said. “Before this, they
				wrote that the liberals created the economic crisis. In this country, we have created demand for anger and
				hate.”
				Ilya Yashin, a political ally of Mr. Nemtsov’s, drew attention again to the pamphlet Mr. Nemtsov was
				preparing on Russian military aid to pro-Russian rebels in Ukraine. Speaking on the Echo of Moscow radio
				station, he said Mr. Nemtsov had “some materials that directly proved” the participation of the Russian army
				in the Donbas war in Ukraine.
				Mr. Yashin said he knew no details, or what had become of those materials.
				Ms. Albats, who had discussed with Mr. Nemtsov his unfinished exposé, said of this state of affairs in
				domestic Russian politics, “We are at war now.”
				“Those who are believers in democracy, those who for some reason, back in the late 1980s, got on board
				this train, and had all these hopes and aspirations,” she said, “they are at war today.”
								"""

	nytest = NLP(nytitle, nytext)

	print nytest.title

	print nytest.NER()

	# mytitle = "Nathan Danielsen"

	# mytext = "My name is Charlie and I work for Altamira in Tysons Corner."

	# mytest = NLP(mytitle, mytext)

	# print mytest.title
	# print mytest.NERTagger()

	"""
	Classmethod Constructor for importing text files needs work
	"""

	# ftester = NLP.from_txt('nytimes.txt')

	# print (ftester.title)

	# print (ftester.text)