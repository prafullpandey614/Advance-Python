from tasks import cooking_task

table_1_dishes =  ["Malai Kofta","Cutlet" , "Butter Cch"]
result = cooking_task.delay("Table -1 ",table_1_dishes,)
print(result)