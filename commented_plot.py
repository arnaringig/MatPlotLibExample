import matplotlib.pyplot as plt
import csv

# Helping a friend in geoscience understand how matplotlib can
# be easily used to plot data he fetched with Google Earth Engine


with open('alldata.csv') as f: 
    fig, ax = plt.subplots()
    reader = csv.DictReader(f, delimiter=',')
    timestamps = reader.fieldnames[1:] # Here we extract all the 'column names' except the first one which is not a timestamp
    
    # Now we have to think: How do we want to structure the data within
    # our data structures after we read it?
    # Probably we will benefit from having a dictionary where the key
    # is a lake_id and the value of the key is a list of lists.
    # {
    #   '235' : [ [list of all timestamps], [values pertaining to the lake_id] ]
    #   '142' : [ [list of all timestamps], [values pertaining to the lake_id] ]
    #   ...
    #   ...
    #   ...
    # }
    lake_ids = [] # we will fill this one soon
    plot_data = [] # and this one as well
    id_dict = {} # this is where we will have all the lake_ids as keys and the plot data as values
    
    for row in reader:
        lake_ids.append(row['lake_id']) # for each row put lake_id into lake_ids 
        
        # the following lines populate row_values for each timestamp and
        # then append the timestamps and corresponding values to plot_data.
        # This is actually unnecessarily memory consuming since it´s 
        # always the same timestamps anyway (we only need them once) 
        # but it doesn´t matter in this case.
        row_values = [] 
        for timestamp in timestamps:
            row_values.append(row[timestamp])
     
        plot_data.append([timestamps,row_values])
 
    # create a dictionary with lake_ids as key and [timespamps,values] as value
    for idx, id in enumerate(lake_ids):
        id_dict[id] = plot_data[idx]  

    choice = 2 # choose 1 for plotting from a list of lake_ids and 2 for a range

    list_of_ids = ['235','142']  

    if(choice == 1): # If you only want to plot these lake_ids
        for i in list_of_ids:
            plot_data = id_dict[i] # Here we are not using the dictionary because we don´t need the values for plotting a range of data.
        
            plt.scatter(plot_data[0],plot_data[1],s=1,label=i)
    elif(choice == 2): # If you want to plot a sub-range of the data
        for i in range(20,30):
            ax.scatter(plot_data[i][0],plot_data[i][1],s=1) # Here however, we are using the dictionary because the lake_ids matter here.

    ax.legend() 
    ax.axis('off')

plt.show()
