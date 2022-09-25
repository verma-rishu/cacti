import os
import csv
with open('Observations.csv', 'w', newline='') as file:
    header = ["FileName","Cache Size (bytes)", "Associativity", "Access Time (ns)","Dynamic read energy/access (nJ)","Area (mm2)"];
    writer = csv.writer(file)
    writer.writerow(header);

    new_list = []
    idx = 0

    path_of_the_directory = 'Observations'
    object = os.scandir(path_of_the_directory)
    for file in object :
        temp_list=[]
        temp_idx = 1;
        if file.is_file():
            temp_list.insert(0, file.name)
            with open(file, 'r') as fp:
                lines = fp.readlines()
                for row in lines:
                    words = ["Total cache size (bytes):", "Associativity:","Access time (ns):","Data array: Total dynamic read energy/access  (nJ): ", "Data array: Area (mm2):"]
                    for word in words:
                        if word in row:
                            splitRow = row.split()
                            #value = row.partition(word)[2]
                            temp_list.insert(idx, splitRow[len(splitRow) -1])
                            temp_idx =temp_idx+1
                print(temp_list);
        fp.close();
        new_list.insert(idx,temp_list);
        idx+=1;


    if len(new_list)==0:
        print("\n\"" +word+ "\" is not found in \"" +file.name+ "\"!")
    else:
        print (new_list)
        writer.writerows(new_list)
    object.close()


                        # print it.
