import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "7201_NPCDance"

NPC=[7201]
ADENA_ID=57
QuestId     = 7201
QuestName   = "NPCDance"
QuestDesc   = "custom"
InitialHtml = "8.htm"

print "INFO  importing custom: 7201: NPCDance"

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

			#Dance of Warrior
			if event == "80":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(271,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(271, 1), False, False)
				return "8.htm"
				st.setState(COMPLETED)

			#Dance of Inspiration
			if event == "81":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(272,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(272,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Mystic
			if event == "82":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(273,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(273,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Fire
			if event == "83":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(274,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(274,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Fury
			if event == "84":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(275,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(275,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Concentration
			if event == "85":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(276,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(276,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Light
			if event == "86":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(277,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(277,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Aqua Guard
			if event == "87":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(307,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(307,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Earth Guard
			if event == "88":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(309,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(309,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Vampire
			if event == "89":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(310,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(310,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Protection
			if event == "90":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(311,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(311,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Siren's Dance 
			if event == "91":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(365,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(365,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Shadow
			if event == "92":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(366,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(366,1),False,False)
				return "8.htm"		
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
