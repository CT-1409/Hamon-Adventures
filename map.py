from items import*
from characters import*

Room = "jmeno komnaty"
Story = "komnaty"
Item = "item v mistnosti"
Boss = "jestli v mistnosti je boss tak zde bude jeho jmeno jinak false"
Hadanka = "zde bude hadanka pokud ne tak false"
Up = "up", "north"
Back = "back", "south"
Left = "left", "west"
Right = "right", "east"

map = {
     'a1':{
          Room: "katedrála",
          Story: "v katedrále je pohřbena královská rodina a jsou zde také schovány boty strážce Zoubka",
          Item: boots.__dict__,
          Boss: mini_boss_1.__dict__,
          Hadanka: "zde bude hadanka pokud ne tak false",
          Up: False,
          Back: 'b1',
          Left: False,
          Right: 'a2'
     },
     'a2':{
          Room: "Královská síň",
          Story: "síň Králů",
          Item: scroll.__dict__,
          Boss: main_boss.__dict__,
          Hadanka: True,
          Up: False,
          Back: 'b2',
          Left: 'a1',
          Right: 'a3'
     },
     'a3':{
          Room: "měsíční komnata",
          Story: "očarovaná komnata kde se z měsíčního světla stáva sluneční svit, diky tomu královská garda porazila Drákulu",
          Item: "zde není žádní předmět",
          Boss: minion.__dict__,
          Hadanka: False,
          Up: False,
          Back: 'b3',
          Left: 'a2',
          Right: 'a4'
     },
     'a4':{
          Room:"věž milenců",
          Story: "tradiční místo kde král žádá o ruku svojí královnu",
          Item: potion.__dict__,
          Boss: False,
          Hadanka: False,
          Up: False,
          Back: 'b4',
          Left: 'a3',
          Right: False
     },
     'b1':{
          Room: "kasárny královské gardy",
          Story: "královská garda, speciální vojenská složka založená proti Drakulovi",
          Item: kovovy_mec.__dict__,
          Boss: mini_boss_2.__dict__,
          Hadanka: True,
          Up: 'a1',
          Back: 'c1',
          Left: False,
          Right: 'b2'
     },
     'b2':{
          Room: "hradní náměstí",
          Story: "místo kde se mohou shromažďovat lidé hradu",
          Item: potion.__dict__,
          Boss: False,
          Hadanka: False,
          Up: False,
          Back: 'd2',
          Left: 'b1',
          Right: 'c3'
     },
     'b3':{
          Room: "tajemná komnata",
          Story: "zde měl hrob Drákula, jden z starodávných členů královské rodiny, který však podlehl moci kamenné masky a museli ho uveznit zde",
          Item: titanovy_mec.__dict__,
          Boss: mini_boss_4.__dict__,
          Hadanka: True,
          Up: 'a3',
          Back: 'c3',
          Left: 'b2',
          Right: 'b4'
     },
     'b4':{
          Room: "hradní hlídková věž",
          Story:  "věž kam chodívala stráž",
          Item: potion.__dict__,
          Boss: minion.__dict__,
          Hadanka: False,
          Up: ["up", "north"],
          Back: ["back", "south"],
          Left: ["left", "west"],
          Right: ["right", "east"]
     },
     'c1':{
          Room: "sál dobyvatelů",
          Story: "legendární očarovaný sál do kterého mohou vztoupit pouze ti, kteří toho jsou hodni",
          Item: potion.__dict__,
          Boss: minion.__dict__,
          Hadanka: True,
          Up: 'b1',
          Back: 'd1',
          Left: False,
          Right: False
     },
     'c2':{
          Room: "most krále Šalamouna",
          Story: "most pastavený na počest krále Šalamouna",
          Item: "MAPA",
          Boss: minion.__dict__,
          Hadanka: False,
          Up: 'b2',
          Back: 'd2',
          Left: False,
          Right: False
     },
     'c3':{
          Room: "Královské zahrady",
          Story: "zahrada kam může jen královská rodina",
          Item: apple.__dict__,
          Boss: False,
          Hadanka: False,
          Up: False,
          Back: 'd3',
          Left: 'c2',
          Right: 'c4'
     },
     'c4':{
          Room: "jižní zahrady hradu",
          Story: "podle legendy zde rostou jablka, která léčí",
          Item: apple.__dict__,
          Boss: False,
          Hadanka: False,
          Up: 'b4',
          Back: 'd4',
          Left: 'c3',
          Right: False
     },
     'd1':{
          Room: "sklep žalářníka pojsliče",
          Story: "zradil královskou rodinu a stal se zombie",
          Item: "potion",
          Boss: minion.__dict__,
          Hadanka: False,
          Up: 'c1',
          Back: False,
          Left: False,
          Right: False
     },
     'd2':{
          Room: "pláž",
          Story: "pláž blízko hradu, nachízí se před mostem krále Šalamouna",
          Item: False,
          Boss: False,
          Hadanka: False,
          Up: 'c3',
          Back: False,
          Left: False,
          Right: False
     },
     'd3':{
          Room: "vězení hluboko pod hradem",
          Story: "zde byl vězněn Drákula, člen královské rodiny který podlehl moci kamenné masky, zemřel před 400 lety",
          Item: key.__dict__,
          Boss: mini_boss_3.__dict__,
          Hadanka: True,
          Up: 'c3',
          Back: False,
          Left: False,
          Right: 'd4'
     },
     'd4':{
          Room: "mučírna",
          Story:  "mučírna vězeňů",
          Item: potion.__dict__,
          Boss: False,
          Hadanka: False,
          Up: False,
          Back: False,
          Left: 'd3',
          Right: False
     },
}

# print(map['a1'][Room])
# print(scroll.name)
# print(map['a1'][Item]['name'])
# print(main_boss.n)






