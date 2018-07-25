import itertools
nMjLen=9
temp_list1 = [1,2,2,3,3,3,4,4,5,5,5,9,9]


bTest=False

list_mode=[]
list_Num = [i for i in range(0,14)]
dict_Type_Mode_Normal={1:3,2:4,3:5,4:5,5:5,6:5,7:5,8:4,9:3,'02':20,'024':25,'01':30,'00':40,'022':60,'002':61,'011':70,'001':71,'012':100,'000':100}
nLevel=0

group_list1=[]
group_list0=[]

def Count_By_Mode(temp_list,group_list,ret):
    #print 'temp_list:',temp_list
    
    nLen = len(temp_list)
    if nLen==0:
    	  return 0
    elif nLen==1:
    	  return dict_Type_Mode_Normal.get(temp_list[0],0)
    elif nLen>nMjLen:
    	  return 0
        
    #print list_mode[nLen]
    list_tmp=list_mode[nLen][:]
    nMode_Num = len(list_mode[nLen])
    lCount=[0,0]
    lMode_Len=[0,0]
    
    nTemp=0
    nRet=0
    lMode_count=[]
    nCount=0
    for nn in range(0,nMode_Num):
  	    
    	  for ii in range(0,2):
    	  	  
    	  	  #print list_tmp[nn][ii]
    	  	  
    	  	 
    	  	  lMode_Len[ii] = len(list_tmp[nn][ii])
    	  	  #print  nMode_Num,lMode_Len[ii]
    	  	  strMode=''
    	  	  list_dg=[]
    	  	  for jj in range(0,lMode_Len[ii]):
    	  	  	  
    	  	      if lMode_Len[ii]>3 and lMode_Len[ii]==nLen:
    	  	      	  #print 'nMode_Num; ',nMode_Num
    	  	      	  nTemp = dict_Type_Mode_Normal.get(temp_list[list_tmp[nn][ii][jj]],0)
    	  	      	  lCount[ii]+=nTemp
    	  	      	  continue
    	  	      if lMode_Len[ii]>1:
    	  	      	  #print list_tmp[nn][ii][jj]
    	  	      	  
    	  	      	  #for kk in range(1,lMode_Len[ii]):
    	  	      	  strMode += str(temp_list[list_tmp[nn][ii][jj]]-temp_list[list_tmp[nn][ii][0]])
    	  	      	  list_dg.append(temp_list[list_tmp[nn][ii][jj]])
    	  	      else:
    	  	      	  nTemp = dict_Type_Mode_Normal.get(temp_list[jj],0)
    	  	      	  lCount[ii]+=nTemp
    	  	      	  
    	  	      	  
    	  	      	  
    	  	  
    	  	  if lMode_Len[ii]<1:
    	  	  	  continue
    	  	  #print strMode
    	  	  nTemp = dict_Type_Mode_Normal.get(strMode,0)
    	  	    
    	  	  if nTemp==0 :
    	  	  	  #nTemp = Count_By_Mode(list_dg,0)
    	  	  	  if lMode_Len[ii]==3 and nLen==3:
    	  	  	  	  continue
    	  	  	  if lMode_Len[ii]==2:
    	  	  	  	  #print '1:',temp_list[list_tmp[nn][ii][0]]
    	  	  	  	  #print '2:',temp_list[list_tmp[nn][ii][1]]
    	  	  	  	  nTemp = dict_Type_Mode_Normal.get(temp_list[list_tmp[nn][ii][0]],0) + dict_Type_Mode_Normal.get(temp_list[list_tmp[nn][ii][1]],0)
    	  	  	  	  
    	  	  	  	  lCount[ii]+=nTemp
    	  	  	  else:
    	  	  	  	 #print 'list_dg:',list_dg
    	  	  	  	 if len(list_dg)==0:
    	  	  	  	     continue
    	  	  	  	 elif len(list_dg)==1:
    	  	  	  	     #print 'list_dg:11111111',list_dg
    	  	  	  	     nTemp = dict_Type_Mode_Normal.get(temp_list[list_tmp[nn][ii][0]],0)
    	  	  	  	     lCount[ii]+=nTemp
    	  	  	  	     
    	  	  	  	 nTemp = Count_By_Mode(list_dg,group_list,ret+1)
    	  	  	  	 lCount[ii]+=nTemp
    	  	  else:
    	  	  	  lCount[ii]+=nTemp   	
    	  
    	  nCount = lCount[0]+lCount[1]
    	  
    	  lMode_count.append(nCount)
    	  lCount[0]=0
    	  lCount[1]=0
    	  
    #print lMode_count
    nMax = max(lMode_count)
    #print 'list_tmp:',list_tmp[lMode_count.index(nMax)]
    
    #group_list.append(list_tmp[lMode_count.index(nMax)])
    if ret==0:
        li_tmp = list_tmp[lMode_count.index(nMax)][:]
        
        for j in range(0,2):
            li_gr=[]
            for i in range(0,len(li_tmp[j])):
                li_gr.append( temp_list[li_tmp[j][i]] )
                #group_list0.append( temp_list[li_tmp[j][i]] )
            group_list0.append(li_gr)
        #group_list0.append(list_tmp[lMode_count.index(nMax)][1])
    
    return nMax
    

