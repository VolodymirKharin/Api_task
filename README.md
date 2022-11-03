
GET    - /boards/                           Get BOARDS<br/>
GET    - /boards/?name=name&op=op&val=val   Get BOARDS<br/>
name ={crd - created date<br/>
       mdd - modification_date<br/>
      st  - status<br/>
       }<br/>
op = {gt greater-than<br/>
      lt less-than <br/>
      eq 	equal to<br/>
      }<br/>
val = {created date        YYYY-MM-DD<br/>
       modification_date   YYYY-MM-DD<br/>
       status             ARCHIVED/OPEN<br/>
      }<br/>
Examples:      
/boards/?name=mdd&op=gt&val=2022-11-01<br/>
/boards/?name=st&op=eq&val=ARCHIVED<br/>

GET    - /task/{id}'                    Get task<br/>
GET    - /tasks/'                       Get tasks<br/>
GET    - /tasks/?status={true/false}    Get tasks <br/>
POST   - /tasks/                        Create task<br/>
PUT    - /task/{id}'                    Update Task<br/>
DELETE - /task/{id}'                    Delete Task<br/>
