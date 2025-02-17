from phBot import *
from threading import Timer
from threading import *
import threading
import struct
import QtBind
import time
import random
from time import sleep
import os
import json

pName = 'DungeonSupporter'
pVersion = '0.0.1'

# ______________________________ ' Initializing ' ______________________________ #

# Graphic user interface

gui = QtBind.init(__name__,pName)

FIXSOUNDPATH = 'c:\\Windows\\Media\\chimes.wav'
Alert = 0
Remaining = 0
AdvancedL = 0
IntermediateL = 0
BeginnerL = 0
Return = 0
MembersReturn = 0
WaitMaster = 0
Advanced_remaining = 5
Intermediate_remaining = 5
Beginner_remaining = 5
SilverCoin_gain = 0
elaman1 = 1
eleman2 = 2
SkipCommand = False
Finished_HWT = False
ReturnCommand = False
DodgeAttackBool = False
CheckPoint = False
timer = None
gofgw = False
Done = 0

MainMenu = QtBind.createList(gui,5,5,270,305)
lbl = QtBind.createLabel(gui,'<font color="red">---------------------------MainMenu----------------------------<font>',6,5)
Info = QtBind.createList(gui,280,5,200,150)
lbl = QtBind.createLabel(gui,'<font color="red"> ------------------Information------------------</font>',280,5)
Info = QtBind.createList(gui,485,5,236,305)
lbl = QtBind.createLabel(gui,'<font color="red"> -----------------------Conditions------------------------</font>',485,5)
HolyMolyEntrance = QtBind.createCheckBox(gui,'HolyMoly2_clicked','Holy Water Temple Entrance',10,19)
NoNPremium = QtBind.createCheckBox(gui,'NoNPremium_clicked','noN-Premium',170,19) 
first = QtBind.createCheckBox(gui,'first_clicked','1',170,60)
second = QtBind.createCheckBox(gui,'second_clicked','2',200,60) 
third = QtBind.createCheckBox(gui,'third_clicked','3',230,60) 
beginner1 = QtBind.createCheckBox(gui,'beginner1_clicked','1',175,80)
intermediate2 = QtBind.createCheckBox(gui,'intermediate2_clicked','2',205,80) 
advanced3 = QtBind.createCheckBox(gui,'advanced3_clicked','3',235,80) 
lbl = QtBind.createLabel(gui,'Başlamadan Önce           Parti Üyesinin Girmesini Bekle',10,40)
txtPartyMembers = QtBind.createLineEdit(gui,"8",100,35,25,20)
lbl = QtBind.createLabel(gui,'Hangi Yolu Tercih edeceğini seç',10,60)
lbl = QtBind.createLabel(gui,'Sadece Dönmek istediğin katı seç',10,80)
lbl = QtBind.createLabel(gui,'<font color="blue">#WeAreALLSTAR #NacyaFTW</font>',10,100)
cbxspinixref = QtBind.createCheckBox(gui,'spinixref_clicked','Sphinx Reflect Counter (Attack Radius)',10,160) 
txtRangeSphinx = QtBind.createLineEdit(gui,"30",220,158,27,20)
cbxSilverStop = QtBind.createCheckBox(gui,'cbxSilverStop_clicked','Stop Bot or Tracing if drop Silver Coin',10,180) 
cbxSilverCoin = QtBind.createCheckBox(gui,'scdrop_clicked','Silver Coin Alert',10,200)
cbxSafeWay = QtBind.createCheckBox(gui,'SafeWay_clicked','Radius Setting for attack (Attack Radius)',10,220)
txtRange = QtBind.createLineEdit(gui,"30",227,216,27,20)
lbl = QtBind.createLabel(gui,'Katı Tamamladıktan Sonra Return At',100,120)
returnfirst = QtBind.createCheckBox(gui,'returnfirst_clicked','1.',10,118)
returnsecond = QtBind.createCheckBox(gui,'returnsecond_clicked','2.',40,118) 
returnthird = QtBind.createCheckBox(gui,'returnthird_clicked','3.',70,118) 
cbxSafeWay2 = QtBind.createCheckBox(gui,'SafeWay2_clicked','Dodge Bridge (Attack Radius) ',10,140)
txtRange2 = QtBind.createLineEdit(gui,"30",172,135,27,20)
cbxIgnoreSphnix = QtBind.createCheckBox(gui,'ignoresphnix_clicked','Ignore Beginner Sphnix',10,240)
cbxNotrace = QtBind.createCheckBox(gui,'notrace_clicked','Stop trace after teleporting ',10,260)
cbxEnter = QtBind.createButton(gui,'ManuelEntrance_clicked','       Manuel Entrance       ',140,280)
cbxSave = QtBind.createButton(gui,'onSaveButtonClicked','		Save		',10,280)
lbl = QtBind.createLabel(gui,'Advanced Remaining Stage: ',285,20)
lblAdvanced = QtBind.createLabel(gui,"5",445,20)
lbl = QtBind.createLabel(gui,'Intermediate Remaining Stage: ',285,40)
lblIntermediate = QtBind.createLabel(gui,"5",445,40)
lbl = QtBind.createLabel(gui,'Beginner Remaining Stage: ',285,60)
lblBeginner = QtBind.createLabel(gui,"5",445,60)
cbxSilverCoinCounter = QtBind.createCheckBox(gui,'scdrop_clicked','Silver Coin Counter:',285,90)
lblSilver = QtBind.createLabel(gui,"0",401,92)
lbl = QtBind.createLabel(gui,'[ FGW ] Trace Master :',285,166)
txtFGWMASTER = QtBind.createLineEdit(gui,'',397,160,83,20)
lbl = QtBind.createLabel(gui,'[ HWT ] Trace Master :',285,196)
txtHWTMASTER = QtBind.createLineEdit(gui,'',397,190,83,20)

lbl = QtBind.createLabel(gui,'Main [ HWT ] Profile Name :',285,226)
txtHWTPROFILE = QtBind.createLineEdit(gui,'',420,220,60,20)
lbl = QtBind.createLabel(gui,'<font color="red">** Default Profile Name : [ HWT ] **<font>',285,240)

lbl = QtBind.createLabel(gui,'Main [ FGW ] Profile Name :',285,260)
txtCHANGEPROFILE = QtBind.createLineEdit(gui,'',420,254,60,20)
lbl = QtBind.createLabel(gui,'<font color="blue">** Default Profile Name : [ FGW ] **<font>',285,274)

cbxChangeProfile = QtBind.createCheckBox(gui,'changeprofile_clicked','Change Profile ',285,110)

cbxDisabledEventLoop = QtBind.createCheckBox(gui,'disabled_checked','Disabled Plugin ',610,19)

cbxLogMessage = QtBind.createCheckBox(gui, 'logMessage_checked','Log Inject Message',285,130)
logMessage = False
def logMessage_checked(checked):
	global logMessage
	logMessage = checked

uids = set()

#----------------------------------------------Conditions------------------------------------------------#

cbxEnabledConditions = QtBind.createCheckBox(gui,'enabled_checked','Enabled Conditions',490,19)
cbxTrace = QtBind.createCheckBox(gui,'trace_clicked','[ Trace the Party Master ]',500,40)
lbl = QtBind.createLabel(gui,'<font color="red">[ ALL ]<font>',683,42)
cbxStart = QtBind.createCheckBox(gui,'start_clicked','[ Start Bot in Town ]',500,60)
lbl = QtBind.createLabel(gui,'<font color="red">[ HWT ]<font>',683,62)
cbxResetRadius = QtBind.createCheckBox(gui,'ResetRadius_clicked','[ Reset Training Area Radius ]',500,80)
lbl = QtBind.createLabel(gui,'<font color="red">[ HWT ]<font>',683,82)
cbxEntranceON = QtBind.createCheckBox(gui,'EntranceON_clicked','[ Auto Active Holy Water Temple ]',500,100)
lbl = QtBind.createLabel(gui,'<font color="red">[ HWT ]<font>',683,102)

