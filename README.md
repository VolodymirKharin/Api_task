GET    - /boards/                           Get BOARDS
GET    - /boards/?name=name&op=op&val=val   Get BOARDS
name ={crd - created date
       mdd - modification_date
       st  - status
       }
op = {gt greater-than
      lt less-than 
      eq 	equal to
      }
val = {created date        YYYY-MM-DD
       modification_date   YYYY-MM-DD
       status             ARCHIVED/OPEN
      }
Examples:      
/boards/?name=mdd&op=gt&val=2022-11-01
/boards/?name=st&op=eq&val=ARCHIVED

GET    - /task/{id}'                    Get task
GET    - /tasks/'                       Get tasks
GET    - /tasks/?status={true/false}    Get tasks 
POST   - /tasks/                        Create task
PUT    - /task/{id}'                    Update Task
DELETE - /task/{id}'                    Delete Task
