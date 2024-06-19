from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)


# 
# Text to be spoken
title1 = "Soccer Star's Surprise: Teamwork Trumps Solo Glory"
filename1 = "soccer_story2"
text1 = '''In the bustling town of Willowbrook, there lived a young soccer prodigy named Jake. Jake was known far and wide for his remarkable skills on the soccer field. His lightning-fast dribbles and powerful shots had led his team, the Willowbrook Warriors, to numerous victories. But there was one thing Jake loved more than winning: basking in the glory of his own success.
One sunny afternoon, the Willowbrook Warriors found themselves facing their toughest opponents yet: the formidable Falcons. The match was crucial, with the winner advancing to the regional championship. Excitement buzzed through the air as the two teams took to the field.
From the very start, Jake was determined to be the hero of the match. He sprinted across the field, leaving defenders in his wake, and took shot after shot at the Falcons' goal. But try as he might, Jake couldn't seem to find the back of the net. Frustration began to gnaw at him as the first half ended in a stalemate.
As the second half began, Jake's frustration turned into desperation. He decided to take matters into his own hands, dribbling past the entire Falcons' defense in a daring solo run. With the goal in sight, Jake wound up for a powerful shot, only to be tackled at the last moment by the Falcons' goalkeeper.
As Jake lay sprawled on the ground, defeated and deflated, he heard a voice from behind him. It was his teammate, Emily, offering him a hand up. "We need to work together, Jake," she said with a determined glint in her eye.
Jake looked around and realized that while he had been focused on his own glory, his teammates had been tirelessly supporting each other, passing the ball with precision and executing clever plays. With newfound determination, Jake joined his teammates, and together they launched attack after attack on the Falcons' goal.
In the final minutes of the match, a perfectly executed corner kick found its way to Jake's feet. Instead of going for glory, Jake made a split-second decision and passed the ball to Emily, who was positioned perfectly to score. With a swift kick, Emily sent the ball soaring into the net, securing victory for the Willowbrook Warriors.
As the final whistle blew, the crowd erupted into cheers. Jake looked around at his teammates, realizing that true victory didn't come from individual glory, but from working together as a team. With a smile on his face, Jake joined his teammates in celebration, knowing that their teamwork had triumphed over solo glory.
From that day forward, Jake approached every match with a newfound appreciation for teamwork. And while he still dazzled the crowd with his skills, he knew that the real magic happened when he played alongside his teammates, united in their pursuit of victory.
'''

title2 = "Home Run Hilarity: Bases Loaded with Laughter"
filename2 = "baseball_story"
text2 = '''
In the heart of a small town nestled between rolling hills and fields of golden wheat, there stood a quaint baseball field. The field wasn't the most magnificent, nor were the players the most skilled, but what they lacked in talent, they made up for in spirit and camaraderie.

One sunny Saturday afternoon, the town's annual baseball tournament was in full swing. The teams, composed of neighbors, friends, and families, competed with zest and enthusiasm. Among them was the underdog team, the "Wildcats," known for their wild antics and love for the game.

In the final inning of the championship game, the Wildcats found themselves in a tight spot. Bases were loaded, and they were trailing by three runs. Their star hitter, Jake, stepped up to the plate, a mix of determination and nervousness written across his face.

The pitcher wound up, sending the ball hurtling towards Jake. With a mighty swing, Jake connected, sending the ball soaring into the air. The crowd held its breath as the ball arched towardBut instead of landing in the waiting gloves of the outfielders, the ball took a wild bounce, ricocheting off a passing bird and veering off course. The outfielders stumbled over each other, trying in vain to catch the unpredictable ball.

Meanwhile, the runners on base dashed around the diamond, their legs pumping with determination. Amidst the chaos, the Wildcats' coach could barely contain his laughter, his belly shaking with mirth.

As Jake rounded third base, he couldn't help but chuckle at the absurdity of the situation. By the time the ball was finally retrieved, all three runners had crossed home plate, tying the game.

The stadium erupted into cheers and applause, the spectators delighting in the unexpected turn of events. Even the opposing team couldn't help but join in the laughter, realizing that sometimes, in the game of baseball and in life, you have to expect the unexpected.

In the end, the Wildcats went on to win the championship, but the memory of that hilarious home run remained etched in the hearts of the townsfolk for years to come.

And as the sun dipped below the horizon, casting a warm glow over the field, the lesson was clear: life may throw you curveballs, but it's how you handle them that truly matters. With laughter, camaraderie, and a sprinkle of good-natured fun, even the most daunting challenges can turn into triumphant victories.
'''

