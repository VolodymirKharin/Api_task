GET<md-tab>    - /boards/                           Get BOARDS<br/>
GET<md-tab>    - /boards/?name=name&op=op&val=val   Get BOARDS<br/>
name ={crd - created date<br/>
<md-tab>       mdd - modification_date<br/>
<md-tab>       st  - status<br/>
<md-tab>       }<br/>
op = {gt greater-than<br/>
<md-tab>      lt less-than <br/>
<md-tab>      eq 	equal to<br/>
<md-tab>      }<br/>
val = {created date        YYYY-MM-DD<br/>
<md-tab>       modification_date   YYYY-MM-DD<br/>
<md-tab>       status             ARCHIVED/OPEN<br/>
<md-tab>      }<br/>
Examples:      
/boards/?name=mdd&op=gt&val=2022-11-01<br/>
/boards/?name=st&op=eq&val=ARCHIVED<br/>

GET    - /task/{id}'                    Get task<br/>
GET    - /tasks/'                       Get tasks<br/>
GET    - /tasks/?status={true/false}    Get tasks <br/>
POST   - /tasks/                        Create task<br/>
PUT    - /task/{id}'                    Update Task<br/>
DELETE - /task/{id}'                    Delete Task<br/>
