import math
import time
import mj_mode

#import os
#import ConfigParser

####coding=utf-8

global bTest
global dict_info

##########user ini######

def read_cfg():
    global dict_info
    try:
        fp = open('mj.cfg','r')
        strLine = fp.readline()
        dict_info = eval(strLine)
        #print dict_info
        #print dict_info.get('a')
        #dict_info['a']='test'
        #print dict_info['a']
        #for key, value in dict_info.items():
        #    print "\'%s\':\'%s\'" %(key, value)
        print dict_info
        
        fp.close()
    except IOError:
        print 'create mj.cfg!!'
        fp = open('mj.cfg','w')
        fp.write("{'user_win_times': 0,'user_score': 5000,'computer_win_times': 0,'computer_score': 5000}")
        fp.close() 
        fp = open('mj.cfg','r')
        strLine = fp.readline()
        dict_info = eval(strLine)
        #print dict_info
        fp.close()

        
    #finally:
    #    fp.close()
    print "Your win_times: ",dict_info.get('user_win_times')
    print 'Your score: ',dict_info['user_score']
    print 'Computer\'s win_times: ',dict_info['computer_win_times']
    print 'Computer\'s score: ',dict_info['computer_score']
    #print str(dict_info)

def write_cfg():
    #global dict_info
    if bTest: print 'write_cfg mj.cfg!!'
    print "Your win_times: ",dict_info.get('user_win_times')
    print 'Your score: ',dict_info['user_score']
    print 'Computer\'s win_times: ',dict_info['computer_win_times']
    print 'Computer\'s score: ',dict_info['computer_score']
    fp = open('mj.cfg','w')
    fp.write(str(dict_info))
    fp.close()



read_cfg()
###########################################
def play_dh():
    ndhcount=0
    strSp=' '
    nDhLen=20
    li_DhZf = ['\\','|','/','-']
    while True:
        nflag=1
        for kk in range(0,nDhLen):
            #os.system('cls')
            time.sleep(0.1)
            strDh=''
            for jj in range(0,1):
                #strDh+=li_DhZf[1]
                for mm in range(0,4):
                    strDh+=li_DhZf[(mm+kk)%4]
    
            if ndhcount%2==0:
                strDh+=kk*strSp
            else:
                strDh+=(nDhLen-kk)*strSp
            for jj in range(0,1):
                #strDh+=li_DhZf[1]
                for mm in range(0,4):
                    strDh+=li_DhZf[(mm+kk)%4]
    
            #strDh=''
            #strDh+=(60-kk)*strSp
            if ndhcount%2==1:
                strDh+=kk*strSp
            else:
                strDh+=(nDhLen-kk)*strSp
    
            for jj in range(0,1):
                #strDh+=li_DhZf[1]
                for mm in range(0,4):
                    strDh+=li_DhZf[(mm+kk)%4]
    
            if ndhcount%2==1:
                strDh+=kk*strSp
            else:
                strDh+=(nDhLen-kk)*strSp
            for jj in range(0,1):
                #strDh+=li_DhZf[1]
                for mm in range(0,4):
                    strDh+=li_DhZf[(mm+kk)%4]
    
            if ndhcount%2==0:
                strDh+=kk*strSp
            else:
                strDh+=(nDhLen-kk)*strSp
    
            for jj in range(0,1):
                #strDh+=li_DhZf[1]
                for mm in range(0,4):
                    strDh+=li_DhZf[(mm+kk)%4]
            
            print strDh
        
        ndhcount+=1
        if ndhcount>4:
            break
   

play_dh()
###########initial Pai###################
pai_num=['1','2','3','4','5','6','7','8','9']
pai_type=['T','B','W']
pai_feng=['D O','N A','X i','B e','Z h','F a','B B']

print '____________________________'
print '| M | a | J | i | a | n | g |'
print '| T | o | W | j | Z | y | m |'
print '|___|___|___|___|___|___|___|'
print '|(1)|(2)|(3)|(4)|(5)|(6)|(7)|'


mj_list_init=[]

initial_value=''
mj_total=136
mj_list = [initial_value for i in range(mj_total)]

#print mj_list

#print 'Start initial mj pai:'

count=-1
for ii in range(0,3):
    for jj in range(0,9):
        for kk in range(0,4):
            count+=1
            str1='%03d'%count
            mj_list[count] =str1 + ' '+ pai_num[jj] + ' '+pai_type[ii]

#print count
for mm in range(0,7):
    for nn in range(0,4):
        count+=1
        str1='%03d'%count
        mj_list[count] = str1 + ' '+pai_feng[mm] 
#print 'after initial:'
#print mj_list
mj_list_init = mj_list[:]
###########initial pai End###################

###########xi pai###################

xipai_list = [initial_value for i in range(mj_total)]

#print xipai_list
#print 'Start xi pai:'
rand1=int(time.time())
count=136

index=1
mm=0
while True:
    index = int((rand1-index)*math.sqrt(count-index))
    index = index%count
    #print mj_list[index],index
    xipai_list[mm]=mj_list[index]
    mm+=1
    del mj_list[index]
    count-=1
    if count==1:
        xipai_list[mj_total - 1]=mj_list[0]
        break

#print xipai_list    