#----------------------------------------------Load Configs------------------------------------------------#

def saveConfigs():
	# Save if data has been loaded
	if isJoined():
		# Save all data
		data = {}

		data['notrace'] = QtBind.isChecked(gui,cbxNotrace)
		data['reflect'] = QtBind.isChecked(gui,cbxspinixref)
		data["silvercoin"] = QtBind.isChecked(gui,cbxSilverCoin)
		data["ignoresph"] = QtBind.isChecked(gui,cbxIgnoreSphnix)
		data["ignoreNav"] = QtBind.isChecked(gui,cbxSafeWay)
		data["ignoreNav2"] = QtBind.isChecked(gui,cbxSafeWay2)
		data["first"] = QtBind.isChecked(gui,first)
		data["second"] = QtBind.isChecked(gui,second)
		data["third"] = QtBind.isChecked(gui,third)
		data["returnfirst"] = QtBind.isChecked(gui,returnfirst)
		data["returnsecond"] = QtBind.isChecked(gui,returnsecond)
		data["returnthird"] = QtBind.isChecked(gui,returnthird)
		data["NoNPremium"] = QtBind.isChecked(gui,NoNPremium)
		data["silverstop"] = QtBind.isChecked(gui,cbxSilverStop)
		data["silvercounter"] = QtBind.isChecked(gui,cbxSilverCoinCounter)
		data["changeprofile"] = QtBind.isChecked(gui,cbxChangeProfile)
		data["PartyMembers"] = QtBind.text(gui,txtPartyMembers)
		data["RangeSphinx"] = QtBind.text(gui,txtRangeSphinx)
		data["Range"] = QtBind.text(gui,txtRange)
		data["Range2"] = QtBind.text(gui,txtRange2)
		data["fgwmaster"] = QtBind.text(gui,txtFGWMASTER)
		data["hwtmaster"] = QtBind.text(gui,txtHWTMASTER)
		data["hwtprofile"] = QtBind.text(gui,txtHWTPROFILE)
		data["fgwprofile"] = QtBind.text(gui,txtCHANGEPROFILE)
		#------------------------Conditions-----------------------#

		data['Enabled'] = QtBind.isChecked(gui,cbxEnabledConditions)
		data['trace'] = QtBind.isChecked(gui,cbxTrace)
		data["start"] = QtBind.isChecked(gui,cbxStart)
		data["EntranceON"] = QtBind.isChecked(gui,cbxEntranceON)
		data["ResetRadius"] = QtBind.isChecked(gui,cbxResetRadius)

		#------------------------Conditions-----------------------#

		# Overrides
		with open(getConfig(),"w") as f:
			f.write(json.dumps(data, indent=4, sort_keys=True))

# Return xInjectLeader folder path
def getPath():
	return get_config_dir()+pName+"\\"

def connected():
	global inGame
	inGame = None

# Return character configs path (JSON)
def getConfig():
	return getPath()+inGame['server'] + "_" + inGame['name'] + ".json"

# Check if character is ingame
def isJoined():
	global inGame
	inGame = get_character_data()
	if not (inGame and "name" in inGame and inGame["name"]):
		inGame = None
	return inGame

# Load default configs
def loadDefaultConfig():
	# Clear data
	QtBind.setChecked(gui,cbxNotrace,False)
	QtBind.setChecked(gui,cbxspinixref,False)
	QtBind.setChecked(gui,cbxSilverCoin,False)
	QtBind.setChecked(gui,cbxIgnoreSphnix,False)
	QtBind.setChecked(gui,cbxSafeWay,False)
	QtBind.setChecked(gui,cbxSafeWay2,False)
	QtBind.setChecked(gui,first,False)
	QtBind.setChecked(gui,second,False)
	QtBind.setChecked(gui,third,False)
	QtBind.setChecked(gui,returnfirst,False)
	QtBind.setChecked(gui,returnsecond,False)
	QtBind.setChecked(gui,returnthird,False)
	QtBind.setChecked(gui,NoNPremium,False)
	QtBind.setChecked(gui,cbxSilverStop,False)
	QtBind.setChecked(gui,cbxSilverCoinCounter,False)
	QtBind.setChecked(gui,cbxChangeProfile,False)
	#------------------------Conditions-----------------------#

	QtBind.setChecked(gui,cbxEnabledConditions,False)
	QtBind.setChecked(gui,cbxStart,False)
	QtBind.setChecked(gui,cbxTrace,False)
	QtBind.setChecked(gui,cbxEntranceON,False)
	QtBind.setChecked(gui,cbxResetRadius,False)

	#------------------------Conditions-----------------------#
# Loads all config previously saved
def loadConfigs():
	loadDefaultConfig()
	if isJoined():
		# Check config exists to load
		if os.path.exists(getConfig()):
			data = {}
			with open(getConfig(),"r") as f:
				data = json.load(f)
			if 'notrace' in data and data['notrace']:
				QtBind.setChecked(gui,cbxNotrace,True)
			if 'reflect' in data and data['reflect']:
				QtBind.setChecked(gui,cbxspinixref,True)
			if 'ignoresph' in data and data['ignoresph']:
				QtBind.setChecked(gui,cbxIgnoreSphnix,True)
			if 'silvercoin' in data and data['silvercoin']:
				QtBind.setChecked(gui,cbxSilverCoin,True)
			if 'ignoreNav' in data and data['ignoreNav']:
				QtBind.setChecked(gui,cbxSafeWay,True)
			if 'ignoreNav2' in data and data['ignoreNav2']:
				QtBind.setChecked(gui,cbxSafeWay2,True)
			if 'first' in data and data['first']:
				QtBind.setChecked(gui,first,True)
			if 'second' in data and data['second']:
				QtBind.setChecked(gui,second,True)
			if 'third' in data and data['third']:
				QtBind.setChecked(gui,third,True)
			if 'returnfirst' in data and data['returnfirst']:
				QtBind.setChecked(gui,returnfirst,True)
			if 'returnsecond' in data and data['returnsecond']:
				QtBind.setChecked(gui,returnsecond,True)
			if 'returnthird' in data and data['returnthird']:
				QtBind.setChecked(gui,returnthird,True)
			if 'NoNPremium' in data and data['NoNPremium']:
				QtBind.setChecked(gui,NoNPremium,True)
			if 'silverstop' in data and data['silverstop']:
				QtBind.setChecked(gui,cbxSilverStop,True)
			if 'silvercounter' in data and data['silvercounter']:
				QtBind.setChecked(gui,cbxSilverCoinCounter,True)
			if 'changeprofile' in data and data['changeprofile']:
				QtBind.setChecked(gui,cbxChangeProfile,True)
			if 'PartyMembers' in data and data['PartyMembers']:
				QtBind.setText(gui,txtPartyMembers,str(data["PartyMembers"]))
			if 'RangeSphinx' in data and data['RangeSphinx']:
				QtBind.setText(gui,txtRangeSphinx,str(data["RangeSphinx"]))
			if 'Range' in data and data['Range']:
				QtBind.setText(gui,txtRange,str(data["Range"]))
			if 'Range2' in data and data['Range2']:
				QtBind.setText(gui,txtRange2,str(data["Range2"]))
			if 'fgwmaster' in data and data['fgwmaster']:
				QtBind.setText(gui,txtFGWMASTER,str(data["fgwmaster"]))
			if 'hwtmaster' in data and data['hwtmaster']:
				QtBind.setText(gui,txtHWTMASTER,str(data["hwtmaster"]))
			if 'hwtprofile' in data and data['hwtprofile']:
				QtBind.setText(gui,txtHWTPROFILE,str(data["hwtprofile"]))
			if 'fgwprofile' in data and data['fgwprofile']:
				QtBind.setText(gui,txtCHANGEPROFILE,str(data["fgwprofile"]))
			#------------------------Conditions-----------------------#
   
			if 'Enabled' in data and data['Enabled']:
				QtBind.setChecked(gui,cbxEnabledConditions,True)
			if 'trace' in data and data['trace']:
				QtBind.setChecked(gui,cbxTrace,True)
			if 'start' in data and data['start']:
				QtBind.setChecked(gui,cbxStart,True)
			if 'EntranceON' in data and data['EntranceON']:
				QtBind.setChecked(gui,cbxEntranceON,True)
			if 'ResetRadius' in data and data['ResetRadius']:
				QtBind.setChecked(gui,cbxResetRadius,True)

			#------------------------Conditions-----------------------#

