import csv


#cuslist =[]
#inventorylist=[]

#f = open('orders.txt')  # create file object
#contents_order = f.read()  # read file text into a string
#orderlist = contents_order.split('\n')
#print(orderlist)

orderlist = ['CO77812002D10212020', '125^LO917^11212020', '235^IL993^11252020', 'CO77812002S10212020', '125^LO917^11212020', '235^IL993^11252020', 'CO95307005D06092019', '194^AF977^06292019', '72^L223^07142019', '370^IL993^08022019', '258^Y337^07072019', '253^O261^06182019', 'CO30950003D06012019', '139^LM485^06272019', '113^N669^06192019', '249^P530^07112019', 'CO37501001D05252020', '479^IL993^06162020', 'CO98416004S07132019', '463^UN941^08092019', '14^W555^07182019', '173^TH851^09112019', '298^O662^09032019', 'CO34198012D09202020', '33^Q25^11152020', '360^IW804^10042020', '354^UC428^11092020', '135^YJ195^10112020', '72^UN941^09252020', '238^O646^11162020', '116^K233^10062020', '211^NG108^10082020', '323^F603^09282020', '222^NQ813^11062020', '258^NO204^10292020', '434^YC871^10162020', 'CO14151010S09102020', '11^L223^11032020', '172^F603^10262020', '354^TH851^09132020', '414^TD834^09152020', '246^N669^11072020', '197^IW804^10152020', '31^NQ813^10022020', '178^W555^11032020', '38^K733^10182020', '475^PX218^09262020', 'CO95307002D07182020', '112^PX218^07292020', '456^Q25^07302020', 'CO95307003D09132020', '447^T5333^10282020', '402^R207^09252020', '229^TD834^09272020', 'EOF']
cuslist = [['24155', 'Carey, Drew Allison', '838.41', 'Bo7&J'], ['24426', 'Butler, Geoffrey Barbara', '722.93', 'Ep5&'], ['21017', 'Burkhart, Jackie Beulah', '1102.57', 'Ti5)7'], ['27823', 'Sheffield, Maxwell B', '20514.93', 'Bi6)'], ['34198', 'Deveraux, Blanche E', '1607.33', 'Cw1&('], ['17936', 'Ricardo, Lucy Esmeralda', '11800.52', 'Vb2^'], ['61531', 'Mosby, Ted Evelyn', '953.62', 'Vw6!&'], ['76294', 'Montgomery, Dharma F', '14071.65', 'Vk6^4'], ['14151', 'Addams, Wednesday Friday', '453.17', 'Cg8$'], ['38108', 'Scott, Michael Gary', '0', 'In4$d$'], ['86551', 'Fonzarelli, Arthur H', '775.75', 'Gp6$a^'], ['38046', 'Torres, Callie Iphigenia', '657.99', 'Cu7#Y'], ['21796', 'Simpson, Bart Jojo', '0', 'Eg3^'], ['98417', 'Sisko, Benjamin L', '846.79', 'Mk7**'], ['97685', 'Hofstadter, Leonard L', '0', 'Xt4&'], ['30950', 'Norton, Edward Lilywhite', '1584.38', 'Qm9*p'], ['77812', 'Costanza, George Louis', '515.55', 'Eo2!%'], ['94515', 'Griffin, Peter Lowenbrau', '542.85', 'Jq9!)'], ['37501', 'Burns, Frank Marion', '19210.32', 'Dm9%6'], ['47414', 'Lemon, Liz Miervaldis', '604.62', 'Xj8#$'], ['34292', 'Bing, Chadler Muriel', '1062.24', 'Kl1('], ['53053', 'Keaton, Alex P', '0', 'Ce4%'], ['95307', 'Petrie, Ritchie Rosebud', '733.83', 'Ut8(%'], ['89041', 'Hennessey, Cate Stinky', '901.01', 'Mi2@$'], ['67537', 'Boyd, Woody Tiberius', '16608.05', 'Bj8)@'], ['54969', 'Carter, John Truman', '0', 'Dx5&Uw'], ['33378', 'Douglass, Oliver Wendell', '1381.61', 'Yy1*'], ['40063', 'Feeney, Shirley Wilhemina', '2014.28', 'Ih0^Qv'], ['74113', 'Mulder, Fox William', '757.69', 'Of6%0'], ['60904', 'Crane, Frasier Winslow', '1077.48', 'Sk9)^']]
inventorylist = [['K733', 'Pens', '86.2'], ['LO917', 'Pencils', '74.01'], ['L223', 'Markers', '26.96'], ['O261', 'Highlighters', '60.42'], ['NQ813', 'Paper clips', '27.52'], ['TH851', 'Tape', '80.15'], ['YJ467', 'Rubber bands', '29.44'], ['UN941', 'Erasers', '74.07'], ['WR893', 'Stamp pads', '95.73'], ['SD743', 'Ink for stamp pads', '2.9'], ['IL993', 'Spiral notebooks', '72.7'], ['L761', 'Writing pads', '95.97'], ['NO204', 'Post-it(R) notes', '47.97'], ['GO642', 'Phone message pads', '38.24'], ['BC571', 'Laser printer paper', '67.54'], ['TX31', 'Copy paper', '20.56'], ['NG108', 'Fax paper', '64.58'], ['AF977', 'Graph paper', '87.72'], ['SA868', 'Colored paper', '9.52'], ['A411', 'Pocket notebook', '54.32'], ['YJ195', 'Manila file folders', '77.27'], ['YC871', 'Hanging file folders', '93.83'], ['NN896', 'Pocket folders', '17.69'], ['D636', 'File labels', '21.44'], ['K233', 'Index dividers', '93.87'], ['BM608', 'Tabs', '56'], ['L982', 'Letter envelopes', '13.03'], ['UO399', 'Catalog envelopes', '17.33'], ['Y337', 'Padded envelopes', '73.27'], ['T397', 'Shipping paper', '79.98'], ['NA485', 'Shipping labels', '94.82'], ['T533', 'Disk mailers', '59.23'], ['W555', 'Bubble wrap', '31.42'], ['NL309', 'Sealing tape', '13.73'], ['RV82', 'Toner cartridges', '71.36'], ['TD834', '3.5" high density disks', '71.47'], ['H858', 'CD-Roms', '90.25'], ['H115', 'Zip drive tapes', '85.95'], ['N669', 'Calendar', '97.84'], ['H55', 'Refills for planner', '86.09'], ['O662', 'Time cards', '91.62'], ['Q445', 'Scheduling boards', '49.84'], ['ST820', 'To-do lists', '59.87'], ['IW804', 'Staples', '62.06'], ['EZ134', 'Bulldog clamps', '3.95'], ['PX218', 'Fasteners', '71.2'], ['R207', 'Glue', '79.46'], ['P530', 'Glue sticks', '49.22'], ['ZB188', 'Reinforcements', '48.74'], ['UC428', '3-ring binders', '71.94'], ['F603', 'Pushpins', '62.49'], ['O646', 'Thumbtacks', '9.92'], ['Q25', 'Map pins', '46.22'], ['G758', 'Price tags', '18.62'], ['MR949', 'Name badges', '35'], ['E790', 'Labels', '93.81'], ['LM485', 'Color coding labels', '66.65']]


