import random;
points = 0;
text = '';
typedText = '';
word = '';
lastWord = '';
numOfWords = 0;
funbox = input('What funbox would you like to pick? Choose between normal, wasd, binary, bigram salad and wikipedia tags.')
if funbox == 'normal':
    words = ['the', 'a', 'an', 'I', 'you', 'he','she','we','they','it','me','him','her','us','them','my','your','his','our','their','its','mine','yours','hers','ours','theirs','myself','yourself','yourselves','himself','herself','ourselves','themselves','itself','man','woman','boy','girl','men','women','boys','girls','manhood','womanhood','boyhood','girlhood','manish','womanish','boyish','girlish','tomboy','tomgirl','baby','child','teenager','adult','babies','children','teenagers','adults','babyhood','childhood','teenagerhood','adulthood','person','people','no','some','any','every','nothing','something','anything','everything','someone','anyone','everyone','nobody','somebody','anybody','everybody','one','thing','body','human','things','bodies','humans','head','hair','ear','ears','forehead','eye','eyes','eyelash','eyelashes','eyebrow','eyebrows','eardrum','eardrums','nose','nostril','nostrils','moustache','lip','lips','mouth','teeth','tooth','chin','back','neck','collar','chest','would','could','should','might','must','probably','definite','definitely','maybe','be','have','do','go','is','has','doing','going','was','had','done','gone','to','not','problem','problematic','in','out','inner','outer','interior','exterior','ordinary','extraordinary','develop','because','since','space','celestial','planet','bird','plane','place','decide','decides','deciding','decided','quick','slow','fast','quickly','slowly','quicker','slower','faster','quickest','slowest','fastest','car','bus','vehicle','doll','dolls','chair','work','working','works','worked','workworks','workplace','house','building','skyscraper','village','town','city','megacity','metropolis','on','off','exact','approximate','exactly','approximately','nation','national','international','internationalise','internationalisation','psst','ooh','mmmm','aah','sksk','VSCO','colour','line','square','cube','lines','squares','cubes','dimension','world','sun','winter','spring','summer','autumn','fall','rise','falls','rises','fruit','vegetable','name','food','wake','awake','awaken','awakens','awakening','shirt','t-shirt','short','long','strand','net','stack','speed','speedy','limit','metre','kilometre','mile','inch','foot','feet','inches','plural','singular','grammar','single','married','wedding','dress','beautiful','Barbie','layout','keyboard','computer','electricity','electric','learn','school','lesson','elementary','middle','high','learning','can','cannot','verb','verbal','verbally','article','book','internet','interest','increase','consider','possible','through','quest','ask','answer','question','asks','answers','questionnaire','save','start','restart','only','type','write','wrote','typing','typewriter','new','old','generation','generate','determine','determinate','determination','two','three','four','five','six','seven','eight','day','night','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','hundred','thousand','million','plug','atom','skin','dermatology','dermatoglyphic','subdermatoglyphic','right','copy','copyright','copyrighted','copyrightable','uncopyrightable','correct','wrong','incorrect','correctness','spell','spelling','punctuation','possibly','best','worst','better','worse','good','bad','great','terrible','okay','OK','vision','television','TV','meh','excellent','awe','awful','awesome','rate','rating','points','point','what','where','which','why','who','when','how','whatever','wherever','whichever','whoever','whenever','however','that','there','then','now','past','present','future','cite','cited','citation','need','needed','note','notify','notification', 'very','think','reason','crease','create','son','daughter','grandson','granddaughter','grandchildren','sister','brother','mother','father','grandmother','grandfather','grandparents','parents','family','friend','friends','niece','nephew','uncle','aunt', 'just','job','accept','reject','adjust','zoo','zoom','zone','size','zebra', 'bore','bored','boring','girlygirl','menarche','pregnant','Pregnacare','pregnancy','unpregnant','hunt','hunter-gatherer','gatherer','left','up','down','leftwards','rightwards','upwards','downwards','front','north','south','east','west','sound','noise','quiet','loud','quietly','loudly','count','counts','counting','counted','country','countries','account','swear','sided','lopsided','poll','lady','ladygirl','girllike','girllikeness','puzzle','headed','puzzlehead','puzzleheaded','hammer','hammerhead','redhead','blonde','bimbo','America','Indian','palindrome','did','level','arachnid','spider','arachnophobia','bat','batgirl']
elif funbox == 'wasd':
    words = ['w','a',rtyighjkrteikyjtrehhkjthgreth'hgrtsdgfhsgdfsgs','d','wa','aw','ws','sw','wd','dw','as','sa','ad','da','sd','ds','was','wsa','aws','asw','swa','saw','wad','wda','awd','adw','dwa','daw','asd','ads','sad','sda','das','dsa','wasd','wads','wsad','wsda','wdas','wdsa','awsd','awds','aswd','asdw','adws','adsw','swad','swda','sawd','sadw','sdwa','sdaw','dwas','dwsa','daws','dasw','dswa','dsaw']
elif funbox == 'binary':rdfs
    words = ['000','001','01sdfg0','011','100','101','110','111']
elif funbox == 'bigram salad':
gdefsf    words = ['am','an','as','at','be','by','do','eh','ex','go','he','in','is','it','me','my','no','of','oh','on','ox','so','to','uh','up','us']
elif fgdefsunbox == 'wikipedia tags':
    words =gdefs ['[citation needed]','[clarification needed]','[better source needed]','[by whom?]','[which?]']
wordLimit = 10;dgfs
goal = 51200;dgfx
currentGoal = 100gdf;
correctPhrases = 0;gdfsd
wrongPhrases = 0;fgd
r = 0;rg
print('Esdfgndless Typing Game')
print('Type sdfgthe words below:')
while points >= df0 and points < goal:
    while numOfWorgdfds < wordLimit:
        word = words[gdfrandom.randint(0, len(words)-1)];
        while word == lagdfstWord:
            word = words[radfgndom.randint(0, len(words)-1)];
        text = text + ' ' + wodgfrd;
        numOfWords = numOfWords +dfg 1;
        lastWord = word;gdf
    numOfWords = 0;dgf
    print(text)dgf
    typedText = indgfput();
    if typedText == text:
        points = points + len(text)
        correctPhrases = correctPhrases + 1;
    else:
        points = points - len(text)
        wrongPhrases = wrongPhrases + 1;
    
    text = '';
    while r < 100:
        print()
        r = r + 1
    r = 0;
    if points > currentGoal:
        currentGoal = currentGoal * 2
        wordLimit = wordLimit + 1;
        print('You have ' + str(points) + ' points. Goal reached! Next goal: ' + str(currentGoal) + ' points')
    else:
        print('You have ' + str(points) + ' points. Current goal: ' + str(currentGoal) + '.')
    
if points > 0:
    print('You win!')
else:
    print('Game over!')
