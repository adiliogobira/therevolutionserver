import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "9999_NPCBuffer"

NPC=[7106]
ADENA_ID=57
QuestId     = 9999
QuestName   = "NPCBuffer"
QuestDesc   = "custom"
InitialHtml = "1.htm"

print "[ADILIO] importing custom: 9999: NPCBuffer"

class Quest (JQuest) :

	def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

	def onEvent(self,event,st):
		htmltext = event
		count=st.getQuestItemsCount(ADENA_ID)
		if count < 150000 or st.getPlayer().getLevel() < 10 :
			htmltext = "<html><head><body>No Tienes Adena.<br></body></html>"
		else:
			st.takeItems(ADENA_ID,0)
			st.getPlayer().setTarget(st.getPlayer())
			
			if event == "1":
				st.takeItems(ADENA_ID,1000)
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(9951,5),False,False)
				st.getPlayer().restoreHPMP()
				return "1.htm"		
				st.setState(COMPLETED)

			#Wind Walk
			if event == "2":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1204,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Arcane Protection
			if event == "3":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1354,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Shield
			if event == "4":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1040,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Might
			if event == "5":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1068,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Mental Shield
			if event == "6":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1035,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless the Body
			if event == "7":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1045,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless the Soul
			if event == "8":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1048,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Magic Barrier
			if event == "9":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1036,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Resist Shock
			if event == "10":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1259,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Concentration
			if event == "11":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1078,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Berserker Spirit
			if event == "12":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1062,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless Shield
			if event == "13":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1243,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Vampiric Rage
			if event == "14":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1268,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Acumen
			if event == "15":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1085,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Empower
			if event == "16":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1059,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Haste
			if event == "17":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1086,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Guidance
			if event == "18":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1240,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Focus
			if event == "19":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1077,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Death Whisper
			if event == "20":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1242,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			if event == "21":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(271,1).getEffects(st.getPlayer(),st.getPlayer())	
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "22":
				st.takeItems(ADENA_ID,20000)	
				SkillTable.getInstance().getInfo(272,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "23":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(273,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "24":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(274,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "25":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(275,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "26":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(276,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "27":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(277,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "28":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(307,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "29":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(309,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "30":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(310,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "31":
				st.takeItems(ADENA_ID,20000)		
				SkillTable.getInstance().getInfo(311,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "32":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(366,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "3.htm"

			if event == "33":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(365,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()			
				return "3.htm"

			if event == "34":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(264,1).getEffects(st.getPlayer(),st.getPlayer())	
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "35":
				st.takeItems(ADENA_ID,20000)	
				SkillTable.getInstance().getInfo(265,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "36":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(266,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "37":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(267,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "38":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(268,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "39":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(269,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "40":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(270,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "41":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(304,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "42":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(305,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "43":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(306,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"	

			if event == "44":
				st.takeItems(ADENA_ID,20000)	
				SkillTable.getInstance().getInfo(308,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "45":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(363,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"

			if event == "46":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(364,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"	
              
			if event == "47":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(349,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "4.htm"	
				st.setState(COMPLETED)
				
				
			#Chant of Battle
			if event == "48":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1007,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Shielding
			if event == "49":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1009,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Fire
			if event == "50":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1006,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Flame
			if event == "51":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1002,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of life
			if event == "52":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1229,18).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Fury
			if event == "53":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1251,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Evasion
			if event == "54":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1252,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Rage
			if event == "55":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1253,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Revenge
			if event == "56":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1284,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Vampire
			if event == "57":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1310,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Eagle
			if event == "58":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1309,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Predator
			if event == "59":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1308,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Spirit
			if event == "60":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1362,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#Chant of Victory
			if event == "61":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1363,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)
				
			#chant of magnus
			if event == "62":
				st.takeItems(ADENA_ID,20000)
				SkillTable.getInstance().getInfo(1413,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)	
			
			#MPreg
			if event == "63":
				st.takeItems(ADENA_ID,1000)
				SkillTable.getInstance().getInfo(1013,32).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "1.htm"		
				st.setState(COMPLETED)			

			#greatmight
			if event == "64":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1388,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#greatshield
			if event == "65":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1389,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#holyresist
			if event == "66":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1392,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#Unholyresist
			if event == "67":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1393,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#pof
			if event == "68":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1356,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#elemtprotect
			if event == "69":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1352,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#wildmagic
			if event == "70":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1303,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#advblock
			if event == "71":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1304,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#divProtect
			if event == "72":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1353,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#pow
			if event == "73":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1355,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#powi
			if event == "74":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1357,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#manaregen
			if event == "75":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1047,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)

			#ba
			if event == "76":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1311,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"		
				st.setState(COMPLETED)
                        
			#noble
			if event == "77":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1323,1).getEffects(st.getPlayer(),st.getPlayer())
				return "1.htm"		
				st.setState(COMPLETED)
			
			#Cancellation
			if event == "78":
				st.takeItems(ADENA_ID,5000)
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(9950,1),False,False)
				st.getPlayer().restoreHPMP()
				return "1.htm"
				st.setState(COMPLETED)
                        
			#SongofElemental
			if event == "79":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(529,1).getEffects(st.getPlayer(),st.getPlayer())
				return "4.htm"

                        #DanceofAlignment
			if event == "80":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(530,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"

			#HolyWeapon
			if event == "81":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1043,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)
			
			#Regeneration
			if event == "82":
				st.takeItems(ADENA_ID,5000)
				SkillTable.getInstance().getInfo(1044,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)
                        
			#ResistFire
			if event == "83":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1191,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)

                        #ResistPoison
			if event == "84":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1033,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)

                        #ResistAqua
			if event == "85":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1182,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)

                        #ResistWind
			if event == "86":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1189,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)

                        #WarChant
			if event == "87":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1390,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)

                        #EarthChant
			if event == "88":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1391,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)

                        #Protection
			if event == "89":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1461,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "5.htm"
				st.setState(COMPLETED)

                        #Invigor
			if event == "90":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1032,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)

            #Agility
			if event == "91":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1087,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)

            #Clarity
			if event == "92":
				st.takeItems(ADENA_ID,10000)
				SkillTable.getInstance().getInfo(1397,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().restoreHPMP()
				return "2.htm"
				st.setState(COMPLETED)							
				
			if htmltext != event:
				st.setState(COMPLETED)
				st.exitQuest(1)
		return htmltext

	def onTalk (self,npc,player):
	   st = player.getQuestState(qn)
	   htmltext = "<html><head><body>I have nothing to say to you</body></html>"
	   st.setState(STARTED)
	   return InitialHtml

QUEST = Quest(QuestId,str(QuestId) + "_" + QuestName,QuestDesc)

for npcId in NPC:
 QUEST.addStartNpc(npcId)
 QUEST.addTalkId(npcId)