#----------------------------------------------Load Configs------------------------------------------------#

def first_clicked(checked):
	QtBind.setChecked(gui,second,False)
	QtBind.setChecked(gui,third,False)
	QtBind.setChecked(gui,beginner1,False)
	QtBind.setChecked(gui,intermediate2,False)
	QtBind.setChecked(gui,advanced3,False)
	if QtBind.isChecked(gui,first) :
		if logMessage :						
			log('Plugin: First path (1) : [ Beginner,Intermediate,Advanced ]')
	else:
		if logMessage :
			log('Plugin: No path was chosen. You have to choose a way.')
def beginner1_clicked(checked):
	QtBind.setChecked(gui,first,False)
	QtBind.setChecked(gui,second,False)
	QtBind.setChecked(gui,third,False)
	QtBind.setChecked(gui,intermediate2,False)
	QtBind.setChecked(gui,advanced3,False)
	if QtBind.isChecked(gui,beginner1) :
		if logMessage :
			log('Plugin: One way Beginner ')
	else:
		if logMessage :
			log('Plugin: No path was chosen. You have to choose a way.')
def intermediate2_clicked(checked):
	QtBind.setChecked(gui,first,False)
	QtBind.setChecked(gui,second,False)
	QtBind.setChecked(gui,third,False)
	QtBind.setChecked(gui,beginner1,False)
	QtBind.setChecked(gui,advanced3,False)
	if QtBind.isChecked(gui,intermediate2) :
		if logMessage :
			log('Plugin: One way Intermediate ')
	else:
		if logMessage :
			log('Plugin: No path was chosen. You have to choose a way.')
def advanced3_clicked(checked):
	QtBind.setChecked(gui,first,False)
	QtBind.setChecked(gui,second,False)
	QtBind.setChecked(gui,third,False)
	QtBind.setChecked(gui,intermediate2,False)
	QtBind.setChecked(gui,beginner1,False)
	if QtBind.isChecked(gui,advanced3) :
		if logMessage :
			log('Plugin: One way Advanced')
	else:
		if logMessage :
			log('Plugin: No path was chosen. You have to choose a way.')
def second_clicked(checked):
	QtBind.setChecked(gui,first,False)
	QtBind.setChecked(gui,third,False)
	QtBind.setChecked(gui,beginner1,False)
	QtBind.setChecked(gui,intermediate2,False)
	QtBind.setChecked(gui,advanced3,False)
	if QtBind.isChecked(gui,second) :
		if logMessage :
			log('Plugin: Second path (2) : [ Intermediate,Advanced,Beginner ]')
	else:
		if logMessage :
			log('Plugin: No path was chosen. You have to choose a way.')
def third_clicked(checked):
	QtBind.setChecked(gui,first,False)
	QtBind.setChecked(gui,second,False)
	QtBind.setChecked(gui,beginner1,False)
	QtBind.setChecked(gui,intermediate2,False)
	QtBind.setChecked(gui,advanced3,False)
	if QtBind.isChecked(gui,third) :
		if logMessage :
			log('Plugin: Third path (3) : [ Advanced,Intermediate,Beginner ]')
	else:
		if logMessage :
			log('Plugin: No path was chosen. You have to choose a way.')

def returnfirst_clicked(checked):
	QtBind.setChecked(gui,returnthird,False)
	QtBind.setChecked(gui,returnsecond,False)
def returnsecond_clicked(checked):
	QtBind.setChecked(gui,returnfirst,False)
	QtBind.setChecked(gui,returnthird,False)
def returnthird_clicked(checked):
	QtBind.setChecked(gui,returnfirst,False)
	QtBind.setChecked(gui,returnsecond,False)

def LeaderSelection():
	count = party_count()
	getpartys = get_party()
	name = get_character_data()['name']
	if getpartys and count >= 2 :
		for oyuncu_id, oyuncu_verisi in getpartys.items():
			if oyuncu_verisi['leader'] == True :
				if oyuncu_verisi['name'] == name :
					return True
				else :
					return False

def LeaderName():
	getpartys = get_party()
	if getpartys :
		for oyuncu_id, oyuncu_verisi in getpartys.items():
			LeaderName = oyuncu_verisi['name']
			if oyuncu_verisi['leader'] == True :
				return str(LeaderName)

def End():
	lider_konum = WhereIsLeader()
	x = get_position()['x']
	y = get_position()['y']
	End = x > 17409 and x < 17540 and y > 3761 and y < 3885
	if End and lider_konum == "Town" :
		return 1
	return 0

def ReturnSC():
	global MembersReturn
	if MembersReturn == 0 :
		MembersReturn += 1
		Timer(1,use_return_scroll).start()

def GetUnique():
	gtmonsters = get_monsters()
	if gtmonsters:
		for monster in gtmonsters:
			servername = gtmonsters[monster]['servername']
			name = gtmonsters[monster]['name']
			if servername == "MOB_SD_OSIRIS_3" or name == "Ghost Sereness" :
				return 1
	return 0

