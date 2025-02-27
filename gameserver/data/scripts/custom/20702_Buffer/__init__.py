import sys
from java.lang import System;
from java.util import Iterator;
from com.l2jfrozen.gameserver.model.quest import State;
from com.l2jfrozen.gameserver.model.quest import QuestState;
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest;
from com.l2jfrozen.util.database import L2DatabaseFactory;
from com.l2jfrozen.gameserver.datatables import SkillTable;
from com.l2jfrozen.gameserver.model import L2Effect;
from com.l2jfrozen.gameserver.model import L2Skill;
from com.l2jfrozen.gameserver.model import L2Summon;
from com.l2jfrozen.gameserver.model.zone import L2ZoneType
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance;
from com.l2jfrozen.gameserver.model.actor.instance import L2PetInstance;
from com.l2jfrozen.gameserver.model.actor.instance import L2SummonInstance;
from com.l2jfrozen.gameserver.network.serverpackets import SetSummonRemainTime;
from com.l2jfrozen.gameserver.network.serverpackets import SetupGauge;
import java.util.StringTokenizer;
import javolution.util.FastList;
import javolution.util.FastMap;
import com.l2jfrozen.Config;
import com.l2jfrozen.gameserver.datatables.SkillTable;
import com.l2jfrozen.gameserver.datatables.CharSchemesTable;
import com.l2jfrozen.gameserver.datatables.sql.ItemTable;
import com.l2jfrozen.gameserver.model.L2Effect;
import com.l2jfrozen.gameserver.model.L2Skill;
import com.l2jfrozen.gameserver.model.L2Summon;
import com.l2jfrozen.gameserver.model.actor.instance.L2PcInstance;
import com.l2jfrozen.gameserver.network.serverpackets.ActionFailed;
import com.l2jfrozen.gameserver.network.serverpackets.MagicSkillUser;
import com.l2jfrozen.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jfrozen.gameserver.taskmanager.AttackStanceTaskManager;
import com.l2jfrozen.gameserver.templates.L2NpcTemplate;

QUEST_ID = 5555
QUEST_NAME   = "NPCBuffer"
QUEST_DESCRIPTION   = "custom"
QUEST_LOADING_INFO = str(QUEST_ID)+"_"+QUEST_NAME
NPC_ID = 5555

TITLE_NAME = "Macro Buffer"
SCRIPT_RELOAD = True 
ENABLE_VIP_BUFFER = False
VIP_ACCESS_LEVEL = 1                
ENABLE_BUFF_SECTION = True    
ENABLE_SCHEME_SYSTEM = True              
ENABLE_HEAL = True                       
ENABLE_BUFFS = True                      
ENABLE_RESIST = True                     
ENABLE_SONGS = True                      
ENABLE_DANCES = True                     
ENABLE_CHANTS = True                 
ENABLE_OTHERS = False                     
ENABLE_SPECIAL = True                    
ENABLE_CUBIC = True                    
ENABLE_BUFF_REMOVE = True                
ENABLE_BUFF_SET = True
BUFF_WITH_KARMA = False                  
FREE_BUFFS = False                       
TIME_OUT = False           
TIME_OUT_TIME = 1                    
MIN_LEVEL = 20                           
BUFF_REMOVE_PRICE = 1                 
HEAL_PRICE = 1                      
BUFF_PRICE = 1                     
RESIST_PRICE = 1                    
SONG_PRICE = 1                      
DANCE_PRICE = 1                      
CHANT_PRICE = 1                      
OTHERS_PRICE = 1                     
SPECIAL_PRICE = 1                   
CUBIC_PRICE = 1                    
BUFF_SET_PRICE = 1                 
SCHEME_BUFF_PRICE = 1              
SCHEMES_PER_PLAYER = 4                   
CONSUMABLE_ID = 9846                       
MAX_SCHEME_BUFFS = 24
MAX_SCHEME_DANCES = 16

def rebuildMainHtml(st) :
	MAIN_HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>"; MESSAGE = ""
	bottonA="Auto Buff";bottonB="Heal Me";bottonC="Rem. Buffs";i=0;j=0;Temp="<tr><td> </td> <td> </td></tr>";TRS = Temp.split(" ")
	if st.getInt("Pet-On-Off") == 1:
		bottonA="Auto Buff Pet";bottonB="Heal My Pet";bottonC="Rem. Pet Buffs"
		MAIN_HTML_MESSAGE += "<button value=\"Pet Options\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " buffpet 0 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"	
	else: MAIN_HTML_MESSAGE += "<button value=\"Char Options\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " buffpet 1 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
	if ENABLE_BUFF_SECTION == True :	
		if ENABLE_BUFFS == True :
			if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Buffs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_buffs 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
			i+=2;j+=1
		if ENABLE_RESIST == True :
		       	if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Resist\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_resists 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]	
                	i+=2;j+=1
		if ENABLE_SONGS == True :
			if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Songs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_songs 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
			i+=2;j+=1
		if ENABLE_DANCES == True :
			if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Dances\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_dances 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
			i+=2;j+=1
		if ENABLE_CHANTS == True :
			if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Chants\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_chants 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
			i+=2;j+=1
		if ENABLE_SPECIAL == True :
			if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Special\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_special 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
			i+=2;j+=1
		if ENABLE_OTHERS == True :
			if i>2:i=0
			MESSAGE += TRS[i]+"<button value=\"Others\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_others 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
			i+=2;j+=1
	if ENABLE_CUBIC == True:
		if i>2:i=0
		MESSAGE += TRS[i]+"<button value=\"Cubics\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect view_cubic 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]
		i+=2;j+=1
	if ENABLE_BUFF_SET == True :
		if i>2:i=0
		MESSAGE += TRS[i]+"<button value=\""+bottonA+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " castBuffSet 0 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]		
		i+=2;j+=1
	if ENABLE_HEAL == True :
		if i>2:i=0
		MESSAGE += TRS[i]+"<button value=\""+bottonB+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " heal 0 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]	
		i+=2;j+=1
	if ENABLE_BUFF_REMOVE == True:
		if i>2:i=0
		MESSAGE += TRS[i]+"<button value=\""+bottonC+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " removeBuffs 0 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[i+1]			
		i+=2;j+=1
	if j == 1: MAIN_HTML_MESSAGE+= MESSAGE + "<br>"
	else: MAIN_HTML_MESSAGE+= "<table>" + MESSAGE + "</table><br>"
	if ENABLE_SCHEME_SYSTEM == True : 
		MAIN_HTML_MESSAGE += generateScheme(st) 
	if st.getPlayer().isGM() : 
		MAIN_HTML_MESSAGE += "<br><button value=\"Manage Buffs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect manage_buffs 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
	MAIN_HTML_MESSAGE += "<br><font color=\"303030\">"+TITLE_NAME+"</font>"
	MAIN_HTML_MESSAGE += "</center></body></html>"
	return MAIN_HTML_MESSAGE

