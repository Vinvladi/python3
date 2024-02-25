bin_list = [2,3,6,12,21,22,30,43,45,48,50,51,52,58,64,72]
wine_list = ["Chardonnay","Chardonnay","Chardonnay","Joh. Riesling", "Fume Blanc","Fume Blanc", "Gewurztraminer",
             "Cab. Sauvignon","Cab. Sauvignon","Cab. Sauvignon","Pinot.Noir", "Pinot.Noir", "Pinot.Noir", "Merlot",
             "Zinfandel","Zinfandel"]
producer_list = ["Buena Vista", "Geyser Peak", "Simi", "Jekel", "Ch. St. Jean", "Robt. Mondavi", "Ch. St. Jean",
                 "Windsor","Geyser Peak", "Robt. Mondavi", "Gary Farrell", "Fetzer", "Dehlinger", "Clos du Bois",
                 "Cline", "Rafanelli"]
year_list = [2001,2001,2000,2002,2001,2000,2002,1995,1998,1997,2000,1997,1999,1998,1998,1999]
bottles_list = [1,5,4,1,4,2,3,12,12,12,3,3,2,9,9,2]
ready_list = [2003,2003,2002,2003,2003,2002,2003,2004,2006,2008,2003,2004,2002,2004,2007,2007]
if len(bin_list) == len(wine_list) == len(producer_list) == len(year_list) == len(bottles_list) == len(ready_list):
    print(f"Good, количество элементов для таблицы = {len(bin_list)}")
    database_examination = True  # Проверка дата бызы
else:
    print(f"list = {len(bin_list)}, wine = {len(wine_list)}, producer = {len(producer_list)}, year = {len(year_list)}, "
          f"bottles = {len(bottles_list)}, ready = {len(ready_list)}")
    database_examination = False
if database_examination:
    database_result = f"create table cellar (\n" \
                      f"\t bin VARCHAR(50) NOT NULL,\n" \
                      f"\t wine VARCHAR(50) NOT NULL,\n" \
                      f"\t producer VARCHAR(50) NOT NULL,\n" \
                      f"\t year INT,\n" \
                      f"\t bottles INT,\n" \
                      f"\t ready INT\n" \
                      f");\n"
    for i in range(0,len(bin_list),1):
        database_result += f"insert into cellar (bin, wine, producer, year, bottles, ready) values ('{bin_list[i]}', " \
                           f"'{wine_list[i]}', '{producer_list[i]}', '{year_list[i]}', '{bottles_list[i]}', " \
                           f"'{ready_list[i]}');\n"
    file_sql = open("out.sql","w")
    file_sql.write(database_result)
    file_sql.close()
else:
    print(f"Давай по новой Миша, все хуйня!")