###########xi pai End###################
###########fa pai###################
def Judge_ChiPai(testList,nRoleType=0):
    
    #if bTest:  print 'nType:',nType,testList
    
    initial_value=0
    list_length=14
    #sample_list = [ initial_value for i in range(10)]
    temp_list = [initial_value]*list_length
    nRet=0
    nTmp=0
    if bTest:  print testList
    nValue= int(testList[0][0:3])
    nType = nValue/36
    if nType==3:#It is Feng
        return nRet
    nLen1 =len(testList)
    for kk in range(1,nLen1):
        #print testList[kk][0:3]
        nTmp=int(testList[kk][0:3])
        if nType==nTmp/36:
            temp_list[kk]=nTmp/4-nValue/4
        else:
            temp_list[kk]=100
    
    #print temp_list
    #if ((-2 in temp_list) and (-1 in temp_list)) or ((-1 in temp_list) and (1 in temp_list)) or ((1 in temp_list) and (2 in temp_list)):
    chi_list=[]
    if (-2 in temp_list) and (-1 in temp_list):
        chi_list.append(temp_list.index(-2))
        chi_list.append(temp_list.index(-1))

    if (-1 in temp_list) and (1 in temp_list):
        chi_list.append(temp_list.index(-1))
        chi_list.append(temp_list.index(1))

    if (1 in temp_list) and (2 in temp_list):
        chi_list.append(temp_list.index(1))
        chi_list.append(temp_list.index(2))
    nLen = len(chi_list)
    str1=''
    if nLen>1:
        nRet=1
        if nRoleType==1:
            return nRet
        for kk in range(0,nLen,2):
            str1+= ',  ('+str((kk+2)/2)+') '+testList[chi_list[kk]][4:]+'-'+testList[chi_list[kk+1]][4:]
    else:
        return nRet
    #print str1[1:]
    if nRoleType==1:
        return nRet


    if nLen>2:
        nSe = int(raw_input(str1[1:]+':'))
        if nSe <  (nLen+2)/2:     
            testList.append(testList[chi_list[2*(nSe-1)]])
            testList.append(testList[chi_list[2*(nSe-1)+1]])
            #print testList
    elif nLen==2:
    	  testList.append(testList[chi_list[0]])
    	  testList.append(testList[chi_list[1]])     
    
    if bTest:  print testList
     
    return nRet

def Judge_GangPai(temp_list):
    nRet=0  
    if bTest:  print 'Judge_GangPai'
    if bTest:  print temp_list
    nLen1= len(temp_list)
    if nLen1<5:
        return nRet
    for kk in range(1,nLen1):
        if temp_list[0][4:]==temp_list[kk][4:]:
            if kk<nLen1-2:
                if temp_list[0][4:]==temp_list[kk+1][4:] and temp_list[0][4:]==temp_list[kk+2][4:]:
                    temp_list.append(temp_list[kk])
                    temp_list.append(temp_list[kk+1])
                    temp_list.append(temp_list[kk+2])
                    nRet=3
                    break
    if bTest:  print temp_list
    return nRet


def Judge_PengPai(temp_list):
    nRet=0  
    if bTest:  print 'Judge_PengPai'
    if bTest:  print temp_list
    nLen1= len(temp_list)
    for kk in range(1,nLen1):
        if temp_list[0][4:]==temp_list[kk][4:]:
            if kk<nLen1-1:
                if temp_list[0][4:]==temp_list[kk+1][4:]:
                    temp_list.append(temp_list[kk])
                    temp_list.append(temp_list[kk+1])
                    nRet=2
                    break
    if bTest:  print temp_list
    return nRet
###############Judge_HuPai######################################

def Judge_HuPai_Type(temp_list,ret):
    
    if ret>1:
        return ret

    nRet=0 
    nLen = len(temp_list)
    if nLen==2:
        if temp_list[0]==temp_list[1]:
            ret+=1
        else:
            ret=9
    elif nLen==3:
        if temp_list[0]==temp_list[1]:
            if temp_list[1]!=temp_list[2]:
                ret=9
        else:
            if temp_list[0] == temp_list[1]-1 and temp_list[1] == temp_list[2]-1:
                ret=ret
            else:
                ret=9
    elif nLen>3:
        if temp_list[0]<temp_list[1]:
            nTemp1 = temp_list[0]+1
            nTemp2 = temp_list[0]+2
            if (nTemp1 in temp_list) and (nTemp2 in temp_list):
                temp_list.remove(temp_list[0])
                temp_list.remove(nTemp1)
                temp_list.remove(nTemp2)
                # print temp_list
                ret = Judge_HuPai_Type(temp_list,ret)
            else:
                ret=9
        else:
           if temp_list[0]==temp_list[1] and temp_list[1]==temp_list[2]:
               #print 'XXX234'
               
               if nLen>3:
                  
                  if temp_list[3]- temp_list[2]>1:
                      del temp_list[0:3]
                      #print temp_list
                      ret=Judge_HuPai_Type(temp_list,ret)
                  elif (temp_list[3]- temp_list[2]==1) :
                      #print 'XXX345'
                      temp_list1=temp_list[:]
                      del temp_list1[0:3]
                      nRet=Judge_HuPai_Type(temp_list1,ret)
                      if nRet>1 and nLen%3==2 :
                          #temp_list.remove(temp_list[0])
                          #temp_list.remove(temp_list[0])
                          del temp_list[0:2]
                          ret=Judge_HuPai_Type(temp_list,ret)
                      else:
                          ret = nRet
           elif temp_list[0]==temp_list[1]:
               if nLen>3 and nLen%3==2:
                   
                   del temp_list[0:2]
                   #temp_list.remove(temp_list[0])
                   #temp_list.remove(temp_list[0])
                   #print temp_list
                   ret+=1
                   ret=Judge_HuPai_Type(temp_list,ret)
               else:
                   ret=9
               
    #print ret
    return  ret   
     