def Get_Single_By_Mode(temp_list,nLevel):
    #print 'temp_list:',temp_list,len(temp_list)
     
    nLen = len(temp_list)
    if nLen==0:
    	  return -1
    elif nLen==1:
    	  return 0
    for nn in range(0,nLen):
	  	  if nn==0:#first
	  	  	  #print 'first:',temp_list[nn+1]-temp_list[nn]
	  	  	  if temp_list[nn+1]-temp_list[nn]>2:
	  	  	      return nn
	  	  
	  	  elif nn==nLen-1:
	  	  	 
	  	  	  if temp_list[nn]-temp_list[nn-1]>2:
	  	  	      return nn
	  	  else:
	  	  	  #print 'next:',temp_list[nn+1]-temp_list[nn]
	  	  	  if temp_list[nn+1]-temp_list[nn]>2 and temp_list[nn]-temp_list[nn-1]>2:
	  	  	     return nn
    return -1

def Get_three_By_Mode(temp_list,nLevel):
    #print 'temp_list:',temp_list,len(temp_list)
    ret=-1
    nLen = len(temp_list)
    if nLen<3:
    	  return -1
    if nLen==3:
    	  if temp_list[1]-temp_list[0]==1 and temp_list[2]-temp_list[1]==1:  
    	      return 0
    	  elif temp_list[1]-temp_list[0]==0 and temp_list[2]-temp_list[1]==0:
    	  	  return 0
    	  else:
    	  	  return -1
    
    for nn in range(1,nLen):
	  	  if nn==0:#first
	  	  	  #print 'first:',temp_list[nn+1]-temp_list[nn]
	  	  	  continue
	  	  elif nn>nLen-2:
	  	  	  #print 'end'
	  	  	  break
	  	  else:
	  	  	  #print 'next:',nn,temp_list[nn-1],temp_list[nn],temp_list[nn+1]
	  	  	  if (temp_list[nn]-temp_list[nn-1]==1 and temp_list[nn+1]-temp_list[nn]==1) or (temp_list[nn+1]-temp_list[nn]==0 and temp_list[nn]-temp_list[nn-1]==0):
	  	  	  	  
	  	  	  	  if nn+1 == nLen-1:
	  	  	  	      
	  	  	  	      if temp_list[nn-1] - temp_list[nn-2]>1:
	  	  	  	          return nn-1
	  	  	  	  elif temp_list[nn+2] - temp_list[nn+1]>1:
	  	  	  	      
	  	  	  	      if nn-1==0:
	  	  	  	          return 0
	  	  	  	      else:
	  	  	  	          if bTest:  print '114'
	  	  	  	          if temp_list[nn-1] - temp_list[nn-2]>1:
	  	  	  	              return nn-1
	  	  	  	          else:
	  	  	  	          	  continue
	  	  	          	  
    return ret