title3 = "The Skateboard Showdown: Friendship Rolls Over Rivalry"
filename3 = "skateboard_story"
text3 = '''
    In the small town of Oakridge, skateboarding was more than a hobby; it was a way of life. The local skate park, known as "The Pit," was always buzzing with activity. Among the crowd were two standout skaters: Jake and Sam. Jake was known for his daring tricks and fearless attitude, while Sam was famous for his smooth style and precision.

    Despite their different approaches to skateboarding, Jake and Sam had always been friends. They grew up together, learned to skate together, and spent countless hours perfecting their skills side by side. However, their friendship was put to the test when a big skateboarding competition was announced, with a brand-new skateboard and a sponsorship deal as the grand prize.
    
    As the competition day approached, the tension between Jake and Sam grew. They both wanted to win, and their friendly rivalry began to turn sour. They stopped skating together and started practicing alone, each determined to outdo the other.
    
    On the day of the competition, The Pit was packed with spectators. Jake and Sam barely acknowledged each other as they warmed up. The atmosphere was electric, and everyone could feel the excitement in the air.
    
    The competition began, and both Jake and Sam performed incredibly well. Jake wowed the crowd with his high-flying tricks, while Sam impressed with his flawless execution. As the final round approached, it was clear that the competition was between the two friends.
    
    In the final round, Jake attempted a risky trick he had never tried before. He soared into the air, but miscalculated the landing and fell hard. The crowd gasped, and Jake lay on the ground, clutching his ankle in pain.
    
    Sam, who was up next, saw what happened. He looked at Jake, then at the judges, and made a decision. Instead of performing his final trick, Sam skated over to Jake and helped him up. The crowd was silent as Sam supported his friend and led him off the course.
    
    The judges conferred and made a surprising announcement. They declared Sam the winner, but not for his performance. Instead, they awarded him the prize for showing true sportsmanship and friendship.
    
    Jake and Sam left The Pit together, the rivalry forgotten. As they walked away, Jake looked at Sam and said, "Thanks, man. I guess winning isn't everything."
    
    Sam smiled and replied, "No, it's not. Friendship is."
    
    From that day on, Jake and Sam's bond was stronger than ever. They continued to skate together, not as rivals, but as best friends who knew that the greatest victories were the ones they shared.
'''

title4 = "The Volleyball Vendetta: Spiking Egos for Kindness"
filename4 = "volleyball_story"
text4 = '''
    In the sunny town of Maplewood, volleyball was more than just a sport; it was a passion that united the community. Every summer, the Maplewood Volleyball Tournament was the highlight of the season. Teams from all over the town gathered to compete, but this year, the excitement was marred by a growing tension between two rival teams: The Maplewood Eagles and The Riverstone Ravens.
    
    The Eagles, led by their captain, Sarah, were known for their unbeatable skills and unwavering teamwork. The Ravens, captained by the fierce and competitive Jenna, were equally talented but carried an air of arrogance that often rubbed people the wrong way.
    
    As the tournament progressed, the rivalry between Sarah and Jenna became the talk of the town. Their matches were intense, filled with powerful spikes, incredible saves, and thrilling rallies. However, the competition began to sour as Jenna's ego-driven taunts and boastful remarks escalated. Sarah, known for her sportsmanship, tried to ignore Jenna’s jibes, but her team was growing weary of the negativity.
    
    The tension peaked during the semi-finals, where the Eagles and Ravens faced off. The gym was packed with spectators, all eager to witness the clash. As the game progressed, the atmosphere grew more hostile. Every point scored by the Ravens was met with arrogant cheers, and every mistake by the Eagles was mocked by Jenna.
    
    During a crucial set, Sarah noticed that her teammates were losing their focus, frustrated by the constant taunting. She called for a timeout and gathered her team. "We need to remember why we play this game," she said, her voice calm but firm. "It's about having fun and showing respect, no matter what. Let’s show them what true sportsmanship looks like."
    
    The Eagles returned to the court with renewed determination. They played with grace and humility, their teamwork shining brighter than ever. Sarah led by example, offering words of encouragement and high-fives, even to her opponents. The crowd began to notice the stark contrast between the two teams.
    
    Despite their efforts, the Eagles lost the match by a narrow margin. Jenna’s team celebrated with their usual arrogance, but the crowd’s applause was noticeably lukewarm. Sarah and her teammates shook hands with the Ravens, their smiles genuine. "Good game," Sarah said to Jenna, her eyes meeting the rival captain's with sincerity.
    
    The next day, an article in the Maplewood Gazette highlighted the match, praising the Eagles for their sportsmanship and unity. It pointed out how their positive attitude had won the hearts of the spectators, even in defeat.
    
    Jenna, reading the article, felt a pang of regret. She realized that while her team had won the match, they had lost the respect of the community. Determined to change, she approached Sarah the following day. "I’ve been thinking a lot," Jenna admitted. "Your team showed what true sportsmanship is all about. I want to play like that."
    
    Sarah smiled, extending her hand. "It's never too late to change, Jenna. Let’s make next year’s tournament about respect and kindness.
    
    From that day on, the rivalry between the Eagles and Ravens transformed into a friendly competition. The following summer, the Maplewood Volleyball Tournament was more vibrant and spirited than ever, with teams playing not just for victory but for the love of the game and the bonds it forged.
    
    And so, in Maplewood, the tale of the Volleyball Vendetta became a cherished story, reminding everyone that true greatness in sports comes not just from skill, but from the kindness and respect shown both on and off the court.
'''