def Judge_HuPai(temp_list):
    nRet=0  
    temp_list.sort()
    nType_pre=-1
    list_type=[]
    nLen =len(temp_list)
    for kk in range(0,nLen):
        nTmp=int(temp_list[kk][0:3])
        nType_cur = nTmp/36
        #print temp_list[kk]
        if nType_pre==-1:
            nType_pre=nType_cur
        if nType_pre==nType_cur:
            list_type.append(((nTmp%36)/4)+1)
        else:
            #print list_type
            nLen = len(list_type)
            if nLen%3==1:
                nRet=9
                return nRet
            nRet = Judge_HuPai_Type(list_type,nRet)
            #print nRet
            if nRet>1:
                return nRet
            del list_type[:]#clear list_type
            nType_pre=nType_cur
            list_type.append(((nTmp%36)/4)+1)
    
    nLen = len(list_type)
    if nLen%3==1:
        nRet=0
    elif nLen>1:
        nRet = Judge_HuPai_Type(list_type,nRet)
        #print nRet
        if nRet>1:
            nRet=9  
    return nRet

###################Judge_HuPai end##################################
#print '____________________'
#print '| 1 | 1 | 1 | B | F |'
#print '| T | B | W | e | a |'
#print '|___|___|___|___|___|'
#print '|(1)|(2)|(3)|(4)|(5)|'
###################show pai Start##################################

str_zm=['Q','W','E','R','T','Y','U','I','O','P','H','J','K','L']

def ShowPai(temp_list1,type,strCard=''):
    
    #if True:
    #    return
    temp_list=temp_list1[:]
    if type==3:
        temp_list.append(strCard)
    nLen = len(temp_list)
    if nLen<1:
        return
    
    str1='  _'
    str2='  |'
    str3='  |'
    str4='  |'
    str5='   '
    str0='   '
    
    for kk in range(0,nLen):
        if type==1:
            if kk%3==0 and kk>0:
                str1+='  _'
                str2+='  |'
                str3+='  |'
                str4+='  |'
        
        str1+='____'
        str2+=' '+temp_list[kk][4:5]+' |'
        str3+=' '+temp_list[kk][6:7]+' |'
        str4+='___|'
        #print kk
        if type==3 and kk==nLen-1:
            str0+='<->  '
        else:
            if type==3:
                str0+='    '
            else:
                str0+=' '+str_zm[kk]+'  '
        
        if type==3 and kk==nLen-2:
            str0+='    '
            str1+='   _'
            str2+='   |'
            str3+='   |'
            str4+='   |'
        
        if kk>9:
            if kk==10:
                str5+=' '
            if type==3 and kk==nLen-1:
                str5+='AAA'
            else:
                str5+=str(kk)+'  '
        else:
            if type==3 and kk==nLen-1:
                str5+='AAA'
            else:
                str5+=' '+str(kk)+'  '

    #if type==0:
    #    print str0    

    print str1
    print str2
    print str3
    print str4
    #if type==0:
    #    print str5    
    if type==0 or type==3:
        print str0    

def GetPaiNum(strInput):
     nLen = len(strInput)
     #print nLen 
     nNum = -2
     if nLen==0:
         return -1
     if strInput.isdigit()==False:
         if nLen>1:
             return -2
         strInput = strInput.upper()
         if strInput in str_zm:
             nNum = str_zm.index(strInput)
             #return nNum
     else:
         nNum=int(strInput)
     
     return nNum

###################show pai End##################################


###################Get data##################################
'''
def Get_chipeng_data(li_gr,strCard):
    nTmp=0  
    print li_ret
    
    nTmp=int(strCard[0:3])
    nType_cur = nTmp/36
    nNum = ((nTmp%36)/4)+1
    
    #temp_list.sort()
    #nType_cur=0
    nRet=-1
    list_tmp=li_gr[nType_cur][:]
    
    nLen =len(list_tmp)#4
    for mm in range(0,nLen):
        for nn in range(0,len(list_tmp[mm])):
            if list_tmp[mm][0]==100:
                if list_tmp[mm][nn]==nNum:
                    if list_tmp[mm][1]==list_tmp[mm][2]:
                        nRet=0
                    else:
                        nRet=nn
    
    
    return nRet
'''                        

def Get_Card_Value(li_card,nCard):
    
    
    nTmp=0
    nRet=0
    
    nTmp = nCard - li_card[1]
    if bTest:  print 'Get_Card_Value------000: ',nTmp,nCard,li_card[1]
    if li_card[1]==li_card[2]:
        
        if nTmp==1 or nTmp==-1:  # x-1 xxx x+1 
            nRet=30
        elif nTmp==2 or nTmp==-2: #x-2 xxx x+2 
            nRet=20
    elif li_card[1]+1==li_card[2]:
        if nTmp==-1 or nTmp==3: #  x-1  x_x+1_x+2 x+3
            nRet=17
        elif nTmp==0 or nTmp==2: #  x  x_x+1_x+2 x+2
            nRet=15
        elif nTmp==1 : #  x+1  x_x+1_x+2
            nRet=10
    
    if bTest:  print 'Get_Card_Value------li_card: ',nRet,li_card,nCard
    
    return nRet    
    


