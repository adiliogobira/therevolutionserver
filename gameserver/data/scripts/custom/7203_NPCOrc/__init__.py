import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "7203_NPCOrc"

NPC=[7203]
ADENA_ID=57
QuestId     = 7203
QuestName   = "NPCOrc"
QuestDesc   = "custom"
InitialHtml = "3.htm"

print "INFO  importing custom: 7203: NPCBuffer Orc"

class Quest (JQuest) :

	def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)


	def onEvent(self,event,st):
		htmltext = event
		count=st.getQuestItemsCount(ADENA_ID)
		if count < 0  or st.getPlayer().getLevel() < 1 :
			htmltext = "<html><head><body>You dont have enough Adena,<br> or your level is too low. You must be 40 or higher.</body></html>"
		else:
			st.takeItems(ADENA_ID,0)
			st.getPlayer().setTarget(st.getPlayer())

			#Chant of battle
			if event == "30":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1007,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1007,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Shielding
			if event == "31":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1009,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1009,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Fire
			if event == "32":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1006,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1006,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Flame
			if event == "33":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1002,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1002,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Fury
			if event == "34":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1251,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1251,2),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Evasion
			if event == "35":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1252,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1252,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Rage
			if event == "36":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1253,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1253,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Revenge
			if event == "37":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1284,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1284,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Vampire
			if event == "38":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1310,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1310,4),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Eagle
			if event == "39":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1309,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1309,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Predator
			if event == "40":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1308,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1308,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Spirit
			if event == "41":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1362,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1362,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Victory
			if event == "42":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1363,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1363,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Magnus
			if event == "43":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1413,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1413,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#War Chant
			if event == "44":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1390,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1390,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Earth Chant
			if event == "45":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1391,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1391,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of life
			if event == "46":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1229,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1229,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Body Avatar
			if event == "47":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1311,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1311,6),False,False)
				return "3.htm"		
				st.setState(COMPLETED)


			#Pa'agrio Gifth
			if event == "66":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1003,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1003,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Blessing
			if event == "67":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1005,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1005,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Glory
			if event == "68":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1008,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1008,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Tact
			if event == "69":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1260,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1260,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Wisdom
			if event == "70":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1004,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1004,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Protection
			if event == "71":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1250,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1250,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Rage
			if event == "72":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1261,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1261,2),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Vision
			if event == "73":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1249,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1249,3),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Haste
			if event == "74":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1282,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1282,2),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Eye
			if event == "75":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1364,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1364,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Soul
			if event == "76":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1365,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1365,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Emblem
			if event == "77":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1415,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1415,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Fist
			if event == "78":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1416,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1416,1),False,False)
				return "3.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Victory
			if event == "79":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1414,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1414,1),False,False)
				return "3.htm"		
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

QUEST       = Quest(QuestId,str(QuestId) + "_" + QuestName,QuestDesc)
CREATED=State('Start',QUEST)
STARTED=State('Started',QUEST)
COMPLETED=State('Completed',QUEST)

QUEST.setInitialState(CREATED)

for npcId in NPC:
 QUEST.addStartNpc(npcId)
 QUEST.addTalkId(npcId)