#with open('customers.csv') as csvfile:
    #readCSV = csv.reader(csvfile)
    #for row in readCSV:
        #cuslist.append(row)
    #print(cuslist)
        
#with open('inventory.csv') as csvfile:
 #   readCSV = csv.reader(csvfile)
  #  for row in readCSV:
   #     inventorylist.append(row)
    #print(inventorylist)

nolist=[] 
datelist=[]
indicatorlist=[]
qtylist =[]
itemlist = []
datesecond=[]
itemline=[]
totalnum=[]

for i in range(len(orderlist)):
    no = orderlist[i][2:7]
    if (no.isdigit() == True):
        nolist.append(no)
        datelist.append(orderlist[i][11:])
        indicatorlist.append(orderlist[i][10])
        totalnum.append(int(orderlist[i][7:10]))
    else:
        #qtylist.append(orderlist[i][0:3])
        #itemlist.append(orderlist[i][4:9])
        #datesecond.append(orderlist[i][10:])
        itemline.append(orderlist[i])
        
#print(totalnum)
#[2, 2, 5, 3, 1, 4, 12, 10, 2, 3]

#print(itemline)
itemline2=[]
for i in range(len(itemline)):
    newitemline = itemline[i].split('^')
    itemline2.append(newitemline)
  
#print(itemline2)  

finalqty =[] 
noitem =[]
date2 = []
for i in range(len(itemline2)-1):
    finalqty.append(int(itemline2[i][0]))
    noitem.append(itemline2[i][1])
    date2.append(itemline2[i][2])
    
date3list=[]
for i in range(len(date2)):
    date3= date2[i][:2]+'/'+date2[i][2]+date2[i][3]+'/'+ date2[i][4:]
    date3list.append(date3)
    
#print(date3list)
#['11/21/2020', '11/25/2020', '11/21/2020', '11/25/2020', '06/29/2019', '07/14/2019', '08/02/2019', '07/07/2019', '06/18/2019', '06/27/2019', '06/19/2019', '07/11/2019', '06/16/2020', '08/09/2019', '07/18/2019', '09/11/2019', '09/03/2019', '11/15/2020', '10/04/2020', '11/09/2020', '10/11/2020', '09/25/2020', '11/16/2020', '10/06/2020', '10/08/2020', '09/28/2020', '11/06/2020', '10/29/2020', '10/16/2020', '11/03/2020', '10/26/2020', '09/13/2020', '09/15/2020', '11/07/2020', '10/15/2020', '10/02/2020', '11/03/2020', '10/18/2020', '09/26/2020', '07/29/2020', '07/30/2020', '10/28/2020', '09/25/2020', '09/27/2020']