def WhereAmI():
	x = get_position()['x']
	y = get_position()['y']

	HolyWaterTemple = x > 7338 and x < 12095 and y > 4044  and y < 6519
	ForgottenWorld3 = x > 16317 and x < 19388 and y > 2298 and y < 4991
 #-------------------------Advanced------------------------------------------#
	NephthysOFF = x > 8547 and x < 8712 and y > 5656 and y < 5801 
	SekhmetOFF = x > 8547 and x < 8712 and y > 6070 and y < 6219
	HorusOFF = x > 8998 and x < 9118 and y > 5896 and y < 6063
 #----------------------Intermediate-------------------------------------#
	NephthysOFF2 = x > 11043 and x < 11208 and y > 5658 and y < 5804  
	SekhmetOFF2 = x > 11043 and x < 11208 and y > 6072 and y < 6219
	HorusOFF2 = x > 11494 and x < 11618 and y > 5897 and y < 6065
 #----------------------Beginner-----------------------------------------#
	SphinxOFF3 = x > 10875 and x < 11113 and y > 4566 and y < 4620 
	NephthysOFF3 = x > 11042 and x < 11213 and y > 4313 and y < 4460  
	SekhmetOFF3 = x > 11042 and x < 11213 and y > 4728 and y < 4876
	HorusOFF3 = x > 11496 and x < 11624 and y > 4553 and y < 4719
 #----------------------Sphinx--------------------------------#
	Sphinx3 = x > 10875 and x < 11042 and y > 4523 and y < 4664
	Sphinx2 = x > 10875 and x < 11042 and y > 5865 and y < 6009
	Sphinx = x > 8377 and x < 8545 and y > 5865 and y < 6009 
 #----------------------Forgotten World 3*--------------------------------#
	Bridge1 = x > 18028 and x < 18158 and y > 3845 and y < 3918
	Bridge2 = x > 17873 and x < 17964 and y > 3956 and y < 4135
	Bridge3 = x > 18016 and x < 18186 and y > 4196 and y < 4252
	Bridge4 = x > 18265 and x < 18424 and y > 4252 and y < 4299
	Bridge5 = x > 18467 and x < 18520 and y > 3893 and y < 4089
	Bridge6 = x > 18654 and x < 18680 and y > 3529 and y < 3769
	Bridge7 = x > 18323 and x < 18556 and y > 3242 and y < 3401
	Bridge8 = x > 18081 and x < 18189 and y > 3317 and y < 3473
	Bridge9 = x > 17939 and x < 18103 and y > 4350 and y < 4474
	Bridge10 = x > 17572 and x < 17755 and y > 4419 and y < 4453
	Bridge11 = x > 17246 and x < 17421 and y > 4247 and y < 4357
	Bridge12 = x > 17218 and x < 17274 and y > 3839 and y < 4069
	Bridge13 = x > 17113 and x < 17167 and y > 3414 and y < 3674
	Bridge14 = x > 17303 and x < 17452 and y > 3163 and y < 3288
	Bridge15 = x > 17625 and x < 17794 and y > 3153 and y < 3177
	Bridge16 = x > 17546 and x < 17577 and y > 3237 and y < 3396
	Bridge17 = x > 17714 and x < 17825 and y > 3471 and y < 3689
	Bridge18 = x > 17570 and x < 17718 and y > 3684 and y < 3790
 #-------------------------------------------------------------------------#
	if ForgottenWorld3 or HolyWaterTemple :
		if QtBind.isChecked(gui,cbxSafeWay) :
			if HolyWaterTemple :
				if NephthysOFF or SekhmetOFF or HorusOFF :
					return "OFF_HWT"
				elif NephthysOFF2 or SekhmetOFF2 or HorusOFF2 :
					return "OFF_HWT"
				elif NephthysOFF3 or SekhmetOFF3 or HorusOFF3 :
					return  "OFF_HWT"
				elif QtBind.isChecked(gui,cbxIgnoreSphnix) and SphinxOFF3 :
					return "OFF_HWT"
				elif Sphinx or Sphinx2 or Sphinx3 :
					return 0
				else :
					return "ON_HWT"
		if QtBind.isChecked(gui,cbxSafeWay2) :
			if ForgottenWorld3 :
				if Bridge1 or Bridge2 or Bridge3 or Bridge4 or Bridge5 or Bridge6 :
					return "OFF_FGW"
				elif Bridge7 or Bridge8 or Bridge9 or Bridge10 or Bridge11 or Bridge12 :
					return "OFF_FGW"
				elif Bridge13 or Bridge14 or Bridge15 or Bridge16 or Bridge17 or Bridge18 :
					return "OFF_FGW"
				else :
					return "ON_FGW"
	else :
		return 0

def CheckInDungeon():
	x = get_position()['x']
	y = get_position()['y']
	HolyWaterTemple = x > 7338 and x < 12095 and y > 4044  and y < 6519
	ForgottenWorld3 = x > 16317 and x < 19388 and y > 2298 and y < 4991
	if HolyWaterTemple or ForgottenWorld3 : 
		return 1
	return 0

def DodgeAttack():
	global DodgeAttackBool,CheckPoint
	while CheckInDungeon() == 1 and DodgeAttackBool == True:
		sleep(1)
		radius0 = 0
		AttackRadius = int(QtBind.text(gui,txtRange))
		AttackRadius2 = int(QtBind.text(gui,txtRange2))
		att = WhereAmI()
		gta = get_training_area()['radius']
		if not att == 0 :
			if att == "ON_HWT" or att == "OFF_HWT" :
				if att == "ON_HWT" and gta < AttackRadius :
					CheckPoint = True
					set_training_radius(AttackRadius)
					if logMessage :
						log("Plugin: Training radius set to "+str(AttackRadius)+" m.")
				elif att == "OFF_HWT" and  gta > 0  :
					CheckPoint = False
					set_training_radius(radius0)
					if logMessage :
						log("Plugin: Training radius set to "+str(radius0)+" m.")
			elif att == "ON_FGW" or att == "OFF_FGW" :
				if att == "ON_FGW" and gta < AttackRadius2 :
					set_training_radius(AttackRadius2)
					if logMessage :
						log("Plugin: Training radius set to "+str(AttackRadius2)+" m.")
				elif att == "OFF_FGW" and  gta > 0  :
					set_training_radius(radius0)
					if logMessage :
						log("Plugin: Training radius set to "+str(radius0)+" m.")
		if CheckInDungeon() == 0 :
			DodgeAttackBool = False
			break

def WhereIsLeader():
	getpartys = get_party()
	count = party_count()
	if getpartys and count >= 2 :
		for oyuncu_id, oyuncu_verisi in getpartys.items():
			if oyuncu_verisi['leader'] == True :
				x = oyuncu_verisi['x']
				y = oyuncu_verisi['y']
				r = oyuncu_verisi['region']
				Advanced = x >= 7301 and x <= 9603 and y >= 5385 and y <= 6540
				Intermediate = x >= 9790 and x <= 12095 and y >= 5375 and y <= 6530
				Beginner = x >= 10560 and x <= 12100 and y >= 4030 and y <= 5180
				ForgottenWorld3 = x > 16317 and x < 19388 and y > 2298 and y < 4991
				Town = r == 23088 or r == 23687 or r == 23603 or r == 25000 or r == 26265 or r == 27244 or r == 26959
				Gate = r == 19019
				if Advanced :
					return "Advanced"
				elif Intermediate :
					return "Intermediate"
				elif Beginner :
					return	"Beginner"
				elif Town :
					return	"Town"
				elif Gate :
					return	"Gate"
				elif ForgottenWorld3 :
					return	"FGW"
				else:
					return "Unknown"
			else :
				return 0

def ChangeProfile():
	global Finished_HWT,gofgw
	lider_durumu = LeaderSelection()
	lider_konum = WhereIsLeader()
	Enabled = QtBind.isChecked(gui,cbxChangeProfile)
	ProfileFGW = "FGW"
	FGWProfile = str(QtBind.text(gui,txtCHANGEPROFILE))
	HWTProfile = str(QtBind.text(gui,txtHWTPROFILE))
	SetProfile = (FGWProfile if FGWProfile else ProfileFGW)
	Profile = get_profile()
	Status = get_status()
	if Enabled :
		if lider_durumu == True and Finished_HWT == True :
			if Profile == HWTProfile :
				Finished_HWT = False
				set_profile(SetProfile)
				use_return_scroll()
				gofgw = True
		elif lider_durumu == False and lider_konum == "FGW" :
			if Profile == HWTProfile :
				if Status == "botting" :
					stop_bot()
					set_profile(SetProfile)
					use_return_scroll()
				else :
					set_profile(SetProfile)
					use_return_scroll()


