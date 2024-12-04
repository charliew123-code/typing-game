import random;
points = 0;
text = '';
typedText = '';
word = '';
lastWord = '';
numOfWords = 0;
funbox = input('What funbox would you like to pick? Choose between normal, wasd, binary, bigram salad, weakspot, nospace, wikipedia and wikipedia tags.')
if funbox == 'normal' or funbox == 'nospace':
    words = ['the', 'a', 'an', 'I', 'you', 'he','she','we','they','it','me','him','her','us','them','my','your','his','our','their','its','mine','yours','hers','ours','theirs','myself','yourself','yourselves','himself','herself','ourselves','themselves','itself','man','woman','boy','girl','men','women','boys','girls','manhood','womanhood','boyhood','girlhood','manish','womanish','boyish','girlish','tomboy','tomgirl','baby','child','teenager','adult','babies','children','teenagers','adults','babyhood','childhood','teenagerhood','adulthood','person','people','no','some','any','every','nothing','something','anything','everything','someone','anyone','everyone','nobody','somebody','anybody','everybody','one','thing','body','human','things','bodies','humans','head','hair','ear','ears','forehead','eye','eyes','eyelash','eyelashes','eyebrow','eyebrows','eardrum','eardrums','nose','nostril','nostrils','moustache','lip','lips','mouth','teeth','tooth','chin','back','neck','collar','chest','would','could','should','might','must','probably','definite','definitely','maybe','be','have','do','go','is','has','doing','going','was','had','done','gone','to','not','problem','problematic','in','out','inner','outer','interior','exterior','ordinary','extraordinary','develop','because','since','space','celestial','planet','bird','plane','place','decide','decides','deciding','decided','quick','slow','fast','quickly','slowly','quicker','slower','faster','quickest','slowest','fastest','car','bus','vehicle','doll','dolls','chair','work','working','works','worked','workworks','workplace','house','building','skyscraper','village','town','city','megacity','metropolis','on','off','exact','approximate','exactly','approximately','nation','national','international','internationalise','internationalisation','psst','ooh','mmmm','aah','sksk','VSCO','colour','line','square','cube','lines','squares','cubes','dimension','world','sun','winter','spring','summer','autumn','fall','rise','falls','rises','fruit','vegetable','name','food','wake','awake','awaken','awakens','awakening','shirt','t-shirt','short','long','strand','net','stack','speed','speedy','limit','metre','kilometre','mile','inch','foot','feet','inches','plural','singular','grammar','single','married','wedding','dress','beautiful','Barbie','layout','keyboard','computer','electricity','electric','learn','school','lesson','elementary','middle','high','learning','can','cannot','verb','verbal','verbally','article','book','internet','interest','increase','consider','possible','through','quest','ask','answer','question','asks','answers','questionnaire','save','start','restart','only','type','write','wrote','typing','typewriter','new','old','generation','generate','determine','determinate','determination','two','three','four','five','six','seven','eight','day','night','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','hundred','thousand','million','plug','atom','skin','dermatology','dermatoglyphic','subdermatoglyphic','right','copy','copyright','copyrighted','copyrightable','uncopyrightable','correct','wrong','incorrect','correctness','spell','spelling','punctuation','possibly','best','worst','better','worse','good','bad','great','terrible','okay','OK','vision','television','TV','meh','excellent','awe','awful','awesome','rate','rating','points','point','what','where','which','why','who','when','how','whatever','wherever','whichever','whoever','whenever','however','that','there','then','now','past','present','future','cite','cited','citation','need','needed','note','notify','notification', 'very','think','reason','crease','create','son','daughter','grandson','granddaughter','grandchildren','sister','brother','mother','father','grandmother','grandfather','grandparents','parents','family','friend','friends','niece','nephew','uncle','aunt', 'just','job','accept','reject','adjust','zoo','zoom','zone','size','zebra', 'bore','bored','boring','girlygirl','menarche','pregnant','Pregnacare','pregnancy','unpregnant','hunt','hunter-gatherer','gatherer','left','up','down','leftwards','rightwards','upwards','downwards','front','north','south','east','west','sound','noise','quiet','loud','quietly','loudly','count','counts','counting','counted','country','countries','account','swear','sided','lopsided','poll','lady','ladygirl','girllike','girllikeness','puzzle','headed','puzzlehead','puzzleheaded','hammer','hammerhead','redhead','blonde','bimbo','America','Indian','palindrome','did','level','arachnid','spider','arachnophobia','bat','batgirl','cat','catgirl','equal','equals','Minecraft','craft','game','over','under','undergrad','undergraduate','graduate','full','flow','overflow','ground','underground','become','between','after','before','number','both','public','program','commit','suicide','control','delete','corrupt','glitch','thirty','property','puberty','tween','preadolescence','preadolescent','adolescent','juvenile','gestate','gestation','gluten','gluten-free','free','allergy','allergic','most','all','salad','lettuce','busy','business','businesses','businessman','businesswoman','button','buttoned','unbuttoned','plot','plots','height','burn','turn','fire','fun','gun','mature','preterm']
