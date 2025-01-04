
''' 
FIRST VERSION - Improvements for Next Version:
    * Allow user input of Committees, Members and available Slots (currently 'hardwired')
    * If user does not specify available slots, calculate minimum number of slots and schedule accordingly
    * Auto-create the Conflicts Matrix based on users input of Committees and Members
'''

# SET-UP COMMITTEE CLASS AND MAIN FUNCTION

class Committee:
    def __init__(self, commName, conflicts):
        self.commName = commName
        self.conflicts = conflicts
        self.slots = [1, 2, 3]

def scheduleCommittees():
    
    allCommittees[0].slots = [1]

    for committee in allCommittees:
        firstAvailableSlot = committee.slots[0]
        for i, conflict in enumerate(committee.conflicts):
            currCommCheck = allCommittees[i].slots
            if (conflict == 1) and (firstAvailableSlot in currCommCheck):
                allCommittees[i].slots.remove(firstAvailableSlot)

    for j, committee in enumerate(allCommittees):
        print(f"\nThe {committee.commName} Committee's meeting is scheduled for SLOT {committee.slots}.\n")

    return None


# SET-UP COMMITTEES, CONFLICTS AND AVAILABLE SLOTS

conflictGraph = [
    [0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

academicPolicy = Committee("Academic Policy", conflictGraph[0])
boardOfGovernors = Committee("Board of Governors", conflictGraph[1])
classroomVision = Committee("Classroom Vision", conflictGraph[2])
dei = Committee("Diversity and Equity", conflictGraph[3])
externalRelations = Committee("External Relations", conflictGraph[4])
facultyDevelopment = Committee("Faculty Development", conflictGraph[5])
graduateStudies = Committee("Graduate Studies", conflictGraph[6])

allCommittees = [academicPolicy, boardOfGovernors, classroomVision, dei, externalRelations, facultyDevelopment, graduateStudies]

# RUN!
scheduleCommittees()