def Entrance():
	global Beginner_remaining,Intermediate_remaining,Advanced_remaining,WaitMaster,MembersReturn,Return,ReturnCommand,Finished_HWT,timer,Remaining,Done
	lider_durumu = LeaderSelection()
	lider_konum = WhereIsLeader()
	count = party_count()
	count2 = GetPartyMembersCount()
	PartyMembers = int(QtBind.text(gui,txtPartyMembers))
	ReturnFirst = QtBind.isChecked(gui,returnfirst)
	ReturnSecond = QtBind.isChecked(gui,returnsecond)
	ReturnThird = QtBind.isChecked(gui,returnthird)
	NoPremium = QtBind.isChecked(gui,NoNPremium)
	if ReturnCommand == False :
		if lider_durumu == True and count2 >= PartyMembers :
			if NoPremium :
				if QtBind.isChecked(gui,third) :
						if Advanced_remaining > 3 :
							Advanced()
							if Advanced_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Advanced_remaining -=1
									QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
						elif Intermediate_remaining > 3 :
							Intermediate()
							if Intermediate_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Intermediate_remaining -=1
									QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
						elif Beginner_remaining > 3 :
							Beginner()
							if Beginner_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Beginner_remaining -=1
									QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
						else :
							if Advanced_remaining == 3 and Intermediate_remaining == 3 and Beginner_remaining == 3 :
								if Remaining == 0 :
									Done = 3
									HWTOFF()
									Finished_HWT = True
				elif QtBind.isChecked(gui,second) :
						if Intermediate_remaining > 3 :
							Intermediate()
							if Intermediate_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Intermediate_remaining -=1
									QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
						elif Advanced_remaining > 3 :
							Advanced()
							if Advanced_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Advanced_remaining -=1
									QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
						elif Beginner_remaining > 3 :
							Beginner()
							if Beginner_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Beginner_remaining -=1
									QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
						else :
							if Advanced_remaining == 3 and Intermediate_remaining == 3 and Beginner_remaining == 3 :
								if Remaining == 0 :
									Done = 3
									HWTOFF()
									Finished_HWT = True
				elif QtBind.isChecked(gui,first) :
						if Beginner_remaining > 3 :
							Beginner()
							if Beginner_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Beginner_remaining -=1
									QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
						elif Intermediate_remaining > 3 :
							Intermediate()
							if Intermediate_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Intermediate_remaining -=1
									QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
						elif Advanced_remaining > 3 :
							Advanced()
							if Advanced_remaining > 3 :
								if Remaining == 0 :
									Remaining += 1
									Advanced_remaining -=1
									QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
						else :
							if Advanced_remaining == 3 and Intermediate_remaining == 3 and Beginner_remaining == 3 :
								if Remaining == 0 :
									Done = 3
									HWTOFF()
									Finished_HWT = True
			else :
				if QtBind.isChecked(gui,third) :
					if ReturnThird or ReturnSecond :
						if AdvancedL < 5 :
							Advanced()
							if Advanced_remaining == 1 :
								QtBind.setText(gui,lblAdvanced,'Done')
							elif Advanced_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Advanced_remaining -=1
									QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
						elif AdvancedL >= 5 and Return < 2 and ReturnThird :
								if Return == 0 :
									Return += 1
									ReturnCommand = True
									Timer(random.uniform(0.5,2),use_return_scroll).start()
								else:
									Return += 1
						elif IntermediateL < 5 :
							Intermediate()
							if Intermediate_remaining == 1 :
								QtBind.setText(gui,lblIntermediate,'Done')
							elif Intermediate_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Intermediate_remaining -=1
									QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
						elif IntermediateL >= 5 and Return < 2 and ReturnSecond :
								if Return == 0 :
									Return += 1
									ReturnCommand = True
									Timer(random.uniform(0.5,2),use_return_scroll).start()
								else:
									Return += 1
						elif BeginnerL < 5 :
							Beginner()
							if Beginner_remaining == 1 :
								QtBind.setText(gui,lblBeginner,'Done')
							elif Beginner_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Beginner_remaining -=1
									QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
						elif BeginnerL == 5 :
							HWTOFF()
							Finished_HWT = True
				elif QtBind.isChecked(gui,second) :
					if ReturnSecond or ReturnThird :
						if IntermediateL < 5 :
							Intermediate()
							if Intermediate_remaining == 1 :
								QtBind.setText(gui,lblIntermediate,'Done')
							elif Intermediate_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Intermediate_remaining -=1
									QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
						elif IntermediateL >= 5 and Return < 2 and ReturnSecond :
							if Return == 0 :
								Return += 1
								ReturnCommand = True
								Timer(random.uniform(0.5,2),use_return_scroll).start()
							else:
								Return += 1
						elif AdvancedL < 5 :
							Advanced()
							if Advanced_remaining == 1 :
								QtBind.setText(gui,lblAdvanced,'Done')
							elif Advanced_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Advanced_remaining -=1
									QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
						elif AdvancedL >= 5 and Return < 2 and ReturnThird :
								if Return == 0 :
									Return += 1
									ReturnCommand = True
									Timer(random.uniform(0.5,2),use_return_scroll).start()
								else:
									Return += 1
						elif BeginnerL < 5 :
							Beginner()
							if Beginner_remaining == 1 :
								QtBind.setText(gui,lblBeginner,'Done')
							elif Beginner_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Beginner_remaining -=1
									QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
						elif BeginnerL == 5 :
							HWTOFF()
							Finished_HWT = True
				elif QtBind.isChecked(gui,first) :
					if ReturnFirst or ReturnSecond :
						if BeginnerL < 5 :
							Beginner()
							if Beginner_remaining == 1 :
								QtBind.setText(gui,lblBeginner,'Done')
							elif Beginner_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Beginner_remaining -=1
									QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
						elif BeginnerL >= 5 and Return < 2 and ReturnFirst :
							if Return == 0 :
								Return += 1
								ReturnCommand = True
								Timer(random.uniform(0.5,2),use_return_scroll).start()
							else:
								Return += 1
						elif IntermediateL < 5 :
							Intermediate()
							if Intermediate_remaining == 1 :
								QtBind.setText(gui,lblIntermediate,'Done')
							elif Intermediate_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Intermediate_remaining -=1
									QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
						elif IntermediateL >= 5 and Return < 2 and ReturnSecond :
							if Return == 0 :
								Return += 1
								ReturnCommand = True
								Timer(random.uniform(0.5,2),use_return_scroll).start()
							else:
								Return += 1
						elif AdvancedL < 5 :
							Advanced()
							if Advanced_remaining == 1 :
								QtBind.setText(gui,lblAdvanced,'Done')
							elif Advanced_remaining > 1 :
								if Remaining == 0 :
									Remaining += 1
									Advanced_remaining -=1
									QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
						elif AdvancedL == 5 :
							HWTOFF()
							Finished_HWT = True
				elif QtBind.isChecked(gui,advanced3) :
					if AdvancedL < 5 :
						Advanced()
						if Advanced_remaining == 1 :
							QtBind.setText(gui,lblAdvanced,'Done')
						elif Advanced_remaining > 1 :
							if Remaining == 0 :
								Remaining += 1
								Advanced_remaining -=1
								QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
					elif AdvancedL == 5 :
						HWTOFF()
				elif QtBind.isChecked(gui,intermediate2) :
					if IntermediateL < 5 :
						Intermediate()
						if Intermediate_remaining == 1 :
							QtBind.setText(gui,lblIntermediate,'Done')
						elif Intermediate_remaining > 1 :
							if Remaining == 0 :
								Remaining += 1
								Intermediate_remaining -=1
								QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
					elif IntermediateL == 5 :
						HWTOFF()
				elif QtBind.isChecked(gui,beginner1) :
					if BeginnerL < 5 :
						Beginner()
						if Beginner_remaining == 1 :
							QtBind.setText(gui,lblBeginner,'Done')
						elif Beginner_remaining > 1 :
							if Remaining == 0 :
								Remaining += 1
								Beginner_remaining -=1
								QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
					elif BeginnerL == 5 :
						HWTOFF()
		elif lider_durumu == False and count >= 2:
			if lider_konum == "Advanced" :
				Advanced()
				if Advanced_remaining == 1 :
					QtBind.setText(gui,lblAdvanced,'Done')
				elif Advanced_remaining > 1 :
					if Remaining == 0 :
						Remaining += 1
						Advanced_remaining -=1
						QtBind.setText(gui,lblAdvanced,str(Advanced_remaining))
			elif lider_konum == "Intermediate" :
				Intermediate()
				if Intermediate_remaining == 1 :
					QtBind.setText(gui,lblIntermediate,'Done')
				elif Intermediate_remaining > 1 :
					if Remaining == 0 :
						Remaining += 1
						Intermediate_remaining -=1
						QtBind.setText(gui,lblIntermediate,str(Intermediate_remaining))
			elif lider_konum == "Beginner" :
				Beginner()
				if Beginner_remaining == 1 :
					QtBind.setText(gui,lblBeginner,'Done')
				elif Beginner_remaining > 1 :
					if Remaining == 0 :
						Remaining += 1
						Beginner_remaining -=1
						QtBind.setText(gui,lblBeginner,str(Beginner_remaining))
			elif lider_konum == "Town" :
				if MembersReturn == 0 :
					MembersReturn += 1
					ReturnCommand = True
					Timer(random.uniform(0.5,2),use_return_scroll).start()
					log('Plugin: Party Lideri Şehirde, Şehre dönülüyor.')
			elif lider_konum == "Gate" :
				if WaitMaster == 0 :
					WaitMaster += 1
					log('Plugin: Party Liderinin giriş yapması bekleniyor...')
			else :
				pass