def Get_chupai_data(temp_list,li_gr,li_ret,li_cp):
      
    #print li_ret
    nType=li_ret[0]
    strCard = li_ret[1]
    #if nType==0:
    	  
    
    nCard=int(strCard[0:3])
    nType_Card = nCard/36
    nNum = ((nCard%36)/4)+1
    
    temp_list.sort()
    #nType_cur=0
    nRet=-1
    nMin=100
    nTmp=0
    nTmp0=0
    l_min_tmp=[]
    l_min_tmp_2=[]
    l_cp_tmp=[]
    #list_tmp=li_gr[nType_cur][:]
    
    #nLen =len(list_tmp)#4
    nFind_Flag=0
    nCount_100=0
    nCount_Total=0
    #chi ,peng Num
    nCount_fu=(14 - len(temp_list))/3
    
    for jj in range(0,4):
        for mm in range(0,len(li_gr[jj])):
            nCount_Total+=li_gr[jj][mm][0]
            if li_gr[jj][mm][0]==100:
                nCount_100+=1
            for nn in range(0,len(li_gr[jj][mm])):
                nTmp0=li_gr[jj][mm][0]
                nTmp=li_gr[jj][mm][nn]
                if nTmp0==100:
                    #nCount_100+=1
                    if nType==0 and nFind_Flag==0: 
                        if nTmp==nNum:
                        	  l_cp_tmp=li_gr[jj][mm][:]
                        	  l_cp_tmp.append(jj)
                if nMin>nTmp0:
                    nMin=nTmp0
                    l_min_tmp_2=l_min_tmp[:]
                    l_min_tmp=li_gr[jj][mm][:]
                    l_min_tmp.append(jj)
                    
    
    
    
            
    
    #print 'mj_list_init:',mj_list_init
    if bTest:  print 'l_cp_tmp:',l_cp_tmp

    li_cp_01=[]
    nPPP=0
    if len(l_cp_tmp)>5:
    	  if l_cp_tmp[1]==l_cp_tmp[2]:
    	  	  nTmp=l_cp_tmp[-1]*36+(l_cp_tmp[1]-1)*4
    	  	  li_cp_01 =mj_list_init[nTmp:nTmp+4]
    	  	  nPPP=1
    	  else:
    	  	  nTmp=l_cp_tmp[-1]*36+(l_cp_tmp[1]-1)*4
    	  	  li_cp_01 =mj_list_init[nTmp:nTmp+12]
    	  	  nPPP=2
    	  
    if bTest:  print 'li_cp_01:',li_cp_01
    

    
    
    if bTest:  print 'nCount_fu,nCount_100,l_min_tmp,l_min_tmp_2:',nCount_fu,nCount_100,l_min_tmp,l_min_tmp_2
    
    nCount_Total+=nCount_fu*100
    if nCount_Total==440:###hu
        print 'hu!hu!hu!_test shoud is right!'
        exit(0)
    
    nCount_fu+=nCount_100
    
    
    bDuizi=0
    if nCount_fu==3:
        if l_min_tmp[0]==40: ##dui zi
            if len(l_min_tmp_2)==0:
                bDuizi=1    
            else:
                if l_min_tmp_2[0]>40:
                    l_min_tmp=l_min_tmp_2[:]
                    nTmp = l_min_tmp[0]%2
                    if nTmp==1:
                        l_min_tmp[1]=l_min_tmp[3]

    if bDuizi==1:
        for jj in range(0,4):
            for mm in range(0,len(li_gr[jj])):
                if li_gr[jj][mm][0]==100:
                    nTmp0=li_gr[jj][mm][0]
                    if nTmp0==40:
                        continue
                    if nMin>nTmp0:
                        nMin=nTmp0
                        l_min_tmp_2=l_min_tmp[:]
                        l_min_tmp=li_gr[jj][mm][:]
                        l_min_tmp.append(jj)
    
    #############modify finally card Select#######
    bMinFlag=0
    nMin=100
    if nCount_fu==4 and nCount_100>0 and l_min_tmp[0]<10:
        for jj in range(0,3):
            for mm in range(0,len(li_gr[jj])):
                
                if li_gr[jj][mm][0]<100:
                    nTmp0=li_gr[jj][mm][0]
                    if bTest:  print 'li_gr[jj][mm]---------:',l_min_tmp[-1],li_gr[jj][mm]
                    if li_gr[jj][mm][1]==l_min_tmp[1] and jj == l_min_tmp[-1]:
                        continue
                    if nMin>nTmp0:
                        nMin=nTmp0
                        bMinFlag=1
                        
                        #l_min_tmp_2=l_min_tmp[:]
                        l_min_tmp_2=li_gr[jj][mm][:]
                        l_min_tmp_2.append(jj)
                        if bTest:  print 'l_min_tmp_2_xxxx---------:',l_min_tmp_2
                        
    if bMinFlag==1:    
        if bTest:  print 'l_min_tmp---------:',l_min_tmp
        if bTest:  print 'l_min_tmp_2-------:',l_min_tmp_2
        l_min_gr=[]
        l_min_gr.append(l_min_tmp)
        l_min_gr.append(l_min_tmp_2)
        l_max_sel=[]
        nMax=0
        nSel=1
        for kk in range(0,2):
            l_min_gr_tmp = l_min_gr[kk]
            for jj in range(0,3):
                for mm in range(0,len(li_gr[jj])):
                    if li_gr[jj][mm][0]==100:
                        if jj==l_min_gr_tmp[-1]:
                            nTmp = Get_Card_Value(li_gr[jj][mm],l_min_gr_tmp[1])
                            if nMax<nTmp:
                                nMax=nTmp
                                nSel=kk
                            
                        #nCount_100+=1
        if nMax>0 and nSel==0:
            if bTest:  print 'l_min_tmp--XXXXXXX----swap:'
            l_min_tmp = l_min_tmp_2
    ################################

    if bTest:  print 'l_min_tmp:',l_min_tmp
    li_qp=[]    
    if len(l_min_tmp)>5:
    	  nTmp=l_min_tmp[-1]*36+(l_min_tmp[1]-1)*4
    	  #print 'nTmp:',nTmp
    	  li_qp =mj_list_init[nTmp:nTmp+4]
    if bTest:  print 'li_qp:',li_qp
    jj=0
    strQp=''
    n3P_Count=0
    #nQp=0
    while True:
    	  strTmp = temp_list[jj]
    	  if strTmp in li_qp:
    	  	  strQp=strTmp
    	  	  temp_list.remove(strQp)
    	  	  if bTest:  print 'strQp:',strQp
    	  	  jj-=1
    	  	  li_qp=['','','','']
    	  	  #nQp+=1
    	  elif n3P_Count<3:
    	  	  if strTmp in li_cp_01:
    	  	  	   
    	  	  	  temp_list.remove(strTmp)
    	  	  	  li_cp.append(strTmp)
    	  	  	  if nPPP==2:
    	  	  	  	  nTmp = li_cp_01.index(strTmp)
    	  	  	  	  nTmp=(nTmp/4)*4
    	  	  	  	  li_cp_01[nTmp:nTmp+4]=['','','','']
    	  	  	  n3P_Count+=1
    	  	  	  jj-=1
    	  jj+=1
    	  if jj>len(temp_list)-1:
    	  	  break
    	  
    
    temp_list.append(strQp)
    
    if bTest:  print 'temp_list:',temp_list
    if bTest:  print 'li_cp:',li_cp
    
    return nPPP+1