def generateScheme(st) :
	schemeName = []
	schemeId = []
	HTML = ""
	conn=L2DatabaseFactory.getInstance().getConnection()
	rss = conn.prepareStatement("SELECT * FROM buffer_scheme_list WHERE player_id="+str(st.getPlayer().getObjectId()))
	action=rss.executeQuery()
	while (action.next()) :
		try :
			schemeName += [action.getString("scheme_name")]
			schemeId += [action.getString("id")]
		except : print "Query error!"
	try : conn.close()
	except : pass
	if len(schemeName) > 0:
		MESSAGE = ""
		i=0;j=0;Temp="<tr><td> </td> <td> </td></tr>";TRS = Temp.split(" ")
		while i <= len(schemeName) - 1:
		       	if j>2:j=0
			MESSAGE += TRS[j]+"<button value=\""+schemeName[i]+"\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" cast "+schemeId[i]+" x x\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"+TRS[j+1]
			i+=1;j+=2
		if i == 1: HTML+= MESSAGE + "<br>"
		else: HTML+= "<table>" + MESSAGE + "</table><br>"
	if len(schemeName) < SCHEMES_PER_PLAYER :
		HTML += "<table><tr><td><button value=\"Create\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" create_1 x x x\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td>"
	else : HTML += "<table width=100><tr>"
	if len(schemeName) > 0 :
		HTML += "<td><button value=\"Edit\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" edit_1 x x x\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td>"
		HTML += "<td><button value=\"Delete\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" delete_1 x x x\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td></tr></table>"				
	else : HTML += "</tr></table>"
	return HTML

def reloadPanel(st) :
	HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>"
	HTML_MESSAGE += "<font color=\"303030\">"+TITLE_NAME+"</font><br>"
	HTML_MESSAGE += "<img src=\"L2UI.SquareGray\" width=250 height=1><br>"
	HTML_MESSAGE += "<table width=260 border=0 bgcolor=000000>"
	HTML_MESSAGE += "<tr><td><br></td></tr>"                                                                                                                                                                                                
	HTML_MESSAGE += "<tr><td align=\"center\"><font color=\"00FFFF\">Esta opcao pode ser vista so por GMs e admin<br1>permitem atualizar as alteracoes feitas no<br1>script. Voce pode desabilitar essa opcao<br1>na secao de configuracoes dentro do Script.<br><font color=\"LEVEL\">Para ver os buffer click em Yes</font></font></td></tr>"
	HTML_MESSAGE += "<tr><td></td></tr></table><br>"
	HTML_MESSAGE += "<img src=\"L2UI.SquareGray\" width=250 height=1><br><br>"
	HTML_MESSAGE += "<button value=\"Yes\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" reloadscript 1 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
	HTML_MESSAGE += "<button value=\"No\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" reloadscript 0 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"				
	HTML_MESSAGE += "</center></body></html>"
	return HTML_MESSAGE

def getitemname(st,itemval):
	conn=L2DatabaseFactory.getInstance().getConnection()
	itemidList = conn.prepareStatement("SELECT * FROM etcitem WHERE item_id="+str(itemval))
	il=itemidList.executeQuery()
	val = "No Name"
	if il :
		il.next()
		try : val = il.getString("name")					
		except : pass
	try : conn.close()
	except: pass
	return val

def getBuffCount(scheme) :
	count = 0
	conn=L2DatabaseFactory.getInstance().getConnection()
	rss = conn.prepareStatement("SELECT * FROM buffer_scheme_contents WHERE scheme_id=\""+str(scheme)+"\"")
	action=rss.executeQuery()
	while (action.next()) :
		try : count += 1
		except : count = 0
	try : conn.close()
	except : pass		
	return count

def getBuffType(id) :
	conn=L2DatabaseFactory.getInstance().getConnection()
	act = conn.prepareStatement("SELECT buffType FROM buffer_buff_list WHERE buffId=? LIMIT 1")
	act.setInt(1, int(id))
	rs=act.executeQuery()
	val = "none"
	if rs :
		rs.next()
		try : val = rs.getString("buffType")					
		except : val = "none"
	try : conn.close()
	except: pass
	return val

def isEnabled(id,level) :
	conn=L2DatabaseFactory.getInstance().getConnection()
	act = conn.prepareStatement("SELECT canUse FROM buffer_buff_list WHERE buffId=? AND buffLevel=? LIMIT 1")
	act.setInt(1, int(id))
	act.setInt(2, int(level))
	rs=act.executeQuery()
	val = "False"
	if rs :
		rs.next()
		try : num = rs.getString("canUse")					
		except : pass
	try : conn.close()
	except: pass
	if num == "1" : val = "True"	
	return val	
											
def isUsed(scheme,id,level) :
	count = 0; used = False
	conn=L2DatabaseFactory.getInstance().getConnection()
	rss = conn.prepareStatement("SELECT * FROM buffer_scheme_contents WHERE scheme_id=\""+str(scheme)+"\" AND skill_id=\""+str(id)+"\" AND skill_level=\""+str(level)+"\"")
	action=rss.executeQuery()
	used = False
	while (action.next()) :
		try : count += 1
		except : count = 0
	try : conn.close()
	except : pass		
	if count > 0 : used = True
	return used

def getclassbuff(id):	
	conn=L2DatabaseFactory.getInstance().getConnection()
	getTipo = conn.prepareStatement("SELECT * FROM buffer_buff_list WHERE buffId=\""+id+"\"")
	gt=getTipo.executeQuery()
	val = 0
	if gt :
		gt.next()
		try : val = gt.getInt("buff_class")
		except : pass
	try : conn.close()
	except : pass
	return val

def showText(st,type,text,buttonEnabled,buttonName,location) :
	MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>"
	MESSAGE += "<font color=\"LEVEL\">"+type+"</font><br>"+text+"<br>"
	if buttonEnabled == "True" :
		MESSAGE += "<button value=\""+buttonName+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect "+location+" 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
	MESSAGE += "<font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
	st.playSound("ItemSound3.sys_shortage")
	return MESSAGE

def ReloadConfig(st) :
	try:
		if QuestManager.getInstance().reload(QUEST_ID): st.player.sendMessage("The script and settings have been reloaded successfully.")
		else: st.player.sendMessage("Script Reloaded Failed. you edited something wrong! :P, fix it and restart the server")
	except: st.player.sendMessage("Script Reloaded Failed. you edited something wrong! :P, fix it and restart the server")
	return rebuildMainHtml(st)
	