elif funbox == 'wasd':
    words = ['w','a','s','d','wa','aw','ws','sw','wd','dw','as','sa','ad','da','sd','ds','was','wsa','aws','asw','swa','saw','wad','wda','awd','adw','dwa','daw','asd','ads','sad','sda','das','dsa','wasd','wads','wsad','wsda','wdas','wdsa','awsd','awds','aswd','asdw','adws','adsw','swad','swda','sawd','sadw','sdwa','sdaw','dwas','dwsa','daws','dasw','dswa','dsaw']
elif funbox == 'binary':
    words = ['000','001','010','011','100','101','110','111']
elif funbox == 'bigram salad':
    words = ['am','an','as','at','be','by','do','eh','ex','go','he','in','is','it','me','my','no','of','oh','on','ox','so','to','uh','up','us']
elif funbox == 'wikipedia tags':
    words = ['[citation needed]','[clarification needed]','[better source needed]','[by whom?]','[which?]']
elif funbox == 'weakspot':
    words = ['be','become','between','because','my','after','before','people','number','both','develop','increase','public','problem','program']
elif funbox == 'wikipedia':
    words = ["Girls typically have a female reproductive system. Some intersex children with ambiguous genitals may be classified as girls, while some Transgender youth have a gender identity as girls.[28][29][30][page needed][better source needed]","A special case presents with choirs and choruses, especially in the tradition of the choir school which uses ensemble and musical discipline to ground academic discipline. Male and female voices are distinctive both solo and in ensemble, and segregated singing has an evolved and established aesthetic. Male voices, unlike female voices, break in early adolescence, and accommodating this break in an educational program is challenging in a coed environment. Coeducation tends to stigmatize males, as is often the case in expressive arts, unlike athletics.[citation needed]","India today prides itself in being the world's largest democracy, and the 4th largest economy in the world. Even though much remains to be done, especially in regard to eradicating poverty and securing effective structures of governance, India's achievements since independence in sustaining freedom and democracy have been singular among the world's new nations.[12]"]
wordLimit = 10;
if funbox == 'wikipedia':
    wordLimit = 1;
goal = 51200;
currentGoal = 100;
correctPhrases = 0;
wrongPhrases = 0;
r = 0;
print('Endless Typing Game')
print('Type the words below:')
while points >= 0 and points < goal:
    while numOfWords < wordLimit:
        word = words[random.randint(0, len(words)-1)];
        while word == lastWord:
            word = words[random.randint(0, len(words)-1)];
        if funbox == 'nospace' or funbox == 'binary':
            text = text + word;
        else:
            text = text + ' ' + word;
        numOfWords = numOfWords + 1;
        lastWord = word;
    numOfWords = 0;
    print(text)
    typedText = input();
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