def Gate():
    npcs = get_npcs()
    if npcs:
        for key in npcs:
            if npcs[key]['servername'] == "GATE_TOMB_GATE_IN":
                return 1
    return 0
def IfCancelSpeed():
	npcs = get_npcs()
	if npcs:
		for key in npcs:
			Fgw  = npcs[key]['servername'] == "NPC_FWORLD_RECALL_PARTY"
			In = npcs[key]['servername'] == "GATE_TOMB_GATE_IN"
			Out3 = npcs[key]['servername'] == "GATE_TOMB_GATE_OUT_3"
			Out2 = npcs[key]['servername'] == "GATE_TOMB_GATE_OUT_2"
			Out1 = npcs[key]['servername'] == "GATE_TOMB_GATE_OUT_1"
			if Fgw or Out1 or Out2 or Out3 or In :
				return 1
	return 0

def party_count():
	pt = get_party()
	count = 0
	if pt:
		for key, char in pt.items():
			count += 1
		return count

def event_loop():
	if not QtBind.isChecked(gui,cbxDisabledEventLoop) :
		global Done,ReturnCommand,Finished_HWT,DodgeAttackBool,CheckPoint
		x = get_position()['x']
		y = get_position()['y']
		r = get_position()['region']
		HolyWaterTemple = x > 7338 and x < 12095 and y > 4044  and y < 6519
		ForgottenWorld3 = x > 16317 and x < 19388 and y > 2298 and y < 4991 
		Town = r == 23088 or r == 23687 or r == 23603 or r == 25000 or r == 26265 or r == 27244 or r == 26959
		HolyWaterTemple_Gate = x > -11378 and x < -11345 and y > -3285  and y < -3270
		if ForgottenWorld3 or HolyWaterTemple :
			if HolyWaterTemple :
				if QtBind.isChecked(gui,cbxSafeWay) and DodgeAttackBool == False :
					Status = get_status()
					if Status == "botting" or Status == "tracing":
						DodgeAttackBool = True
						Timer(0.001,DodgeAttack).start()
				elif QtBind.isChecked(gui,cbxSilverCoinCounter) and CheckPoint == True:
					SilverCoinChecker()
			elif ForgottenWorld3 :
				if DodgeAttackBool == False :
					if QtBind.isChecked(gui,cbxSafeWay2) :
						Status = get_status()
						if Status == "botting" or Status == "tracing" :
							DodgeAttackBool = True
							Timer(0.001,DodgeAttack).start()
		elif Town :
			if QtBind.isChecked(gui,cbxChangeProfile) :
				Profile = get_profile()
				ProfileHWT = "HWT"
				HwtProfile = str(QtBind.text(gui,txtHWTPROFILE))
				SetProfile = (HwtProfile if HwtProfile else ProfileHWT)
				if Profile == SetProfile :
					lider_konum = WhereIsLeader()
					if lider_konum == "FGW" :
						ChangeProfile()
		elif HolyWaterTemple_Gate :
			if QtBind.isChecked(gui,HolyMolyEntrance) and ReturnCommand == False and Finished_HWT == False :
				Status = get_status()
				if Status != "botting" :
					Entrance()
			elif Finished_HWT == True :
				Profile = get_profile()
				ProfileHWT = "HWT"
				HwtProfile = str(QtBind.text(gui,txtHWTPROFILE))
				SetProfile = (HwtProfile if HwtProfile else ProfileHWT)
				if Profile == SetProfile :
					ChangeProfile()
		if QtBind.isChecked(gui,cbxEnabledConditions) :
			if ForgottenWorld3 or HolyWaterTemple :
				lider_durumu = LeaderSelection()
				if HolyWaterTemple and lider_durumu == False :
					if QtBind.isChecked(gui,cbxTrace) :
						Status = get_status()
						if Status != "tracing" and Status != "botting":
							trace_master = LeaderName()
							TraceHWT = (hwt_master if hwt_master else trace_master)
							hwt_master = str(QtBind.text(gui,txtHWTMASTER))
							start_trace(TraceHWT)
						elif Status == "botting" :
							trace_master = LeaderName()
							TraceHWT = (hwt_master if hwt_master else trace_master)
							hwt_master = str(QtBind.text(gui,txtHWTMASTER))
							stop_bot()
							Timer(1,start_trace(TraceHWT)).start()
				elif ForgottenWorld3 and Member :
					if QtBind.isChecked(gui,cbxTrace) :
						if ForgottenWorld3 :
							Status = get_status()
							if Status != "tracing" and Status != "botting":
								trace_master = LeaderName()
								fgw_master = str(QtBind.text(gui,txtFGWMASTER))
								TraceFGW = (fgw_master if fgw_master else trace_master)
								start_trace(TraceFGW)
							elif Status == "botting" :
								trace_master = LeaderName()
								fgw_master = str(QtBind.text(gui,txtFGWMASTER))
								TraceFGW = (fgw_master if fgw_master else trace_master)
								stop_bot()
								Timer(1,start_trace(TraceFGW)).start()
			elif Town :
				Profile = get_profile()
				ProfileHWT = "HWT"
				HwtProfile = str(QtBind.text(gui,txtHWTPROFILE))
				SetProfile = (HwtProfile if HwtProfile else ProfileHWT)
				if QtBind.isChecked(gui,cbxStart) and Profile == SetProfile :
					Status = get_status()
					if Status != "tracing" and Status != "botting":
						start_bot()
					elif Status == "tracing" :
						stop_trace()
						Timer(1,start_bot).start()
				elif QtBind.isChecked(gui,HolyMolyEntrance) and Profile != SetProfile :
					HWTOFF()
			elif HolyWaterTemple_Gate :
				if QtBind.isChecked(gui,HolyMolyEntrance) == 0 :
					Profile = get_profile()
					ProfileHWT = "HWT"
					HwtProfile = str(QtBind.text(gui,txtHWTPROFILE))
					SetProfile = (HwtProfile if HwtProfile else ProfileHWT)
					if Profile == SetProfile :
						if QtBind.isChecked(gui,cbxEntranceON) :
							lider_durumu = LeaderSelection()
							if lider_durumu == True and Done < 3:
								HWTON()
							elif lider_durumu == False :
								HWTON()