def Get_Double_By_Mode(temp_list,nLevel):
    if bTest:  print 'Double temp_list:',temp_list,len(temp_list)
    ret=-1
    nLen = len(temp_list)
    if nLen<2:
    	  return -1
    if nLen==2:
    	  if temp_list[1]-temp_list[0]==0:  
    	      return 0
    	  else:
    	  	  return -1
    
    for nn in range(1,nLen):
	  	  if nn==0:#first
	  	  	  if bTest:  print 'first:',temp_list[nn+1]-temp_list[nn]
	  	  elif nn>nLen-1:
	  	  	  if bTest:  print 'end'
	  	  	  break
	  	  else:
	  	  	  if bTest:  print 'next:',nn,temp_list[nn-1],temp_list[nn]
	  	  	  if temp_list[nn]-temp_list[nn-1]==0:
	  	  	  	  if bTest:  print '111'
	  	  	  	  if nn == nLen-1:
	  	  	  	      if bTest:  print '114'
	  	  	  	      if temp_list[nn-1] - temp_list[nn-2]>2:
	  	  	  	          return nn-1
	  	  	  	  elif temp_list[nn+1] - temp_list[nn]>2:
	  	  	  	      if bTest:  print '112'
	  	  	  	      if nn-1==0:
	  	  	  	          return 0
	  	  	  	      else:
	  	  	  	          if bTest:  print '114'
	  	  	  	          if temp_list[nn-1] - temp_list[nn-2]>2:
	  	  	  	              return nn-1
	  	  	  	          else:
	  	  	  	          	  continue
	  	  	          	  
    return ret


def Count_Mode_By_Depth():

    for nn in range(0,len(list_Num)):
    
        if nn<2 or nn>nMjLen:
        	  list_mode.append(0)
        	  continue
        
        list1=list_Num[0:nn]
        
        list2 = []
        list_B=[]
        list_C=[]
        list_single=[]
        
        
        
        nlist1 = len(list1)
        kk=0
        mm=0
        
        for i in range(1,len(list1)+1):
            list3 = []
            #if nlist1==6 and i>3:
            if nlist1>6:
                if i<2:
                    continue
            if i>3:
                break
            #if nlist1<6 and i>2:
            #    break
        
            iter = itertools.combinations(list1,i)
            #print list(iter)
            list3.append(list(iter))
            
            
            #print list3
            #print list3[0]
            nlen =  len(list3[0])
            #print nlen
            if nlen<1:
                continue
            
            for j in range(0,nlen):
                
                list_A=list(list3[0][j])
                list_B=list(set(list1).difference(set(list_A)))
                if list_A in list_single:
                    #print 'go on!'
                    continue
                #list_C.append(0)
                #list_C[0]=list_A[:]
                list_C.append(list_A[:])
                list_single.append(list_A[:])
                
                
                list_single[kk]=list_A[:]
                #list_C.append(0)
                #list_C[1]=list_B[:]
                list_C.append(list_B[:])
        
                #list_single.append(0)
                list_single.append(list_B[:])
                
                
                #print list_C
                list2.append(list_C[:])
                
                #list2[kk] = list_C[:]
                del list_C[:]
                if list2[-1]==0:
                    list2.pop()
                #else:
                #    kk+=1    
            #list2.append(list(iter))
        
        #print 'list2:'
        #print len(list2)
        #print list2      
        list_mode.append(list2[:])
        #print list_single
    #for nn in range(0,len(list_Num)):
    #	  print 'list_mode '+str(nn)+' :'
    #	  print list_mode[nn]
        #print list_mode[nn]
    

#Count_By_Mode(temp_list1,group_list1,0)

#print group_list0


#ret = Get_Single_By_Mode(temp_list1,0)
#ret = Get_three_By_Mode(temp_list1,0)

#print 'ret:',ret