def Think_By_Computer(temp_list,li_ret,li_cp):
    nRet=0  
    #print li_ret
    nType=li_ret[0]
    strCard = li_ret[1]
    
    temp_list.sort()
    nType_pre=-1
    nType_cur=0
    nLevel=0
    nScore=0
    list_type=[]
    list_total=[]
    list_tmp=[]
    li_ret_gr=[]
    #li_ret_tmp=[]
    
    l_gr = [[] for i in range(4)]
    li_ret_gr = [[] for i in range(4)]
    nLen =len(temp_list)
    for kk in range(0,nLen):
        nTmp=int(temp_list[kk][0:3])
        nType_cur = nTmp/36
        #print temp_list[kk]
        if nType_pre==-1:
            nType_pre=nType_cur
        if nType_pre==nType_cur:
            l_gr[nType_cur].append(((nTmp%36)/4)+1)
        else:
            #print list_type
            if bTest:  print l_gr[nType_pre]
            #del li_tmp[:]
            li_tmp = l_gr[nType_pre][:]
            nLen = len(li_tmp)
            
            
            nRet = mj_mode.Get_Group_By_Mode(li_tmp,li_ret_gr[nType_pre],nLevel)
            
            
            
            #print nRet
            
            nScore +=nRet
            #del list_type[:]#clear list_type
            nType_pre=nType_cur
            l_gr[nType_cur].append(((nTmp%36)/4)+1)
    
    nLen = len(l_gr[nType_cur])
    if nLen>0:
        #del li_tmp[:]
        li_tmp = l_gr[nType_cur][:]
        if nType_cur==3:
            nRet = mj_mode.Get_Feng_By_Mode(li_tmp,li_ret_gr[nType_cur],nLevel)
        else:
        	  nRet = mj_mode.Get_Group_By_Mode(li_tmp,li_ret_gr[nType_cur],nLevel)
        nScore +=nRet
    
    
    #print l_gr
    #print nScore,li_ret_gr
    if nType==1:
        if bTest:  print 'Get_chupai_data temp_list:',temp_list
        nRet = Get_chupai_data(temp_list,li_ret_gr,li_ret,li_cp)
        #print 'nRet:',nRet
        return nRet
    elif nType==0:
    	  
    	  
    	  if nScore - li_ret[2]<30: #no chi,no peng
    	      print 'no chi,no peng!'
    	      return -1
    	      #return -1
    	  elif nScore - li_ret[2]<50: #no chi,no peng
    	      print 'good!'
    	  elif nScore - li_ret[2]<120: #no chi,no peng
    	      print 'very good!'
    	  #print nScore,li_ret[2]
    	  nRet = Get_chupai_data(temp_list,li_ret_gr,li_ret,li_cp)
    	  return nRet
    
    if bTest:  print 'temp_list333:',temp_list
    
    return nScore


