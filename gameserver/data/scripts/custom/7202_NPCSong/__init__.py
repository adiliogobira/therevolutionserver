import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "7202_NPCSong"

NPC=[7202]
ADENA_ID=57
QuestId     = 7202
QuestName   = "NPCSong"
QuestDesc   = "custom"
InitialHtml = "9.htm"

print "INFO  importing custom: 7202: NPCSong"

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

			#Dance of Shadow
			if event == "92":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(366,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(366,1),False,False)
				return "8.htm"		
				st.setState(COMPLETED)

			#Song of Earth
			if event == "93":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(264,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(264,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Life
			if event == "94":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(265,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(265,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Water
			if event == "95":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(266,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(266,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Warding
			if event == "96":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(267,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(267,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Wind
			if event == "97":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(268,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(268,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Hunter
			if event == "98":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(269,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(269,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Invocation
			if event == "99":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(270,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(270,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Vitality
			if event == "100":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(304,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(304,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Vengeance
			if event == "101":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(305,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(305,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Flame Guard
			if event == "102":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(306,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(306,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Storm Guard
			if event == "103":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(308,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(308,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Meditation
			if event == "104":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(363,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(363,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Champion
			if event == "105":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(364,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(364,1),False,False)
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Renewal
			if event == "106":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(349,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(349,1),False,False)
				return "9.htm"		
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
