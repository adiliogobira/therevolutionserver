import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "7200_NPCHuman"

NPC=[7200]
ADENA_ID=57
ADENA_AMOUNT=1000
QuestId     = 7200
QuestName   = "NPCHuman"
QuestDesc   = "custom"
InitialHtml = "2.htm"

print "INFO  importing custom: 7200: NPCHuman"

class Quest (JQuest) :

	def __init__(self,id,name,descr):JQuest.__init__(self,id,name,descr)


	def onEvent(self,event,st):
		htmltext = event
		count=st.getQuestItemsCount(ADENA_ID)
		if count < 0  or st.getPlayer().getLevel() < 1 :
			htmltext = "<html><head><body>You dont have enough Adena,<br> or your level is too low. You must be 40 or higher.</body></html>"
		else:
			st.takeItems(ADENA_ID,ADENA_AMOUNT)
			st.getPlayer().setTarget(st.getPlayer())
				
			#Wind Walk
			if event == "2":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1204,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1204,2),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Decrease Weight
			if event == "3":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1257,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1257,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Shield
			if event == "4":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1040,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1040,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Might
			if event == "5":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1068,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1068,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Mental Shield
			if event == "6":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1035,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1035,4),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless the Body
			if event == "7":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1045,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1045,6),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless the Soul
			if event == "8":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1048,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1048,6),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Magic Barrier
			if event == "9":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1036,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1036,2),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Concentration
			if event == "10":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1078,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1078,6),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Berserker Spirit
			if event == "11":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1062,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1062,2),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless Shield
			if event == "12":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1243,6).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1243,6),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Vampiric Rage
			if event == "13":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1268,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1268,4),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Acumen
			if event == "14":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1085,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1085,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Empower
			if event == "15":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1059,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1059,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Haste
			if event == "16":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1086,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1086,2),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Guidance
			if event == "17":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1240,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1240,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Focus
			if event == "18":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1077,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1077,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Death Whisper
			if event == "19":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1242,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1242,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

            #Agility
			if event == "20":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1087,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1087,3),False,False)
				return "2.htm"
				st.setState(COMPLETED)	
                                                
            #Clarity
			if event == "21":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1397,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1397,3),False,False)
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Advanced Block
			if event == "22":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1304,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1304,3),False,False)
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Kiss of Eva
			if event == "23":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1073,2).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1073,2),False,False)
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Greater Shield
			if event == "24":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1389,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1389,3),False,False)
				return "2.htm"
				st.setState(COMPLETED)	
                                               
                        #Wild Magic
			if event == "25":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1303,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1303,1),False,False)
				return "2.htm"
				st.setState(COMPLETED)

			#Regeneration
			if event == "26":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1044,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1044,3),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Holy Weapon
			if event == "27":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1043,1).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1043,1),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Mana Regeneration
			if event == "28":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1047,4).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1047,4),False,False)
				return "2.htm"		
				st.setState(COMPLETED)

			#Greather Might
			if event == "29":
				st.takeItems(ADENA_ID,ADENA_AMOUNT)
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				SkillTable.getInstance().getInfo(1388,3).getEffects(st.getPlayer(),st.getPlayer())
				st.getPlayer().useMagic(SkillTable.getInstance().getInfo(1388,3),False,False)
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
CREATED = State('Start',QUEST)
STARTED = State('Started',QUEST)
COMPLETED = State('Completed',QUEST)

QUEST.setInitialState(CREATED)

for npcId in NPC:
 QUEST.addStartNpc(npcId)
 QUEST.addTalkId(npcId)
