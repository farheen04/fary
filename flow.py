'''opening with statement'''
# with open('query.sql', 'r') as file:
#     # Read & print the entire file
#      print(file.read())
data = pd.r
file = open('query.sql', 'a')
    
    # Read out the sql script text in the file.
# sql_script_string = file.read()
# print(sql_script_string)
# max(case when (name_workstationComponent='workstation_ping_') then value else NULL end) as workstation_ping_ \
#          from
L = ["This is Delhi, \n","This is Paris, \n","This is London, \n"] 
file.writelines(L)

# \n is placed to indicate EOL (End of Line)
# file1.write("Hello, \n")
# print(sql_script_string)
# Close the sql file object.
file.close()

# table ='mac007'
# a  = f"""with pivot as ( 
# select id,timestamp,workstationcomponent,
# rawname,nameid,workstationcode,workstationid from {table}      
#          group by custom_id 
#          order by custom_id  
# )"""

<script>
    const ws = new WebSocket("wss://lf-platform.lambdafunction.ai/ws/chat/ANOMALY/",
['JWT',"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluQGlkc2lsLmNvbSIsImV4cCI6MTYzMDUxMDYyNiwiZW1haWwiOiJhZG1pbkBpZHNpbC5jb20iLCJvcmlnX2lhdCI6MTYzMDQyNDIyNn0.byl-3_RLHJzLH6zeA81HMbVkWkN03REOODu5YJXI2iI"]);
ws.onopen = function(event){
  ws.send(JSON.stringify({
    'message': { 'APS' : 'O5993(5993-050-A)' ,'REMARK':'H','CONFIRMEDBY':'DEFAULT','N_SEQUENCE':'N90','MESSAGE':'YES','CURRENT_VALUE':'1749'}
}));
}

</script>