def SilverCoinChecker():
	global SilverCoin_gain,Alert
	drops = get_drops()
	Status = get_status() 
	if drops: 
		for drop in drops:
			currentUid = drop
			if drops[drop]['servername'] == "ITEM_ETC_SD_TOKEN_03" :
				if currentUid not in uids :
					SilverCoin_gain += 1
					QtBind.setText(gui,lblSilver,str(SilverCoin_gain))
				if QtBind.isChecked(gui,cbxSilverCoin) :
					if Alert == 0 :
						threading.Thread(target=SilverCoinAlert).start()
				if QtBind.isChecked(gui,cbxSilverStop) :
					if Status == "botting" :
						stop_bot()
						if logMessage :
							log('Plugin: Yerde Silver Coin tespit edildi, Bot durduruluyor.')
					elif Status == "tracing" :
						stop_trace()
						if logMessage :
							log('Plugin: Yerde Silver Coin tespit edildi, Takip durduruluyor.')
			uids.add(currentUid)

def fnEnabledPBR():
    x = get_position()['x']
    y = get_position()['y']
    path = get_config_dir()
    CharData = get_character_data()
    ConfigFile = f"{CharData['server']}_{CharData['name']}.{get_profile()}.json" if len(get_profile()) > 0 else f"{CharData['server']}_{CharData['name']}.json"
    ZeroPBR = x > 8600 and x < 8770 and y > 5835 and y < 6035
    if os.path.exists(path + ConfigFile):
        with open(path + ConfigFile, "r", encoding='utf-8') as f:
            Configdata = json.load(f)
            if ZeroPBR:
                if Configdata['Skills']['PartyBuffRadius'] >= 30:
                    if Configdata['Skills']['PartyBuffRadius'] >= 30:
                        Configdata['Skills']['PartyBuffRadius'] = 0
                        log('Plugin: Party Buff Radius = 0')
                    with open(path + ConfigFile, "w", encoding='utf-8') as f:
                        f.write(json.dumps(Configdata, indent=4, ensure_ascii=False))
                        set_profile(get_profile())
            else:
                if Configdata['Skills']['PartyBuffRadius'] <= 0:
                    if Configdata['Skills']['PartyBuffRadius'] <= 0:
                        Configdata['Skills']['PartyBuffRadius'] = 30
                        log('Plugin: Party Buff Radius = 30')
                    with open(path + ConfigFile, "w", encoding='utf-8') as f:
                        f.write(json.dumps(Configdata, indent=4, ensure_ascii=False))
                        set_profile(get_profile())

def handle_joymax(opcode, data) :
	global AdvancedL,IntermediateL,BeginnerL,Done
	formattedOpCode = '{:02X}'.format(opcode)
	if  formattedOpCode == "B05A" :
		if data[0] == 0x02 and data[1] == 0x27 and data[2] == 0x1C :
			if QtBind.isChecked(gui,third) :
				if AdvancedL < 5:
					AdvancedL = 5
					if str(QtBind.text(gui,lblAdvanced)) <= "5" :
						QtBind.setText(gui,lblAdvanced,'Done')
				elif IntermediateL < 5 :
					IntermediateL = 5
					if str(QtBind.text(gui,lblIntermediate)) <= "5" :
						QtBind.setText(gui,lblIntermediate,'Done')
				elif BeginnerL < 5 :
					BeginnerL = 5
					if str(QtBind.text(gui,lblBeginner)) <= "5" :
						QtBind.setText(gui,lblBeginner,'Done')
			elif QtBind.isChecked(gui,second) :
				if IntermediateL < 5 :
					IntermediateL = 5
					if str(QtBind.text(gui,lblIntermediate)) <= "5" :
						QtBind.setText(gui,lblIntermediate,'Done')
				elif AdvancedL < 5:
					AdvancedL = 5
					if str(QtBind.text(gui,lblAdvanced)) <= "5" :
						QtBind.setText(gui,lblAdvanced,'Done')
				elif BeginnerL < 5 :
					BeginnerL = 5
					if str(QtBind.text(gui,lblBeginner)) <= "5" :
						QtBind.setText(gui,lblBeginner,'Done')
			elif QtBind.isChecked(gui,first) :
				if BeginnerL < 5 :
					BeginnerL = 5
					if str(QtBind.text(gui,lblBeginner)) <= "5" :
						QtBind.setText(gui,lblBeginner,'Done')
				elif IntermediateL < 5 :
					IntermediateL = 5
					if str(QtBind.text(gui,lblIntermediate)) <= "5" :
						QtBind.setText(gui,lblIntermediate,'Done')
				elif AdvancedL < 5:
					AdvancedL = 5
					if str(QtBind.text(gui,lblAdvanced)) <= "5" :
						QtBind.setText(gui,lblAdvanced,'Done')
			elif QtBind.isChecked(gui,advanced3) :
				if AdvancedL < 5:
					AdvancedL = 5
					if str(QtBind.text(gui,lblAdvanced)) <= "5" :
						QtBind.setText(gui,lblAdvanced,'Done')
			elif QtBind.isChecked(gui,intermediate2) :
				if IntermediateL < 5 :
					IntermediateL = 5
					if str(QtBind.text(gui,lblIntermediate)) <= "5" :
						QtBind.setText(gui,lblIntermediate,'Done')
			elif QtBind.isChecked(gui,beginner1) :
				if BeginnerL < 5 :
					BeginnerL = 5
					if str(QtBind.text(gui,lblBeginner)) <= "5" :
						QtBind.setText(gui,lblBeginner,'Done')
			Done += 1
	elif  formattedOpCode == "B070" :
		if data[0] == 0x01 and data[1] == 0x00 and data[2] == 0x30 and data[3] == 0x99 and data[4] == 0x7A :
			SpinixReflectCounterStop()
			Timer(16.0,SpinixReflectCounterStart).start()
			if logMessage :
				log('Plugin: Beginner Spinix Reflect Counter')
		elif data[0] == 0x01 and data[1] == 0x00 and data[2] == 0x30 and data[3] == 0x9F and data[4] == 0x7A  :
			SpinixReflectCounterStop()
			Timer(21.0,SpinixReflectCounterStart).start()
			if logMessage :
				log('Plugin: Intermediate Spinix Reflect Counter')
		elif data[0] == 0x01 and data[1] == 0x00 and data[2] == 0x30 and data[3] == 0xA5 and data[4] == 0x7A :
			SpinixReflectCounterStop()
			Timer(26.0,SpinixReflectCounterStart).start()
			if logMessage :
				log('Plugin: Advanced Spinix Reflect Counter')				
	return True

def HWTON():
	if QtBind.isChecked(gui,HolyMolyEntrance) == 0 :
		QtBind.setChecked(gui,HolyMolyEntrance,True)
		if logMessage :
			log('Plugin: Active Holy Water Temple (Entrance)')
def HWTOFF():
	if QtBind.isChecked(gui,HolyMolyEntrance) == 1 :
		QtBind.setChecked(gui,HolyMolyEntrance,False)
		if logMessage :
			log('Plugin: Passive Holy Water Temple (Entrance)')

def Beginner():
	npcs = get_npcs()
	if npcs :
		for npc in npcs:
			if npcs[npc]['servername'] == "GATE_TOMB_GATE_IN" :
				beginner = 165
				pack = struct.pack('<IBI', npc , 2 , beginner)
				inject_joymax(0x705A,pack,False)
				if logMessage :
					log("Plugin: Entering Holy Water Temple (Beginner)")
def Intermediate():
	npcs = get_npcs()
	if npcs :
		for npc in npcs:
			if npcs[npc]['servername'] == "GATE_TOMB_GATE_IN" :
				intermediate = 166
				pack = struct.pack('<IBI', npc , 2 , intermediate)
				inject_joymax(0x705A,pack,False)
				if logMessage :
					log("Plugin: Entering Holy Water Temple (Intermediate)")
