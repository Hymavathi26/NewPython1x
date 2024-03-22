word_list=["Hyma","raj","chaitra","Hyma","raj","Hyma"]
ocuurances_word="chaitra"
n=2
count=0
for i in range(0,len(word_list)-1):
    if (word_list[i] == ocuurances_word):
        count+=1
        if (count==n):
            del word_list[i]  #just deleted 2nd occurances
print("Updated list",word_list)    #out_put==['Hyma', 'raj', 'chaitra', 'raj', 'Hyma']