def Get_Sum_By_Mode(temp_list,group_list,nLevel):
    li_group=[]
    group_list_tmp=[]
    nLoc=0
    ret=0
    ll_tmp = temp_list[:]
    nFlag=0
    nTemp=0
    
    while True:
        ret = Count_By_Mode(ll_tmp,group_list_tmp,0)
        #print group_list0
        
        nLen = len(ll_tmp)
        if nLen==3:
            if ret>50:#ok
                nFlag=1
            elif ret>40 and ret<60:#0 kk
                nFlag=0
            elif ret==25:#024
                nFlag=1
            else:
                nFlag=0
        elif nLen==2:
            if ret>=20:#ok
                nFlag=1
            else:
                nFlag=3
        elif nLen==1:
            nFlag=1
        else:
            nFlag=0
            
        ll_gr=[0,0,0,0,0]
        ll_gr1=[0,0,0,0,0]
        if nFlag==1:
            ll_gr[0]=ret
            ll_gr[1:nLen]=ll_tmp[:]
            li_group.append(ll_gr)
            if len(group_list0)>0:
                group_list0.pop()
            if len(group_list0)>0:
                group_list0.pop()
        elif nFlag==3:
            nTemp = dict_Type_Mode_Normal.get(ll_tmp[0],0)
            ll_gr[0]=nTemp
            ll_gr[1]=ll_tmp[0]
            li_group.append(ll_gr)
            nTemp = dict_Type_Mode_Normal.get(ll_tmp[1],0)
            ll_gr1[0]=nTemp
            ll_gr1[1]=ll_tmp[1]
            li_group.append(ll_gr1)
            group_list0.pop()
            group_list0.pop()
    
        nLen = len(group_list0)
        
        if nLen==0:
               break
            
        
        while True:
            nLen = len(group_list0)
        
            if nLen==0:
               break
            else:
                ll_tmp0=group_list0[0][:]
                if len(ll_tmp0)==1:
                    ll_gr2=[0,0,0,0,0]
                    nTemp = dict_Type_Mode_Normal.get(ll_tmp0[0],0)
                    ll_gr2[0]=nTemp
                    ll_gr2[1]=ll_tmp0[0]
                    li_group.append(ll_gr2)
                    group_list0.pop(0)
                    continue
                del ll_tmp[:]
                group_list0.pop(0)
                ll_tmp = ll_tmp0[:]
                break
    
            
         
            
        #Count_By_Mode(group_list0[0],group_list1,0)
    #Count_By_Mode(group_list0[1],group_list1,0)
    
    #print group_list0
    

    if bTest:  print li_group
    nScore=0
    for jj in range(0,len(li_group)):
 	      nScore+=li_group[jj][0]	
    
    
    #group_list.append(li_group)
    group_list.extend(li_group)
    	  
    return nScore


def Get_Feng_By_Mode(temp_list,group_list,nLevel):
    
    li_group=[]
    ll_tmp = temp_list[:]
    nScore=0 
    nFlag=0
    while True:
        nlen=len(ll_tmp)
        if nlen==0:
            break
        elif nlen==1:
        	  nFlag=1
        elif nlen==2:
        	  if ll_tmp[1]>ll_tmp[0]: 
        	      nFlag=1
        	  else:
        	  	  nFlag=2
        elif nlen>2:
        	  if ll_tmp[1]>ll_tmp[0]: 
        	      nFlag=1
        	  elif ll_tmp[1]==ll_tmp[0]:
        	  	  nFlag=2
        	  	  if ll_tmp[1]==ll_tmp[2]:
        	  	      nFlag=3	
        
        if nFlag==1:
            ll_gr=[0,0,0,0,0]
            ll_gr[0]=2
            ll_gr[1]=ll_tmp[0]
            li_group.append(ll_gr)
            ll_tmp.pop(0)
            nScore+=ll_gr[0]
        elif nFlag==2:
            ll_gr=[0,0,0,0,0]
            ll_gr[0]=40
            ll_gr[1:3]=ll_tmp[0:2]
            li_group.append(ll_gr)
            ll_tmp.pop(0)
            ll_tmp.pop(0)
            nScore+=ll_gr[0]
        elif nFlag==3:
        	  ll_gr=[0,0,0,0,0]
        	  ll_gr[0]=100
        	  ll_gr[1:4]=ll_tmp[0:3]
        	  li_group.append(ll_gr)
        	  ll_tmp.pop(0)
        	  ll_tmp.pop(0)
        	  ll_tmp.pop(0)
        	  nScore+=ll_gr[0]
    
    group_list.extend(li_group)	  
    if bTest:  print nScore,group_list
    return nScore
           
        	  
    
    

