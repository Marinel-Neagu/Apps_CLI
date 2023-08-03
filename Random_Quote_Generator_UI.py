import random

quotes = '''

“Don’t let yesterday take up too much of today.” ~ Will Rogers
“If you’re going through hell, keep going.” ~ Winston Churchill
“Every man dies. Not every man lives.” ~ William Wallace
“Life shrinks or expands in proportion to one’s courage.” ~ Anais Nin
“We need much less than we think we need.” ~ Maya Angelou
“If things go wrong, don’t go with them.” ~ Roger Babson
“Everything has beauty, but not everyone sees it.” ~ Confucius
“When you realize nothing is lacking, the whole world belongs to you.” – Lao Tzu
“Rest and be kind, you don’t have to prove anything.” – Jack Kerouac
“Nothing ever goes away until it has taught us what we need to know.” – Pema Chödrön
“The mind of the beginner is empty, free of the habits of the expert, ready to accept, to doubt, and open to all the possibilities.” – Shunryu Suzuki
“Wherever you are, it’s the place you need to be.” – Maxime Lagacé
“Treat every moment as your last. It is not preparation for something else.” – Shunryu Suzuki
“Learn to be comfortable in adversity but most importantly, learn to be comfortable when you’re bored.” – Maxime Lagacé
“There are only two ways to live your life. One is as if nothing is a miracle. The other is as if everything is a miracle.” – Albert Einstein
“If you know the enemy and know yourself, you need not fear the result of a hundred battles.” – Sun Tzu
“Nature is full of chaos and conflict. Don’t resist these things. Invite them in.” – Charlie Ambler


'''.splitlines()

print(random.choices(quotes))