title5 = "Slam Dunk Dilemma: Fair Play Fouls Out"
filename5 = "basketball_story"
text5 = '''
In the small town of Brooksville, the annual basketball championship was the most anticipated event of the year. The town's high school team, the Brooksville Bears, was known for their teamwork and sportsmanship. This year, they were up against their biggest rivals, the Rivertown Raptors. The stakes were high, and the pressure was on.

Jake, the Bears' star player, was determined to win. He had been practicing day and night, perfecting his slam dunks and three-pointers. His best friend and teammate, Mark, admired Jake's dedication but was worried about his growing obsession with winning.

The day of the championship arrived, and the gymnasium was packed with cheering fans. The game started with both teams playing their hearts out. It was a close match, and tensions were high. Jake was on fire, scoring point after point, but the Raptors were keeping up.

With only a minute left on the clock, the score was tied. The Bears had possession of the ball, and Jake saw his chance. He dribbled past two defenders and went for a slam dunk. As he soared through the air, a Raptors player, Sam, tried to block him. There was a loud collision, and both players crashed to the floor.

The referee blew his whistle and called a foul on Sam. The Raptors' coach and fans erupted in protest, claiming it was a clean block. Jake got up, feeling a sharp pain in his ankle, but more than that, he felt a pang of guilt. He knew the block was clean, and Sam had played fair.

As Jake limped to the free-throw line, he glanced at Sam, who looked defeated. Jake took a deep breath and stepped back from the line. "Coach, I can't take these free throws," he called out. "It wasn't a foul. Sam played fair."

The gym fell silent. The referee, taken aback, conferred with the coaches and ultimately reversed the call. The game resumed with a jump ball, and the Raptors gained possession. With only seconds remaining, Sam made a spectacular three-pointer, winning the game for the Raptors.

The Brooksville Bears were disappointed, but they respected Jake's decision. After the game, Jake approached Sam and congratulated him. "That was an amazing shot," he said, shaking Sam's hand.

"Thanks, Jake," Sam replied. "It took a lot of guts to do what you did. You're a true sportsman.

The Bears' coach gathered the team in the locker room. "I'm proud of all of you," he said. "We may have lost the game, but Jake showed us what true sportsmanship is. Winning isn't everything. Playing fair and respecting the game is what really matters.

The team nodded in agreement, and Jake's actions became a defining moment for Brooksville High. From that day on, the town remembered the championship not for the loss, but for the lesson in integrity and fair play.

And so, the story of the "Slam Dunk Dilemma" became a cherished tale in Brooksville, reminding everyone that true victory lies in the spirit of the game, not just the final score.
'''

# Data For books
books = [
    {'id': 1, 'title': title1, 'storyText': text1, 'audio_file': filename1+'.mp3'},
    {'id': 2, 'title': title2, 'storyText': text2, 'audio_file': filename2+'.mp3'},
    {'id': 3, 'title': title3, 'storyText': text3, 'audio_file': filename3+'.mp3'},
    {'id': 4, 'title': title4, 'storyText': text4, 'audio_file': filename4+'.mp3'},
    {'id': 5, 'title': title5, 'storyText': text5, 'audio_file': filename5+'.mp3'}
]

@app.route('/')
def home():
    return render_template('/book_home.html', books=books)

@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return render_template('book.html', book=book) if book else "Book not found", 404

@app.route('/static/audio/<path:filename>')
def download_file(filename):
    return send_from_directory('static/audio', filename, as_attachment=True)    

if __name__ == '__main__':
    app.run(debug=True)