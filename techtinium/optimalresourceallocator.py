#store per 10 unit cost as a dictionary
countries = {
'newyork' : {'large':120,
           'xlarge':230,
           '2xlarge':450,
           '4xlarge':774,
           '8xlarge':1400,
           '10xlarge':2820},
'india'  : {'large':140,
          'xlarge':0,
          '2xlarge':413,
          '4xlarge':890,
          '8xlarge':1300,
          '10xlarge':2970
        },
'china' : {'large':110,
          'xlarge':200,
          '2xlarge':0,
          '4xlarge':670,
          '8xlarge':1180,
          '10xlarge':0
        }
}

#dic for number of units description
unitdef = {'large':10,
           'xlarge':20,
           '2xlarge':40,
           '4xlarge':80,
           '8xlarge':160,
           '10xlarge':320}

def create10UnitCost(a):
    per10unitcost = a.copy()
    for key in per10unitcost:
        perunitcost = per10unitcost[key]/(unitdef.get(key))
        per10unitcost[key] = perunitcost * 10
        #print (per10unitcost[key])
    return per10unitcost

inputunits = int(input("enter capacity: "))
#TODO: total hours need clarification. 
totalhours = 1

for country in countries.items():
    costdict = create10UnitCost(country[1])
    #sort the dictionary in the ascending order based on 10 unit cost and store it in a list
    sorteddict = sorted(costdict.items(),key=lambda x: x[1])
    #print(sorteddict,type(sorteddict))
    totalunits = inputunits
    #totalhours = 1
    units = 0
    machines = []      
    totalcost = 0
    while(totalunits > 0):
        for elem in sorteddict:
            if (elem[1] == 0):
                continue
            #get the units from unit dic
            noofunits = unitdef.get(elem[0])
            #print(noofunits,totalunits)
            if (noofunits <= totalunits):
                #print(noofunits,totalunits)
                units = int(totalunits/noofunits)
                totalunits = totalunits - (noofunits * units)
                totalcost = totalcost + ((elem[1]*(noofunits/10)*units))
                tup = (elem[0],units)
                machines.append(tup)
                
    
    
    #create the output format
    output = {}
    output.update({"region":country[0]})
    output.update({"total_cost":totalcost})
    output.update({"machines":machines})
    finaloutput = {'output':output}
    
    print (finaloutput)