class Quest (JQuest) :
	
	def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

	def onAdvEvent (self,event,npc,player) :
		st = player.getQuestState(QUEST_LOADING_INFO)
		getpetbuff = 0
		if st.getInt("Pet-On-Off") == 1: getpetbuff = 1

		def createScheme() :
			HTML = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br><br>Voce deve separar novas palavras com um ponto (.)<br><br>Scheme name: <edit var=\"name\" width=100><br><br>"
			HTML += "<button value=\"Create Scheme\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" create $name no_name x x\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			HTML += "<br><button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML
			
		def deleteScheme() : 
			HTML = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>Available schemes:<br><br>"
			conn=L2DatabaseFactory.getInstance().getConnection()
			rss = conn.prepareStatement("SELECT * FROM buffer_scheme_list WHERE player_id="+str(st.getPlayer().getObjectId()))
			action=rss.executeQuery()
			while (action.next()) :
				try : HTML += "<button value=\""+action.getString("scheme_name")+"\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" delete_c "+action.getString("id")+" "+action.getString("scheme_name")+" x\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
				except : print "Query error!"
			try : conn.close()
			except : pass	
			HTML += "<br><button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"			
			HTML += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML
			
		def editScheme() : 
			name = ""; id = ""
			HTML = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>Selecione um esquema que voce gostaria de dirigir:<br><br>"
			conn=L2DatabaseFactory.getInstance().getConnection()
			rss = conn.prepareStatement("SELECT * FROM buffer_scheme_list WHERE player_id="+str(st.getPlayer().getObjectId()))
			action=rss.executeQuery()
			while (action.next()) :
				try :
					name = action.getString("scheme_name")
					id = action.getString("id")
					HTML += "<button value=\""+name+"\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" manage_scheme_select "+id+" x x\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
				except : print "Query error!"
			try : conn.close()
			except : pass	
			HTML += "<br><button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML

		def getOptionList(scheme) :
			Bcount = getBuffCount(scheme)
			HTML = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>tem <font color=\"LEVEL\">"+str(Bcount)+"</font> lustres em corrente scheme!<br><br>"
			if Bcount < MAX_SCHEME_BUFFS + MAX_SCHEME_DANCES:
				HTML += "<button value=\"Add buffs\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" manage_scheme_1 "+str(scheme)+" 1 x\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08_over\">"
			if Bcount > 0 :
				HTML += "<button value=\"Remove buffs\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" manage_scheme_2 "+str(scheme)+" 1 x\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08_over\">"				
			HTML += "<br><button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_1 0 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML += "<button value=\"Home\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML
		
		def buildHtml(buffType):
			HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><br>"
			if FREE_BUFFS == True : HTML_MESSAGE += "All buffs are for <font color=\"LEVEL\">free</font>!"			
			else :
				price = 0
				if buffType == "buff" : price = BUFF_PRICE
                                if buffType == "resist" : price = RESIST_PRICE
				if buffType == "song" : price = SONG_PRICE
				if buffType == "dance" : price = DANCE_PRICE
				if buffType == "chant" : price = CHANT_PRICE
				if buffType == "others" : price = OTHERS_PRICE
				if buffType == "special" : price = SPECIAL_PRICE
				if buffType == "cubic" : price = CUBIC_PRICE
				HTML_MESSAGE += "All special buffs cost <font color=\"LEVEL\">"+str(price)+"</font> adena!"
			HTML_MESSAGE += "<table>"
			conn=L2DatabaseFactory.getInstance().getConnection()
			buffCount = 0; i = 0
			getList = conn.prepareStatement("SELECT * FROM buffer_buff_list WHERE buffType=\""+buffType+"\" AND canUse=1")
			rs=getList.executeQuery()
			while (rs.next()) :
				try : buffCount += 1
				except : buffCount = 0
			if buffCount == 0 : HTML_MESSAGE += "No buffs are available at this moment!<br>"
			else :
				availableBuffs = []
				getList = conn.prepareStatement("SELECT buffId,buffLevel FROM buffer_buff_list WHERE buffType=\""+buffType+"\" AND canUse=1  ORDER BY Buff_Class ASC, id")
				rs=getList.executeQuery()
				while (rs.next()) :
					try :
						bId = rs.getInt("buffId")
						bLevel = rs.getInt("buffLevel")
						bName = SkillTable.getInstance().getInfo(bId,bLevel).getName()
						bName = bName.replace(" ","+")
						availableBuffs += [bName+"_"+str(bId)+"_"+str(bLevel)]
					except: HTML_MESSAGE += "Error loading buff list...<br>"
				try : conn.close()
				except : pass
				avBuffs = len(availableBuffs)
				format = "0000"
				for avBuffs in availableBuffs :
					buff = avBuffs
					buff = buff.replace("_"," ")
					buffSplit = buff.split(" ")
					name = buffSplit[0]
					id = int(buffSplit[1])
					level = buffSplit[2]
					name = name.replace("+"," ")
					if id < 100 : format = "00"+str(id)
					elif id > 99 and id < 1000 : format = "0"+str(id)
					else :
						if id > 4698 and id < 4701 : format = "1331"
						elif id > 4701 and id < 4704 : format = "1332"
						else: format = str(id)
					i += 1
					HTML_MESSAGE += "<tr><td><img src=\"Icon.skill"+format+"\" width=32 height=32></td><td><button value=\""+name+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " giveBuffs "+str(id)+" "+str(level)+" "+buffType+"\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\"></td></tr>"									
			HTML_MESSAGE += "</table><br><button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML_MESSAGE += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML_MESSAGE
		
		def generateQuery(case,case2) :
			aa = 1; count = 0; qry = ""; buffTypes = []
			if ENABLE_BUFFS == True and case < MAX_SCHEME_BUFFS:
				count += 1
				buffTypes += ["\"buff\""]
			if ENABLE_RESIST == True and case < MAX_SCHEME_BUFFS:
				count += 1
				buffTypes += ["\"resist\""]
			if ENABLE_SONGS == True and case2 < MAX_SCHEME_DANCES:
				count += 1
				buffTypes += ["\"song\""]
			if ENABLE_DANCES == True and case2 < MAX_SCHEME_DANCES:
				count += 1
				buffTypes += ["\"dance\""]
			if ENABLE_CHANTS == True and case < MAX_SCHEME_BUFFS:
				count += 1
				buffTypes += ["\"chant\""]
			if ENABLE_OTHERS == True and case < MAX_SCHEME_BUFFS:
				count += 1
				buffTypes += ["\"others\""]
			if ENABLE_SPECIAL == True and case < MAX_SCHEME_BUFFS:
				count += 1
				buffTypes += ["\"special\""]
			while aa <= count :
				if aa == count : qry += buffTypes[aa-1]
				else : qry += buffTypes[aa-1]+","
				aa += 1
			return qry
		
		def viewAllSchemeBuffs(scheme,page,action) :
			def getBuffCount(scheme) :
				count = 0; D_S_Count = 0; B_Count = 0
				conn=L2DatabaseFactory.getInstance().getConnection()
				rss = conn.prepareStatement("SELECT * FROM buffer_scheme_contents WHERE scheme_id=\""+str(scheme)+"\"")
				action=rss.executeQuery()
				while (action.next()) :
					try : 
						val = action.getInt("buff_class")
						count += 1	
						if val == 1 or val == 2: D_S_Count += 1
						else: B_Count += 1			
					except : count = 0; D_S_Count = 0 ; B_Count = 0
				res = str(count) + " " + str(B_Count) + " " + str(D_S_Count)
				try : conn.close()
				except : pass		
				return res
			buffList = []
			conn=L2DatabaseFactory.getInstance().getConnection()
			count = 0; pc = 0; bll = 0; i = 0; buffsPerPage = 0; incPageCount = True; listOrder=""
			HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><br>"
			eventSplit = getBuffCount(scheme).split(" ")
			TOTAL_BUFF = int(eventSplit[0]); BUFF_COUNT = int(eventSplit[1]); DANCE_SONG = int(eventSplit[2])
			if action == "add" :
				HTML_MESSAGE += "You can add <font color=\"LEVEL\">"+str(MAX_SCHEME_BUFFS - BUFF_COUNT)+"</font> Buffs and <font color=\"LEVEL\">"+str(MAX_SCHEME_DANCES - DANCE_SONG)+"</font> Dances more!"
				QUERY = "SELECT * FROM buffer_buff_list WHERE buffType IN ("+ generateQuery(BUFF_COUNT,DANCE_SONG) + ") AND canUse=1 ORDER BY Buff_Class ASC, id"
			if action == "remove" :
				HTML_MESSAGE += "You have <font color=\"LEVEL\">"+str(BUFF_COUNT)+"</font> Buffs and <font color=\"LEVEL\">"+str(DANCE_SONG)+"</font> Dances"
				QUERY = "SELECT * FROM buffer_scheme_contents WHERE scheme_id="+str(scheme)+" ORDER BY Buff_Class ASC, id"				
			getBuffCount = conn.prepareStatement(QUERY)
			rss = getBuffCount.executeQuery()
			while (rss.next()) :
				try :
					if action == "add" :
						name = SkillTable.getInstance().getInfo(rss.getInt("buffId"),rss.getInt("buffLevel")).getName()
						name = name.replace(" ","+")
						buffList += [name+"_"+str(rss.getInt("buffId"))+"_"+str(rss.getInt("buffLevel"))+"_"+str(page)]
					if action == "remove" :
						name = SkillTable.getInstance().getInfo(rss.getInt("skill_id"),rss.getInt("skill_level")).getName()
						name = name.replace(" ","+")
						buffList += [name+"_"+str(rss.getInt("skill_id"))+"_"+str(rss.getInt("skill_level"))+"_"+str(page)]						
					count = count + 1
				except :
					buffList = []
					count = 0
			try : conn.close()
			except : pass
			HTML_MESSAGE += "<table border=\"0\"><tr>"
			buffsPerPage = 20
			while incPageCount == True: # generating page count
				if count < buffsPerPage : incPageCount = False
				else : count = count - buffsPerPage 
				pc += 1 
			ii = 1
			while ii <= pc :
				if pc > 5 :
					width = "25"
					pageName = "P"
				else :
					width = "50"
					pageName = "Page "
				if action == "add" : HTML_MESSAGE += "<td width=\""+width+"\"><button value=\""+pageName+""+str(ii)+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " manage_scheme_1 "+str(scheme)+" "+str(ii)+" x\" width=51 height=21 back=\"botaoes1.s12_over\" fore=\"botaoes1.s12\"></td>"
				if action == "remove" : HTML_MESSAGE += "<td width=\""+width+"\"><button value=\""+pageName+""+str(ii)+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " manage_scheme_2 "+str(scheme)+" "+str(ii)+" x\" width=51 height=21 back=\"botaoes1.s12_over\" fore=\"botaoes1.s12\"></td>"					
				ii += 1
			HTML_MESSAGE += "</tr></table>"
			value = ""; bll = len(buffList); j = 0; k=0
			if buffsPerPage*int(page) > bll : j = bll
			else : j = buffsPerPage*int(page)
			i = buffsPerPage*int(page)-buffsPerPage
			while i < j :
				value = buffList[i]
				value = value.replace("_"," ")
				extr = value.split(" ")
				name = extr[0]
				name = name.replace("+"," ")
				id = int(extr[1])
				level = extr[2]
				page = int(extr[3])
				if id < 100 : format = "00"+str(id)
				elif id > 99 and id < 1000 : format = "0"+str(id)
				else :
					if id > 4698 and id < 4701 : format = "1331"
					elif id > 4701 and id < 4704 : format = "1332"
					else: format = str(id)
				if action == "add":
					if isUsed(scheme,id,level) == False:
						if k % 2 != 0 : HTML_MESSAGE += "<table border=\"0\" bgcolor=FFF500>"
						else : HTML_MESSAGE += "<table border=\"0\" bgcolor=000000>"
						HTML_MESSAGE += "<tr><td width=\"35\"><img src=\"Icon.skill"+format+"\" width=32 height=32></td><td width=\"170\">"+name+"</td><td><button value=\"Add\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" add_buff "+str(scheme)+"_"+str(id)+"_"+str(level)+" "+str(page)+" "+str(TOTAL_BUFF)+"\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td>"
						HTML_MESSAGE += "</tr></table>"; k+=1
				if action == "remove":
					if k % 2 != 0 : HTML_MESSAGE += "<table border=\"0\" bgcolor=FFF500>"
					else : HTML_MESSAGE += "<table border=\"0\" bgcolor=000000>"
					HTML_MESSAGE += "<tr><td width=\"35\"><img src=\"Icon.skill"+format+"\" width=32 height=32></td><td width=\"170\">"+name+"</td><td><button value=\"Remove\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" remove_buff "+str(scheme)+"_"+str(id)+"_"+str(level)+" "+str(page)+" "+str(TOTAL_BUFF)+"\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td>"
					HTML_MESSAGE += "</table>"; k+=1
				i += 1
			HTML_MESSAGE += "<br><br><button value=\"Back\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" manage_scheme_select "+str(scheme)+" x x\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML_MESSAGE += "<button value=\"Home\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"				
			HTML_MESSAGE += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML_MESSAGE

		def viewAllBuffTypes() :
			HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>"
			HTML_MESSAGE += "<font color=\"LEVEL\">[Buff management]</font><br>"
			if ENABLE_BUFFS == True :
				HTML_MESSAGE += "<button value=\"Buffs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list buff Buffs 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_RESIST == True :
				HTML_MESSAGE += "<button value=\"Resist Buffs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list resist Resists 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
                        if ENABLE_SONGS == True :
				HTML_MESSAGE += "<button value=\"Songs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list song Songs 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_DANCES == True :
				HTML_MESSAGE += "<button value=\"Dances\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list dance Dances 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_CHANTS == True :
				HTML_MESSAGE += "<button value=\"Chants\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list chant Chants 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_SPECIAL == True :
				HTML_MESSAGE += "<button value=\"Special Buffs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list special Special_Buffs 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_OTHERS == True :
				HTML_MESSAGE += "<button value=\"Others Buffs\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list others Others_Buffs 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_CUBIC == True :
				HTML_MESSAGE += "<button value=\"Cubics\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list cubic cubic_Buffs 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\">"
			if ENABLE_BUFF_SET == True :
				HTML_MESSAGE += "<button value=\"Buff Sets\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list set Buff_Sets 1\" width=203 height=21 back=\"botaoes1.s08_over\" fore=\"botaoes1.s08\"><br>"			
			HTML_MESSAGE += "<button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML_MESSAGE += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML_MESSAGE
		
		def viewAllBuffs(type,typeName,page) :
			buffList = []
			conn=L2DatabaseFactory.getInstance().getConnection()
			count = 0; pc = 0; bll = 0; i = 0; buffsPerPage = 0; formula = 0 ; incPageCount = True ; listOrder=""
			HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>"
			typeName = typeName.replace("_"," ")
			if type == "set" : QUERY = "SELECT * FROM buffer_buff_list WHERE buffType IN ("+generateQuery(0,0)+") AND canUse=1"
			else : QUERY = "SELECT * FROM buffer_buff_list WHERE buffType=\""+type+"\""
			getBuffCount = conn.prepareStatement(QUERY)
			rss = getBuffCount.executeQuery()
			while (rss.next()) :
				try :	
					name = SkillTable.getInstance().getInfo(rss.getInt("buffId"),rss.getInt("buffLevel")).getName()
					name = name.replace(" ","+")
					usable = rss.getString("canUse")
					forClass = rss.getString("forClass")
					skill_id = rss.getString("buffId")
					skill_level = rss.getString("buffLevel")
					buffList += [name+"_"+forClass+"_"+str(page)+"_"+usable+"_"+skill_id+"_"+skill_level]
					count = count + 1
				except :
					buffList = []
					count = 0
			try : conn.close()
			except : pass
			buffList.sort()
			HTML_MESSAGE += "<font color=\"LEVEL\">[Buff management - "+typeName+" - Page "+str(page)+"]</font><br><table border=\"0\"><tr>"
			if type == "set" : buffsPerPage = 12
			else : buffsPerPage = 20
			while incPageCount == True:
				if count < buffsPerPage :  incPageCount = False
				else : count -= buffsPerPage 
				pc += 1
			ii = 1
			typeName = typeName.replace(" ","_")
			while ii <= pc :
				if pc > 5 :
					width = "25"
					pageName = "P"
				else :
					width = "50"
					pageName = "Page "
				HTML_MESSAGE += "<td width=\""+width+"\"><button value=\""+pageName+""+str(ii)+"\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " edit_buff_list "+type+" "+typeName+" "+str(ii)+"\" width="+width+" height=21 back=\"botaoes1.s12_over\" fore=\"botaoes1.s12\"></td>"
				ii += 1
			HTML_MESSAGE += "</tr></table><br>"
			value = ""; bll = len(buffList); j = 0
			if buffsPerPage*int(page) > bll : j = bll
			else : j = buffsPerPage*int(page)
			i = buffsPerPage*int(page)-buffsPerPage
			while i < j :
				value = buffList[i]
				value = value.replace("_"," ")
				extr = value.split(" ")
				name = extr[0]
				name = name.replace("+"," ")
				forClass = int(extr[1])
				page = extr[2]
				usable = int(extr[3])
				skillPos = extr[4]+"_"+extr[5]
				if i % 2 != 0 : HTML_MESSAGE += "<table border=\"0\" bgcolor=FFF500>"
				else : HTML_MESSAGE += "<table border=\"0\" bgcolor=000000>"
				if type == "set" :
					if forClass == 0 :
						listOrder="List=\"Fighter;Mage;All;None;\""
					if forClass == 1 :
						listOrder="List=\"Mage;Fighter;All;None;\""
					if forClass == 2 :
						listOrder="List=\"All;Fighter;Mage;None;\""
					if forClass == 3 :
						listOrder="List=\"None;Fighter;Mage;All;\""	
					HTML_MESSAGE += "<tr><td width=\"145\">"+name+"</td><td width=\"70\"><combobox var=\"newSet"+str(i)+"\" width=70 "+listOrder+"></td>"
					HTML_MESSAGE += "<td width=\"50\"><button value=\"Update\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " changeBuffSet "+str(skillPos)+" $newSet"+str(i)+" "+page+"\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td></tr>"
				else :
					HTML_MESSAGE += "<tr><td width=\"170\">"+name+"</td><td width=\"80\">"
					if usable == 1 : HTML_MESSAGE += "<button value=\"Disable\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " editSelectedBuff "+skillPos+" 0-"+page+" "+type+"\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td></tr>"
					elif usable == 0 : HTML_MESSAGE += "<button value=\"Enable\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " editSelectedBuff "+skillPos+" 1-"+page+" "+type+"\" width=74 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\"></td></tr>"
				HTML_MESSAGE += "</table>"
				i += 1
			HTML_MESSAGE += "<br><br><button value=\"Back\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect manage_buffs 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML_MESSAGE += "<button value=\"Home\" action=\"bypass -h Quest " + QUEST_LOADING_INFO + " redirect main 0 0\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"				
			HTML_MESSAGE += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML_MESSAGE	
			
		def manageSelectedBuff(buffPosId,canUseBuff) :
			bpid = buffPosId.split("_")
			bId= bpid[0]
			bLvl= bpid[1]
			conn=L2DatabaseFactory.getInstance().getConnection()
			upd=conn.prepareStatement("UPDATE buffer_buff_list SET canUse=\""+canUseBuff+"\" WHERE buffId=\""+str(bId)+"\" AND buffLevel=\""+str(bLvl)+"\" LIMIT 1")
			try :
				upd.executeUpdate()
				upd.close()
				conn.close()
			except :
				try : conn.close()
				except : pass
				
		def manageSelectedSet(id,newVal,opt3) :
			bpid = id.split("_")
			bId= bpid[0]
			bLvl= bpid[1]		
			conn=L2DatabaseFactory.getInstance().getConnection()
			upd=conn.prepareStatement("UPDATE buffer_buff_list SET forClass=? WHERE buffId=? AND bufflevel=?")
			upd.setString(1, newVal)
			upd.setString(2, str(bId))
			upd.setString(3, str(bLvl))
			try :
				upd.executeUpdate()
				upd.close()
				conn.close()
			except :
				try : conn.close()
				except : pass
			return viewAllBuffs("set","Buff Sets",str(opt3))											
										
		def addTimeout(gaugeColor,amount,offset) :
			endtime = int((System.currentTimeMillis() + (amount * 1000))/1000)
			st.set("blockUntilTime",str(endtime))
			st.getPlayer().sendPacket(SetupGauge(gaugeColor, amount * 1000 + offset))	
			
		def heal(case) :
			if case == 0:
				st.getPlayer().getStatus().setCurrentHp(st.getPlayer().getStat().getMaxHp())
				st.getPlayer().getStatus().setCurrentMp(st.getPlayer().getStat().getMaxMp())
				st.getPlayer().getStatus().setCurrentCp(st.getPlayer().getStat().getMaxCp())
			if case == 1 and st.player.getPet() != None :
				st.player.getPet().getStatus().setCurrentHp(st.player.getPet().getStat().getMaxHp())
				st.player.getPet().getStatus().setCurrentMp(st.player.getPet().getStat().getMaxMp())
				try:
					st.player.getPet().setCurrentFed(st.player.getPet().getMaxFed())
					st.player.sendPacket(SetSummonRemainTime(st.player.getPet().getMaxFed(), st.player.getPet().getCurrentFed()))
				except: 
					try: 
						st.player.getPet().decTimeRemaining(st.player.getPet().getTimeRemaining() - st.player.getPet().getTotalLifeTime())
						st.player.sendPacket(SetSummonRemainTime(st.player.getPet().getTotalLifeTime(), st.player.getPet().getTimeRemaining()))
					except: pass
		eventSplit = event.split(" ")
		event = eventSplit[0]
		eventParam1 = eventSplit[1]
		eventParam2 = eventSplit[2]
		eventParam3 = eventSplit[3]

		if event == "reloadscript":
			if eventParam1 == "1": return ReloadConfig(st)
			if eventParam1 == "0": return rebuildMainHtml(st)

		if event == "redirect" :
			if eventParam1 == "main" : return rebuildMainHtml(st)
			if eventParam1 == "manage_buffs" : return viewAllBuffTypes()

		if event == "buffpet" :
			if int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime") :
				st.set("Pet-On-Off",eventParam1)
				if TIME_OUT == True: addTimeout(3,TIME_OUT_TIME/2,600)
			return rebuildMainHtml(st)
		
		if event == "create" :
			con=L2DatabaseFactory.getInstance().getConnection()
			param = eventParam1.replace("."," ")
			if param == "no_name" :
				return showText(st,"Info","Por favor, insira o nome do esquema!","True","Return","main")
			else :
				ins = con.prepareStatement("INSERT INTO buffer_scheme_list (player_id,scheme_name) VALUES (?,?)")
				ins.setString(1, str(st.player.getObjectId()))
				ins.setString(2, param)
				try :
					ins.executeUpdate()
					ins.close()
					con.close()
				except : pass
			return rebuildMainHtml(st)
			
		if event == "delete" :
			conn=L2DatabaseFactory.getInstance().getConnection()
			rem=conn.prepareStatement("DELETE FROM buffer_scheme_list WHERE id=? LIMIT 1")
			rem.setString(1, eventParam1)
			try : rem.executeUpdate()
			except : pass
			rem=conn.prepareStatement("DELETE FROM buffer_scheme_contents WHERE scheme_id=?")
			rem.setString(1, eventParam1)
			try :
				rem.executeUpdate()
				rem.close()
				conn.close()
			except :
				try : conn.close()
				except : pass		
			return rebuildMainHtml(st)
		
		if event == "delete_c" :
			HTML = HTML_MESSAGE = "<html><head><title>"+TITLE_NAME+"</title></head><body><center><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32><br>Voce realmente quer apagar '"+eventParam2+"' scheme?<br><br>"
			HTML += "<button value=\"Yes\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" delete "+eventParam1+" x x\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"
			HTML += "<button value=\"No\" action=\"bypass -h Quest "+QUEST_LOADING_INFO+" delete_1 x x x\" width=60 height=21 back=\"L2UI_CH3.Btn1_normalOn\" fore=\"L2UI_CH3.Btn1_normal\">"				
			HTML += "<br><font color=\"303030\">"+TITLE_NAME+"</font></center></body></html>"
			return HTML			
		
		if event == "create_1" : return createScheme()
			
		if event == "edit_1" : return editScheme()
		
		if event == "delete_1" : return deleteScheme()
		
		if event == "manage_scheme_1" : return viewAllSchemeBuffs(eventParam1,eventParam2,"add")

		if event == "manage_scheme_2" : return viewAllSchemeBuffs(eventParam1,eventParam2,"remove")
			
		if event == "manage_scheme_select" : return getOptionList(eventParam1)
		
		if event == "remove_buff" :
			event = eventParam1.split("_")
			scheme = event[0]
			skill = event[1]
			level = event[2]
			con=L2DatabaseFactory.getInstance().getConnection()
			rem=con.prepareStatement("DELETE FROM buffer_scheme_contents WHERE scheme_id=? AND skill_id=? AND skill_level=? LIMIT 1")
			rem.setString(1, scheme)
			rem.setString(2, skill)
			rem.setString(3, level)
			try : rem.executeUpdate()
			except : pass
			temp=int(eventParam3) - 1
			if temp <= 0 : HTML = getOptionList(scheme)
			else : HTML = viewAllSchemeBuffs(scheme,eventParam2,"remove")
			return HTML
			
		if event == "add_buff" :
			event = eventParam1.split("_")
			scheme = event[0]
			skill = event[1]
			level = event[2]
			idbuffclass = getclassbuff(skill)
			con=L2DatabaseFactory.getInstance().getConnection()
			ins = con.prepareStatement("INSERT INTO buffer_scheme_contents (scheme_id,skill_id,skill_level,buff_class) VALUES (?,?,?,?)")
			ins.setString(1, str(scheme))
			ins.setString(2, str(skill))
			ins.setString(3, str(level))
			ins.setString(4, str(idbuffclass))
			try :
				ins.executeUpdate()
				ins.close()
				con.close()
			except : pass
			temp = int(eventParam3) + 1	
			if temp >= MAX_SCHEME_BUFFS + MAX_SCHEME_DANCES : HTML = getOptionList(scheme)
			else : HTML = viewAllSchemeBuffs(scheme,eventParam2,"add")
			return HTML
		
		if event == "edit_buff_list" :
			return viewAllBuffs(eventParam1,eventParam2,eventParam3)
		
		if event == "changeBuffSet" :
			eventParam2 = eventParam2.replace("Fighter","0")
			eventParam2 = eventParam2.replace("Mage","1")
			eventParam2 = eventParam2.replace("All","2")
			eventParam2 = eventParam2.replace("None","3")
			return manageSelectedSet(eventParam1,eventParam2,eventParam3)
				
		if event == "editSelectedBuff" :
			eventParam2 = eventParam2.replace("-"," ")
			split = eventParam2.split(" ")
			action = split[0]
			page = split[1]		
			manageSelectedBuff(eventParam1,action)
			if eventParam3 == "buff" : typeName = "Buffs"
                        if eventParam3 == "resist" : typeName = "Resists"
			if eventParam3 == "song" : typeName = "Songs"
			if eventParam3 == "dance" : typeName = "Dances"
			if eventParam3 == "chant" : typeName = "Chants"
			if eventParam3 == "others" : typeName = "Others_Buffs"
			if eventParam3 == "special" : typeName = "Special_Buffs"
			if eventParam3 == "cubic" : typeName = "Cubics"
			return viewAllBuffs(eventParam3,typeName,page)
				
		if event == "viewSelectedConfig" : return viewSelectedConfig(eventParam1,eventParam2)
					
		if event == "changeConfig" : return updateConfigValue(eventParam1,eventParam2,eventParam3)
		
		if event == "redirect" :
			if eventParam1 == "view_buffs" : return buildHtml("buff")
                        if eventParam1 == "view_resists" : return buildHtml("resist")
			if eventParam1 == "view_songs" : return buildHtml("song")
			if eventParam1 == "view_dances" : return buildHtml("dance")
			if eventParam1 == "view_chants" : return buildHtml("chant")
			if eventParam1 == "view_others" : return buildHtml("others")
			if eventParam1 == "view_special" : return buildHtml("special")
			if eventParam1 == "view_cubic" : return buildHtml("cubic")

		if event == "heal" :
			if int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime"):
				if st.getQuestItemsCount(CONSUMABLE_ID) < HEAL_PRICE  : 
					return showText(st,"Desculpe","Voce nao tem os elementos suficientes:<br>Voce precisa: <font color =\"LEVEL\">"+str(HEAL_PRICE)+" "+str(getitemname(st,CONSUMABLE_ID))+"!","False",0,0)
				else :
					if getpetbuff == 1 :
						if st.player.getPet() != None : heal(getpetbuff)
						else: return showText(st,"Info","Voce nao pode usar as opcoes do animal.<br>Chame o seu animal de estimacao primeiro!","False","Return","main")
					else : heal(getpetbuff)				
					st.takeItems(CONSUMABLE_ID,HEAL_PRICE)
					st.giveItems(CONSUMABLE_ID,BUFF_SET_PRICE)
					if TIME_OUT == True: addTimeout(1,TIME_OUT_TIME/2,600)
					return rebuildMainHtml(st)
			return rebuildMainHtml(st)
			
		if event == "removeBuffs" :
			if int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime"):						
				if st.getQuestItemsCount(CONSUMABLE_ID) < BUFF_REMOVE_PRICE : 
					return showText(st,"Desculpe","Voce nao tem os elementos suficientes:<br>Voce precisa: <font color =\"LEVEL\">"+str(BUFF_REMOVE_PRICE)+" "+str(getitemname(st,CONSUMABLE_ID))+"!","False",0,0)
				else :
					if getpetbuff == 1 :
						if st.player.getPet() != None : st.player.getPet().stopAllEffects()
						else: return showText(st,"Info","Voce n�o pode usar as opcoes do animal.<br>Chame o seu animal de estimacao primeiro!","False","Return","main")
					else :
						st.getPlayer().stopAllEffects()
                				if st.player.getCubics() != None:
                       					for cubic in st.player.getCubics().values():  
                            					cubic.stopAction() 
                            					st.player.delCubic(cubic.getId())   
					st.takeItems(CONSUMABLE_ID,BUFF_REMOVE_PRICE)
					st.giveItems(CONSUMABLE_ID,BUFF_SET_PRICE)
					if TIME_OUT == True: addTimeout(2,TIME_OUT_TIME/2,600)
					return rebuildMainHtml(st)
			return rebuildMainHtml(st)

		if event == "cast" :
			if int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime") :
				buffs = []; levels = []; id = 0; level = 0
				conn=L2DatabaseFactory.getInstance().getConnection()
				rss = conn.prepareStatement("SELECT * FROM buffer_scheme_contents WHERE scheme_id="+eventParam1+" ORDER BY id")
				action=rss.executeQuery()
				while (action.next()) :
					try :
						enabled = 1
						id = int(action.getString("skill_id"))
						level = int(action.getString("skill_level"))
						skillType = getBuffType(id)
						if skillType == "buff" :
							if ENABLE_BUFFS == True :
								if isEnabled(id,level) == "True" : 
									buffs += [id]
									levels += [level]
						if skillType == "resist" :
							if ENABLE_RESIST == True :
								if isEnabled(id,level) == "True" :
									buffs += [id]
									levels += [level]
						if skillType == "song" :
							if ENABLE_SONGS == True :
								if isEnabled(id,level) == "True" :
									buffs += [id]
									levels += [level]
						if skillType == "dance" :
							if ENABLE_DANCES == True :
								if isEnabled(id,level) == "True" :
									buffs += [id]
									levels += [level]
						if skillType == "chant" :
							if ENABLE_CHANTS == True :
								if isEnabled(id,level) == "True" :
									buffs += [id]
									levels += [level]
						if skillType == "others" :
							if ENABLE_OTHERS == True :
								if isEnabled(id,level) == "True" :
									buffs += [id]
									levels += [level]
						if skillType == "special" :
							if ENABLE_SPECIAL == True :
								if isEnabled(id,level) == "True" :
									buffs += [id]
									levels += [level]
					except : print "Query error!"
				try : conn.close()
				except : pass
					
				if len(buffs) == 0 : return viewAllSchemeBuffs(eventParam1,1,"add")
				else :
					if FREE_BUFFS == False :
						if st.getQuestItemsCount(CONSUMABLE_ID) < SCHEME_BUFF_PRICE : 
							return showText(st,"desculpe","Voce nao tem os elementos suficientes:<br>que voce precisa: <font color =\"LEVEL\">"+str(SCHEME_BUFF_PRICE)+" "+str(getitemname(st,CONSUMABLE_ID))+"!","False",0,0)
					i = 0
					while i <= len(buffs) - 1 :
						if getpetbuff == 0 : SkillTable.getInstance().getInfo(buffs[i],levels[i]).getEffects(st.player,st.player)
						else:
							if st.player.getPet() != None : SkillTable.getInstance().getInfo(buffs[i],levels[i]).getEffects(st.getPlayer().getPet(),st.getPlayer().getPet())
							else: return showText(st,"Info","Voce nao pode usar as opcoes do animal de estimacao.<br>Chame o seu animal de estimacao primeiro!","False","Return","main")
						i += 1
					heal(getpetbuff)
					st.takeItems(CONSUMABLE_ID,SCHEME_BUFF_PRICE)
					st.giveItems(CONSUMABLE_ID,BUFF_SET_PRICE)
					if TIME_OUT == True: addTimeout(3,TIME_OUT_TIME,600)
					return rebuildMainHtml(st)
			else : return rebuildMainHtml(st)

		if event == "giveBuffs" :
			if eventParam3 == "buff" : cost = BUFF_PRICE
			if eventParam3 == "resist" : cost = RESIST_PRICE
			if eventParam3 == "song" : cost = SONG_PRICE
			if eventParam3 == "dance" : cost = DANCE_PRICE
			if eventParam3 == "chant" : cost = CHANT_PRICE
			if eventParam3 == "others" : cost = OTHERS_PRICE
			if eventParam3 == "special" : cost = SPECIAL_PRICE	
			if eventParam3 == "cubic" : cost = CUBIC_PRICE			
			if int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime") :
				if FREE_BUFFS == False :
					if st.getQuestItemsCount(CONSUMABLE_ID) < cost :
						return showText(st,"desculpe","Voce nao tem os elementos suficientes:<br>que voce precisa: <font color =\"LEVEL\">"+str(cost)+" "+str(getitemname(st,CONSUMABLE_ID))+"!","False",0,0)
				skill=SkillTable.getInstance().getInfo(int(eventParam1),int(eventParam2))
				if str(skill.getSkillType()) == "SUMMON":
					if st.getQuestItemsCount(skill.getItemConsumeId()) < skill.getItemConsume():
						return showText(st,"desculpe","Voce nao tem os elementos suficientes:<br>que voce precisa: <font color =\"LEVEL\">"+str(skill.getItemConsume())+" "+str(getitemname(st,skill.getItemConsumeId()))+"!","False",0,0)
				if getpetbuff == 0 :
					if eventParam3 == "cubic" :
                				if st.player.getCubics() != None:
                       					for cubic in st.player.getCubics().values():  
                            					cubic.stopAction() 
                            					st.player.delCubic(cubic.getId())
						st.getPlayer().useMagic(SkillTable.getInstance().getInfo(int(eventParam1),int(eventParam2)),False,False)
					else: SkillTable.getInstance().getInfo(int(eventParam1),int(eventParam2)).getEffects(st.getPlayer(),st.getPlayer())
				else:
					if eventParam3 == "cubic": 
                				if st.player.getCubics() != None:
                       					for cubic in st.player.getCubics().values():  
                            					cubic.stopAction() 
                            					st.player.delCubic(cubic.getId())
						st.getPlayer().useMagic(SkillTable.getInstance().getInfo(int(eventParam1),int(eventParam2)),False,False)
					else: 
						if st.player.getPet() != None : SkillTable.getInstance().getInfo(int(eventParam1),int(eventParam2)).getEffects(st.getPlayer().getPet(),st.getPlayer().getPet())
						else: return showText(st,"Info","Voce nao pode usar as opcoes do animal de estimacao.<br>Chame o seu animal de estimacao primeiro!","False","Return","main")
				st.takeItems(CONSUMABLE_ID,cost)
				st.giveItems(CONSUMABLE_ID,BUFF_SET_PRICE)
				if TIME_OUT == True: addTimeout(3,TIME_OUT_TIME/10,600)
				return buildHtml(eventParam3)
			else : return buildHtml(eventParam3)
				
		if event == "castBuffSet" :
			if int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime") :
				if FREE_BUFFS == False :
					if st.getQuestItemsCount(CONSUMABLE_ID) < BUFF_SET_PRICE : 
						return showText(st,"desculpe","Voce nao tem os elementos suficientes:<br>que voce precisa: <font color =\"LEVEL\">"+str(BUFF_SET_PRICE)+" "+str(getitemname(st,CONSUMABLE_ID))+"!","False",0,0)
				buff_sets=[]; i = 0; player_class = 3
				if st.getPlayer().isMageClass() : player_class = 1
				else : player_class = 0
				if getpetbuff == 0 :
					conn=L2DatabaseFactory.getInstance().getConnection()
					getSimilarNameCount = conn.prepareStatement("SELECT buffId,buffLevel FROM buffer_buff_list WHERE forClass IN (?,?) ORDER BY id ASC")
					getSimilarNameCount.setString(1, str(player_class))
					getSimilarNameCount.setString(2, "2")
					rss = getSimilarNameCount.executeQuery()
					while (rss.next()) :
						try :
							id = rss.getInt("buffId")
							lvl = rss.getInt("buffLevel")
							buff_sets += [id,lvl]
						except : buff_sets = []
					try: conn.close()
					except: pass
					while i <= len(buff_sets)-2 :
						SkillTable.getInstance().getInfo(buff_sets[i],buff_sets[i+1]).getEffects(st.getPlayer(),st.getPlayer())
						i += 2
				else:
					if st.player.getPet() != None :
						i = 0
						conn=L2DatabaseFactory.getInstance().getConnection()
						getSimilarNameCount = conn.prepareStatement("SELECT buffId,buffLevel FROM buffer_buff_list WHERE forClass IN (?,?) ORDER BY id ASC")
						getSimilarNameCount.setString(1, "0")
						getSimilarNameCount.setString(2, "2")
						rss = getSimilarNameCount.executeQuery()
						while (rss.next()) :
							try :
								id = rss.getInt("buffId")
								lvl = rss.getInt("buffLevel")
								buff_sets += [id,lvl]
							except : buff_sets = []
						try: conn.close()
						except: pass
						while i <= len(buff_sets)-2 :
							SkillTable.getInstance().getInfo(buff_sets[i],buff_sets[i+1]).getEffects(st.getPlayer().getPet(),st.getPlayer().getPet())
							i += 2
					else: return showText(st,"Info","Voce nao pode usar as opcoes do animal de estimacao.<br>Chame o seu animal de estimacao primeiro!","False","Return","main")
				heal(getpetbuff)
				st.takeItems(CONSUMABLE_ID,BUFF_SET_PRICE)
				st.giveItems(CONSUMABLE_ID,BUFF_SET_PRICE)
				if TIME_OUT == True: addTimeout(3,TIME_OUT_TIME,600)
				return rebuildMainHtml(st)
			else : return rebuildMainHtml(st)
		return rebuildMainHtml(st)

	def onFirstTalk (self,npc,player):
		st = player.getQuestState(QUEST_LOADING_INFO)
		if not st : st = self.newQuestState(player)
		if player.isGM(): 
			if SCRIPT_RELOAD == True: return reloadPanel(st)
			else: return rebuildMainHtml(st)
		elif int(System.currentTimeMillis()/1000) > st.getInt("blockUntilTime"):

			if ENABLE_VIP_BUFFER == False or player.getAccessLevel().getLevel() == VIP_ACCESS_LEVEL and ENABLE_VIP_BUFFER == True:

				if BUFF_WITH_KARMA == False and player.getKarma() > 0 :
					return showText(st,"Info","Voce tem muito <font color=\"FF0000\">karma!</font><br>vir back,<br>quando voce nao tem nenhum karma!","False","Return","main")

				elif st.player.getLevel() < MIN_LEVEL :
					return showText(st,"Info","Seu n�vel � muito baixo!<br>Voce tem que ter pelo menos n�vel <font color\"LEVEL\">"+str(MIN_LEVEL)+"</font>,<br>para usar os meus servicos!","False","Return","main")
			
				elif st.player.getPvpFlag() > 0 :
					return showText(st,"Info","Voce nao pode buff enquanto voce esta nesta are <font color=\"800080\">flagged!</font><br>Espere algum tempo e tente novamente!","False","Return","main")

				elif st.player.isInCombat() :
					return showText(st,"Info","Voce nao pode buff enquanto voce esta atacando!<br>Pare de luta e tente novamente!","False","Return","main")

				else: return rebuildMainHtml(st)

			else: return showText(st,"desculpe","Este buffer e apenas para VIP!<br>Contacte o administrador para obter mais informacoes!","False","Return","main")	
	   	else: return showText(st,"desculpe","Voce tem que esperar um pouco!!<br>Se voce quiser usar o meu servico!","False","Return","main")

		
QUEST = Quest(QUEST_ID,QUEST_LOADING_INFO,QUEST_DESCRIPTION)
QUEST.addStartNpc(NPC_ID)
QUEST.addFirstTalkId(NPC_ID)
QUEST.addTalkId(NPC_ID)