##################################
def Get_Com_Oper(list_card,li_ret,li_cp):
    
    #print 'Computer is thinking......Please wait!'
    li_tmp=list_card[:]
    li_tmp_ret=[]

    nType=li_ret[0]
    strCard = li_ret[1]
    
    if nType==0:
        print 'Computer is thinking for discard card of player......Please wait!'
    else:
        print 'Thinking for draw card......Please wait!'
    
    
    ret=Judge_HuPai(li_tmp)
    if ret==1:
    	  print 'hu!hu!hu!hu!!'
    	  
    	  dict_info['computer_win_times']+=1
    	  nTemp=100
    	  if nType==1:
    	      nTemp=200
    	  dict_info['computer_score']+=nTemp
    	  write_cfg()
    	  return 100

    nFlag=0
    nScore_Cur=0
    if bTest: print 'temp_list001:',list_card,nType
    if nType==0:
        
        li_tmp=list_card[:]
        if 1 == Judge_ChiPai(li_tmp,1):
            nFlag=1
            print 'I may chi pai!'

        elif 2 == Judge_PengPai(li_tmp):
            nFlag=2
            print 'I may peng pai!'
        #go to mo pai
        if nFlag <1:
        	  list_card.remove(strCard)
        	  return 0
            ###return 0
        
        li_ret[0]=-1
        if bTest: print 'temp_list002:',list_card
        li_tmp=list_card[:]
        li_tmp.remove(strCard)
        nScore_Cur= Think_By_Computer(li_tmp,li_ret,li_cp)   
        
        if bTest:  print 'temp_list003:',list_card

         
    
    li_ret[0]=nType
    li_ret.append(nScore_Cur)
    
    nScore_next= Think_By_Computer(list_card,li_ret,li_cp)
    
    if bTest:  print 'temp_list004:',list_card
    if nType==1:
        return nScore_next
    else:
    	  if nScore_next==-1:
    	      list_card.remove(strCard)
    	      return 0 
    return nScore_next  



