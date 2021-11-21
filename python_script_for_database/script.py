import sqlite3, csv


root_path = "C:/Projects/Android Studio Projeleri/Flutter/english_learning_app/python_script_for_database/"
conn = sqlite3.connect(root_path+'en_tr_dct.db')
c = conn.cursor()



##Concatanating txt files in one txt file
def concat_txt():
    input_a = open(root_path+"ingilizce.txt",encoding="utf-8")
    input_b = open(root_path+"turkce.txt",encoding="utf-8")
    output = open(root_path+"en_tr.txt", "w",encoding="utf-8")
    for left, right in zip(input_a, input_b):
        #use rstrip to remove the newline character from the left string
        output.write(left.rstrip() + "," + right)

    input_a.close()
    input_b.close()
    output.close()


#concat_txt()

def create_table():                                                   
    c.execute("""CREATE TABLE IF NOT EXISTS EN_TR (   
                english TEXT,                             
                turkish TEXT                                  
                )""")


def merge(list1, list2):
      
    merged_list = []
    for i in range(max((len(list1), len(list2)))):
  
        while True:
            try:
                tup = (list1[i], list2[i])
            except IndexError:
                if len(list1) > len(list2):
                    list2.append('')
                    tup = (list1[i], list2[i])
                elif len(list1) < len(list2):
                    list1.append('')
                    tup = (list1[i], list2[i])
                continue
  
            merged_list.append(tup)
            break
    return merged_list


def read_file():
    with open(root_path+"ingilizce.txt","r",encoding="utf-8") as f:                                                                          
            file_data = f.readlines()

    list = []
    for item in file_data:
        print(item.strip())
        list.append(item.strip())
        
    f.close()

    with open(root_path+"turkce.txt","r",encoding="utf-8") as s:                                                                          
            file_data2 = s.readlines()

    list2 = []
    for item2 in file_data2:
        print(item2.strip())
        list2.append(item2.strip())
    s.close()
        
    c.executemany("INSERT INTO EN_TR (english, turkish) VALUES(?, ?)",merge(list,list2))
    conn.commit()
    

    
    
    c.close()
    conn.close()

create_table()
read_file()