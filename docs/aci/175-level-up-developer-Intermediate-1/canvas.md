# Canvas - Level Up Development Intermediate 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)
* back to [Level Up Developer Intermediate 1 main page](./level-up-developer-intermediate-1.md)

## [Level Up Developer Intermediate Syllabus](./canvas_files/Level%20Up%20Developer%20Intermediate%20Syllabus.pdf)

## AWS Cloud Institute Program Links

* [Learner Handbook](https://explore.skillbuilder.aws/pages/84/learner-handbook)
* [Program Calendar](https://explore.skillbuilder.aws/pages/83/program-calendar)
* [Quick start guide](https://explore.skillbuilder.aws/pages/95/quick-start-guide)
* [AWS Support - Learning & Certification](https://support.aws.amazon.com/#/contacts/aws-training)

### Instructor Information

#### Nikki Barry | she/they | <barnikki@amazon.com>

* Sr. Technical Instructor
* Currently living in Edmonds, WA (~20 miles North of Seattle)
* Born & Raise in Anaheim, CA (Home of Disneyland)
* BS in computer science from Cal State Fullerton
* Software Engineer since 2012, instructor since 2020
* AWS Authorized Instructor,  AWS Certified Solutions Architect - Associate
* I am an amateur at many, many things (lock-picking, knitting, crochet, euro-rack music production)
* I like tabletop RPGs, video games (Switch, PS5), and board games

#### Jason Cordes | he/him | <jlcordes@amazon.com>

* Technical Trainer
* College Station, TX (Aggieland)
* BS Computer Science New Mexico State University
* 10 years Software Engineering
  * NASA - real time command and control systems
  * 3D Oilfield Well Mapping and Simulation
  * Building Energy Conservation
  * Online Certification and Training
* 15 years teaching Computer Science
  * Web Design
  * Robotics
  * Video Game Design
  * Software Engineering
* I collect and study boardgames, develop video games, edit and produce videos and build and program animatronics

## Schedule

| Day | Topic |
| --------------- | ----------------------------- |
| January 10th | Business Requirements |
| January 17th | Functional Requirements / Test Plan |
| January 24th | Frontend Design |
| January 31st | API Design |
| February 7th | Service Design - Part I |
| February 14th | Service Design - Part II |
| February 21st | Database Table Design |
| February 28th | Database Query Design |
| March 7th | Architecture Design |
| March 14th | Technology Decisions |
| March 21st | Project Tracking |

## Design Document Progress

| Week | Document |
| -------------------- | --------------------------- |
| 0 - Initial Document | [Design Document.docx](./canvas_files/Design%20Document_v00.docx) |
| 1 - Business Requirements | [Design Document.docx](./canvas_files/Design%20Document_v01.docx) |
| 2 - Functional Requirements | [Design Document.docx](./canvas_files/Design%20Document_v02.docx) |
| 3 - Frontend Design | [Design Document.docx](./canvas_files/Design%20Document_v03.docx) |
| 4 - API Design | [Design Document.docx](./canvas_files/Design%20Document_v04.docx) |
| 5 - Service Design I | [Design Document.docx](./canvas_files/Design%20Document_v05.docx) |
| 6 - Service Design II | [Design Document.docx](./canvas_files/Design%20Document_v06.docx) |
| 7 - Database Table Design | [Design Document.docx](./canvas_files/Design%20Document_v07.docx) |
| 8 - Database Query Design | [Design Document.docx](./canvas_files/Design%20Document_v08.docx) |
| 9 - Architecture Design | [Requirements.docx](./canvas_files/Requirements.docx) [Design Document.docx](./canvas_files/Design%20Document_v09.docx) |
| 10 - Technology Decisions | [Design Document.docx](./canvas_files/Design%20Document_v10.docx) |
| 11 - Project Tracking | [Design Document.docx](./canvas_files/Design%20Document_v11.docx) |

## Diagram Sources

### Architecture Diagram

[NDS_Arch.drawio](./canvas_files/NDS_Arch.drawio)

### Diagramming Tools

| Title | Link |
| ----- | ---- |
| draw.io | [https://app.diagrams.net/](https://app.diagrams.net/) |
| PlantUML | [plantuml.com](http://plantuml.com/) |

#### [PlantUML Reference Guide](./canvas_files/PlantUML_Language_Reference_Guide_en.pdf)

#### PlantUML Diagram Templates

##### [Class Diagram](./canvas_files/class_diagram.puml)

```uml
@startuml

class SuperClass {
}

class Subclass extends SuperClass {
+ public_attribute
--
- _private_attribute
--
+ public_method(<args>)
--
- _private_method(<args>)
}

class Class2 {
+ public_attribute_2
--
- _private_attribute_2
--
+ public_method_2(<args>)
--
- _private_method_2(<args>)
}

enum Enum1 {
VALUE_1
VALUE_2
VALUE_3
}

Subclass *-- Class2 : contains

@enduml
```

##### [Sequence Diagram](./canvas_files/sequence_diagram.puml)

```uml
@startuml

actor user
participant component1
participant component2
database "database" as db

autonumber

user -> component1: request1
activate component1

  loop loop description
    component1 -> component2: request2
    activate component2
      component2 -> db: request3
      activate db
        component2 <-- db: response3
      deactivate db
      component2 -> component2: self action
      component1 <-- component2: response2
    deactivate component2
  end loop1

  alt case1
    user <-- component1: error response
  else case2
   user <-- component1: response1
  end
deactivate component1

@enduml
```

##### [Entity Relationship Diagram (DynamoDB)](./canvas_files/dynamodb_erd.puml)

```uml
@startuml


! $PrimaryHashKeyIcon = "<color:red><&key></color>"
! $PrimaryRangeKeyIcon = "<color:red><&layers></color>"
! $GSIHashKeyIcon = "<color:darkgreen><&key></color>"
! $GSIRangeKeyIcon = "<color:darkgreen><&layers></color>"
! $DefaultType = ""

hide methods

!unquoted procedure Table($table)
entity $table << (T,#FF7700) Table >>
!endprocedure

!unquoted procedure PrimaryHashKey($val, $type=$DefaultType)
Type($val, $type, $PrimaryHashKeyIcon)
!endprocedure

!unquoted procedure PrimaryRangeKey($val, $type=$DefaultType)
Type($val, $type, $PrimaryRangeKeyIcon)
!endprocedure

!unquoted procedure GSIHashKey($val, $type=$DefaultType)
Type($val, $type, $GSIHashKeyIcon)
!endprocedure

!unquoted procedure GSIRangeKey($val, $type=$DefaultType)
Type($val, $type, $GSIRangeKeyIcon)
!endprocedure

!unquoted procedure Attribute($val, $type=$DefaultType)
Type($val, $type)
!endprocedure

!unquoted procedure Type($val, $type=$DefaultType, $icon="")
!if ($type=="")
+$icon $val
!else
+$icon $val : $type
!endif
!endprocedure

Table(MyTable) {
    PrimaryHashKey(primaryHashKey, String)
    PrimaryRangeKey(primaryRangeKey, String)

    <GSI Name>: GSI
    GSIHashKey(gsiHashKey, String)
    GSIRangeKey(gsiRangeKey, String)

    Attributes:
    Attribute(attribue, String)
}

legend top right
|= Icon |= Type |
|  $PrimaryHashKeyIcon | Primary Hash Key |
|  $PrimaryRangeKeyIcon | Primary Range Key |
|  $GSIHashKeyIcon | GSI Hash Key |
|  $GSIRangeKeyIcon | GSI Range Key |
end legend
@enduml
```
