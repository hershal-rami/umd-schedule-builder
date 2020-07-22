'''
Holds all Section objects for a Schedule
Is a more specific instance of CourseList
'''

import Section

class Schedule:

    def __init__(self):
        self.sections = []      # Array of Section objects
        self.compiled_sections = [] # 2D array acting as a boolean heat-map for course times

        # Initialize array to be all false
        for i in range(5):
            self.compiled_sections.append([])
            for j in range(68):
                self.compiled_sections[i].append(False)

    def __str__(self):
        out = "{"
        for section in self.sections:
            out += section.section_id + ", "
        out = out[:-2]
        out += "}"

        return out

    # Compares the boolean array of the new section to the rest of schedule
    # Adds the section and returns true if legal, returns false otherwise
    def add_section(self, section):
        # Stores ordered tuples representing indices for active time slots
        active_slots = []
        boolean_heatmap = section.get_boolean_heatmap()
        
        # Finds all active slots in the section parameter and stores them in active_slots
        for x in range(5):
            # Represents each day of the week M-F
            day = boolean_heatmap[x]

            # 6am-11pm = 17 hours = 68 time slots of 15 mins each
            for y in range(68):
                # Represents a single 15 min slot
                if day[y] == True:
                    active_slots.append([x,y])

        # Compare active_slots to compiled master list
        for indices in active_slots:
            day = indices[0]
            slot = indices[1]

            if self.compiled_sections[day][slot] == True:
                # The new section overlaps with an existing section
                return False
        
        # New section does not overlap, add it to the schedule and return
        self.sections.append(section)
        for indices in active_slots:
            day = indices[0]
            slot = indices[1]
            self.compiled_sections[day][slot] = True
        return True
    
    def add_sections(self, sections):
        for section in sections:
            self.add_section(section)
    
    # Removes the section from the Schedule and the boolean heatmap
    def remove_section(self, section):
        boolean_heatmap = section.get_boolean_heatmap()

        for x in range(5):
            for y in range(68):
                if boolean_heatmap[x][y] == True:
                    self.compiled_sections[x][y] = False

        self.sections.remove(section)
    
    def remove_sections(self, sections):
        for section in sections:
            self.remove_section(section)

    def clear(self):
        self.sections.clear()
        self.compiled_sections.clear()

    # Can add other functions to manipulate array later