def Start_Play_With_Computer():
    
    index =0
    nPlayer=0
    nComputer=1
    nRole=0
    global bTest
    bTest=True
    
    strRole=['Player','Computer']
    
    li_card = [[] for i in range(2)]
    
    
    for ii in range(2):
        for jj in range(0,13):
            li_card[ii].append(xipai_list[index])
            index+=1
    
    
    #print li_card[nRole]
    
    cp_list=[[] for i in range(2)]
    str1=''
    #print index
    strCurCard=xipai_list[index]
    nCount=0
    
    
    while True:
        
        nRole=nCount%2
        
        
        str1=''
        if bTest: print 'Card index:', index
        if index>=135: 
            print 'Card is end!'
            break
        print strRole[nRole]+'\'s pai: '
        
        
        ShowPai(cp_list[nRole],1)
    
        li_card[nRole].sort()
        ShowPai(li_card[nRole],3,strCurCard)
        
        #index+=1
        nSelect=-1
        #print strRole[(nRole+1)%2]+' chu pai:    '+ strCurCard[4:]
        
        if nRole==nComputer:
            li_ret=[]
            #temp_list=li_card[
            #li_card[nRole]=['004 2 T', '005 2 T', '008 3 T', '009 3 T', '012 4 T', '013 4 T', '014 4 T',  '017 5 T', '053 5 B', 
            #       '057 6 B', '060 7 B', '065 8 B', '118 X i']
            #print li_card[nRole]
            #strCurCard = '062 7 B'
            
            li_ret.append(0)
            li_ret.append(strCurCard)
            li_card[nRole].insert(0, strCurCard)
            nSelect = Get_Com_Oper(li_card[nRole],li_ret,cp_list[nRole])
            
            print 'My Seclect:',nSelect
            
            if nSelect==1:
            	  strCurCard = li_card[nRole].pop()
            	  print 'Get pai,chu pai:',strCurCard
            elif nSelect==2:
            	  strCurCard = li_card[nRole].pop()
            	  print 'peng pai,chu pai:',strCurCard
            elif nSelect==3:
            	  strCurCard = li_card[nRole].pop()
            	  print 'chi pai,chu pai:',strCurCard
            elif nSelect==100:
            	  print 'hahaha!,hu pai!!!!'
            	  break
            else:
            	  print 'this is a bad card,no need! go on:',strCurCard
            	  del li_ret[:]
            	  index+=1
            	  strCurCard=xipai_list[index]
            	  print 'Computer mo pai:',strCurCard
            	  li_ret.append(1)
            	  li_ret.append(strCurCard)
            	  li_card[nRole].insert(0, strCurCard)
            	  nSelect = Get_Com_Oper(li_card[nRole],li_ret,cp_list[nRole])
            	  if nSelect==100:
            	      print 'hahaha!,hu pai!!!!'
            	      break
            	      
            	  strCurCard = li_card[nRole].pop()
            #print temp_list,strCurCard
            #print cp_list[nRole]
            #nSelect = Get_Com_Oper(li_card[nComputer],strCurCard,0,li_ret)
            if bTest:
                print strRole[nRole]+'\'s pai: '
                ShowPai(cp_list[nRole],1)
                ShowPai(li_card[nRole],0)
            nCount+=1
            #if nSelect==0:
            #    index+=1
            continue
        
        #index+=1
        #print '[Q] mo;','[W] chi;','[E] peng;','[R] Gang;','[Y] hu;','[U]C Pai;','[P] exit.'
        strNum =raw_input('[Q]mo [W]chi [E]peng [R]Gang [Y]hu [P]exit. Please select:')
        nSelect = GetPaiNum(strNum)
            
        if nSelect==-2:
            #index-=1
            continue
        elif nSelect==-1:
            nSelect=0
        
        if nSelect not in [0,1,2,3,5,6,9,99]:
            #index-=1
            continue
        
        if nSelect==0:
            index+=1
            print strRole[nRole]+' mo pai: '+ xipai_list[index][4:]
            #li_card[nRole][0] = xipai_list[index]
            li_card[nRole].append(xipai_list[index])
            #list.insert(index, obj
            
            str1=''
            print 'Player\'s pai: '
            
            li_card[nRole].sort()
            
            ShowPai(li_card[nRole],0)
            
            #print 'if you zi mo!Please input 100!'
            #nSelect = int(raw_input('Player chu pai number(0-13):'))
            strNum =raw_input('Player chu pai Select(0-13):')
            nSelect = GetPaiNum(strNum)
            
            if nSelect>len(li_card[nRole])-1:
                nSelect=-1
            
            if nSelect==-2:
                nSelect=-1
            if nSelect==100:
            	  tempList=li_card[nRole][:]
            	  ret=Judge_HuPai(tempList)
            	  if ret==1:
            	      print 'zi mo!'
            	      dict_info['user_win_times']+=1
            	      dict_info['user_score']+=200
            	      write_cfg()
            	      break
                #ret=Judge_HuPai(tempList)
                #if ret==1:
                #	   print 'zi mo!'
                #	   break
                #else:
                #	   print 'You zi mo Fail!'
                #	   nSelect = int(raw_input('Player chu pai Select(0-13):'))
                
            if nSelect==-1:
                strCurCard = xipai_list[index]
                li_card[nRole].remove(xipai_list[index])
                
            else:
                strCurCard = li_card[nRole][nSelect]
                li_card[nRole].remove(li_card[nRole][nSelect])
                
                
            #li_card[nRole][nSelect]=''
        elif nSelect==1 or nSelect==2 or nSelect==3:
            tempList=li_card[nRole][:]
            #tempList[0] = xipai_list[index]
            
            
            tempList.insert(0, strCurCard)
            #tempList.insert(0, xipai_list[index])
           
            if nSelect==1:
                #tempList=['010 3 T', '004 2 T', '005 2 T', '008 3 T', '009 3 T', '012 4 T', '013 4 T', '014 4 T', '014 4 T',  '017 5 T', '018 5 T', '053 5 B', 
                #       '059 6 B', '060 7 B']
                #print tempList
                
                if 1 != Judge_ChiPai(tempList): #tempList
                    print 'You can not chi '
                    #index-=1
                    continue
                print tempList
                cp_list[nRole].append(tempList[0])
                cp_list[nRole].append(tempList[-1])
                cp_list[nRole].append(tempList[-2])
                
                #li_card[nRole].remove(tempList[0])
                li_card[nRole].remove(tempList[-1])
                li_card[nRole].remove(tempList[-2])
                #cp_list[nRole].sort()
                #print cp_list[nRole] 
                
                #tempList.
            elif nSelect==2: #peng pai
                #tempList=li_card[nRole][:]
                #tempList[0] = xipai_list[index]
                
                #tempList=[ '012 4 T','000 1 T', '004 2 T', '005 2 T', '008 3 T', '009 3 T', '013 4 T', '014 4 T', '014 4 T',  '017 5 T', '018 5 T', '053 5 B', 
                #       '059 6 B', '060 7 B']
                #print temp_list
                
                if 2 != Judge_PengPai(tempList):
                    print 'You can not peng'
                    #index-=1
                    continue
                #print temp_list
                cp_list[nRole].append(tempList[0])
                cp_list[nRole].append(tempList[-1])
                cp_list[nRole].append(tempList[-2])
                
                #li_card[nRole].remove(tempList[0])
                li_card[nRole].remove(tempList[-1])
                li_card[nRole].remove(tempList[-2])
                #cp_list[nRole].sort()
                #print cp_list[nRole] 
                      
            elif nSelect==3: #gang pai
                #tempList=li_card[nRole][:]
                #tempList[0] = xipai_list[index]
                
                #tempList=[ '012 4 T','000 1 T', '004 2 T', '005 2 T', '008 3 T', '009 3 T', '013 4 T', '014 4 T', '014 4 T',  '017 5 T', '018 5 T', '053 5 B', 
                #       '059 6 B', '060 7 B']
                #print temp_list
                
                if 3 != Judge_GangPai(tempList):
                    print 'You can not gang'
                    #index-=1
                    continue
                #print temp_list
                cp_list[nRole].append(tempList[0])
                cp_list[nRole].append(tempList[-1])
                cp_list[nRole].append(tempList[-2])
                cp_list[nRole].append(tempList[-3])
                
                #li_card[nRole].remove(tempList[0])
                li_card[nRole].remove(tempList[-1])
                li_card[nRole].remove(tempList[-2])
                li_card[nRole].remove(tempList[-3])
                #cp_list[nRole].sort()
                #print cp_list[nRole] 
 
            #li_card[nRole][0] = xipai_list[index]
            
            str1=''
            print 'Player\'s pai: '
            
                   
            li_card[nRole].sort()
            ShowPai(li_card[nRole],0)
            while True:
                strNum =raw_input('Player chu pai Select(0-13):')
                nSelect = GetPaiNum(strNum)
                
                if nSelect<len(li_card[nRole]) and nSelect>-1:
                    strCurCard=li_card[nRole][nSelect]
                    li_card[nRole].remove(li_card[nRole][nSelect])
                    break
            
        elif nSelect==5:
            tempList=li_card[nRole][:]
            #tempList[0] = xipai_list[index]
            tempList.insert(0, xipai_list[index])
    
            
            ret = Judge_HuPai(tempList)
            if ret==1:
                print 'Hu!Hahaha!'
                dict_info['user_win_times']+=1
                dict_info['user_score']+=100
                write_cfg()
                break
            else:
                print 'You cannot Hu!Go on'
                index-=1
                #continue
            
           
        elif nSelect==6:
            print strRole[nComputer]+'\'s pai: '
            ShowPai(cp_list[nComputer],1)
            ShowPai(li_card[nComputer],0)
            strNum =raw_input('Please input any key:')
            continue
            #break 
        elif nSelect==99:
            #global bTest
            if bTest:
                bTest=False
            else:
                bTest=True
            
            mj_mode.bTest=bTest

            continue

        elif nSelect==9:
            break 
        nCount+=1
        #os.system('cls')






