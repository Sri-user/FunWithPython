# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:21:01 2020

@author: srith


"""

def flames(name1,name2):
    '''
       we calculate a temp total, by calculating the remaining letters after the cancelled letter
        and subtracting it from the main total
        
        Because after one cut, we need to start counting the 'total' from the cut index place
        
        So if we subtract the remaining letters after the cut index, all we have to do is find modulo
        of total and limit
        
        We subtract the one to compensate the list starting from 0 and our variable limit is set 6, because
        there are 6 elements in the list
        '''
    name1 = name1.replace(" ","")
    name2 = name2.replace(" ","")
    
    relationship = ['F','L','A','M','E','S']
    rel_dic = {'F':'Friends','L':'Love','A':'Affection','M':'Marriage','E':'Enemy','S':'Sibling'}
    
    chars_after_cut_index = 0 
    limit=6
    
    name1_list = [x for x in name1]
    name2_list = [x for x in name2]
    
    for x in name1_list:
        if x in name2_list:
            name1_list.remove(x)
            name2_list.remove(x)
        else:
            pass
       
    for x in name2_list:
        if x in name1_list:
            name1_list.remove(x)
            name2_list.remove(x)
        else:
            pass
    
    total = len(name1_list)+len(name2_list) # Get the number of remaining letters after removing common letters
    
    while limit>=2: # Check until there is one element is present in flames list
        if(total)==0:
            return(name1,name2,rel_dic[relationship['S']])
        else:
            temp_total = total-chars_after_cut_index 
            to_be_cut_index = (temp_total%limit)-1
            if to_be_cut_index == -1:
                to_be_cut_index = limit-1
            else:
                pass
            chars_after_cut_index = (limit - to_be_cut_index)-1
            relationship.pop(to_be_cut_index)
            limit = limit-1
            #print(f'limit inside loop is {limit}')
        
    future_relation = rel_dic[relationship[0]]
    return(name1,name2,future_relation)

name1,name2,Future_Relationship = flames('Romeo','Juliet')

if Future_Relationship=='Sibling':
    print(f'{name1} and {name2} are {Future_Relationship}s')
elif Future_Relationship=='Affection':
    print(f'{name1} and {name2} will be always {Future_Relationship}ate to each other')
elif Future_Relationship=='Friends':
    print(f'{name1} and {name2} are {Future_Relationship}s')
elif Future_Relationship=='Love':
    print(f'{name1} and {name2} are in {Future_Relationship}')
elif Future_Relationship=='Marriage':
    print(f'{name1} will marry {name2}')
elif Future_Relationship=='Enemy':
    print(f'{name1} and {name2} are enemies. But remember fights increase the love between each other')