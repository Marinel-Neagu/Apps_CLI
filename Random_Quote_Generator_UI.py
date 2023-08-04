import random

quotes = '''“Act without expectation.” ~ Lao Tzu
“All know the way, but few actually walk it.” ~ Bodhidharma
“Don’t let yesterday take up too much of today.” ~ Will Rogers
“Every man dies. Not every man lives.” ~ William Wallace
“Everything has beauty, but not everyone sees it.” ~ Confucius
“I live by letting things happen.” ~ Dogen
“If things go wrong, don’t go with them.” ~ Roger Babson
“If you know the enemy and know yourself, you need not fear the result of a hundred battles.” – Sun Tzu
“If you realize you have enough, you are truly rich.” ~ Lao Tzu
“If you’re going through hell, keep going.” ~ Winston Churchill
“Learn to be comfortable in adversity but most importantly, learn to be comfortable when you’re bored.” – Maxime Lagacé
“Life shrinks or expands in proportion to one’s courage.” ~ Anais Nin
“Love is the absence of judgment.” ~ Dalai Lama
“Mind is like a mad monkey.” ~  Sathya Sai Baba
“Nature is full of chaos and conflict. Don’t resist these things. Invite them in.” – Charlie Ambler
“Nothing ever goes away until it has taught us what we need to know.” – Pema Chödrön
“Rest and be kind, you don’t have to prove anything.” – Jack Kerouac
“The real meditation is how you live your life.” ~ Jon Kabat-Zinn
“There is no mistake in nature.” ~ Byron Katie
“To seek is to suffer. To seek nothing is bliss.” ~ Bodhidharma
“Treat every moment as your last. It is not preparation for something else.” – Shunryu Suzuki
“We need much less than we think we need.” ~ Maya Angelou
“When you realize nothing is lacking, the whole world belongs to you.” – Lao Tzu
“Wherever you are, it’s the place you need to be.” – Maxime Lagacé
"Smile, breathe and go slowly." ~ Thich Nhat Hahn
“Life is a balance of holding on and letting go.” ~ Rumi
“The most important point is to accept yourself and stand on your two feet.” ~ Shunryu Suzuki
“Treat every moment as your last. It is not preparation for something else.” ~ Shunryu Suzuki
“Self-realization is effortless. What you are trying to find is what you already are.”- Ramesh Balsekar
“Forget the years, forget distinctions. Leap into the boundless and make it your home.” ~ Zhuangzi
“Wise men don’t judge – they seek to understand.” ~ Wei Wu Wei
“One must be deeply aware of the impermanence of the world.”~ Dogen
“Because we cannot accept the truth of transience, we suffer.” ~ Shunryu Suzuki'''.strip()

quote_dic = {}
quote_list = quotes.splitlines()
random_quotes = list()
for key, value in enumerate(quote_list, start=1):
	quote_dic[value] = key
print(quote_dic)
while True:
	enter = input('To generate a quote please press ENTER: ').strip()
	
	if enter == '':
		for k, v in quote_dic.items():
			list_word = quote_dic[k]
			
		random_word= random.choices(list_word)
		print(random_word)
	else:
		print("Please just press enter!")