################


#####################
def Start_Play_By_Self():
    kk=0
    index =0
    player_list = [initial_value for i in range(13)]
    for jj in range(0,13):
        player_list[jj]= xipai_list[index]
        index+=1
    
    #computer_list = [initial_value for i in range(13)]
    #for jj in range(0,13):
    #    computer_list[jj]= xipai_list[index]
    #    index+=1
    
    
    #print player_list
    
    cp_list=[]
    str1=''
    #print index
    
    while True:
        
        str1=''
        print 'Player\'s pai: '
        
        
        ShowPai(cp_list,1)
    
        player_list.sort()
        ShowPai(player_list,0)
        
        index+=1
    
        print 'Computer chu pai:    '+ xipai_list[index][4:]
        
        print '[Q] mo;','[W] chi;','[E] peng;','[R] Gang;','[Y] hu;','[P] exit.'
        strNum =raw_input('Please select:')
        nSelect = GetPaiNum(strNum)
    
        if nSelect==-2:
            index-=1
            continue
        elif nSelect==-1:
            nSelect=0
        
        if nSelect not in [0,1,2,3,5,9]:
           index-=1
           continue
        
        if nSelect==0:
           index+=1
           print 'Player mo pai: '+ xipai_list[index][4:]
           #player_list[0] = xipai_list[index]
           player_list.append(xipai_list[index])
           #list.insert(index, obj
           
           str1=''
           print 'Player\'s pai: '
           
           player_list.sort()
           
           ShowPai(player_list,0)
           
           #print 'if you zi mo!Please input 100!'
           #nSelect = int(raw_input('Player chu pai number(0-13):'))
           strNum =raw_input('Player chu pai Select(0-13):')
           nSelect = GetPaiNum(strNum)
    
           if nSelect>len(player_list)-1:
               nSelect=-1
     
           if nSelect==-2:
               nSelect=-1
           if nSelect==100:
           	   tempList=player_list[:]
               #ret=Judge_HuPai(tempList)
               #if ret==1:
               #	   print 'zi mo!'
               #	   break
               #else:
               #	   print 'You zi mo Fail!'
               #	   nSelect = int(raw_input('Player chu pai Select(0-13):'))
               
           if nSelect==-1:
               player_list.remove(xipai_list[index])
           else:
               player_list.remove(player_list[nSelect])
           #player_list[nSelect]=''
        elif nSelect==1 or nSelect==2:
           tempList=player_list[:]
           #tempList[0] = xipai_list[index]
           tempList.insert(0, xipai_list[index])
     
           if nSelect==1:
               #temp_list=['010 3 T', '004 2 T', '005 2 T', '008 3 T', '009 3 T', '012 4 T', '013 4 T', '014 4 T', '014 4 T',  '017 5 T', '018 5 T', '053 5 B', 
               #       '059 6 B', '060 7 B']
               #print temp_list
               
               if 1 != Judge_ChiPai(tempList): #tempList
                   print 'You can not chi '
                   index-=1
                   continue
               #print temp_list
               cp_list.append(tempList[0])
               cp_list.append(tempList[-1])
               cp_list.append(tempList[-2])
               
               #player_list.remove(tempList[0])
               player_list.remove(tempList[-1])
               player_list.remove(tempList[-2])
               #cp_list.sort()
               #print cp_list 
               
               #tempList.
           else: #peng pai
               #tempList=player_list[:]
               #tempList[0] = xipai_list[index]
               
               #tempList=[ '012 4 T','000 1 T', '004 2 T', '005 2 T', '008 3 T', '009 3 T', '013 4 T', '014 4 T', '014 4 T',  '017 5 T', '018 5 T', '053 5 B', 
               #       '059 6 B', '060 7 B']
               #print temp_list
    
               if 2 != Judge_PengPai(tempList):
                   print 'You can not peng'
                   index-=1
                   continue
               #print temp_list
               cp_list.append(tempList[0])
               cp_list.append(tempList[-1])
               cp_list.append(tempList[-2])
               
               #player_list.remove(tempList[0])
               player_list.remove(tempList[-1])
               player_list.remove(tempList[-2])
               #cp_list.sort()
               #print cp_list 
                      
           #player_list[0] = xipai_list[index]
           
           str1=''
           print 'Player\'s pai: '
           
                  
           player_list.sort()
           ShowPai(player_list,0)
           while True:
               strNum =raw_input('Player chu pai Select(0-13):')
               nSelect = GetPaiNum(strNum)
        
               if nSelect<len(player_list) and nSelect>-1:
                   player_list.remove(player_list[nSelect])
                   break
           
        elif nSelect==5:
            tempList=player_list[:]
            #tempList[0] = xipai_list[index]
            tempList.insert(0, xipai_list[index])
    
            
            #temp_list=['000 1 T', '004 2 T', '005 2 T', '008 3 T', '009 3 T', '012 4 T', '013 4 T', '014 4 T', '014 4 T',  '017 5 T', '018 5 T', '053 5 B', 
            #       '059 6 B', '060 7 B']
            #print temp_list
            ret = Judge_HuPai(tempList)
            if ret==1:
                print 'Hu!'
                break
            else:
                print 'You cannot Hu!Go on'
                index-=1
                #continue
            
           
        elif nSelect==9:
            break 
        #os.system('cls')





###############main()###################




Start_Play_With_Computer()