#print(noitem)
#['LO917', 'IL993', 'LO917', 'IL993', 'AF977', 'L223', 'IL993', 'Y337', 'O261', 'LM485', 'N669', 'P530', 'IL993', 'UN941', 'W555', 'TH851', 'O662', 'Q25', 'IW804', 'UC428', 'YJ195', 'UN941', 'O646', 'K233', 'NG108', 'F603', 'NQ813', 'NO204', 'YC871', 'L223', 'F603', 'TH851', 'TD834', 'N669', 'IW804', 'NQ813', 'W555', 'K733', 'PX218', 'PX218', 'Q25', 'T5333', 'R207', 'TD834']

#print(finalqty)
#[125, 235, 125, 235, 194, 72, 370, 258, 253, 139, 113, 249, 479, 463, 14, 173, 298, 33, 360, 354, 135, 72, 238, 116, 211, 323, 222, 258, 434, 11, 172, 354, 414, 246, 197, 31, 178, 38, 475, 112, 456, 447, 402, 229]

itemname=[]  
pricelist=[]


invlist=[]
for j in range(len(inventorylist)):
    inv = inventorylist[j][0]
    invlist.append(inv)
    
for i in range(len(noitem)):
    for j in range(len(inventorylist)):
        if (noitem[i] == inventorylist[j][0]):
            itemname.append(inventorylist[j][1])
            pricelist.append(float(inventorylist[j][2]))
            
    if ((noitem[i] in invlist) == False):
        itemname.append('*** Item not found ***')
        pricelist.append(0.00)
 

#print(indicatorlist)
#['D', 'S', 'D', 'D', 'D', 'S', 'D', 'S', 'D', 'D']

#print(nolist)
#['77812', '77812', '95307', '30950', '37501', '98416', '34198', '14151', '95307', '95307']


numlist=[]
for i in range(len(cuslist)):
    numlist.append(cuslist[i][0])
    
namelist=[] 
balancelist=[]
for i in range(len(nolist)):
    for j in range(len(numlist)):
        if(nolist[i] == numlist[j]):
            namelist.append(cuslist[j][1])
            balancelist.append(float(cuslist[j][2]))
    if( (nolist[i] in numlist) == False ):
        namelist.append('')
        balancelist.append(0.00)
        
#print(namelist)
#['Costanza, George Louis', 'Costanza, George Louis', 'Petrie, Ritchie Rosebud', 'Norton, Edward Lilywhite', 'Burns, Frank Marion', '', 'Deveraux, Blanche E', 'Addams, Wednesday Friday', 'Petrie, Ritchie Rosebud', 'Petrie, Ritchie Rosebud']                               
#print(balancelist)
#[515.55, 515.55, 733.83, 1584.38, 19210.32, 0.0, 1607.33, 453.17, 733.83, 733.83]  
#print(itemname)
#['Pencils', 'Spiral notebooks', 'Pencils', 'Spiral notebooks', 'Graph paper', 'Markers', 'Spiral notebooks', 'Padded envelopes', 'Highlighters', 'Color coding labels', 'Calendar', 'Glue sticks', 'Spiral notebooks', 'Erasers', 'Bubble wrap', 'Tape', 'Time cards', 'Map pins', 'Staples', '3-ring binders', 'Manila file folders', 'Erasers', 'Thumbtacks', 'Index dividers', 'Fax paper', 'Pushpins', 'Paper clips', 'Post-it(R) notes', 'Hanging file folders', 'Markers', 'Pushpins', 'Tape', '3.5" high density disks', 'Calendar', 'Staples', 'Paper clips', 'Bubble wrap', 'Pens', 'Fasteners', 'Fasteners', 'Map pins', '*** Item not found ***', 'Glue', '3.5" high density disks']    
#print(pricelist)
#[74.01, 72.7, 74.01, 72.7, 87.72, 26.96, 72.7, 73.27, 60.42, 66.65, 97.84, 49.22, 72.7, 74.07, 31.42, 80.15, 91.62, 46.22, 62.06, 71.94, 77.27, 74.07, 9.92, 93.87, 64.58, 62.49, 27.52, 47.97, 93.83, 26.96, 62.49, 80.15, 71.47, 97.84, 62.06, 27.52, 31.42, 86.2, 71.2, 71.2, 46.22, 0.0, 79.46, 71.47]  
#print(finalqty)
#[125, 235, 125, 235, 194, 72, 370, 258, 253, 139, 113, 249, 479, 463, 14, 173, 298, 33, 360, 354, 135, 72, 238, 116, 211, 323, 222, 258, 434, 11, 172, 354, 414, 246, 197, 31, 178, 38, 475, 112, 456, 447, 402, 229]
#print(totalnum)
#[2, 2, 5, 3, 1, 4, 12, 10, 2, 3]