def Get_Group_By_Mode(temp_list,group_list,nLevel):
    
    li_group=[]
    group_list_tmp=[]
    nScore=0 
    nlen=len(temp_list)
    if nlen<=nMjLen:
    	 nScore=Get_Sum_By_Mode(temp_list,group_list,nLevel)
    	 return nScore
    ll_tmp = temp_list[:]
    nRet=0
    nFlag=3
    while True:
    	  if nFlag==3:
		        nRet= Get_three_By_Mode(ll_tmp,nLevel)
		        if nRet>-1: 
		           ll_gr=[0,0,0,0,0]
		           ll_gr[0]=100
		           ll_gr[1:4]=ll_tmp[nRet:nRet+3]
		           li_group.append(ll_gr)
		           ll_tmp.pop(nRet)
		           ll_tmp.pop(nRet)
		           ll_tmp.pop(nRet)
		           nScore+=ll_gr[0]
		           continue
		        else:
		        	  nFlag=2
		    #Get_Double_By_Mode
    	  elif nFlag==2:
		        nRet= Get_Double_By_Mode(ll_tmp,nLevel)
		        if nRet>-1: 
		           ll_gr=[0,0,0,0,0]
		           ll_gr[0]=40
		           ll_gr[1:3]=ll_tmp[nRet:nRet+2]
		           li_group.append(ll_gr)
		           ll_tmp.pop(nRet)
		           ll_tmp.pop(nRet)
		           nScore+=ll_gr[0]
		           continue
		        else:
		        	  nFlag=1
    	  elif nFlag==1:
		        nRet= Get_Single_By_Mode(ll_tmp,nLevel)
		        if nRet>-1: 
		           ll_gr=[0,0,0,0,0]
		           ll_gr[0]=dict_Type_Mode_Normal.get(ll_tmp[nRet],0)
		           ll_gr[1:2]=ll_tmp[nRet:nRet+1]
		           li_group.append(ll_gr)
		           ll_tmp.pop(nRet)
		           nScore+=ll_gr[0]
		           continue
		        else:
		        	  break
    #print li_group
    #print ll_tmp        
    nlen=len(ll_tmp)
    ll_tmp_gr=[]
    
    nTemp=0
    if len(li_group)>0:
        group_list.extend(li_group)	
    
    if nlen<=nMjLen:
    	  nTemp=Get_Sum_By_Mode(ll_tmp,group_list,nLevel)
    	  nScore+=nTemp
    	  #return
    else:
    	  for j in range(2,nlen):
    	  	  if j<nMjLen and nlen-j<nMjLen:
    	  	  	  nS=0

    	  	  	  ll_tmp1=ll_tmp[0:j]
    	  	  	  ll_tmp2=ll_tmp[j:]
    	  	  	  nTemp = Get_Sum_By_Mode(ll_tmp1,group_list_tmp,nLevel)
    	  	  	  nS+=nTemp
    	  	  	  nTemp = Get_Sum_By_Mode(ll_tmp2,group_list_tmp,nLevel)
    	  	  	  nS+=nTemp
    	  	  	  #print 'nS:',nS
    	  	  	  ll_tmp_gr.append(j)#-20
    	  	  	  ll_tmp_gr.append(nS)
    	  nLoc = ll_tmp_gr.index(max(ll_tmp_gr))
    	  nLoc = ll_tmp_gr[nLoc-1]
    	  ll_tmp1=ll_tmp[0:nLoc]
    	  ll_tmp2=ll_tmp[nLoc:]
    	  nTemp = Get_Sum_By_Mode(ll_tmp1,group_list,nLevel)
    	  nScore+=nTemp
    	  nTemp = Get_Sum_By_Mode(ll_tmp2,group_list,nLevel)
    	  nScore+=nTemp
    if bTest:  print group_list
    return nScore
   
   
    	 



Count_Mode_By_Depth()
#print 'temp_list1:',temp_list1
#Get_Group_By_Mode(temp_list1,group_list1,nLevel)
#print 'temp_list2:',temp_list1
#Get_Feng_By_Mode(temp_list1,group_list1,nLevel)