def Advanced():
	npcs = get_npcs()
	if npcs :
		for npc in npcs:
			if npcs[npc]['servername'] == "GATE_TOMB_GATE_IN" :
				advanced = 167
				pack = struct.pack('<IBI', npc , 2 , advanced)
				inject_joymax(0x705A,pack,False)
				if logMessage :
					log("Plugin: Entering Holy Water Temple (Advanced)")

def ManuelEntrance_clicked():
	Timer(1,Advanced).start()
	Timer(3,Intermediate).start()
	Timer(5,Beginner).start()

def SpinixReflectCounterStop():
	radius0 = 0
	set_training_radius(radius0)
	if logMessage :
		log("Plugin: Training radius set to "+str(radius0)+" m.")
def SpinixReflectCounterStart():
	AttackRadius = int(QtBind.text(gui,txtRangeSphinx))
	set_training_radius(AttackRadius)
	if logMessage :
		log("Plugin: Training radius set to "+str(AttackRadius)+" m.")

def ResetCount():
	global AdvancedL,IntermediateL,BeginnerL
	global Return,SilverCoin_gain,Done
	global Advanced_remaining,Intermediate_remaining,Beginner_remaining
	Advanced_remaining = 5
	Intermediate_remaining = 5
	Beginner_remaining = 5
	SilverCoin_gain = 0
	AdvancedL = 0
	IntermediateL = 0
	BeginnerL = 0
	Return = 0
	Done = 0
	QtBind.setText(gui,lblAdvanced,str("5"))
	QtBind.setText(gui,lblIntermediate,str("5"))
	QtBind.setText(gui,lblBeginner,str("5"))
	QtBind.setText(gui,lblSilver,str("0"))

#------------------------------------------------------FGW INVITE------------------------------------------------------------#

def ListPartyUID():
	pt = get_party()
	global SkipCommand
	results = []
	if pt:
		for uid, pdata in pt.items():
			results.append(uid)
		return results
	else :
		SkipCommand = True
		start_bot()

def InjectInvitesPackets():
	global elaman1,eleman2,SkipCommand
	data_list = ListPartyUID()
	count = len(data_list)
	data_list = data_list[elaman1:eleman2]
	if count >= 2 :
		if eleman2 <= count and SkipCommand == False :
			if data_list:
				for uid in data_list:
					elaman1 += 1
					eleman2 += 1
					opcode = 0x751A
					data = struct.pack('I', uid)
					inject_joymax(opcode,data,False)
					Timer(2.0,InjectInvitesPackets).start()
		elif eleman2 > count :
			SkipCommand = True
			elaman1 = 1
			eleman2 = 2
			start_bot()

def FGW(args):
	global SkipCommand
	gt = get_status()
	if SkipCommand == False and gt == "botting" :
		stop_bot()
		Timer(2.0,InjectInvitesPackets).start()
	return 0

#----------------------------------------------------------------------------------------------------------------------------------#

def Party(args):
	name = ''
	if len(args) > 1:
		name = args[1]
		if get_party() :
			if name == "leave" :
				log("Plugin: Leaving the party..")
				inject_joymax(0x7061,b'',False)
	return 0

def WaitParty(args):
	# Read member count
	memberCount = 8
	if len(args) >= 2:
		memberCount = round(float(args[1]))
	# Count to start waiting
	if GetPartyMembersCount() < memberCount:
		# Stop scripting
		stop_bot()
		# Starts waiting avoiding thread lock
		Timer(0.001,WaitPartyTask,[memberCount]).start()
	return 0

def GetPartyMembersCount():
	# It will be counting myself
	count2 = 1
	player_data = get_party()
	for player_id, player_data in player_data.items():
		if player_data['player_id'] > 0:
			count2 += 1
	return count2

def WaitPartyTask(MemberCount):
	log('Plugin: Waiting for #'+str(MemberCount)+' members to continue')
	while GetPartyMembersCount() < MemberCount:
		sleep(0.5)
	# Retart bot
	log('Plugin: Wait finished, all members are ready!')
	start_bot()

def SilverCoinAlert():
	global Alert
	if Alert == 0 :
		for Alert in range(1,11):
			play_wav(FIXSOUNDPATH)
			time.sleep(1.05)
			if Alert == 10 :
				Alert = 0		

def teleported():
	global WaitMaster,MembersReturn,SkipCommand,ReturnCommand,Remaining,gofgw
	uids.clear()
	lider_durumu = LeaderSelection()
	Status = get_status()
	x = get_position()['x']
	y = get_position()['y']
	r = get_position()['region']
	if gofgw == True :
		start_bot()
		gofgw = False
	if ReturnCommand == True :
		ReturnCommand = False
	if SkipCommand == True :
		SkipCommand = False
	if Remaining > 0 :
		Remaining = 0
	if WaitMaster > 0 :
		WaitMaster = 0
	if MembersReturn > 0 :
		MembersReturn = 0
	if QtBind.isChecked(gui,cbxNotrace) and Status == "tracing" :
		Town = r == 23088 or r == 23687 or r == 23603 or r == 25000 or r == 26265 or r == 27244 or r == 26959
		Gate = x > -11680 and x < -11330 and y > -3360  and y < -3190
		if Gate or Town :
			stop_trace()
	if QtBind.isChecked(gui,HolyMolyEntrance) and lider_durumu == True :
		HolyWaterTemple = x > 7338 and x < 12095 and y > 4044  and y < 6519
		Gate = x > -11680 and x < -11330 and y > -3360  and y < -3190
		if HolyWaterTemple :
			if Status != "botting" :
				start_bot()
			elif Status == "botting" :
				stop_bot()
				Timer(1,start_bot).start()
		elif Gate and Status == "botting" :
			stop_bot()
	if QtBind.isChecked(gui,cbxResetRadius) and QtBind.isChecked(gui,cbxEnabledConditions) :
		Timer(1,OutCheck).start()

def OutCheck():
	npcs = get_npcs()
	gta = get_training_area()['radius']
	AttackRadius = int(QtBind.text(gui,txtRange))
	if gta < AttackRadius :
		if npcs:
			for key in npcs:
				Out3 = npcs[key]['servername'] == "GATE_TOMB_GATE_OUT_3"
				Out2 = npcs[key]['servername'] == "GATE_TOMB_GATE_OUT_2"
				Out1 = npcs[key]['servername'] == "GATE_TOMB_GATE_OUT_1"
				if Out2 or Out3 :
					set_training_radius(AttackRadius)
					if logMessage :
						log('Plugin: Saldırı Menzilin [ %s ] ile değiştirildi. '%(AttackRadius))
				elif Out1 :
					if not QtBind.isChecked(gui,cbxEnabledConditions) :
						set_training_radius(AttackRadius)
						if logMessage :
							log('Plugin: Saldırı Menzilin [ %s ] ile değiştirildi. '%(AttackRadius))
	else :
		pass



#-------------------------------------------------------------------------------------------------------------#

# For save your settings
def onSaveButtonClicked():
    global timer  # timer değişkenini global olarak kullan
    if timer is None or not Timer.is_alive(timer):
        # Timer henüz başlatılmamışsa veya çalışmıyorsa
        timer = Timer(3, saveConfigs)
        timer.start()
        log('Plugin: Ayarlarınız Kaydedildi.')
    else:
        log('Plugin: Kaydetmek için hala zaman var.(Tekrar deneyin.)')
        pass

# Called when the character enters the game world
def joined_game():
	loadConfigs()

# Plugin loaded
log('Plugin: '+pName+' v'+pVersion+' succesfully loaded')

if os.path.exists(getPath()):
	# Adding RELOAD plugin support
	loadConfigs()
else:
	# Creating configs folder
	os.makedirs(getPath())
	log('Plugin: '+pName+' folder has been created.')